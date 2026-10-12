"""PDF-превью DOCX через LibreOffice (UNO) с обновлением оглавления.

Зачем: _lib.md2docx.docx_to_pdf() конвертирует без обновления полей, поэтому поле
«Содержание», вставленное pandoc, в PDF остаётся пустым. Здесь документ открывается
в LibreOffice, все указатели (оглавление) обновляются и только затем экспортируется PDF.
Сам DOCX не перезаписывается: Word обновит поле оглавления при открытии (updateFields).

    python lo_pdf.py файл.docx [файл.pdf]
"""
from __future__ import annotations

import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path


def _free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def docx_to_pdf_toc(docx_path: str | Path, pdf_path: str | Path | None = None, timeout=180) -> Path:
    import uno
    from com.sun.star.beans import PropertyValue

    docx_path = Path(docx_path).resolve()
    pdf_path = Path(pdf_path).resolve() if pdf_path else docx_path.with_suffix(".pdf")
    port = _free_port()
    profile = tempfile.mkdtemp(prefix="lo_mhtp_")
    proc = subprocess.Popen(
        ["soffice", f"-env:UserInstallation=file://{profile}", "--headless", "--invisible",
         "--nologo", "--norestore", f"--accept=socket,host=127.0.0.1,port={port};urp;"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def prop(name, value):
        p = PropertyValue()
        p.Name, p.Value = name, value
        return p
    try:
        local = uno.getComponentContext()
        resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
        t0 = time.time()
        while True:
            try:
                ctx = resolver.resolve(f"uno:socket,host=127.0.0.1,port={port};urp;StarOffice.ComponentContext")
                break
            except Exception:
                if time.time() - t0 > timeout:
                    raise RuntimeError("LibreOffice не запустился")
                time.sleep(0.5)
        desktop = ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
        doc = desktop.loadComponentFromURL(docx_path.as_uri(), "_blank", 0, (prop("Hidden", True),))
        idx = doc.getDocumentIndexes()
        for i in range(idx.getCount()):
            idx.getByIndex(i).update()
        doc.refresh()
        for i in range(idx.getCount()):          # повторно — номера страниц после вставки строк
            idx.getByIndex(i).update()
        doc.storeToURL(pdf_path.as_uri(), (prop("FilterName", "writer_pdf_Export"),))
        doc.close(True)
    finally:
        try:
            desktop.terminate()
        except Exception:
            pass
        try:
            proc.wait(timeout=30)
        except subprocess.TimeoutExpired:
            proc.kill()
        shutil.rmtree(profile, ignore_errors=True)
    return pdf_path


if __name__ == "__main__":
    print(docx_to_pdf_toc(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None))
