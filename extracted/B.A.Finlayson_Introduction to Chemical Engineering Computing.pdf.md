# B.A.Finlayson_Introduction to Chemical Engineering Computing.pdf

Источник: `B.A.Finlayson_Introduction to Chemical Engineering Computing.pdf` (извлечено pdfplumber, текст дословно, постранично)

---

## Стр. 1

```text
P1:OTA/XYZ P2:ABC
JWBS084-fm JWBS084-Finlayson May18,2012 10:43 PrinterName:YettoCome Trim:7in×10in
INTRODUCTION TO
CHEMICAL ENGINEERING
COMPUTING
```

---

## Стр. 2

```text
P1:OTA/XYZ P2:ABC
JWBS084-fm JWBS084-Finlayson May18,2012 10:43 PrinterName:YettoCome Trim:7in×10in
INTRODUCTION TO
CHEMICAL ENGINEERING
COMPUTING
Second Edition
BRUCEA.FINLAYSON
RehnbergProfessorEmeritusofChemicalEngineering
DepartmentofChemicalEngineering
UniversityofWashington
Seattle,WA
AJOHNWILEY&SONS,INC.,PUBLICATION
```

---

## Стр. 3

```text
P1:OTA/XYZ P2:ABC
JWBS084-fm JWBS084-Finlayson May18,2012 10:43 PrinterName:YettoCome Trim:7in×10in
Copyright©2012byJohnWiley&Sons,Inc.Allrightsreserved
PublishedbyJohnWiley&Sons,Inc.,Hoboken,NewJersey
PublishedsimultaneouslyinCanada
Nopartofthispublicationmaybereproduced,storedinaretrievalsystem,ortransmittedinanyformor
byanymeans,electronic,mechanical,photocopying,recording,scanning,orotherwise,exceptas
permittedunderSection107or108ofthe1976UnitedStatesCopyrightAct,withouteithertheprior
writtenpermissionofthePublisher,orauthorizationthroughpaymentoftheappropriateper-copyfeeto
theCopyrightClearanceCenter,Inc.,222RosewoodDrive,Danvers,MA01923,(978)750-8400,
fax(978)750-4470,oronthewebatwww.copyright.com.RequeststothePublisherforpermission
shouldbeaddressedtothePermissionsDepartment,JohnWiley&Sons,Inc.,111RiverStreet,Hoboken,
NJ07030,(201)748-6011,fax(201)748-6008,oronlineathttp://www.wiley.com/go/permission.
LimitofLiability/DisclaimerofWarranty:Whilethepublisherandauthorhaveusedtheirbesteffortsin
preparingthisbook,theymakenorepresentationsorwarrantieswithrespecttotheaccuracyor
completenessofthecontentsofthisbookandspecificallydisclaimanyimpliedwarrantiesof
merchantabilityorfitnessforaparticularpurpose.Nowarrantymaybecreatedorextendedbysales
representativesorwrittensalesmaterials.Theadviceandstrategiescontainedhereinmaynotbesuitable
foryoursituation.Youshouldconsultwithaprofessionalwhereappropriate.Neitherthepublishernor
authorshallbeliableforanylossofprofitoranyothercommercialdamages,includingbutnotlimitedto
special,incidental,consequential,orotherdamages.
Forgeneralinformationonourotherproductsandservicesorfortechnicalsupport,pleasecontactour
CustomerCareDepartmentwithintheUnitedStatesat(800)762-2974,outsidetheUnitedStatesat
(317)572-3993orfax(317)572-4002.
Wileyalsopublishesitsbooksinavarietyofelectronicformats.Somecontentthatappearsinprintmay
notbeavailableinelectronicformats.FormoreinformationaboutWileyproducts,visitourwebsiteat
www.wiley.com
LibraryofCongressCataloging-in-PublicationData:
Finlayson,BruceA.
Introductiontochemicalengineeringcomputing/BruceA.Finlayson.–2nded.
p.cm.
Includesindex.
ISBN978-0-470-93295-7(pbk.)
1.Chemicalengineering–Dataprocessing. I.Title.
TP184.F562012
660.0285–dc23
2011045242
PrintedintheUnitedStatesofAmerica
10 9 8 7 6 5 4 3 2 1
```

---

## Стр. 4

```text
P1:OTA/XYZ P2:ABC
JWBS084-fm JWBS084-Finlayson May18,2012 10:43 PrinterName:YettoCome Trim:7in×10in
MATLAB®isatrademarkofTheMathWorks,Inc.,andisusedwithpermission.TheMath
Worksdoesnotwarranttheaccuracyofthetextorexercisesinthisbook.Thisbook’suse
ordiscussionofMATLABsoftwareorrelatedproductsdoesnotconstituteendorsementor
sponsorshipbyTheMathWorksofaparticularpedagogicalapproachorparticularuseof
theMATLABsoftware.
Comsol Multiphysics® is a trademark of COMSOL AB. COMSOL product screen shots
reprintedwithpermissionfromCOMSOLAB.
©2011AspenTechnology,Inc.AspenTech®,aspenONE®,AspenPlus®andtheAspenleaf
logoaretrademarksofAspenTechnology,Inc.Allrightsreserved.
```

---

## Стр. 5

```text
P1:OTA/XYZ P2:ABC
JWBS084-fm JWBS084-Finlayson May18,2012 10:43 PrinterName:YettoCome Trim:7in×10in
CONTENTS
Preface xv
1 Introduction 1
Organization, 2
AlgebraicEquations, 3
ProcessSimulation, 3
DifferentialEquations, 3
Appendices, 4
2 EquationsofState 7
EquationsofState—MathematicalFormulation, 8
SolvingEquationsofStateUsingExcel(SingleEquationinOneUnknown), 12
SolutionUsing“GoalSeek”, 12
SolutionUsing“Solver”, 13
ExampleofaChemicalEngineeringProblemSolvedUsing“GoalSeek”, 13
SolvingEquationsofStateUsingMATLAB(SingleEquationin
OneUnknown), 15
ExampleofaChemicalEngineeringProblemSolvedUsingMATLAB, 16
AnotherExampleofaChemicalEngineeringProblemSolvedUsing
MATLAB, 18
EquationsofStateWithAspenPlus, 20
ExampleUsingAspenPlus, 20
SpecificVolumeofaMixture, 21
ChapterSummary, 26
Problems, 26
NumericalProblems, 28
vii
```

---

## Стр. 6

```text
P1:OTA/XYZ P2:ABC
JWBS084-fm JWBS084-Finlayson May18,2012 10:43 PrinterName:YettoCome Trim:7in×10in
viii CONTENTS
3 Vapor–LiquidEquilibria 29
FlashandPhaseSeparation, 30
IsothermalFlash—DevelopmentofEquations, 30
ExampleUsingExcel, 32
ThermodynamicParameters, 33
ExampleUsingMATLAB, 34
ExampleUsingAspenPlus, 35
NonidealLiquids—TestofThermodynamicModel, 39
NISTThermoDataEngineinAspenPlus, 41
ChapterSummary, 44
Problems, 44
NumericalProblems, 48
4 ChemicalReactionEquilibria 49
ChemicalEquilibriumExpression, 50
ExampleofHydrogenforFuelCells, 51
SolutionUsingExcel, 52
SolutionUsingMATLAB, 53
ChemicalReactionEquilibriawithTwoorMoreEquations, 56
MultipleEquations,FewUnknownsUsingMATLAB, 56
ChemicalReactionEquilibriaUsingAspenPlus, 59
ChapterSummary, 59
Problems, 60
NumericalProblems, 63
5 MassBalanceswithRecycleStreams 65
MathematicalFormulation, 66
ExampleWithoutRecycle, 68
ExamplewithRecycle;ComparisonofSequentialandSimultaneous
SolutionMethods, 70
ExampleofProcessSimulationUsingExcelforSimpleMassBalances, 72
ExampleofProcessSimulationUsingAspenPlusforSimple
MassBalances, 73
ExampleofProcessSimulationwithExcelIncludingChemicalReaction
Equilibria, 74
DidtheIterationsConverge?, 75
Extensions, 76
ChapterSummary, 76
ClassExercises, 76
ClassDiscussion(AfterViewingProblem5.10ontheBookWebsite), 76
Problems, 77
6 ThermodynamicsandSimulationofMassTransferEquipment 85
Thermodynamics, 86
GuidelinesforChoosing, 89
PropertyMethodSelectionAssistant, 89
ThermodynamicModels, 90
```

---

## Стр. 7

```text
P1:OTA/XYZ P2:ABC
JWBS084-fm JWBS084-Finlayson May18,2012 10:43 PrinterName:YettoCome Trim:7in×10in
CONTENTS ix
Example:MulticomponentDistillationwithShortcutMethods, 91
MulticomponentDistillationwithRigorousPlate-to-PlateMethods, 95
Example:PackedBedAbsorption, 97
Example:GasPlantProductSeparation, 100
Example:WaterGasShiftEquilibriumReactorwithSensitivityBlockand
DesignSpecificationBlock, 102
ChapterSummary, 106
ClassExercise, 106
Problems(usingAspenPlus), 106
7 ProcessSimulation 109
ModelLibrary, 110
Example:AmmoniaProcess, 110
DevelopmentoftheModel, 112
SolutionoftheModel, 115
ExaminationofResults, 115
TestingtheThermodynamicModel, 118
UtilityCosts, 118
GreenhouseGasEmissions, 120
ConvergenceHints, 120
Optimization, 122
IntegratedGasificationCombinedCycle, 125
CellulosetoEthanol, 126
ChapterSummary, 128
ClassExercise, 128
Problems, 128
ProblemsInvolvingCornStoverandEthanol, 131
8 ChemicalReactors 137
MathematicalFormulationofReactorProblems, 138
Example:PlugFlowReactorandBatchReactor, 138
Example:ContinuousStirredTankReactor, 140
UsingMATLABtoSolveOrdinaryDifferentialEquations, 140
SimpleExample, 140
Useofthe“Global”Command, 142
PassingParameters, 143
Example:IsothermalPlugFlowReactor, 144
Example:NonisothermalPlugFlowReactor, 146
UsingComsolMultiphysicstoSolveOrdinaryDifferentialEquations, 148
SimpleExample, 148
Example:IsothermalPlugFlowReactor, 150
Example:NonisothermalPlugFlowReactor, 151
ReactorProblemswithMoleChangesandVariableDensity, 153
ChemicalReactorswithMassTransferLimitations, 155
PlugFlowChemicalReactorsinAspenPlus, 158
ContinuousStirredTankReactors, 161
SolutionUsingExcel, 162
```

---

## Стр. 8

```text
P1:OTA/XYZ P2:ABC
JWBS084-fm JWBS084-Finlayson May18,2012 10:43 PrinterName:YettoCome Trim:7in×10in
x CONTENTS
SolutionUsingMATLAB, 163
CSTRwithMultipleSolutions, 163
TransientContinuousStirredTankReactors, 164
ChapterSummary, 168
Problems, 169
NumericalProblems(SeeAppendixE), 174
9 TransportProcessesinOneDimension 175
ApplicationsinChemicalEngineering—MathematicalFormulations, 176
HeatTransfer, 176
DiffusionandReaction, 177
FluidFlow, 178
UnsteadyHeatTransfer, 180
IntroductiontoComsolMultiphysics, 180
Example:HeatTransferinaSlab, 181
SolutionUsingComsolMultiphysics, 181
SolutionUsingMATLAB, 184
Example:ReactionandDiffusion, 185
ParametricSolution, 186
Example:FlowofaNewtonianFluidinaPipe, 188
Example:FlowofaNon-NewtonianFluidinaPipe, 190
Example:TransientHeatTransfer, 193
SolutionUsingComsolMultiphysics, 193
SolutionUsingMATLAB, 195
Example:LinearAdsorption, 196
Example:Chromatography, 199
PressureSwingAdsorption, 203
ChapterSummary, 204
Problems, 204
ChemicalReaction, 204
ChemicalReactionandHeatTransfer, 205
MassTransfer, 207
HeatTransfer, 207
ElectricalFields, 207
FluidFlow, 208
NumericalProblems(SeeAppendixE), 213
10 FluidFlowinTwoandThreeDimensions 215
MathematicalFoundationofFluidFlow, 217
Navier–StokesEquation, 217
Non-NewtonianFluid, 218
Nondimensionalization, 219
OptionOne:SlowFlows, 219
OptionTwo:High-SpeedFlows, 220
Example:EntryFlowinaPipe, 221
Example:EntryFlowofaNon-NewtonianFluid, 226
Example:FlowinMicrofluidicDevices, 227
Example:TurbulentFlowinaPipe, 230
```

---

## Стр. 9

```text
P1:OTA/XYZ P2:ABC
JWBS084-fm JWBS084-Finlayson May18,2012 10:43 PrinterName:YettoCome Trim:7in×10in
CONTENTS xi
Example:Start-UpFlowinaPipe, 233
Example:FlowThroughanOrifice, 235
Example:FlowinaSerpentineMixer, 239
Microfluidics, 240
MechanicalEnergyBalanceforLaminarFlow, 243
PressureDropforContractionsandExpansions, 245
GenerationofTwo-DimensionalInletVelocityProfilesfor
Three-DimensionalSimulations, 246
ChapterSummary, 249
Problems, 249
11 HeatandMassTransferinTwoandThreeDimensions 259
ConvectiveDiffusionEquation, 260
NondimensionalEquations, 261
Example:HeatTransferinTwoDimensions, 262
Example:HeatConductionwithaHole, 264
Example:ConvectiveDiffusioninMicrofluidicDevices, 265
Example:Concentration-DependentViscosity, 268
Example:ViscousDissipation, 269
Example:ChemicalReaction, 270
Example:WallReactions, 272
Example:MixinginaSerpentineMixer, 272
Microfluidics, 274
CharacterizationofMixing, 276
AverageConcentrationalonganOpticalPath, 276
PecletNumber, 276
Example:ConvectionandDiffusioninaThree-DimensionalT-Sensor, 278
ChapterSummary, 280
Problems, 280
Steady,Two-DimensionalProblems, 280
HeatTransferwithFlow, 283
ReactionwithKnownFlow, 284
ReactionwithNoFlow, 285
SolveforConcentrationandFlow, 286
NumericalProblems, 289
AppendixA HintsWhenUsingExcel® 291
Introduction, 291
Calculation, 292
Plotting, 293
ImportandExport, 294
Presentation, 294
AppendixB HintsWhenUsingMATLAB® 297
GeneralFeatures, 298
ScreenFormat, 298
Stop/ClosingtheProgram, 299
m-filesandScripts, 299
```

---

## Стр. 10

```text
P1:OTA/XYZ P2:ABC
JWBS084-fm JWBS084-Finlayson May18,2012 10:43 PrinterName:YettoCome Trim:7in×10in
xii CONTENTS
WorkspacesandTransferofInformation, 300
“Global”Command, 300
DisplayTools, 301
ClassesofData, 301
ProgrammingOptions:Input/Output,Loops,ConditionalStatements,
Timing,andMatrices, 302
Input/Output, 302
Loops, 303
ConditionalStatements, 303
TimingInformation, 304
Matrices, 304
MatrixMultiplication, 304
ElementbyElementCalculations, 305
MoreInformation, 306
FindingandFixingErrors, 306
EigenvaluesofaMatrix, 307
EvaluateanIntegral, 307
SplineInterpolation, 307
InterpolateData,EvaluatethePolynomial,andPlottheResult, 308
SolveAlgebraicEquations, 309
Using“fsolve”, 309
SolveAlgebraicEquationsUsing“fzero”or“fminsearch”
(BothinStandardMATLAB), 309
IntegrateOrdinaryDifferentialEquationsthatareInitialValue
Problems, 309
Differential-AlgebraicEquations, 311
ChecklistforUsing“ode45”andOtherIntegrationPackages, 311
Plotting, 312
SimplePlots, 312
AddDatatoanExistingPlot, 312
DressUpYourPlot, 312
MultiplePlots, 313
3DPlots, 313
MoreComplicatedPlots, 314
UseGreekLettersandSymbolsintheText, 314
Bold,Italics,andSubscripts, 314
OtherApplications, 315
PlottingResultsfromIntegrationofPartialDifferentialEquations
UsingMethodofLines, 315
Import/ExportData, 315
Import/ExportwithComsolMultiphysics, 318
ProgrammingGraphicalUserInterfaces, 318
MATLABHelp, 318
ApplicationsofMATLAB, 319
AppendixC HintsWhenUsingAspenPlus® 321
Introduction, 321
Flowsheet, 322
```

---

## Стр. 11

```text
P1:OTA/XYZ P2:ABC
JWBS084-fm JWBS084-Finlayson May18,2012 10:43 PrinterName:YettoCome Trim:7in×10in
CONTENTS xiii
ModelLibrary, 322
PlaceUnitsonFlowsheet, 323
ConnecttheUnitswithStreams, 323
Data, 323
Setup, 324
DataEntry, 324
SpecifyComponents, 325
SpecifyProperties, 325
SpecifyInputStreams, 326
SpecifyBlockParameters, 326
RuntheProblem, 327
ScrutinizetheStreamTable, 327
CheckingYourResults, 328
ChangeConditions, 328
Report, 328
TransfertheFlowsheetandMassandEnergyBalancetoaWord
ProcessingProgram, 328
PrepareYourReport, 328
SaveYourResults, 329
GettingHelp, 329
AdvancedFeatures, 329
FlowsheetSections, 329
MassBalanceOnlySimulationsandInclusionof
Solids, 330
TransferBetweenExcelandAspen, 331
BlockSummary, 331
CalculatorBlocks, 331
AspenExamples, 332
MoleculeDraw, 332
ApplicationsofAspenPlus, 334
AppendixD HintsWhenUsingComsolMultiphysics® 335
BasicComsolMultiphysicsTechniques, 336
OpeningScreens, 336
Equations, 337
SpecifytheProblemandParameters, 337
Physics, 339
Definitions, 339
Geometry, 339
Materials, 340
Discretization, 341
BoundaryConditions, 341
Mesh, 342
SolveandExaminetheSolution, 342
Solve, 342
Plot, 342
PublicationQualityFigures, 343
Results, 343
```

---

## Стр. 12

```text
P1:OTA/XYZ P2:ABC
JWBS084-fm JWBS084-Finlayson May18,2012 10:43 PrinterName:YettoCome Trim:7in×10in
xiv CONTENTS
Probes, 344
DataSets, 344
AdvancedFeatures, 345
Mesh, 345
TransfertoExcel, 346
LiveLinkwithMATLAB, 347
Variables, 348
Animation, 349
Studies, 349
HelpwithConvergence, 349
HelpwithTime-DependentProblems, 350
JumpDiscontinuity, 350
Help, 351
ApplicationsofComsolMultiphysics, 351
AppendixE MathematicalMethods 353
AlgebraicEquations, 354
SuccessiveSubstitution, 354
Newton–Raphson, 354
OrdinaryDifferentialEquationsasInitialValueProblems, 356
Euler’sMethod, 356
Runge–KuttaMethods, 357
MATLABandode45andode15s, 357
OrdinaryDifferentialEquationsasBoundaryValueProblems, 358
FiniteDifferenceMethod, 359
FiniteDifferenceMethodinExcel, 360
FiniteElementMethodinOneSpaceDimension, 361
InitialValueMethods, 363
PartialDifferentialEquationsintimeandOneSpaceDimension, 365
ProblemswithStrongConvection, 366
PartialDifferentialEquationsinTwoSpaceDimensions, 367
Finite-DifferenceMethodforEllipticEquationsinExcel, 367
FiniteElementMethodforTwo-DimensionalProblems, 368
Summary, 370
Problems, 370
References 373
Index 379
```

---

## Стр. 13

```text
P1:OTA/XYZ P2:ABC
JWBS084-Preface JWBS084-Finlayson March28,2012 7:53 PrinterName:YettoCome Trim:7in×10in
PREFACE
Chemicalengineeringstudentsandchemicalengineersarebeingaskedtosolveproblems
that are increasingly complex, whether the applications are in refineries, fuel cells, mi-
croreactors,orpharmaceuticalplants.Manyyearsago,studentswrotetheirownprograms,
first in the FORTRAN programming language, then in languages such as MATLAB®.
However, with the growth in personal computers, software has been written that solves
manyproblemsforstudents,providedtheyusetheprogramscorrectly.Thus,theemphasis
shifted from a small group of people who were interested in writing their own programs
to a large group of students who will use the programs, but do not write them. In my 42
yearsofteachingattheUniversityofWashington,Itaughtthosesmallgroupsofstudents
howtousenumericalanalysistosolvecomplicatedproblems.Now,Iteachallthestudents
how to use the computer wisely. Only a few of the students I teach are interested in the
numerical analysis (to my sorrow!), but all the students know they must be able to solve
difficultproblems,andtheyneedtousethecomputertodothat.
The goals of this book are to illustrate (a) the problems chemical engineers have to
solve, (b) the type of computer programs used to solve them, and (c) how engineers
check to be sure they have solved the problems correctly. This is done in the context of
how contemporary students learn—minimal reading, just-in-time learning, with lots of
computerusage.TheprogramsdemonstratedhereareExcel®,MATLAB®,AspenPlus®,
andComsolMultiphysics®.
Whenwritingthisbook,Iassumedthatreadersarenotabsolutebeginners.Juniorand
seniorchemicalengineeringstudentshavehadexperiencewithspreadsheetprogramssuch
as Excel, and they can easily learn on the computer when provided a direction and key
ideas or phrases. In fact, many students are more computer-savvy than their instructors.
However, a beginner chemical engineering student may not know the application very
wellandmaynothavegainedasolidunderstandingofthephysicalphenomenonbehindan
engineeringproblem.Furthermore,theymaynothavesolvedverydifficultproblems.Thus,
it is important to give some explanation of why students need to solve certain problems
xv
```

---

## Стр. 14

```text
P1:OTA/XYZ P2:ABC
JWBS084-Preface JWBS084-Finlayson March28,2012 7:53 PrinterName:YettoCome Trim:7in×10in
xvi PREFACE
andhowtoovercometheobstacleswhentheproblemstaxthenumericalmethods.Ihave
drawnonmyexperiencetogiveinsightsintotheproblemsinthisbook.
My teaching philosophy is that the problems engineers are solving today are usually
intractablewithanalyticalmethods,buttheycanbesolvedwiththesophisticatedsoftware
available today. Thus, every engineer will be solving a problem that no one knows the
answerto,anditistheengineer’sjobtoensurethattheproblemisposedcorrectlyonpaper
and in the computer, and it is correctly solved. Engineering students must know how to
determineifthecomputersolvedtheproblemcorrectlybyvalidatingtheworkdonebythe
computer.Iftheycandothis,theycanconvincetheirinstructor—ortheirfutureboss—that
theyhaveasolutionthatiseverybitasreliableasananalyticalsolution,althoughwithout
theanalyticalformandforaproblemthatcannotbesolvedanalytically.Infact,98%ofthe
problemsinthisbookarenonlinearandonlyafewofthemhaveanalyticalsolutions.
HOWTOUSETHISBOOKINTEACHING
ThisbookgrewoutofacourseIdevelopedattheUniversityofWashington,beginningin
2003.Thecourseispartlectureandparthands-oncomputerworkinacomputerlaboratory.
I usually provide simple problems for the students to solve in the laboratory, when help
is available, to help them get over the barrier of using an unfamiliar program. But then,
students have to solve a problem that expands their knowledge of chemical engineering
and demonstrates they have used the program correctly (and described the checks they
made).Sincetheapplicationscovermuchofthechemicalengineeringfield,Ijokewiththe
students, saying, “I’m teaching you the entire field in 20 hours.” Although I retired from
teachingthecoursein2009,thesameobjectivesstillapply.
Thisbookcanalsobeusedinothercoursessinceeachchapteriskeyedtoacoursein
thecurriculum.OncechemicalreactionequilibriumhasbeendiscussedintheThermody-
namicsclass,forexample,instructorscanholdalaboratorysessionthatteachescomputer
applications,usingthechapteronchemicalreactionequilibrium.Thematerialonchoiceof
thermodynamicmodel(andcomparisons)alsoaddsabitofrealismtotheThermodynamics
course.Otherchapterscouldbeusedinothercourses.Inthisway,thestudentswoulduse
thebookduringtheirentireeducation,incourseaftercourse:MassandEnergyBalances,
Transport of Heat, Mass, and Momentum, Reactor Design, and courses concentrating on
projectssuchasbiomedicalengineering.Thehopeis,ofcourse,thatstudentswouldthen
beabletoconcentratemoreonthechemicalengineeringprinciplesandusethecomputer
asatool.
There are four programs that are featured in this book. It is possible that your school
doesnotuseallfour.Althoughthescreenimagesmaybedifferent,theideasandprocedures
are the same. Certainly the problems can be solved using other programs. In a working
environment,engineersusewhattheircompanyprovides.Thus,engineersmayusealess
powerfulprogrambecauseitisavailable.Themorepowerfulprogrammaycostmore,too.
Thus,inseveralchapters,thesameproblemissolvedusingdifferentprograms,whichlets
studentsseefirst-handthatthemoregeneralpurposeprogramsrequiresignificantlymore
programming to solve complicated problems. In my experience, when given a suite of
programs, students will use the one that allows them to solve their problem fastest. The
programComsolMultiphysicscomesinmanymodules.Nearlyalltheproblemsinthisbook
canbesolvedbythebasicmodule,althoughtherearecaseswheretheChemicalReaction
Engineering Module is useful. Connections with MATLAB are made with LiveLinkTM
```

---

## Стр. 15

```text
P1:OTA/XYZ P2:ABC
JWBS084-Preface JWBS084-Finlayson March28,2012 7:53 PrinterName:YettoCome Trim:7in×10in
PREFACE xvii
for MATLAB, another module. There are only a couple of problems involving turbulent
flow, and those require the CFD module. A complete list of what you get with various
combinationsisavailablefromComsolandmylistisonthebookwebsite(seeAppendixD).
Eachchapterbeginswithalistofinstructionalobjectives.Inaddition,thebookwebsite
has a list of principles learned from each problem, both from a chemical engineering
viewpointandacomputer/computertechniqueviewpoint.Professorsthatusethebookare
encouraged to discuss possible use in other chemical engineering courses so that more
advanced problems can be solved in them, too. The indices are available on the book
website,too,sincestudentspreferusingtheInternetratherthanturningtothebackofthe
book;moreimportantly,theycanbedownloadedandsearchedforaphrase.
WHATISNEW?
Onebigchangefromthefirsteditionisthefactthatallfourprogramsnowhavedifferent
interfacesthantheydidin2005.Moreimportantly,theyhavegreatlyenhancedcapabilities.
Ihavecutbackonsomeexplanationsandrefertheusertothehelpmenusthatcomewith
the programs, since those have improved, too, and they give more information than the
bookcan.But,Iprovidehintswheretolook.
The number of problems has approximately doubled. More importantly, the added
problemsareconcentratedinthefieldofenergy:integratedgas-combinedcycle,including
low temperature air separation, making ethanol from switchgrass, and pressure swing
adsorption to make hydrogen to fuel cars. In each case a discussion of the field precedes
the definition of the problem so that students can see the applicability. Microfluidics has
expandedsince2005,andthereareaddedproblemsinthefieldofbiomedicalapplications.
Thishasleadtomanymoreexamplesandproblemsinvolvingfluidflowanddiffusionintwo
andthreedimensions.AnimportantadditionwasmadeinAspenPlus7.3:nowyouhave
direct access within the program to experimental data on pressure–volume–temperature
of pure components and binary vapor–liquid equilibria as summarized by the National
InstituteofStandardsandTechnology.Thisisveryimportantforchemicalengineers,since
the choice of thermodynamic model must usually be accompanied by a comparison with
experimentaldata,andthatisnowmadeveryeasy—soeasythatitwouldbeunprofessional
nottodothecomparison.Thus,thethermodynamicsectionsofthebookincludeindustrial
guidelines,somemolecularconsiderations,andexperimentaldataforcomparison.Aspen
Plusalsohasthecapabilitytoeasilysummarizethegreenhouseimpactofaprocess.There
are talks made by professors about how they used AspenTech products in their courses;
contact: University.Program@aspentech.com. One thing that is pointed out by Professor
Luyben is that material and energy balances are primarily flow-based, whereas safety
problems must be pressure based (and dynamic). The dynamic options are not treated
hereindetail,butareoftencoveredinacontrolcourse.AspenPlusrunsunderMicrosoft
Windows,buttheauthorranitunderWindowsbyusingParallelsDesktopforMaconan
Applecomputer.ThesecondeditionalsohasexamplesrunningAspenPluswithasimple
user-definedFORTRANprogram.
Someprofessorsliketohavemorenumericalprogrammingintheircourses,soanumber
of problems like that have been added to the end of many chapters. They make a good
contrast—solvethemusingthenumericalprogrammingandthensolvethemusingoneof
thefourprogramsemphasizedheretocomparetheeaseofuseofeachmethod.AppendixE
providesmoredetailaboutthenumericalmethods.Whiletheprogramsmakethenumerical
```

---

## Стр. 16

```text
P1:OTA/XYZ P2:ABC
JWBS084-Preface JWBS084-Finlayson March28,2012 7:53 PrinterName:YettoCome Trim:7in×10in
xviii PREFACE
analysis easy to use, it is also important to recognize that most problems involve an
approximationfromcontinuoustodiscretevariables.Afewproblemsinthebookaskthe
studentstodotheactualnumericalanalysis(andcomparewithotherprograms).Instructors
maysay,“Ifyoudon’tprogramthemethod,youhaven’treallyunderstoodtheproblem.”
Ireplybypointing outthatwhenadoctor prescribesanMRI,youdonotsayyouwould
not do it until he/she explains how the magnetic field works in the machine, discusses
hydrogenmoleculesflippingorientation,anddescribeshowtheimagingtakesplace.The
doctorandtechnicianknowhowtointerprettheresultsandhowtodetectifthemachineis
notoperatingcorrectly;engineeringstudentscandothat,too.
Thenumberofproblemshasbeendoubled,andtheyareorganizedintoeasyproblems
(subscript1),harderproblems(subscript2),andproblemsthataresuitableasprojects,either
foronestudentorforteams.Finally,moretechniquesthatareinComsolMultiphysicsare
explained.
Thecodeusedtosolvetheexamplesinthebookisnotprovidedonthebookwebsite,
because the author believes that learning takes place when you try to duplicate the steps
in the book. However, some material needed to start problems is on the book website,
such as geometries for three dimensional flow/diffusion problems. Depending upon the
memory of your computer, and what can be allocated to Comsol Multiphysics, some of
thethreedimensionalproblemsmaynotbesolubleonyourcomputer.Thebookwebsiteis
http://www.ChemEComp.com.
ACKNOWLEDGMENTS
In writing this book, I owe a great thanks to the students in my classes. Sometimes
students taught me how to use an advanced technique, and their questions brought
out the best of the programs. I had over 100 undergraduate research students work
with me over the past decade, and the results of their work are available on my web-
sites: http://faculty.washington.edu/finlayso/ and http://courses.washington.edu/microflo.
The Department provided a challenge grant to write textbooks, funded by a gift in the
memoryofalumnusMauriceRichford,BS1926.Withoutthatchallengegrant,thefirstedi-
tionwouldnothavebeenwrittensoitcouldnothavebeenrevised.Mydaughter,Christine
Finlayson,improvedmywritinggreatlybyservingasacopyeditorofthefirstedition,and
the clarity is due to her work; any confusion left is my responsibility. I thank especially
ProfessorStanleySandler,UniversityofDelaware,forreviewingtherevisedtreatmentof
thermodynamics—Ilearnedalot,too!ThefolksatComsolandAspenTechhavebeenvery
helpfulsincebothComsolMultiphysicsandAspenPlushavebeenimprovedoverthepast
fewyears.Mostofall,Ithankmywife,Pat,forputtingupwiththelonghoursofworkthat
suchaprojectrequires.Shehasalwayssupportedmeandmadesacrificesthatenabledme
tofinish.AndIwassmartenoughtotakeafewweeksofffromthisrewritetocelebrateour
50thweddinganniversary!
BruceFinlayson
Seattle,October,2011
```

---

## Стр. 17

```text
P1:OTA/XYZ P2:ABC
JWBS084-c01 JWBS084-Finlayson May31,2012 10:7 PrinterName:YettoCome Trim:7in×10in
1
INTRODUCTION
Computershaverevolutionizedthewaychemicalengineersdesignandanalyzeprocesses,
whetherdesigninglargeunitstomakepolyethyleneorsmallmicroreactorsusedtodetect
biologicalagents.Infact,theengineeringproblemsthatmanyofyouwillstudyasunder-
graduatesaresimilarincomplexitytoproblemsPhDstudentssolved30or40yearsago.
Computer programs can now solve difficult problems in a fraction of the time it used to
take.Nowadays,younolongerhavetowriteyourownsoftwareprogramstousecomputers
effectively.Computerprogramscandothenumericalcalculationsforyou,butyouwillstill
needtounderstandhowtoapplytheseprogramstospecificengineeringchallenges.
Thegoalofthisbookistohelpyoupracticebetterchemicalengineering.Computersare
valuable tools that enable progressive, far-reaching chemical engineering. Unfortunately,
computers arenotas basicasDVDplayers,whereyou insertaDVD,pushabutton,and
getthesameresulteverytime.Sometimescomputerprogramsdonotworkproperlyforthe
parametersyouhavegiventhem.Thus,youmustbecarefultousethemwisely.
Thisbookwillalso
1. Illustratetheproblemsthatyouaschemicalengineersmayneedtosolve.
2. Comparethetypesofcomputerprogramsyoucanuseandillustratewhichonesare
bestforcertainapplications.
3. Describehowtocheckyourworktoensureyouhavesolvedtheproblemscorrectly.
This book demonstrates four computer programs: Excel®, MATLAB®, Aspen Plus®,
and Comsol Multiphysics®. You may have access to other programs created by other
companies.Whiletheexactdetailswillnotbethesame,thestepsyoutakewillbesimilar.
Computer skills are invaluable, but as an engineer, you also need to understand
the physical phenomena. Each chemical engineering application chapter starts with a
IntroductiontoChemicalEngineeringComputing,SecondEdition.BruceA.Finlayson.
©2012JohnWiley&Sons,Inc.Published2012byJohnWiley&Sons,Inc.
1
```

---

## Стр. 18

```text
P1:OTA/XYZ P2:ABC
JWBS084-c01 JWBS084-Finlayson May31,2012 10:7 PrinterName:YettoCome Trim:7in×10in
2 INTRODUCTION
description of the physical problem in general terms. Then those general terms are put
into a mathematical context so the computer can represent them. Next, the chapter gives
severalexamplesinwhichsuchproblemsaresolved,providingstep-by-stepinstructionsso
youcanfollowalongonyourowncomputer.Sometimes,thesameproblemissolvedusing
different programs so you can see the advantages of each program. Finally, the chapters
givemorecomplicatedproblemsyourinstructormayuseashomeworkproblems.
Examplesthroughoutthisbookdemonstratehowtocheckyourworkandhowtolearn
fromtheanswersthecomputergivesyou.Whenusingcomputers,itisalwaysimportantto
knowifthecomputerobtainedthecorrectanswer.Ifyoufollowthisstrategyyouwillhave
notroubleconvincingyourinstructor—oryourboss—thatyouhaveasolutioneverybitas
reliableasananalyticalsolutionforaproblemthatcannotbesolvedanalytically:
1. Solvetheproblem
2. Validateyourwork
3. Understandhowyoureachedthatanswer
ORGANIZATION
ThebookisorganizedintoelevenchaptersfollowedbyfiveappendicesaslistedinTable1.1.
Eachchaptertreatsatypeofchemicalengineeringphenomenon,suchasprocesssimulation
TABLE1.1 ComputerProgramsUsedinDifferentChapters
Aspen Comsol Numerical
Chapters Excel MATLAB Plus Multiphysics Methods
1 Introduction √ √ √ √
2 Equationsofstate √ √ √ √
3 Vapor–liquidequilibria √ √ √ √
4 Chemicalreactionequilibria √ √
5 Massbalanceswithrecyclestreams √
6 Simulationofmasstransfer
equipment √
7 Processsimulation √ √ √ √ √
8 Chemicalreactorsandinitialvalue
problems √ √ √ √ √
9 Transportprocessesin1Dand
boundaryvalueproblems √
10 Navier–Stokesequationin2Dand3D √ √
11 Convectivediffusionequationin2D
and3Dandellipticpartial
differentialequations √
A HintswhenusingExcel √
B HintswhenusingMATLAB √
C HintswhenusingAspenPlus √
D HintswhenusingComsol
Multiphysics √ √ √ √ √
E Mathematicalmethods
```

---

## Стр. 19

```text
P1:OTA/XYZ P2:ABC
JWBS084-c01 JWBS084-Finlayson May31,2012 10:7 PrinterName:YettoCome Trim:7in×10in
ORGANIZATION 3
orconvectivediffusion.Fouroftheappendicesgiveadditionaldetailsabouteachcomputer
program. The fifth appendix provides the nitty-gritty details of many of the numerical
methods.Anappendixonparameterestimationthatwasinthe1steditionisavailableon
thebookwebsite.
Asamodernchemicalengineeringstudent,manyofyouarecomputer-savvy.Thisbook
assumesthatyouarenotacompletebeginner,buthavesomeexperiencewithspreadsheet
programssuchasExcel.Thechaptersprovideexamplesandstep-by-stepinstructionsfor
usingthecomputerprogramstosolvechemicalengineeringproblems.Ifneeded,youcan
findmoredetailedinformationabouttheindividualprogramsintheappendices.
AlgebraicEquations
Chapters 2–5 deal with chemical engineering problems that are expressed as algebraic
equations—usually sets of nonlinear equations, perhaps thousands of them to be solved
together. In Chapter 2, you can study equations of state that are more complicated than
the perfect gas law. This is especially important because the equation of state provides
the thermodynamic basis for not only volume but also fugacity (phase equilibrium) and
enthalpy(departurefromidealgasenthalpy).Chapter3coversvapor–liquidequilibrium,
andChapter4coverschemicalreactionequilibrium.Allthesetopicsarecombinedinsimple
processsimulationinChapter5.Thismeansthatyoumustsolvemanyequationstogether.
ThesefourchaptersmakeextensiveuseofprogramminglanguagesinExcelandMATLAB
aswellasAspenPlus.
ProcessSimulation
Chapter 6 provides an extensive discussion of the possible (and reasonable) choices of
thermodynamicmodels,andhowyoucheckyourchoice.Itthenintroducesmasstransfer
problems such as distillation and absorption and single units. Chapter 7 gives a more
detailedlookatprocesssimulation,wherethepowerofprocesssimulatorslikeAspenPlus
really is evident. These chapters make use of commercial codes that are run by inserting
dataintotheircustom-designedinterface.
DifferentialEquations
Chapters8–11treatproblemsthataregovernedbydifferentialequations.Chapter8gives
methods to model chemical reactors. These are usually initial value problems, which are
illustratedinEq.(1.1):
dc
u =−kc2, c(z =0)=c (1.1)
0
dz
Note that the dependent variable, c, is a function of only one independent variable, z,
andthattheinitialvalueisspecified.Forreactors,youstartattheinletandintegratedown
thereactorusingeitherExcel,MATLAB,AspenPlus,orComsolMultiphysics.
Chapter 9 then solves transport problems in one space dimension (1D) using Comsol
Multiphysics. If you consider heat transfer through a slab, one side of the slab is kept at
```

---

## Стр. 20

```text
P1:OTA/XYZ P2:ABC
JWBS084-c01 JWBS084-Finlayson May31,2012 10:7 PrinterName:YettoCome Trim:7in×10in
4 INTRODUCTION
one temperature, T , and the other side of the slab is maintained at another temperature,
0
T .Thegoverningequationis
L
d2T
k =0 (1.2)
dx2
withboundaryconditions
T(0)=T , T(L)=T (1.3)
0 L
Thedifferentialequation,(1.2),isanordinarydifferentialequationbecausethereisonly
oneindependentvariable,x.Inthiscase,equationsinonespacedimensionareboundary
value problems, because the conditions are provided at two different locations. While
it is also possible to solve this problem using Excel, it is much simpler to use Comsol
Multiphysics or MATLAB since the numerical analysis will have been done for you.
Transientheattransferinonespacedimensionisgovernedby
∂T ∂2T
ρC =k (1.4)
p ∂t ∂x2
andthisproblemcanbesolvedusingComsolMultiphysicsorMATLAB,too.
Chapters 10 and 11 use Comsol Multiphysics to solve fluid flow, heat transfer, and
mass transfer problems in 2D and 3D. Here, again the power of the software program
showsthrough.Yougettosolverealproblemsthatgobeyondthesimple1Dcasesinyour
textbook.Those1Dproblemsaregoodforlearningthesubject,butinreal-lifesituations,
complicationsoftenarisethatcanonlybehandlednumerically.Theseproblemsarepartial
differentialequations,becausetherearetwoormoreindependentvariables(sayxandy).
Forexample,theNavier–StokesequationsinCartesiangeometryandtwodimensionsare
(cid:2) (cid:3) (cid:2) (cid:3)
∂u ∂u ∂u ∂p ∂2u ∂2u
ρ +u +v =− +μ +
∂t ∂x ∂y ∂x ∂x2 ∂y2
(cid:2) (cid:3) (cid:2) (cid:3)
∂v ∂v ∂v ∂p ∂2v ∂2v
ρ +u +v =− +μ + (1.5)
∂t ∂x ∂y ∂y ∂x2 ∂y2
∂u ∂v
+ =0
∂x ∂y
Appendices
Ifyouneedmorebackgroundinformationwhilesolvingtheproblemsinthebook,consult
theappendices.AppendicesA–Ddiscusshints,examples,andstep-by-stepinstructionsfor
thefourcomputerprogramsdemonstratedinthisbook.Youareencouragedtoconsultthe
appendices while looking at examples or solving problems using those programs—many
ofthedetailsaresummarizedintheappendices.AppendixEillustratesthemathematical
methods built into each computer program. While you will not usually need to program
the methods, you may be curious about the mathematical analysis behind the programs.
An appendix on parameter estimation using Excel or MATLAB is available on the book
website.
```

---

## Стр. 21

```text
P1:OTA/XYZ P2:ABC
JWBS084-c01 JWBS084-Finlayson May31,2012 10:7 PrinterName:YettoCome Trim:7in×10in
ORGANIZATION 5
Whether you tackle one chemical engineering problem or work chapter by chapter
through the book, try to enjoy yourself. You and a classmate can sit down and work
together—possibly on adjacent computers—to share insights and answer each others’
questions.Remember,too:gobackandforthfromtheapplicationchapterstothecomputer
program appendices; build up your knowledge bit by bit. Your reward is to be a better-
trained engineer, be able to use your inherent creativity, and be able to compete in a
fast-paced global environment. As you take other chemical engineering courses you can
use the programs to solve more advanced problems that are not soluble using analytical
methods.Ninety-eightpercentoftheproblemsinthisbookarenonlinearandfewofthem
haveanalyticalsolutions.
```

---

## Стр. 22

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
2
EQUATIONS OF STATE
Solvingequationsofstate(EOS)allowsustofindthespecificvolumeofagaseousmixture
of chemicals at a specified temperature and pressure. Without using equations of state, it
wouldbevirtuallyimpossibletodesignachemicalplant.Byknowingthisspecificvolume,
youcandeterminethesize—andthuscost—oftheplant,includingthediameterofpipes,
the horsepower of compressors and pumps, and the diameter of distillation towers and
chemicalreactors.Imaginehowchallengingitwouldbetodesignaplantwithoutknowing
thisimportantinformation!
Determining the specific volume is the first step in calculating the enthalpy and
vapor–liquidpropertiesofmixtures.Calculatingthisenthalpyisespeciallyimportantwhen
makingenergybalancestoreduceenergyuseandhelptheenvironment.Inthischapter,we
workonlywiththevaporphase,andtheliquidphaseisintroducedinthenextchapter.
To solve equations of state, you must solve algebraic equations as described in this
chapter. The later chapters cover other topics governed by algebraic equations, such as
phaseequilibrium,chemicalreactionequilibrium,andprocesseswithrecyclestreams.This
chapter introduces the ideal gas EOS, then describes how computer programs such as
Excel®, MATLAB®, and Aspen Plus® use modified EOS to easily and accurately solve
problemsinvolvinggaseousmixtures.
Step-by-step instructions will guide you in using each of these computer programs to
determinethespecificvolumeofgaseousmixtures.Practiceproblemsaregivenattheendof
thechapter.Thelessonslearnedfromthischapterarecarriedforwardtootherapplications
involving algebraic equations in Chapters 3–6 and 8. After completing this chapter, not
onlywillyoubeabletosolvealgebraicequationsbutyouwillalsobeabletodeterminethe
sizeoftheequipmentinachemicalplant,certainlythesizeofthosepiecesofequipment
containinggases.
IntroductiontoChemicalEngineeringComputing,SecondEdition.BruceA.Finlayson.
©2012JohnWiley&Sons,Inc.Published2012byJohnWiley&Sons,Inc.
7
```

---

## Стр. 23

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
8 EQUATIONSOFSTATE
InstructionalObjectives: Afterworkingthroughthischapter,youshouldhave
1. UpdatedyourskillsusingExcel.
2. LearnedtouseMATLABforsimpleproblems.
3. LearnedtouseAspenPlustoperformthermodynamiccalculations.
4. Learnedtocheckyournumericalwork.
5. Reviewed and expanded your chemistry and chemical engineering knowledge of
EOS.
EQUATIONSOFSTATE—MATHEMATICALFORMULATION
The ideal gas EOS, which relates the pressure, temperature, and specific volume, is a
familiarequation:
V
pV =nRT or pvˆ = RT wherevˆ = (2.1)
n
Thetermpistheabsolutepressure,V isthevolume,nisthenumberofmoles,Risthe
gasconstant,andT istheabsolutetemperature.TheunitsofRhavetobeappropriatefor
theunitschosenfortheothervariables.Thisequationisquiteadequatewhenthepressure
islow(suchas1atm).However,manychemicalprocessestakeplaceatveryhighpressure.
Forexample,ammoniaismadeatpressuresof220atmormore.Undertheseconditions,the
idealgasEOSmaynotbeavalidrepresentationofreality.Inparticular,theidealgas,while
itincludesrotationalandvibrationaldegreesoffreedom,ignoresintramolecularpotential
energy, which is important when the molecules are closer together at high pressure. The
rule-of-thumb is that the ideal gas is a good approximation for pressures up to 10 atm,
althoughthiscanchangedependingonthetemperature.
Other equations of states have been developed, usually in conjunction with process
simulators,toaddresschemicalprocessesathighpressure.Therearetwokeycriteria:(1)
theequation isable torepresentthe realp–V–T behavior and (2)theparameters mustbe
easily found, including for mixtures. This last criterion is no small requirement. There
are more than 25 million chemicals, leading to an infinite number of different mixtures.
Obviously,youcannotlookupthepropertiesofallthosemixturesontheWeb.
ThefirstgeneralizationoftheidealgaslawwasthevanderWaalsEOS:
RT a
p = − (2.2)
vˆ−b vˆ2
Inthisequation,the“b”accountsfortheexcluded volume(asecondmoleculecannot
usethesamespacealreadyusedbythefirstmolecule),andthe“a”accountsfortheforce
ofinteractionbetweentwomolecules.Thisextensionisjustafirststep,however,because
itwillnotbeagoodapproximationatextremelyhighpressures.Theconstantsaandbare
giveninTable2.1.
TheRedlich–KwongEOS(1949)isamodificationofthevanderWaalsEOS:
RT a
p = − (2.3)
vˆ−b vˆ(vˆ+b)
```

---

## Стр. 24

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
stnenopmoCeruProfetatSfosnoitauqE
1.2ELBAT
Z
ω
α
b
a
SOE
ledoM
c
(cid:3)
(cid:2)
(cid:3)
(cid:2)
TRn=
Vp
saglaedI
TR
2T2R
a
TR
573.0
c
521.0=b
c
88124.0=a
−
=p
laaWrednav
p
p
2vˆ
b−vˆ
(cid:3)
c(cid:2)
(cid:3)
c
(cid:2)
1
TR
2T2R
a
TR
333.0
=α
c
46680.0=b
α
c
84724.0=a
−
=p
gnowK–hcildeR
5.0T
p
p
)b+vˆ(vˆ
b−vˆ
r
(cid:3)
c
(cid:2)
(cid:3)
c
(cid:2)
(cid:7)(cid:6)
(cid:5)
(cid:4)
TR
2T2R
a
TR
333.0
084.0=
m
2
5.0T−1
m+1
=α
c
46680.0=b
α
c
84724.0=a
−
=p
evaoS–KR
ω475.1+
r
c p
c p
)b+vˆ(vˆ
b−vˆ
2ω671.0−
(cid:3)
(cid:2)
(cid:3)
(cid:2)
(cid:7)(cid:6)
(cid:5)
(cid:4)
TR
2T2R
a
TR
703.0
46473.0=
m
2
5.0T−1
m+1
=α
c
08770.0=b
α
c
42754.0=a
−
=p
nosniboR–gneP
ω62245.1+
r
c p
c p
)b−vˆ(b+)b+vˆ(vˆ
b−vˆ
2ω29962.0−
9
```

---

## Стр. 25

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
10 EQUATIONSOFSTATE
where equations for a and b are given in Table 2.1 in terms of the critical temperature
andpressureandthereducedtemperature,T =T/T .Intheseequations,T isthecritical
r c c
temperature(inabsoluteterms),p isthecriticalpressure,T iscalledthereducedtemper-
c r
ature(theabsolutetemperaturedivided bythecriticaltemperature).α isparticulartothe
Redlich–KwongEOS.
The Redlich–Kwong EOS was modified further by Soave to give the Redlich–
Kwong–Soave EOS (Soave, 1972) (called RKS in Aspen Plus, see Table 2.1)1, which
is a common one in process simulators. The purpose of the modification was to account
for situations in which the molecular structure was asymmetric by introducing the Pitzer
acentricfactor,ω,whichisatabulatedquantityformanysubstances.Thus,thevalueofα
canbecomputedforeachchemicalandreducedtemperature.
The Peng–Robinson EOS (1976) is another variation appropriate for molecules that
are asymmetric, and it is an important one that is used in later chapters to improve the
simulationofvapor–liquidequilibria:
RT a
p = − (2.4)
vˆ−b vˆ(vˆ+b)+b(vˆ−b)
OnecriterionthatcanbeappliedtotheEOSisthevalueofthecompressibilityfactorat
thecriticalpoint.Experimentalvaluesrangefrom0.23to0.31(Sandler,2006).AsTable2.2
shows,thePeng–RobinsonEOSisclosesttosatisfyingthiscondition.
Alltheseequationscanberearrangedintoacubicfunctionofspecificvolume.Theform
oftheRedlich–KwongandRedlich–Kwong–SoaveEOSis
vˆ3(p)−vˆ2(RT)+vˆ(a− pb2− RTb)−ab=0 (2.5)
Whenthetemperatureandpressureofagaseousmixture,andtheparametersaandbare
given,thentofindthespecificvolumeyouwouldhavetosolvethecubicEOSforspecific
volume, vˆ. This represents one algebraic equation in one unknown, the specific volume.
ThePeng–RobinsonEOSresultsin
vˆ3(p)+vˆ2(bp− RT)+vˆ(a−3pb2−2RTb)+(pb3+ RTb2−ab)=0 (2.6)
Forapurecomponent,theparametersaandbaredeterminedfromthecriticaltempera-
tureandcriticalpressure,andpossiblytheacentricfactor.Thesearealltabulatedquantities,
andthereareevencorrelationsforthemintermsofvaporpressureandnormalboilingpoint,
forexample.Formixtures,itisnecessarytocombinethevaluesofaandbforeachcom-
ponentaccordingtothecompositionofthegaseousmixture.Sincetheparametersaandb
comeaboutbecauseofintramolecularpotentialenergy,itcanbejustifiedthatwhenspecies
1isinamixturewithspecies2,themolecule1willinteractdifferentlywithmolecule2than
itdoes withanother molecule 1.Furthermore,theinteractionofmolecule1withanother
molecule1willbethesameasinapurespecies(usually),andwillbeproportionaltothe
molefractionsquared(i.e.,therelativeamountofbothofthem).Thus,anexpectedform
ofthemixingruleforabinaryis(Koretsky,2004)
a = y2a +y y a +y y a +y2a = y2a +2y y a +y2a (2.7)
1 1 1 2 12 1 2 21 2 2 1 1 1 2 12 2 2
1AspenPlusalsohasaSoave–RKequation,whichdiffersslightly.Inthistext,theyareusedinterchangeably.
```

---

## Стр. 26

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
serutxiMrofetatSfosnoitauqE
2.2ELBAT
b
a
α
b
a
ledoM
i
i
(cid:3)
(cid:2)
(cid:3)
(cid:2)
(cid:3)
(cid:2)
PM(cid:8)OCN
2
PM(cid:8)OCN
1
TR
2T2R
by
=b
5.0ay
=a
=
α
ic
46680.0=
b
α
ic
84724.0=
a
gnowK–hcildeR
i
i
1=i
i
i
1=i
5.0
ir
T
i
ic
p
i
i
ic p
i
(cid:3)
(cid:2)
(cid:3)
(cid:2)
(cid:3)
(cid:2)
PM(cid:8)OCN
2
PM(cid:8)OCN
(cid:7)(cid:6)
(cid:5)
(cid:4)
TR
2T2R
by
=b
5.0ay
=a
2
5.0T−1
m+1
=
α
ic
46680.0=
b
α
ic
84724.0=
a
evaoS–KR
i
i
1=i
i
i
1=i
ir
i
i
(cid:3)
ic
p
(cid:2)
i
i
(cid:3)
ic p
(cid:2)
i
PM(cid:8)OCN
PM(cid:8)OCN
(cid:7)(cid:6)
(cid:5)
(cid:4)
TR
2T2R
by
=b
a
y
y
=a
2
5.0T−1
m+1
=
α
ic
08770.0=
b
α
ic
42754.0=
a
nosniboR–gneP
i
i
1=i
ji
j
i
1=j,i
ir
i
i
ic
p
i
(cid:6)
i
(cid:5)ic
p
√
ii
k−1
a
a
=
a=
a
ji
jj
ii
ij
ji
11
```

---

## Стр. 27

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
12 EQUATIONSOFSTATE
because the interaction of molecule 1 with molecule 2 is the same as the inverse. The
mixingruleforthebparameterrepresentingtheexcludedvolumeisexpectedtobealinear
equationbasedontherelativeamountofeachspecies:
b= y b +y b (2.8)
1 1 2 2
CommonmixingrulesformulticomponentmixturesareshowninTable2.2intermsof
the pure component properties {a ,b ,α} for the major equations of state. The {k } for
i i i ij
thePeng–Robinsonequationarecalledbinaryinteractionparametersandaretabulatedfor
manybinarymixtures(Sandler,2006).Thus,theonlydifferencebetweenthemathematical
problem for a pure component and for a mixture is in the evaluation of the parameters a
andb.
Here is a mathematical problem to be solved. Given a set of chemicals, temperature
andpressure,findthespecificvolumeofthemixture.Todothis,youmustfindthecritical
temperature and pressure of each chemical, plus possibly the acentric factors. Once you
havetheparameters,youmustsolvethecubicequation,Eq.(2.5or2.6),whichisanonlinear
equationinonevariable.Becauseitisacubicequation,itispossibletofindthesolutionin
aseriesofanalyticalsteps(PerryandGreen,2008,pp.3–10),butthisisnotusuallydone
becauseitisquickertofindthesolutionnumerically,albeititeratively.
Programs such as Excel and MATLAB allow us easily to solve the specific volumes.
However,oneadvantageofprocesssimulatorslikeAspenPlusisthatthephysicalproperties
ofmanycomponentsaresavedinadatabasethatuserscanaccess.Infact,usersdonotneed
tolookupthenumbersbecauseAspenPluswilldothatwhenitneedsthem.Inaddition,
some of the equations of state involve much calculation, all of which is subject to error.
However,therearesituationswhenyouwillneedtoprogramtheequationsyourself.The
nextsectionillustrateshowtouseeachoftheseprogramstosolveequationsofstate.
SOLVINGEQUATIONSOFSTATEUSINGEXCEL2
(SINGLEEQUATIONINONEUNKNOWN)
ThereareatleasttwomethodstosolvealgebraicequationsusingExcel.Thefirstoneuses
“GoalSeek”whiletheotheruses“Solver,”andbothareillustratedusingasimpleexample:
findthexthatmakesf(x)zero:
f(x)= x2−2x −8 (2.9)
SolutionUsing“GoalSeek”
Step1 OpenaspreadsheetandputthefollowingstatementincellB1.
=A1∗A1 - 2∗A1 − 8
Cell B1 is the equation that should be zero, and cell A1 contains the variable that is
adjustedtomakethishappen.
2ExcelisaregisteredtrademarkofMicrosoftCorporation,Inc.
```

---

## Стр. 28

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
SOLVINGEQUATIONSOFSTATEUSINGEXCEL(SINGLEEQUATIONINONEUNKNOWN) 13
Step2 Under“Tools”choose“GoalSeek.”Whenasmallscreenappears,fillinthespaces
toshowthefollowing:
Setcell $B$1
Tovalue 0
Bychangingcell A1
Step3 ClickOK.Theanswerappearsinthespreadsheet.
-2.000007 4.1137E-06
Thus,thesolutionfoundis−2,withatinyerror-–asmallfractionofapercent.Thetest
ofwhetherthecalculationiscorrectisshownincellB1,whichis4.1×10−6.Thisisnot
zero,butitissmallenoughformostpurposes.
Step 4 If you want to decrease the tolerance to make the solution more accurate, under
“Tools”and“Options”choose“Calculation.”Then,in“MaximumChange”addafewzeros
inthemiddle(changingitfrom0.001to0.000001),addazerotothemaximumnumberof
iterations,chooseOK,andrepeatthe“GoalSeek.”Thistimetheansweris
-2 -1.376E-8
Step5 Togettheotherroot,putthevalue3incellA1andchoose“GoalSeek.”
SolutionUsing“Solver”
Youcansolvethesameproblemusingthe“Solver”optioninExcel.
Step 1 Under the Tools menu, click on “Solver.” Note: If the choice “Solver” does not
appear, choose Add-Ins and loadSolver fromthe Analysis ToolPak or theoriginal Excel
program disk (or see your system administrator for help). For the Macintosh, install the
SolverprovidedbyFrontlineSystems.
Step 2 When the window opens, choose the option to make a cell equal to a value (or
a maximum or minimum) by changing another cell. If you insert the appropriate cell
locations,youwillobtainthesameansweraswith“GoalSeek.”Thistime,however,itis
muchmoreaccurate.
-2 5.3291E-14
ExampleofaChemicalEngineeringProblemSolvedUsing“GoalSeek”
Find the specific volume of n-butane at 393.3 K and 16.6 atm using the Redlich–Kwong
EOS.Themolecularstructureofn-butaneissymmetric,soweexpecttheRedlich–Kwong
EOS to give values close to experimental ones, and using Redlich–Kwong–Soave or
Peng–Robinson may not be necessary. Since the pressure is above 10 atm, we expect
somedifferencesbetweenthepredictionsbyanyoftheseequationsandtheresultsforan
idealgas.
```

---

## Стр. 29

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
14 EQUATIONSOFSTATE
A B C D E F G
18 Redlich-KwongEquationofState
19 n-Butane
20 BruceFinlayson
21
22 Parameters-n-Butane Data
23 Tc 425.2 K T 393.3 K
24 pc 37.5 atm p 16.6 atm
25 R 0.08206 liter-atm/gmolK
26
27 Formulas Results
28 Tr F23/B23 Tr 0.9250
29 a 0.42748*(B25^2*B23^2/B24)*(B23/F23)^0.5 a 14.4301
30 b 0.08664*(B25*B23/B24) b 0.0806
31 f(v) F24*F31^3-B25*F23*F31^2 v 1.5064 liter/gmol
32 +(F29-B25*F23*F30-F24*F30^2)*F31-F29*F30 f(v) 1.358E-08 Eq.(2.4)
33 idealgas volume B25*F23/F24 idealgas 1.9442 Eq.(2.1)
FIGURE 2.1 Excelspreadsheettofindthevolumeofanonidealgas.
Step 1 You must first find the critical temperature and pressure; Perry and Green (2008)
givesT =425.2Kandp =37.5atm.
c c
Step2 Calculatevaluesof“a”and“b”usingtheformulaeinTable2.1.Thevalueofgas
constantintheseunitsis0.08206L-atm/gmolK.
Step3 PreparethespreadsheetshowninFigure2.1.Thetitle,name,anddatawillbeuseful
whenyoucomebacktotheproblematafuturedate.
Step 4 You enter the parameters in the parameter box. The cells containing the critical
parametersandthetemperatureandpressurecanbenamed,Tc,pc,T,andp,respectively.
Thatwaytheequationforf(v)wouldbeeasiertounderstand.
Step5 Thelowerboxgivestheequationsactuallyusedaswellastheresults.Usethe“Goal
Seek”commandtomakef(v)(cellF32)equaltozerobychangingcellv(F31).
Step6 Forreference,theresultforanidealgasisalsoshown,andindeedn-butaneisnot
wellrepresentedbyanidealgasundertheseconditions.
Step7 Howcanyoucheckthisresult?First,youhavetobesureyouhaveputthecorrect
formulasintothespreadsheet,andthattheunitsareconsistent.Thatcanonlybedetermined
byreferencetotheoriginalequationsandcriticalproperties.Itiseasytotellthatf(v)=0,
butthesolutioniscorrectonlyiftheequationforf(v)iscorrect.Infact,themostchallenging
part of checking this calculation is the paper and pencil work before you developed the
spreadsheet—to test the equations in the spreadsheet. Calculate the value of a on your
calculator—is it the same as in the spreadsheet? You can also find a published problem,
insertthosevaluesofaandbandseethatyougetthepublishedresult.(Thatworkshere,
too, when you go to solve the problems at the end of the chapter.) Be careful, though: it
is possible that for a certain pressure and temperature some of the terms in the cubic are
toosmalltorevealanerrorwhentheonlycheckisthefinalresult.Laterinthechapter,it
isshownthatAspenPlusgivesananswerof1.49L/gmol,usingslightlydifferentcritical
properties.Thus,weexpectthecalculationinTable2.1iscorrect.Wenotethattheidealgas
volumeisabout29%higherthantheresultobtainedusingtheRedlich–Kwongequation,
as expected at pressures above 10 atm. If we search the literature for an experimental
```

---

## Стр. 30

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
SOLVINGEQUATIONSOFSTATEUSINGMATLAB(SINGLEEQUATIONINONEUNKNOWN) 15
A B C D E F G
18 Redlich-KwongEquationofState
19 n-Butane
20 BruceFinlayson
21
22 Parameters-n-Butane Data
23 Tc 425.2 K T 393.3 K
24 pc 37.5 atm p 16.6 atm
25 R 0.08206 liter-atm/gmolK
26
27 Formulas Results
28 Tr =T/Tc Tr 0.9250
29 a =0.42748*(RGas^2*Tc^2/pc)*(1/Tr)^0.5 a 14.4301
30 b =0.08664*(Rgas*Tc/pc) b 0.0806
31 v 1.5064 liter/g mol
32 f(v) =p*v^3-RGas*T*v^2+(a-Rgas*T*b-p*b^2)*v-a*b f(v) 1.358E-08 Eq.(2.4)
33 idealgas volume =RGas*T/p idealgas 1.9442 Eq.(2.1)
FIGURE 2.2 Excelspreadsheetusingnamedcells.
measurement(Sageetal.,1937),wefind,forexample,thatthevolumeis1.47L/gmolat
16.6atmand393.3K;thisprovidesacheckonthecalculationsaswellasthedatausedto
makethem.Thereasonfortheirregularchoiceoftemperatureandpressurewastocompare
withthisdata.PVTdatacanbefoundeitherbysearchingontheWeb(chemicalnamePVT
experimentaldata)orusingthecitationsgivenbyAspen(seebelow).
The techniques used to create this spreadsheet are shown in more detail in Appendix
A, including (a) inserting an equation for calculation, (b) inserting a text version of the
equation for display, (c) creating a border around a group of cells, and (d) using “Goal
Seek.”
While this works, using equations involving the cell numbers, like B25 and F29, is
inconvenient and can lead to errors. Instead, we can name the cells using physical terms
thatrelatetotheEOS.Todothis,putthecursorinoneofthecellsthatcontainsanumber,
suchasB23.Thenchooseinsert/name/defineandtypeTc.Thenintheformulas,everywhere
we want to use the critical temperature we replace B23 with Tc. The formulas now look
likeours,andthatmakesiteasiertofindandcorrectmistakes.TheresultisFigure2.2.This
isthepreferredmethodusedintherestofthebook.
SOLVINGEQUATIONSOFSTATEUSINGMATLAB3
(SINGLEEQUATIONINONEUNKNOWN)
NonlinearalgebraicequationscanbesolvedusingMATLAB,too.First,youhavetodefine
theproblemtosolvebywritingafilecalledanm-file;then,youcheckit;finally,youissue
acommandtosolveit.ThesestepsareanalogoustothestepsusedinExcel.Youcanuse
MATLABmosteffectivelyifyoulearntousetheCommandWindowandlearntocreate
m-filesandsavethemproperly;seeAppendixBforadditionaldetails.
Step1 Definethefunction.Itiscreatedasanm-file,calledf.mhere.
function y = f(x)
y = x∗x - 2∗x - 8;
3MATLABisaregisteredtrademarkofTheMathWorks,Inc.
```

---

## Стр. 31

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
16 EQUATIONSOFSTATE
Change the current directory in MATLAB (at the top of the command window) to a
directorywhereyouwishtosaveyourworkandsaveitasf.m.
Step2 Checkthefunction.Issuethecommand:(cid:4)feval(@f,2)togettheresult:ans=−8.
YoucaneasilycalculateEq.(2.9)toseethatforx=2,thefunctionvalueis−8.Nowyou
knowthatf.miscorrect.Notethatweusedavalueforxthatmeantthateveryterminthe
functionwasimportant.Ifwehadusedx=1e−5,thenwewouldhaveobtainedsomething
closeto−8,too,butthex∗xtermwouldnotbeused;hence,wewouldnothavecheckedthe
entirefunction.Thevaluex=1.0isnotagoodchoiceeither,sinceanincorrectfunction
f.m = x−2∗x−8 would return the same value as x∗x−2∗x−8, hence the error would not
be discovered. This is a trivial example, and it is more important for more complicated
problems.
Step3 Tofindthevalueofxthatmakesf(x)=0inMATLAB,usethe“fzero”function.In
thecommandwindow,issuethefollowingcommand.
>>fzero(@f, 0)
ans = -2
This command solves the following problem for x: f(x)=0 starting from an initial
guess of 0. Sometimes the function will have more than one solution, and that can be
determinedonlybyusingthecommandwithadifferentinitialguess.Youcantesttheresult
by:»feval(@f,ans).
Tosummarizethesteps,Step1definedtheproblemyouwishedtosolve,Step2checked
yourprogramming,andStep3instructedMATLABtosolvetheproblem.Itistemptingto
skipthesecondstep—checkingyourprogramming—butremember:iftheprogrammingis
wrong,youwillsolvethewrongproblem.
When examining the command “fzero(@f, x0)” in MATLAB, the f defines which
problemtosolve,thex0isyourbestguessofthesolution,andfzerotellsMATLABtovary
x,startingfromx0untilthef iszero.InExcel’s“GoalSeek,”theanalogousstepswereto
make a cell zero by varying the value of another cell. “Goal Seek” becomes fzero, a cell
withanequationbecomesf,andanothercellbecomesx0.
Inallthecommandsandm-filesintheprevioustext,the“f”canbereplacedbyother
things,say“prob1.”Justbesureyouchangeitinthreeplaces:thefilenameofthem-file,
thefirstlineofthem-file(notabsolutelynecessary),andinthecommand.Additionalforms
ofthecommandareasfollows.
>>fzero(@function, x0, options)
>>z = fzero(‘f’,x0)
Inthelastexample,theresultisputintothevariablez.Theoptionsvectorallowsyou
to set certain quantities, like the tolerance; see how by saying: (cid:4)help foptions. For the
example used earlier, you can find the other root by running the program with x0 = 3.
Multiplerootscanbefoundonlyifyousearchforthemstartingwithdifferentguesses.
ExampleofaChemicalEngineeringProblemSolvedUsingMATLAB
Findthespecificvolumeofn-butaneat393.9◦Kand16.6atmusingtheRedlich–Kwong
EOS.
```

---

## Стр. 32

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
SOLVINGEQUATIONSOFSTATEUSINGMATLAB(SINGLEEQUATIONINONEUNKNOWN) 17
Step1 First,youneedtoprepareanm-filethatwillcalculatethef(x),orheref(v),giventhe
temperature, pressure, and thermodynamic properties. The file is shown in the following
text.
% calculate Eq. (2.4), Chapter 2
function y = specvol(v)
% in K atm l/gmol
% parameters for n-butane
Tc = 425.2
pc = 37.5
T = 393.3
p = 16.6
R = 0.08206
aRK = 0.42748∗(R∗Tc)ˆ2/pc
aRK = aRK∗(Tc/T)ˆ0.5
bRK = 0.08664∗(R∗Tc/pc)
y = p∗vˆ3 - R∗T∗vˆ2 + (aRK - p∗bRKˆ2 - R∗T∗bRK)∗v -aRK∗bRK;
Thisfunction,called“specvol,”definestheproblemyouwishtosolve.
Step2 Totestthefunction“specvol,”youissueeitherofthefollowingcommands.
feval(’specvol’,2) or ans = specvol(2)
The feval function causes MATLAB to compute the value of y (the output defined in
specvol)usingthem-filenamedspecvolwhenv=2.Theoutputyougetis
Tc = 425.2000
pc = 37.5000
T = 393.3
p = 16.6
R = 0.08206
aRK = 13.8782
aRK = 14.4301
bRK = 0.0806
y = 25.98
Youshouldchecktheseresultslinebyline,especiallythecalculationofaRK,bRK,and
y.Alternatively,youcanusethespreadsheetyoudeveloped,putinv=1.506andseewhat
f(v)is;itshouldbethesameasinMATLABsincethecubicfunctionandparametersare
thesame.
Step3 Whenyouuse“fzero,”thefunction“specvol”willbeevaluatedforavarietyofv.
Thus,itisinconvenienttohavetheconstantsprintedoutonthescreeneveryiteration.To
avoidthis,youchangethefunction“specvol”byaddingasemicolon(;)attheendofeach
line.Thissuppressestheoutput.Dothisandsavethem-file,“specvol”.
Step4 Next,youissuethecommand
v = fzero(@specvol,2)
v = 1.5064
```

---

## Стр. 33

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
18 EQUATIONSOFSTATE
In feval, the 2 was the v to be used in the calculation, whereas with fzero, the 2 is an
initialguessoftheanswer.Tocheck,youmightevaluatethefunctiontofindhowcloseto
zerof(v)is.
>> ans = specvol(v)
ans = 1.7764e-15
Ofcourse,youexpectthistobezero(orveryclosetozero)becauseyouexpectMATLAB
toworkproperly.IfMATLABcannotfindasolution,itwilltellyou.Youcanalsousethe
command“fsolve”inthesameway.Tofindoutmoreabout“fzero”and“fsolve,”enterthe
command“helpfzero”or“helpfsolve.”Ifyouuseaninitialguessof0.2,youmightgetthe
specificvolumeoftheliquidratherthanthegas.
AnotherExampleofaChemicalEngineeringProblemSolvedUsingMATLAB
NextrearrangetheMATLABcodetocomputethecompressibilityfactorforanumberof
pressurevalues.ThecompressibilityfactorisdefinedinEq.(2.10):
pv
Z = (2.10)
RT
Forlowpressures,wherethegasisideal,thecompressibilityfactorwillbecloseto1.0.
Asthepressureincreases,itwillchange.Thus,theresultswillindicatethepressureregion
wheretheidealgasisnolongeragoodassumption.Therearetwonewfeaturesillustrated:
theuseofglobalandplotting.
Step1 Thecodecalled“run_volplot”computesthespecificvolumeforpressuresfrom1
to31atmatatemperatureof500Kandthencalculatesthecorrespondingcompressibility
factor.Thefirststatementin“run_volplot”isaglobalcommand.Thevariablesareidentified,
T, p, Tc, and so on, and then assigned values. In other programs, such as “specvol,” the
sameglobalcommandisused,andthesevariablescanthenbeaccessed;seeAppendixB
formoreinformation.
Thenextpartoftheprogramisaloopwith31steps.Thepressureischangedfrom1to
2,3,4,...,31.Foreachpressure,theconstantsaandbarecalculated,asaRK andbRK,
respectively.Then“specvol”iscalledtofindthespecificvolumeforthoseconditions;the
answer is stored in the variable vol as an array, or vector. The compressibility factor is
calculatedandstoredinthevectorZ.Finally,aplotismadewithpresalongthex-axisand
Zalongthey-axis.
% run_volplot
global T p Tc pc R aRK bRK
% in K atm l/gmol
% parameters for n-butane
Tc = 425.2
pc = 37.5
T = 500
R = 0.08206
for i=1:31
pres(i) = i;
```

---

## Стр. 34

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
SOLVINGEQUATIONSOFSTATEUSINGMATLAB(SINGLEEQUATIONINONEUNKNOWN) 19
p = i;
aRK = 0.42748∗(R∗Tc)ˆ2/pc;
aRK = aRK∗(Tc/T)ˆ0.5;
bRK = 0.08664∗(R∗Tc/pc);
vol(i) = fzero(’specvol’,0.2);
Z(i)=pres(i)∗vol(i)/(R∗T);
end
plot(pres,Z)
xlabel(’pressure (atm)’)
ylabel(’Z’)
Step 2 The m-file “specvol” is changed to use the global command, as shown in the
followingtext.Nowtheparametersareavailableto“specvol”becausetheyaredefinedas
globalvariablesandhavebeensetintheprogram“run_volplot.”
% calculate Eq. (2.4), Chapter 2
function y = specvol(v)
global T p Tc pc R aRK bRK
y = p∗vˆ3 - R∗T∗vˆ2 + (aRK - p∗bRKˆ2 - R∗T∗bRK)∗v -aRK∗bRK;
Step 3 Because you have already checked the program “specvol,” you do not need to
check it again. You will want to put semicolons (;) at the end of the lines in “specvol”
becauseyoudonotneedintermediateresults.YoucancheckthevaluesofaRK andbRK
foroneofthepressures,toensuretheyarecorrectintheprogram“run_volplot,”buthere
these statements were copied from “specvol” directly, so that they need not be checked
again.Theuseofvol(i),Z(i),pres(i)iseasytocheckfromthegraph,Figure2.3.(Onlythe
Redlich–KwongEOSwillbeplottedbytheprogramgivenintheprevioustext.)Alsoshown
inFigure2.3arethepredictionsmadeusingtheRedlich–Kwong–SoaveEOS(ω=0.193)
and the Peng–Robinson EOS (ω = 0.193). They differ by only a few percentage points.
1
0.95
0.9
0.85
0.8
0 5 10 15 20 25 30
Pressure (atm)
z
n−Butane
Redlich−Kwong EOS
Redlich−Kwong−Soave EOS
Peng−Robinson EOS
FIGURE 2.3 Compressibilityfactorforn-butane.
```

---

## Стр. 35

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
20 EQUATIONSOFSTATE
Theeffectofpressureissignificant,althoughanidealgasiswithin10%forpressuresless
than10atm.
Step 4 An alternative way to calculate the compressibility factor would be to use the
following command after the loop: Z = pres.∗vol/(R∗T). This command computes the
samethingas
Z(i)=pres(i)∗vol(i)/(R∗T)insidetheloop,butdoesitelementbyelementoutsidethe
loop. Note the symbol.∗; the period causes the element by element calculation, pres(2)
timesvol(2)andsoforth.
EQUATIONSOFSTATEWITHASPENPLUS4
YoucanalsofindthespecificvolumeusingAspenProperties(orthePropertiesAnalysis
inAspenPlus).Givenherearecommandsthatwillenableyoutofindthespecificvolume
ofn-butaneatthestatedconditions.YoumayneedtoreviewAppendixC,too,whichhas
moredetailaboutAspenPlus.
ExampleUsingAspenPlus
Findthespecificvolumeofn-butaneat393.3Kand16.6atmusingtheSRKEOSoption
inAspenProperties(seethefollowingtextforthereason).
Step1
1. StartAspenPlusandchooseTemplate.
2. Whenthewindowappears,chooseGeneralwithMetricUnits.
3. If you are using Aspen Plus, in the Run Type (lower right-hand corner), choose
PropertyAnalysis.
4. Click OK when the Aspen Plus engine window appears. Note that this last step is
specifictoyourinstallation.
Step2 Ontheleftsideofthelist,chooseComponent/Specificationsandenterthenamesor
formulasofthechemicals,asshowninFigure2.4.Ifthereisnolistontheleft,clickonthe
eyeglassesorchoosethemenuData/Components.IfAspenPlusdoesnotrecognizeyour
chemical,awindowappearsthatallowsyoutosearchagain,anditwillsuggestanumber
ofpossibilities.Whenthecomponentsarecompletelyspecified,itisimportantthatthereis
anentryforeverychemicalinthecolumnlabeled“Componentname.”Thefirstcolumnis
whatyouarenamingthechemicals,butthethirdcolumniswhatAspenPlususeswhenit
getsphysicalproperties.Ifthatcolumnisblank,theprogramwillnotwork.
Step 3 On the left side of the list, choose Property/Specifications. Before selecting the
propertymethod,letsseewhatAspenrecommends.UnderToolschoosePropertyMethod
Selection Assistant. Choose, component type, hydrocarbon system, no petroleum assays,
or pseudocomponents, respectively. The three methods suggested are Peng–Robinson,
4AspenPlusisaregisteredtrademarkofAspenTechnology,Inc.
```

---

## Стр. 36

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
EQUATIONSOFSTATEWITHASPENPLUS 21
FIGURE 2.4 AspenPropertieswindowforcomponentnames.
Soave–Redlich–Kwong, and Lee–Kesler–Plocker methods. For this application, choose
SRKinthePropertieswindow.Nowalltheiconsontheleftshouldbeblue,meaningthe
menus are completely filled out. If any menus are still red, go back and click on them
toacceptAspen’sparameters.Ifyouwanttoknowwhattheparametersareforn-butane,
choose Tools/Retrieve Parameter Results. In this case the dipole moment is zero, which
suggeststhatnonidealgasbehaviorwouldonlyoccurathighpressuresorlowtemperatures.
Step 4 In the menus at the top choose: Tools/Analysis/Pure. (The pure will be grayed
out until you do Steps 2 and 3. In the window that appears (see Figure 2.5), choose the
following.
Property type: Thermodynamic
Property: V (need to move the cursor down to see it)
Check vapor, uncheck liquid
Units: choose ml/mol
Components: select n-butane
Temperature, choose Units: K and • List, put in 393.3 and 400
Pressure: choose 16.6 atm
Property: scroll down to find SRK
Click Go.
Step 5 A graph appears with the result plotted (see Figure 2.6). You can read results
from the graph or use the table behind the graph, giving the exact answer. The result is
1490mL/mol,or1.49cm3/gmol,whichcomparesfavorablywiththeresultof1.51when
using Excel or MATLAB. The critical properties are slightly different in the three cases.
TheaxisofFigure2.6hasbeenchangedfromthedefaultvalueinAspen.Doubleclickon
eachaxisandchangetherangeandinterval.
SpecificVolumeofaMixture
Ifyouwishtogetthespecificvolumeofamixture,itisnecessarytouseanotherapproach,
sincetheprocedureintheprevioustextworksonlyforpuresubstances.Thistime,useone
oftheunitsandspecifythestreamintotheunit.Thecalculationwilltellyouthespecific
volume.
Find the specific volume of a mixture consisting of 630 kmol/h of carbon monoxide,
1130 kmol/h of water, 189 kmol/h of carbon dioxide, and 63 kmol/h of hydrogen at 1
atm and 500 K. The specific volume is the solution to the Redlich–Kwong–Soave EOS,
```

---

## Стр. 37

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
22 EQUATIONSOFSTATE
FIGURE 2.5 AspenPluswindowforpurecomponentpropertyanalysis.
FIGURE 2.6 AspenPluswindowshowingpurecomponentpropertyanalysis.
```

---

## Стр. 38

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
EQUATIONSOFSTATEWITHASPENPLUS 23
Eq. (2.5). Since the pressure is low, an ideal gas is probably sufficient, but we will also
use the Redlich–Kwong–Soave EOS for comparison. Aspen recommends (oil and gas
processing): Peng–Robinson, PR–BM (Boston–Mathias), RKS–BM, SRK, under these
conditionsRK–Soavewouldbesimilar.
Step1
1. StartAspenPlusandchooseTemplate;OK.
2. Whenawindowappears,chooseGeneralwithMetricUnits.
3. IntheRunType(lowerright-handcorner),chooseflowsheet.
4. ClickOKwhentheAspenPlusenginewindowappears.(Thislaststepisspecificto
yourinstallation.)
Step 2 If the bottom of the screen does not show the units, use the View/Model Library
pull-downmenuorpresstheF10key.
1. Inthetabsatthebottom,choosePressureChanges.
2. ClickontheCompressor.
3. Clickontheflowsheet,andacompressorappears.
Step 3 To add the input and output streams, click on Material Streams (lower left-hand
corner), click on the flowsheet and drag a stream to the red arrow that is input to the
compressorunitandclick.Next,clicktheredarrowcomingoutanddragthestreamaway
andclick,givingFigure2.7.Note:Tomakechangesinthelocationofthestreamsorunits,
youcanclickonthearrowjustabovetheMaterialStreambutton.Youcantogglebackand
forth between the arrow and Material Stream in the lower left corner as you improve the
presentationofyourflowsheet.Whentheflowsheetisshowing,clickonMaterialStreams.
Ifanyredarrowsshowintheflowsheet,itmeansthattheunitisnotproperlyconnected;
aninputoroutputstreamisnecessary.Fixthatbeforeproceeding—youmayhaveplaced
yourcursorincorrectlywhenyoudrewthestreams.
Step 4 Click on the glasses. This will bring a menu to the left of the screen. The red
boxes indicate that you still need to supply information. Start at the top and work down,
turningtheredboxesintoblueboxesbyfillingintheforms.Inthelistattheleft,choose
Component/Specifications(seeFigure2.4).Typeinthenamesorformulasofeachchemical.
IfAspenPlusdoesnotrecognizeachemical(liken-pentane),youcanselectthatchemical
andchooseFind.Awindowappearsthatallowsyoutosearchagain,andtheprogramwill
suggestanumberofpossibilities.
Step 5 In the list at the left, choose Property/Specifications. In property method, scroll
downtogetRK–Soave.Toeliminatethered“pairparameters,”openthewindowandclick
onthedesignated(recommended)dataset.
Step6 Inthelistattheleft,chooseStreamsbydoubleclickingonit.Insidethatfolderare
twoormorefolders,oneforeachstream.Choosetheinputstream,clickonit,andinsertthe
```

---

## Стр. 39

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
24 EQUATIONSOFSTATE
1
B1
2
(a)
(b)
FIGURE 2.7 Flowsheetforsinglecompressor:(a)flowsheet;(b)Modellibrary(F10key).
temperature,pressure,andflowrateinunitsyouchoose,asshowninFigure2.8.Youcan
specifytheunitsforinputnumbers,thusavoidinghavingtodounitconversionsyourself.
Step 7 In the list at the left, choose Blocks, then B1 (or whatever you have named your
compressor). Choose Specifications, and choose Type: isentropic; insert the discharge
pressure,asshowninFigure2.9.(Forthisproblem,youwillusetheinletstream;thusyou
canputanydischargepressureyouwant,aslongasitisabovetheinletpressure.)
Step8 Choosethe atthetop.Iftheinputisincomplete,awindowwillappeartonotify
youanddirectyoutothemissingdata.Iftheinputiscomplete,awindowwillappear to
notifyyouofthat,too.Clickonthebuttontoperformthecalculation.Oncethecalculations
finish(readtheerrormessages,ifany),clicktheResultsbox(lowerone)toreturntothe
regularmenu.ThenlookatResults/Streams.Thestreamdatawillappearintabularform
asshowninTable2.3.
Step 9 You can obtain the specific volume by dividing the volumetric flow rate by the
molarflowrate,83,537/2012=40.98m3/kmol.ToobtainTable2.3inspreadsheetformat,
place your cursor in the upper left cell of the Stream table, click it and it will be copied
totheclipboard.ThenpasteintoExcel.YoucanalsohavetheStreamTablecopiedtothe
flowsheet,anditcanbecopiedfromthereasapicture.
```

---

## Стр. 40

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
EQUATIONSOFSTATEWITHASPENPLUS 25
FIGURE 2.8 Settingstreaminformation.
Your report of the results should explain what problem you have solved and how
you solved it (focus on the chemical engineering information rather than the detailed
step-by-step process on each screen), describe how you checked your results, and give
the results. In this case you took a stream of specified composition, pressure and tem-
perature, sent it to a compressor, and obtained the data shown in the Table 2.3. The type
of thermodynamic option must be specified (here Redlich–Kwong–Soave) and justified
(dependinguponyourlevelofexpertiseinchemicalengineering).Youmightassumethat
FIGURE 2.9 Settingcompressorinformation.
```

---

## Стр. 41

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
26 EQUATIONSOFSTATE
TABLE2.3 StreamInformationforCompressorProblem
Temperature(◦C) 226.8 622.7
Pressure(bar) 1 7.093
Vaporfraction 1 1
Moleflow(kmol/h) 2012 2012
Massflow(kg/h) 46448.67 46448.67
Volumeflow(cum/h) 83537.33 21141.45
Enthalpy(Gcal/h) −96.444 −89.534
Moleflow(kmol/h)
CO 630 630
Water 1130 1130
CO 189 189
2
H 63 63
2
Aspen Plus did the calculation correctly, but you should also review the results to see if
theyarereasonable.
CHAPTERSUMMARY
You have solved a very simple problem to find the specific volume of a pure component
or a mixture using three programs: Excel, MATLAB, and Aspen Plus. Excel is readily
available, and easy to use. MATLAB is a bit more difficult for beginners to use because
it uses files, which require data transfer. It is extremely powerful, though, and is needed
forothertypesofproblems.WithbothExcelandMATLAB,youmustlookupthecritical
temperature,criticalpressure,andperhapstheacentricfactorofeachchemical.Youthen
must carefully and laboriously check your equations, one-by-one. When you use Aspen
Plus,theparametersarestoredinadatabase,andthecalculationsarepreprogrammed.Your
mainconcernistousethegraphicaluserinterface(GUI)correctly.AspenPlusisextremely
powerfulandisneededforotherclassesofproblems.
Whenusinganyoftheprograms,youwanttocompareatleastsomeofthecalculationsto
experimentaldata,toverifythatthetypeofthermodynamicsyouhavechosenisappropriate
tothephysicalcaseyouaresolving.
PROBLEMS
2.1 Findthemolarvolumeofammoniagasat56atmand450KusingtheRedlich–Kwong
1
equationofstate,T =405.5K,p =111.3atm,a=4.2527,b=0.02590;unitsof
c c
aandbcorrespondtovinL/gmol.(a)UseExcel;(b)useMATLAB.
2.2 Fortheproblemin2.1,useAspenPluswiththeRKSandPeng–Robinsonthermo-
1
dynamicoptions.GivereasonsthattheRKSandPeng–Robinsonoptionsmightbe
necessary.
2.3 Find the compressibility factor of ammonia gas at conditions from 50 to 250 atm
2
and400KusingtheRedlich–Kwong–SoaveequationofstateinExcel.(Hint:before
beginning your spreadsheet, think about how you can organize it so that you can
```

---

## Стр. 42

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 27
copy formulas from cell to cell easily.) Experimental data is available that gives a
volumeof0.459l/gmolat66.8atmand446K(GroenierandThodos,1960).
2.4 Considerthefollowingmixturegoingintoawater-gasshiftreactortomakehydrogen
2
forthehydrogeneconomy.CO,630;H O,1130;CO ,189;H ,63kmol/h.Thegas
2 2 2
is at 1 atm and 500 K. Use Excel (or MATLAB) to compute the specific volume
using
(a) idealgaslaw
(b) Redlich–Kwongequationofstate
(c) Redlich–Kwong–Soaveequationofstate.
TheacentricfactorsfortheRK–Soavemethodare:CO,0.049;water,0.344;CO ,
2
0.225;Hydrogen,−0.22.
Wheredidyougettheotherdatayouneeded?Howdothethreeanswerscompare?
Isthegasidealornot?Comment.Thenredothecalculationsforapressureof200
atmandcommentontheresults.
2.5 Consideramixtureof25%ammonia,therestnitrogenandhydrogenina1:3ratio.
1
Thegasisat270atmand550K.UseExcel(orMATLAB)tocomputethespecific
volumeusing
(a) idealgaslaw
(b) Redlich–Kwongequationofstate
(c) Redlich–Kwong–Soaveequationofstate.
Wheredidyougetthedatayouneeded?Howdothethreeanswerscompare?Isthe
gasidealornot?CommentonthereasonstheRKSequationmightbeexpectedto
bebetter.
2.6 Find the molar volume of methanol gas at 100 atm and 300◦C using the
1
Redlich–Kwong–SoaveEOS,T =512.6K,p =79.9atm,ω =0.559,a=8.96,
c c
b=0.04561;unitsofaandbcorrespondtovinL/gmol.Givereasonswhytheideal
gas or Redlich–Kwong equations of state are not expected to be valid choices. At
9.174MPaand300.0◦C,thevolumeis0.373l/gmol(Stratyetal.,1986).
2.7 Considerthefollowingmixturethatiscomingoutofamethanolreactor.CO,100;
1
H , 200; methanol, 100 kmol/h. The gas is at 100 atm and 300◦C. Compute the
2
specificvolumeusing
(a) idealgaslaw
(b) Redlich–Kwongequationofstate
(c) Redlich–Kwong–Soaveequationofstate.
GivereasonswhytheidealgasorRedlich–Kwongequationsofstatearenotexpected
tobevalidchoices.TheacentricfactorsfortheRK–Soavemethodare:CO,0.049;
H ,−0.22;methanol,0.559.Wheredidyougettheotherdatayouneeded?Howdo
2
thethreeanswerscompare?Isthegasidealornot?Comment.
2.8 Barron (1985) lists the specific volume of nitrogen at 5 MPa and 150 K as
1
0.116m3/kmol.Thegasconstantintheseunitsis8317Pam3/kmolK.
(a) UsetheRedlich–Kwongequationofstatetocalculatethespecificvolumeand
comparewiththisvalue.Thecriticalconstantsfornitrogenare126.2Kand3.4
MPa.
```

---

## Стр. 43

```text
P1:OTA/XYZ P2:ABC
JWBS084-c02 JWBS084-Finlayson May26,2012 13:2 PrinterName:YettoCome Trim:7in×10in
28 EQUATIONSOFSTATE
(b) DothesamethingwiththeRedlich–Kwong–Soaveequationofstate.Theacen-
tricfactorfornitrogenis0.040.Isthismoleculesymmetricorasymmetric?Is
theSoaveversionnecessary?
(c) Barron(1985)givestheDietericiequationofstateforhighpressures.
p(v−b)exp(a/vRT)= RT (2.11)
For nitrogen, a = 1.754 • 105 Pa m6/kmol2; b = 0.04182 m3/kmol. Compute the
specificvolumefromthisequationofstateandcomparewithparts(a)and(b).
2.9 Aspen recommends one of the following equations of state for n-butane:
1
Peng–Robinson,Soave–Redlich–Kwong,Lee–Kesler–Plo¨cker.Comparethepredic-
tionsofspecificvolumeat393.3Kand16.6atm.
NumericalProblems
2.10 SolvetheprobleminFigure2.2usingtheNewton–Raphsonmethod.
1
2.11 SolveProblem2.1usingtheNewton–Raphsonmethod.
1
```

---

## Стр. 44

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
3
VAPOR–LIQUID EQUILIBRIA
Haveyoueverdrivenbyarefineryandwonderedwhathappensinthosetalltowers?Some
ofthemaredistillationtowersthatareusedtoseparateamixtureofchemicalsintotwoor
morestreams,eacharelativelypurestreamofoneofthechemicals.Thephysicalprocess
governingthatseparationisvapor–liquidequilibria.Ithasbeenestimatedthat10%ofthe
energyusedcommerciallyintheUnitedStatesisusedindistillationprocesses.Thus,itis
importanttomakethisprocessasefficientaspossible.
Take a mixture of two or more chemicals in a temperature regime where both have a
significant vapor pressure. The composition of the mixture in the vapor is different from
that of the liquid. By harnessing this difference, you can separate two chemicals, which
isthebasisofdistillation.Tocalculatethisphenomenon,though,youneedtopredictthe
thermodynamicquantitiessuchasfugacity,andthenperformmassandenergybalancesover
the system. This chapter explains how to predict the thermodynamic properties and then
howtosolveequationsforaphaseseparation.Whilephaseseparationisonlyonepartofthe
distillationprocess,itisthebasisfortheentireprocess.Inthischapteryouwilllearntosolve
vapor–liquidequilibriumproblems.Theprinciplesintroducedinthischapterareemployed
incalculationsfordistillationtowersthatarediscussedinChapters6and7.Vapor–liquid
equilibriaproblemsareexpressedasalgebraicequations,andthemethodsusedarethesame
onesintroducedinChapter2.Chapter2waslimitedtothegasphase,whereasvapor–liquid
equilibriaobviouslyincludesliquids,too.Thus,thethermodynamicmodelsneedtobeable
topredictthermodynamicpropertiesforliquids,andcanbeverycomplicated.
InstructionalObjectives: Afterworkingthroughthischapter,youwillhave
1. ReaffirmedyourskillsusingExcel® andMATLAB®forsimpleproblems.
2. LearnedtouseAspenPlustoperformvapor–liquidequilibriacalculations.
IntroductiontoChemicalEngineeringComputing,SecondEdition.BruceA.Finlayson.
©2012JohnWiley&Sons,Inc.Published2012byJohnWiley&Sons,Inc.
29
```

---

## Стр. 45

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
30 VAPOR–LIQUIDEQUILIBRIA
3. LearnedtousetheNISTThermoDataEnginetoprovidedataforcomparison.
4. Reviewed and expanded your chemistry and chemical engineering knowledge of
activitycoefficients.
FLASHANDPHASESEPARATION
Supposeyouputsomewaterinanopenpanonthestove,initiallyatroomtemperature.The
partial pressure of water in the air (at equilibrium) will be equal to the vapor pressure of
wateratthattemperature.Nowheatthepan;thevaporpressureincreasesasthetemperature
rises.Ifthevaporpressureofwateratthepantemperatureexceedsthepartialpressureof
waterintheroom(usuallysetbyhumidity),thewaterwillevaporate.
Next,imaginedoingthesamethingwithamixtureoftwochemicalsinaclosedvessel.
The closed vessel is one with a piston that can move so that the pressure inside remains
constant.Thetwochemicalshavedifferentboilingpoints,anddifferentvaporpressuresata
giventemperature.Asyouincreasethetemperatureofthevessel,therelativeamountofeach
chemicalinthevaporchanges,becauseoneismorevolatilethantheother.Attemperatures
belowthebubblepoint,T ,themixtureisentirelyaliquid.Attemperaturesabovethe
bubble
dew point, T , the mixture is entirely a vapor. At temperatures in between, both liquid
dew
and vapor coexist. However, the composition of the liquid and vapor are not the same .
Thus,asyougraduallyincreasethetemperaturefromalowvalue,somevaporforms,and
thisvaporisricherinthemorevolatilecomponent.Asthetemperatureincreasesfurther,
moreandmorevaporforms.Finally,asthelastdropofliquidevaporates,allthematerialis
inthevaporphase,whichhasthesamecompositionastheoriginalliquid.However,between
the bubble point and dew point, the composition of the liquid and vapor are changing as
thetemperatureincreases,anditisthischangethatyouneedtocalculate.
This chapter looks first at equations governing an isothermal flash, and then shows
howyoucanpredictthethermodynamicquantitiesyouneedtosolvetheisothermalflash
problem.Theproblemsareallsetsofalgebraicequations,andyoucansolvetheseproblems
using Excel and MATLAB. The chapter then addresses more complicated vapor–liquid
separations,butnowusingAspenPlusbecauseofitslargedatabase.
ISOTHERMALFLASH—DEVELOPMENTOFEQUATIONS
ConsidertheflowsheetshowninFigure3.1.Supposeyouknowthetemperature,pressure,
andoverallcompositionoftheinletstream.Themolefractionsofthechemicalsintheinlet
are called {z}. In the phase separator, however, the liquid and vapor are separated. The
i
molefractionsofthechemicalsinthevaporphasearecalled{y}andthoseintheliquid
i
phasearecalled{x}.Whenthevaporandliquidareinequilibrium,youcanrelatethemole
i
fractionsofeachchemicalinthevaporandliquidbytheequation
y = K x (3.1)
i i i
Thesetof{K}arecalledK-values,andtheycanbepredictedfromthermodynamicsas
i
showninthefollowingtext.Fornow,though,assumethatyouknowtheirvalues.
```

---

## Стр. 46

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
ISOTHERMALFLASH—DEVELOPMENTOFEQUATIONS 31
V
y
F i
z
i p
Phase out
separator
p in T out
L
T
in
x
i
FIGURE 3.1 Flashphaseseparator.
To derive the equation governing the phenomenon, you firstadd the mole fractions of
vaporandliquidofallcomponents:
NC(cid:2)OMP NC(cid:2)OMP
y =1, x =1 (3.2)
i i
i=1 i=1
Then,subtractthosetwoequations:
NC(cid:2)OMP NC(cid:2)OMP
y − x =0 (3.3)
i i
i=1 i=1
Next,substitutetheequilibriumexpressionandrearrangetoget
NC(cid:2)OMP NC(cid:2)OMP NC(cid:2)OMP
K x − x =0 or (K −1)x =0 (3.4)
i i i i i
i=1 i=1 i=1
Next,makeamassbalanceforeachcomponentoverthephaseseparator.F isthetotal
molar flow rate, V is the molar flow rate of vapor, and L is the molar flow rate of liquid.
Themolebalanceisthen
z F = y V +x L and F = V +L (3.5)
i i i
DividebyFanddefinev(cid:2)asthefractionoffeedthatisvapor:
V
z = yv(cid:2)+x (1−v(cid:2) ), v(cid:2) = (3.6)
i i i
F
Byusingtheequilibriumexpressionagain,youcanwritethisas
z = K x v(cid:2)+x (1−v(cid:2) )=(K −1)x v(cid:2)+x (3.7)
i i i i i i i
```

---

## Стр. 47

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
32 VAPOR–LIQUIDEQUILIBRIA
Solveforthemolefractionsintheliquid:
z
x = i (3.8)
i 1+(K −1)v(cid:2)
i
PutthatexpressionintoEq.(3.3)toobtainthefinalequation:
NC(cid:2)OMP (K −1)z
i i =0 (3.9)
1+(K −1)v(cid:2)
i=1 i
ThisiscalledtheRachford–Riceequation.NoticethatiftheK-valuesandinletcomposi-
tions{z}areknown,thisisanonlinearequationtosolveforv(cid:2).Thus,youcanapplyherethe
i
samemethodsusedwithExcelandMATLABinChapter2.Oncethevalueofv(cid:2)isknown,
youcancalculatethevalueoftheliquidcompositions,{x},andvaporcompositions,{y},
i i
usingEqs.(3.1)and(3.8).Themolebalanceisthencomplete.
ExampleUsingExcel
Suppose you have a mixture of hydrocarbons in the inlet stream. You want to find the
fractionofthestreamthatisvaporandfindthemolefractionofeachchemicalinthevapor
andliquidstreams.Table3.1showstheflowratesandK-valuesat180◦Fand70psia,using
a basis of one mole per unit of time. To solve this problem, prepare the spreadsheet as
shown.
Step1 “Term1”isthenumeratorinEq.(3.9)and“Term2”isthedenominator,andthese
arecalculatedincolumnsDandE.
Step 2 The ratios of “Term 1” over “Term 2” are calculated and put into column F; this
columnissummedincellF9,whichrepresentsEq.(3.9).
Step3 Youcanthenuse“GoalSeek”tomaketheRachford–Riceequation(cellF9)zero
bychangingthefractionofthefeedthatisvapor(cellE1),givingtheresultshown.Once
youfindthefractionvapor,themolefractionsinthetwophasesareeasytocalculateusing
Eq.(3.8)and(3.1),andtheseareincludedincolumnsGandH.
TABLE3.1 SpreadsheetforFlashExample
A B C D E F G H
1 v=0.425837
2 Phase
3 Equil. Terml= Term2= Ratio=
4 z K-Value (K−l)z (K−l)v+l Terml/Term2 x y
i i i i i i
5 Propane 0.1 6.8 0.58 3.4699 0.1672 0.0288 0.1960
6 n-Butane 0.3 2.2 0.36 1.5110 0.2383 0.1985 0.4368
7 n-Pentane 0.4 0.8 −0.08 0.9148 −0.0874 0.4372 0.3498
8 n-Octane 0.2 0.052 −0.1896 0.5963 −0.3180 0.3354 0.0174
1 f(v)=8.2719E-07 0.9999996 1.0000005
```

---

## Стр. 48

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
THERMODYNAMICPARAMETERS 33
Howmightyouchecktheseresults?
Step1 Ofcourse,themostimportantaspectistohavethecorrectK-values,whichcanonly
bedeterminedbycomparingthemwithexperimentaldata.Theentirecalculationdepends
uponthoseK-values.
Step 2 You need the Rachford–Rice equation to sum to zero, which is evident in the
spreadsheet.
Step 3 You can check that the sum of vapor mole fractions equals one, and the sum of
liquidmolefractionsequalsone.
Step4 YoucanalsocheckonetermintheRachford–Riceequationbydetailedcalculations,
andthencopytheequationdown.Thisensuresthattheformulaiscorrectforallcomponents.
THERMODYNAMICPARAMETERS
Wheredidthevapor–liquidequilibriumK-valuecomefrom?Itisdefinedas
γ fo
K = i i (3.10)
i ϕ p
i
whereγ istheactivitycoefficient, foisthefugacityofthepurechemical,ϕ isthefugacity
i i i
coefficientinthevaporphase,andpisthetotalpressure.Mostofthesequantitiescanbe
calculatedusingthermodynamics.Forexample,yourthermodynamictextbookderivesthe
followingequationforfugacityofapuresubstance:
(cid:3) (cid:4) (cid:5)p(cid:3) (cid:4)
f RT
ln =−RT −vˆ dp (3.11)
p p
0
Thismeansthatifyouknowthep–V–T behaviorofachemical,thenyoucanfindthe
fugacitybycalculatingtheintegral.Inthistextyoudonotneedtodothat,becauseAspen
Pluswilldothatforyou.InsteadyoucaneitheruseK-valuesfromtheliteratureordothe
calculationswithaprocesssimulator.
TheotherimportantparameterinEq.(3.10)istheactivitycoefficient.Itdependsupon
the chemicals involved, their symmetry, forces of attraction like van der Waal forces and
electric dipoles, whether they chemicals are polar or not (have a dipole moment) and
various other considerations. An important part of modeling any chemical system is to
choose activity coefficient models that are appropriate to the situation being modeled.
Chapter6discussesthistopicinmoredetailandillustratesoptionsavailableinAspenPlus.
Inthischapteritsufficestosaythatifthechemicalshavedipolemoments,goodchoices
areNRTL,UNIQUAC(andUNIFAC),andWilson.BothNRTLandUNIQUACcanmodel
azeotropesandtwoliquidphases,whiletheWilsonequationcanmodelazeotropeswhere
thereisonlyoneliquidphase.
Formostoftheseoptions,theactivitycoefficientdependsupontheliquidmolefractions,
andthatmeanstheK-valuesdependupontheliquidmolefractions,too.Thus,thereisnot
```

---

## Стр. 49

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
34 VAPOR–LIQUIDEQUILIBRIA
justoneK-valuethatyoucanuseinthecalculations.Instead,oneoptionistochoosethe
liquidmolefractions,determinetheactivitycoefficients,thentheK-valuesandseeifthe
liquidmolefractionschangedsignificantly.Ifso,youmightusethenewvaluesandrepeat
the process. If this procedure did not work, you would have to use more sophisticated
methodstosolvetheRachford–RiceequationusingprocesssimulatorssuchasAspenPlus
orotheriterativealgorithms.
Thereisonespecialcasethatiseasy,however.Iftheliquidisanidealliquidmixture,
the activity coefficients are 1.0. If the pressure is low enough (say less than 10 atm.) the
vaporphaseisessentiallyanidealgasandthefugacitycoefficientofthevaporis1.0,too.
Thefugacityoftheliquidinthestandardstateisthevaporpressure,too,atlowpressures.
Withthoseassumptions,theK-valuebecomes
vp
K = i (3.12)
i
p
wherevp isthevaporpressureatagiventemperature.Inthisspecialcase,youcanfindthe
i
K-valuesknowingthevaporpressureasafunctionoftemperatureandthetotalpressureof
thesystem.Clearly,lightcomponents(lowerboilingpoints)haveahighervaporpressure
than heavy components, and thus their K-value will be larger. If two phases coexist at
equilibrium, at least one of the components needs a K-value greater than 1 and at least
oneoftheothercomponentsneedsaK-valuelessthanone.Eventhentwophasesarenot
guaranteed,andtheresultdependsuponthecompositionaswellastheK-values.
ExampleUsingMATLAB
Youcansolvethesameproblem(Table3.1)usingMATLAB.First,youdefineafunction
that represents the problem you wish to solve [Eq. (3.9)]. Then, you check the function
to make sure it is correct. Finally, you use the “fzero” function to find the solution. The
functiondefiningtheproblemis
% vapor-liquid equilibrium
function y = vpequil(v)
z = [0.1 0.3 0.4 0.2]
K = [6.8 2.2 0.8 0.052] (3.13)
sum1 = 0.;
for i=1:4 or
num = (K(i)-1)∗z(i) num = (K-1).∗z
denom = 1 + (K(i)-1)∗v denom = 1 + (K-1)∗v
sum1 = sum1 + num/denom sum1 = sum(num./denom)
end
y = sum1
Step1 Programthefunctionandsaveitinyourworkingdirectoryasvpequil.m.
Step2 Issuethecommand“vpequil(0.2)”inthecommandwindow;theoutputshouldbe
z = 0.1000 0.3000 0.4000 0.2000
K = 6.8000 2.2000 0.8000 0.0520
num = 0.5800 (3.14)
```

---

## Стр. 50

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
THERMODYNAMICPARAMETERS 35
denom = 2.1600
sum1 = 0.2685
....
ans = 0.2415
CalculationusingtheExcelspreadsheet(verifiedinTable3.1)givesthesameanswers,
soyouhaveverifiedthattheprogramiscorrect.
Step3 Addsemicolonsattheendofeachlineofthem-fileandsaveit.Solvetheproblem
byissuingthefzerocommandinthecommandwindow.
>> fzero(@vpequil,0.2) (3.15)
ans = 0.4258
Asexpected,theresultisthesameasobtainedusingExcel.
ExampleUsingAspenPlus
AspenPlusallowsyoueasilytosolvethissameproblemusingtheFlash2unitoperation.
Step 1 Open Aspen Plus User Interface and choose Template; OK. When the window
appears, choose General with English Units. In the Run Type (lower right-hand corner),
choose Flowsheet. Click OK when the Aspen engine window appears. (This last step is
specifictoyourinstallation.)
Step 2 If the bottom of the screen does not show the units, use the View/Model Library
pull-downmenuorpresstheF10key.Intheunitsatthebottom,chooseSeparations,and
thenclickontheFlash2.
Step 3 Click on the flowsheet, and a flash (phase separation) unit appears. To add the
inputandoutputstreams,clickonMaterialStreams(lowerleft-handcorner),clickonthe
flowsheetanddragastreamtotheredarrowthatisinputtotheflashunit.Clickonthered
arrowscomingoutanddragthestreamaway.Note:Tomakechangesinthelocationofthe
streams or units, you can click on the arrow just above the Material Stream button. You
cantogglebackandforthbetweenthearrowandMaterialStreaminthelowerleftcorner
asyouimprove thepresentationofyourflowsheet.Whentheflowsheet isshowing,click
onMaterialStreams.Ifanyredarrowsshowintheflowsheet,itmeansthattheunitisnot
properlyconnected;aninputoroutputstreamisnecessary.Fixthatbeforeproceeding—you
may have placed your cursor incorrectly when you drew the streams. The result should
looksomethinglikeFigure3.2.
Step4 Clickontheglasses.Thiswillbringamenutotheleftofthescreen.Theboxesthat
areredindicatethatyoustillneedtosupplyinformation.Startatthetopandworkdown,
turningtheredboxesintoblueboxesbyfillingintheforms.
Step5 Inthelistattheleft,chooseComponent/Specificationsandidentifythecomponents
as you did in Chapter 2 (see Figure 2.4). Type the name or formula of the chemicals. If
AspenPlusdoesnotrecognizeyourchemical(suchasn-pentane),selectthen-pentanebox
```

---

## Стр. 51

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
36 VAPOR–LIQUIDEQUILIBRIA
(a)
(b)
FIGURE 3.2 FlowsheetforFlash2unit:(a)flashunit;(b)ModelLibrary.
and then Find. A window appears that allows you to search again, and it will suggest a
numberofpossibilities.Forn-pentane,twochemicalsarelisted,oneofwhichisn-pentane;
chooseitadclosethewindow.Whenthecomponentsarecompletelyspecified,youshould
have an entry for every chemical in the column labeled “Component name.” The first
column is what you are naming the chemicals, but the third column is what Aspen Plus
useswhenitgetsphysicalproperties.Ifthatcolumnisblank,theprogramwillnotwork.
Step6 Inthelistattheleft,chooseProperty/Specificationsandchoosethethermodynamic
modelasyoudidinChapter2.Inpropertymethod,scrolldowntogetRK–Soave.Youalso
need to tell the computer which database to use for the binary interaction parameters in
RK–Soave. We use the default database. Select Property/Parameters/Binary and click all
theredboxestoacceptthem.
Step 7 In the list at the left, choose Streams by clicking on it or the + in front of it.
Insidethatfolderaretwoormorefolders,oneforeachstream.Choose theinputstream,
clickonit,andinsertthetemperature,pressure,andflowratesofeverychemicalasshown
in Figure 3.3. Note that you can specify the units you would like to use as you put in
the numbers. That way you can use the numbers as given to you, without doing the unit
conversionyourself.
```

---

## Стр. 52

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
THERMODYNAMICPARAMETERS 37
FIGURE 3.3 StreaminformationforFlash2unit.
Step 8 In the list at the left, choose Blocks, then B1 (or whatever you have named your
Flash2unit),thenInput.ChooseSpecifications,andinsertthetemperatureandpressureof
theunitasshowninFigure3.4.(Forthisproblem,youcanusethesametemperatureand
pressureastheinletstream,andregardtheunitsimplyasaphaseseparator.)
Step9 Choosethe atthetop:seeFigure3.3.Iftheinputisincomplete,awindowwill
appeartonotifyyouanddirectyoutothemissingdata.Ifyouhadnotspecifiedatitlein
Specifications, a window may appear to insert it. If the input is complete, a window will
FIGURE 3.4 BlockinformationforFlash2unit.
```

---

## Стр. 53

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
38 VAPOR–LIQUIDEQUILIBRIA
appeartonotifyyouofthat,too.Clickonthebuttontomakeitperformthecalculation.This
willcausethecalculationoftheprocess(hereoneunit)toproceed.Oncethecalculations
finish(readtheerrormessages,ifany),clicktheResultsbox(lowerone)toreturntothe
regularmenu.ThenlookatResults/Streams.Thestreamdatawillappearintabularformas
showninTable3.2.IfyouclickStreamTable,itwillalsobereproducedonyourflowsheet.
Thedefaultreportdoesnotlistthemolefractions;toseethem,gotoSpecifications/Report
OptionsandclickonStreams;thencheckthemolefractionbasisandrepeatthecalculations.
Step 10 For your report, select the sketch of the process by putting your cursor on the
upperleftcorneranddraggingittothelowerrightcorner.ChooseCopy,switchtoaword
processingprogram,andchoosePaste.Dothesamethingwiththestreamtable:clickon
theupperleftboxandpasteintoExcel.Yourwrittenreportshouldincludemorethanthe
process sketch and stream table. You stillneed toexplain what problem you have solved
andhowyousolvedit,focusingonthechemicalengineeringinformation,notthedetailed
stepsonthecomputerscreen.Describehowyoucheckedyourresults,andgivetheresults.
Inthiscase,youtookastreamofspecifiedcomposition,pressureandtemperaturethatwas
in two phases, and separated the gas from the liquid, and calculated the composition of
eachphase.Dependingonyourlevelofexpertiseinchemicalengineering,youalsoneed
tospecifyandjustifythetypeofthermodynamicmodelyouchose.Youmightassumethat
Aspen Plus did the calculation correctly, but you also should look at the results to see if
theyarereasonable.
FromtheTable3.2,youcanseethatthevaporfractionis0.419(comparedwith0.426in
Table3.1).SinceAspenPluscomputedtheK-values,itmayhaveuseddifferentonesthan
youdid.YoucanfindoutwhatAspenPlususedbydividingy byx foreachcomponent.
i i
Theresultsare:propane,5.2;n-butane,2.1;n-pentane,0.84;n-octane,0.067.Whilethese
numbersdifferslightlyfromtheonesusedinTable3.1,themolefractionsofeachchemical
TABLE3.2 Flash2Results
1 2 3
Temperature(◦F) 180 180 180
Pressure(psia) 70 70 70
Vaporfraction 0.419 1 0
Moleflow(lbmol/h) 100 41.898 58.102
Massflow(lb/h) 7355.297 2587.239 4768.058
Volumeflow(cuft/h) 3865.909 3735.26 130.649
Enthalpy(MMBtu/h) −6.768 −2.263 −4.505
Moleflow(lbmol/h)
Propane 10 7.881 2.119
n-Butane 30 18.016 11.984
n-Pentane 40 15.096 24.904
n-Octane 20 0.905 19.095
Molefraction
Propane 0.1 0.188 0.036
n-Butane 0.3 0.43 0.206
n-Pentane 0.4 0.36 0.429
n-Octane 0.2 0.022 0.329
```

---

## Стр. 54

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
NONIDEALLIQUIDS—TESTOFTHERMODYNAMICMODEL 39
inthevaporandliquidstreamsareclose.TheK-valuesarealsolistedinthereportmade
fromAspen(seeAppendixC).
NONIDEALLIQUIDS—TESTOFTHERMODYNAMICMODEL
In the examples given earlier, you were either given the K-values or you were told what
thermodynamic model to choose. Usually, that decision is yours to make, and your re-
sults are only as good as your choice. Consequently, it is important to test your choice,
preferably against experimental data. One easy way to do that is to model the T–xy or
p–xy diagram for vapor–liquid of binary pairs. You can do this easily using the Property
Analysis option in Aspen Plus. Given here are commands that will enable you to create
such diagrams. You may also need to review Appendix C, which has more detail about
AspenPlus.
Step 1 Start Aspen Properties and choose Template. A window appears; choose General
withMetricUnits.IfyouopenAspenPlusUserInterfaceinstead,intheRunType(lower
right-hand corner), choose Property Analysis.Click OK when the Aspen engine window
appears.(Thislaststepisspecifictoyourinstallation.)
Step 2 In the list at the left, choose Component/Specifications and enter the names or
formulasofthechemicals;seeStep5mentionedearlier.Here,weusewaterandethanol.
Step 3 In the list at the left, choose Property/Specifications. For the first calculation,
choosetheidealpropertymethod(activitycoefficientsareall1.0).Forthesecondcalcula-
tion,chooseWILS-2.Thisoptionusesanidealgas,Henry’sLaw,andtheWilsonbinary
parameters,whichisapplicabletoalcohols.
Step4 (Skipthiscalculationforanidealliquid.)
You also need to tell the computer which database to use for the binary interaction
parameter with the WILS-2 choice. Choose the default WILS-2 binary parameters. Now
alltheiconsontheleftshouldbeblue,meaningthemenusarecompletelyfilledout.
Step5 Inthemenusatthetopchoose:Tools/Analysis/Binary(whenusingAspenProper-
ties)orTools/Analysis/Property/Binary(whenusingAspenPlus).(Thebinaryoptionwill
begrayedoutuntilyoudoSteps2–4.)Awindowappears;choosethefollowing.
Components: Water and Ethanol should show
Pressure: set the pressure for a T-xy diagram
or
Temperature: set the temperature for a p-xy diagram
Click Go.
Step6 Agraphwillappearshowingtheresult.Youcanreadfromthisgraph,oryoucan
lookatthetablebehindit.Togetthey–xplot,lookatthetableofresults.Thelowerlefthas
aboxforPlotWizard.Clickthatandchoosethetypeofplotyouwant.Theyx-diagramfor
idealthermodynamicsisshowninFigure3.5.Thisisnotagoodfit.Youknowthatethanol
andwaterformanazeotrope,andthepredictionsdonotgiveanazeotrope(wherey=x).
```

---

## Стр. 55

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
40 VAPOR–LIQUIDEQUILIBRIA
1
0.9
0.8
0.7
0.6
0.5
y
0.4
0.3
0.2
0.1
0
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
x
FIGURE 3.5 Ethanol–watervapor–liquiddiagramforidealthermodynamicscalculationsforan
idealliquid(line)withdata(circles);plotmadeinMATLAB;yandxaremolefractionsofethanol.
1
0.9
0.8
0.7
0.6
0.5
y
0.4
0.3
0.2
0.1
0
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
x
FIGURE 3.6 Ethanol–water vapor–liquid diagram with Wilson binary interaction parameters
(line);data(circles);plotmadeinMATLAB;yandxaremolefractionsofethanol.
```

---

## Стр. 56

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
NISTTHERMODATAENGINEINASPENPLUS 41
You should conclude that an ideal solution is not a good thermodynamic model for this
system.
GobacktoStep3andrepeatusingtheWilsonthermodynamics;theresultsareshownin
Figure3.6,andthecalculationsagreewiththedata.Thetable(behindthegraphinAspen
Plus) also lists K-values and activity coefficients. When you have good comparison with
data, whether in the form of a T–xy diagram, K-values, or activity coefficients, you have
validatedathermodynamicsmodelforthisbinarypair.Inaprocess,withmanychemicals,
you may have to do this for all binary pairs before deciding on the best thermodynamic
model.
NISTTHERMODATAENGINEINASPENPLUS
Using the NIST Thermo Data Engine blue and red TDE icon we can compare experi-
mentaldatawithresultsofcalculationsmadewithourchosenequationofstate.Consider
a simulation that already has ethanol and water in it. Click the TDE icon and choose
ethanol as the first component and water as the second one for a binary mixture. Then
click“retrievedata”.Awindowwillopenthatcontainsexperimentaldataforthissystem
fromavarietyofsources.Inthisexample,scrolldowntoBinaryVLE/Isobaric/VLE045.
Click on that to obtain Figure 3.7. The data are from Jones et al. (1943). Click on the
“Plot” box to plot the data, Figure 3.8. Click on “Consistency” and the data will be
evaluated for internal consistency (satisfyingthe Gibbs–Duhem equation). Two windows
show the results, Figure 3.9. For additional information about the test, use the Help
FIGURE 3.7 Experimentaldataforethanol–watersystemat101,000Pa.
```

---

## Стр. 57

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
42 VAPOR–LIQUIDEQUILIBRIA
FIGURE 3.8 T–xyofethanol–water.
(a)
(b)
FIGURE 3.9 Consistencyresultsforethanol–watersystem.
```

---

## Стр. 58

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
NISTTHERMODATAENGINEINASPENPLUS 43
FIGURE 3.10 T–xycurveforethanol–waterusingtheWILS-2EOS.
menu and enter NIST TDE VLE Consistency Test. Once we have made choices of the
thermodynamic model (here WILS-2), we can plot the same T–xy curve, Figure 3.10. In
both cases it is possible to capture the data and copy it to Excel. Then the calculations
can be compared point by point with experimental results. Figure 3.11 does this using
MATLAB.
375
370
365
360
355
350
0 0.2 0.4 0.6 0.8 1
x or y −Ethanol
)K(
T
T−x data
T−y data
T−x calculations
T−y calculations
FIGURE 3.11 ComparisonofcalculatedVLEwithexperimentaldataat1atm.
```

---

## Стр. 59

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
44 VAPOR–LIQUIDEQUILIBRIA
CHAPTERSUMMARY
In this chapter, you have derived the equations governing phase equilibrium and seen
how the key parameters can be estimated using thermodynamics. You have solved the
resulting problems using Excel, MATLAB, and Aspen Plus. You also learned to pre-
pare a T–xy diagram as a way of testing the thermodynamic model chosen to represent
thephenomenon.Youhavebeenintroducedtoavarietyofmodelsoftheliquid,andyou
have found that some of them model reality and some do not. Thus, the material in later
chapterswillbeimportantwhenmodelingaprocesswithbothvaporandliquids.
PROBLEMS
3.1 ThestreaminTable3.3isat100psiaand178◦F.Calculatethefractionthatisvapor
1
bysolvingtheRachford–Riceequation(a)usingExcel;(b)usingMATLAB.
TABLE3.3 InputStreamforProblem3.1
Chemical lbmol/h K-value
Propane 20 3.7
n-Butane 30 1.4
n-Pentane 50 0.6
3.2 Consideramixtureof78%nitrogen,21%oxygen,and1%argonat2atmospheres
1
and 86 K. Barron (1985) gives the K-values as 1.23, 0.37, and 0.47, respectively.
Determine the composition of liquid and vapor that are in equilibrium at these
conditions.
3.3 A reservoir in Northern Louisiana contains a volatile oil. The reservoir conditions
1
atdiscoverywere246◦F,4800psia.ThecompositionofthestreamisinTable3.4.
Youwillhavetochoosehowtomodelthebutanesandpentanes:normal?Iso-?You
willalsohavetochoosewhichchemicaltousetomodeltheheptanesplus:heptane?
octane? Aspen suggests using either Peng–Robinson, LK–PLOCK, or SRK. Use
Peng–Robinson.
1. Thegas–liquidseparatoratthesurfaceisat500psia,65◦F.Findthecomposition
ofthegasandliquidstreamsandthevaporfraction.
TABLE3.4 InputStreamforProblem3.3
Chemical MoleFraction
Nitrogen 0.0167
Methane 0.6051
Carbondioxide 0.0218
Ethane 0.0752
Propane 0.0474
Butane 0.0412
Pentane 0.0297
Hexane 0.0138
Heptaneplus 0.1491
2. Theliquidistakentothestocktank,whichisat14.7psia,70◦F.Findthevapor
fractionattheseconditions.
```

---

## Стр. 60

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 45
3.4 UsingtheRachford–Riceequation,Eq.(3.9),provethatfortwophasestocoexist,
1
at least one component needs a K-value greater than one and another component
needsaK-valuelessthanone.
3.5 The stream in Table 3.5 comes out of a distillation tower (described in detail in
1
Chapter6).Itisat138psiaand197.5◦F.Ifthepressureisreduced(adiabatically)to
51psia,whatwillbethevaporfractionandtemperature?(Hint:inAspenPlus,puta
valvebeforetheFlash2unit,andreducethepressurewiththevalveblock.)Forhy-
drocarbonsattheseconditionsAspensuggestsusingPeng–Robinson,LK–PLOCK,
orSRK.UseSRK.
TABLE3.5 InputStreamforProblem3.5
Chemical lbmol/h
Propane 1.00
Isobutane 297.00
n-Butane 499.79
i-Pentane 400.00
n-Pentane 500.00
3.6 The stream in Table 3.6 comes out of a distillation tower (described in detail in
1
Chapter6).Itisat36psiaand141.5◦F.Ifthepressureisreduced(adiabatically)to
20psia,whatwillbethevaporfractionandtemperature?Solvethesamewayasin
Problem3.5.
TABLE3.6 InputStreamforProblem3.6
Chemical lbmol/h
n-Butane 4.94
i-Pentane 396.00
n-Pentane 499.65
3.7 The stream in Table 3.7 comes of an ammonia reactor at 700◦F and 3000 psia. If
1
the temperature is reduced to 60◦F in a flash unit, keeping the pressure the same,
determine the flow rate of each species in the vapor and the liquid stream. Aspen
suggests that for chemicals at high pressure,one can use an equation of statewith
advancedmixingrules,suchasWong–Sandler.UseRKSWS,andcomparewiththe
datalistedintheNISTTDEsystem.
TABLE3.7 InputStreamforProblem3.7
Chemical lbmol/h
Nitrogen 143.3
Hydrogen 450.4
Ammonia 221.6
Carbondioxide 1.8
3.8 TheflowratesoutofamethanolreactorareCO:100;hydrogen:200;methanol:100
2
lbmol/h. This stream is at 100 atm and 300◦C. Cool it to 30◦C and determine the
flowratesofeachspeciesinthevaporandliquidstream.
1. WhataretheK-valuesforthethreespeciesattheseconditions?Aflashseparation
(Flash2inAspen)isadequatetomodelthecondenser.Usingthemolefractions
```

---

## Стр. 61

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
46 VAPOR–LIQUIDEQUILIBRIA
y andx obtainedbyAspenPlusforthevaporandliquidrespectively;calculate
i i
theK-values,K =y/x.
i i i
2. Dothesimulationforanidealsolutionandalsoforanotherchoiceofthermody-
namicmodel(yourchoice).Whatconsiderationsdidyouusetochoose?
3. Your report should have a flowsheet and give the mass balances. Discuss the
difference between the two cases and why you think one might be better. How
canyoufindoutwhichthermodynamicmodelismorerealistic?Note:Thedipole
momentsofthethreespeciesareasfollows:CO:0.1;hydrogen:0;methanol,1.7
debyes(Reidetal.,1977).
3.9 The flow rates out of an equilibrium reactor to make hydrogen were CO: 5.25,
hydrogen: 1095, carbon dioxide: 699, and water: 364.2 (use these as lbmol/h).
Ideally,youcouldcoolthestreamandremoveallthewater.Inactuality,youmight
notbeabletocondenseallthewater,andthewatermaycontaintraceamountsofthe
other components. This problem challenges you to find out how much. The outlet
fromthereactorisat450K,1atm,andiscooledto80◦F,stillat1atm.
1. WhataretheK-valuesforthethreespeciesattheseconditions?Aflashseparation
(Flash2inAspen)isadequatetomodelthecondenser.Usingthemolefractions
y andx obtainedbyAspenPlusforthevaporandliquidrespectively,calculate
i i
theK-values,K =y/x.
i i i
2. Dothesimulationforanidealsolutionandalsoforanotherchoiceofthermody-
namicmodel.AspensuggeststhatforchemicalsuseNRTL,Wilson,UNIQUAC,
orUNIFAC.UseNRTLhere.
3. Your report should have a flowsheet and give the mass balances. Discuss the
difference between the two cases and why you think one might be better. How
canyoufindoutwhichismorerealistic?
3.10 Model the vapor–liquid equilibria data (Table 3.8) of ethyl acetate(1) and water at
1
760 mm Hg using the UNIQUAC and Wilson–RK models in Aspen Plus. Also
compare with experimental data obtained using the NIST TDE system (Ellis and
Garbett,1960).
TABLE3.8 Vapor-LiquidEquilibriumDataforProblem3.10
x y T(◦C)
1 1
0.0006 0.0405 98.85
0.0011 0.1256 96.20
0.0049 0.5910 86.50
0.0086 0.6680 76.20
0.0459 0.7140 70.55
0.1440 0.7025 70.55
0.2690 0.7060 70.50
0.3540 0.7090 70.45
0.4080 0.7090 70.55
0.5140 0.7100 70.50
0.6080 0.7025 70.50
0.6900 0.7070 70.45
0.7750 0.6990 70.50
0.8737 0.7650 71.45
0.9444 0.8650 73.35
```

---

## Стр. 62

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 47
3.11 Modelthevapor–liquidequilibriadata(Table3.9)ofethylalcohol(1)andethylacetate
1
at1atmusingtheUNIQUACmodelinAspenPlus.Alsocomparewithexperimental
dataobtainedusingtheNISTTDEsystem(MurtiandVanWinkle,1959).
TABLE3.9 Vapor-LiquidEquilibriumDataforProblem3.11
x y T(◦C)
1 1
0.1260 0.2146 73.82
0.1343 0.2146 73.78
0.2271 0.2960 73.04
0.3128 0.3634 72.50
0.3358 0.3643 72.28
0.5052 0.4803 72.18
0.5441 0.5074 72.35
0.6442 0.5618 72.70
0.6828 0.6092 72.90
0.7850 0.6819 74.14
0.8774 0.7908 75.50
0.9482 0.8924 76.70
3.12 Model the following vapor–liquid equilibria data (Table 3.10) of acetaldehyde (1)
1
andethylalcoholat1atmusingtheWilsonRKmodelinAspenPlus.Alsocompare
withexperimentaldataobtainedusingtheNISTTDEsystem(DeLeeuw,1911).
TABLE3.10 Vapor-LiquidEquilibriumDatafor
Problem3.12
x y T(◦C)
1 1
0.0690 0.2410 30.10
0.2030 0.6530 23.30
0.3160 0.7950 15.90
3.13 The air separation process operates at high pressure and low temperature, and the
2
choice of thermodynamic model is important. Using Aspen Plus, prepare a T–xy
diagram for nitrogen–oxygen using an ideal system, UNIFAC, NRTL–RK, and
RK–SOAVE. Barron gives the following results at 20 atm and nitrogen mole frac-
tion = 0.6: vapor temperature = 125.4 K and liquid temperature = 122.6. Which
thermodynamics did a better job? Will it matter? In this process the temperature
differencefromthereboilertothecondenserisverysmall,sothatasmallerrorin
thevapor–liquidpropertiesmighthaveabigeffectonthedesignofthecolumn.
3.14 Table 2.9 of Perry and Green (2008) gives the vapor pressure of inorganic liquids.
2
Usedatafornitrogen,oxygen,andargonandfitthedatatoacurveofthefollowing
form(pisinPa,T inK):
lnp =C +C /T +C lnT +C T0.5 (3.16)
1 2 3 4
ThencheckyourresultsinTable2.8ofPerryandGreen(2008)toseeifyouget
thesameformulacitedbytheHandbook.Youprobablyknowhowtodothecurve
fit,butadetailedexplanationisonthebookwebsite.
```

---

## Стр. 63

```text
P1:OTA/XYZ P2:ABC
JWBS084-c03 JWBS084-Finlayson May26,2012 13:8 PrinterName:YettoCome Trim:7in×10in
48 VAPOR–LIQUIDEQUILIBRIA
3.15 The formula you derived in Problem 3.14 is based on pressures below 1 atm. The
2
formula given by the Handbook does not specify the range of applicability. Since
the air separation unit operates at high pressure, compare the three predictions at
pressuresfrom−180◦Cto−140◦C:yourformula,theformulafromtheHandbook,
AspenPlus.(Note:thecriticaltemperuresare:nitrogen,126.2K,oxygen,154.6K,
andargon,150.8K.)
NumericalProblems
3.16 SolvetheprobleminTable3.1usingtheNewton–Raphsonmethod.
1
3.17 SolveProblem3.2usingtheNewton–Raphsonmethod.
1
```

---

## Стр. 64

```text
P1:OTA/XYZ P2:ABC
JWBS084-c04 JWBS084-Finlayson May30,2012 8:39 PrinterName:YettoCome Trim:7in×10in
4
CHEMICAL REACTION EQUILIBRIA
Hydrogencanbemadeforfuelcellsbyusingthewater–gasshiftreaction.Infact,hydrogen
ismadethiswayeverydayinoilrefineries.Thereactionisveryfast,andtheeffluentfromthe
reactorisclosetobeinginchemicalequilibrium.Ammoniaismadebyreactinghydrogen
andnitrogen,andtheeffluentfromanammoniareactorisusuallyinchemicalequilibrium.
The ammonia is then used to make fertilizer, which helps increase food production for
the world. Thus, chemical reaction equilibrium is important for both energy and food
production.
Thischaptershowshowtosolveproblemsinvolvingchemicalreactionequilibrium.The
chemical reaction equilibrium gives the upper limit for the conversion, so knowing the
equilibriumconversionisthefirststeptoanalyzingaprocess.Thesecondquestion,whatis
therateofreaction,canthenbeansweredtodecidethevolumeofthereactor.Thissecond
question, using kinetics, is covered in Chapter 8. Chemical reaction equilibrium leads to
one or more nonlinear algebraic equations that must be solved simultaneously, and such
problemsaredescribedinthischapter.
InstructionalObjectives: Afterworkingthroughthischapter,youwillhave
1. AdditionalpracticeusingExcelandMATLAB®.
2. UsedtheRGibbsblockinAspenPlustoperformreactionequilibriacalculations.
3. Continuedlearningtocheckyournumericalwork.
4. Reviewed and expanded your chemistry and chemical engineering knowledge of
chemicalreactionequilibrium.
IntroductiontoChemicalEngineeringComputing,SecondEdition.BruceA.Finlayson.
©2012JohnWiley&Sons,Inc.Published2012byJohnWiley&Sons,Inc.
49
```

---

## Стр. 65

```text
P1:OTA/XYZ P2:ABC
JWBS084-c04 JWBS084-Finlayson May30,2012 8:39 PrinterName:YettoCome Trim:7in×10in
50 CHEMICALREACTIONEQUILIBRIA
CHEMICALEQUILIBRIUMEXPRESSION
Whenyoutakesomechemicalsthatcanreactandmixtheminavessel,thereactioncanbe
representedas
A+B⇒C+D (4.1)
Ifthereactionisreversible,thereversereactioncanalsotakeplace:
C+D⇒A+B (4.2)
Youcanwritethisas
A+B⇔C+D (4.3)
If the reaction rate is very fast, then the forward and reverse reactions proceed quickly,
and the ultimate mixture contains all four chemicals, in specific amounts. If you change
the temperature, these amounts may change. Sometimes in a gaseous reaction, changing
the pressure has the same effect. In this chapter, your goal is to predict the composition
ofthefinalmixture,determinedbychemicalreactionequilibrium.
Of course, the reaction rate may not be infinitely high, and you may use a catalyst to
speed up the reaction. However, even if the reaction rate is increased, you can never go
beyondthecompositiondeterminedbychemicalreactionequilibrium.Hereishowtoset
upthisproblemmathematically.
In thermodynamics courses, you have learned that chemical reaction equilibrium is
determinedbytheequilibriumconstant,whichisdefinedintermsofthechangeofGibbs
freeenergy:
(cid:2)Go =−RT lnK (4.4)
The Gibbs free energy is tabulated at 298 K for pure components, and it is possible
to extend the Gibbs free energy for a reaction to any temperature using the van’t Hoff
equation:
dlnK (cid:2)Ho
= R (4.5)
dT RT2
Here,(cid:2)Hoistheheatofreaction.Whenthereactionis
R
aA+bB ⇔cC +dD (4.6)
theequilibriumconstantisdefinedintermsoftheactivitiesofthespecies:
acad
K = C D (4.7)
aaab
A B
In the gas phase, the activity is the fugacity, since the activity is the fugacity divided by
thefugacityofthestandardstate,whichis1atm.Inturn,youcanwritethefugacityasthe
```

---

## Стр. 66

```text
P1:OTA/XYZ P2:ABC
JWBS084-c04 JWBS084-Finlayson May30,2012 8:39 PrinterName:YettoCome Trim:7in×10in
CHEMICALEQUILIBRIUMEXPRESSION 51
productofthefugacitycoefficient(providingacorrectionfromidealgasbehavior)times
thetotalpressuretimesthemolefractioninthevaporphase:
f
f =ϕ p =ϕ py,where ϕ ≡ i (4.8)
i i i i i i
p
i
The fugacity coefficient can be calculated using the equation of state (Denbigh, 1971,
p.126):
(cid:2)p(cid:3) (cid:4)
vˆ 1
lnϕ = i − dp (4.9)
i
RT p
0
When the pressure is less than 10 atm, the gas is usually ideal. From the formula, it is
clearthatforanidealgastheintegralvanishes.Thenlnϕ =0orϕ =1.Youcanusethat
assumptionandcombineallthetermsinEq.(4.7)intoEq.(4.10):
ycyd
K = C D pc+d−a−b (4.10)
p yayb
A B
ExampleofHydrogenforFuelCells
Asaspecificexample,considerthewater–gasshiftreactionthatcanbeusedinachemical
processtomakehydrogenforfuelcellapplications:
CO+H O⇔CO +H (4.11)
2 2 2
Atequilibrium,Eq.(4.10)holdswithc+d−a−b=0,andthenumberofmolesremains
constant when the reaction takes place. Thermodynamic data give the value of lnK =5
(or K =148.4) at 500 K. If you start with a stoichiometric mixture of carbon monoxide
andwater,whatwilltheequilibriumcompositionbe?Inthiscase,andyouareleftwith,
y y
148.4= CO2 H2 (4.12)
y y
CO H2O
Step1 Tobegin,makeamolebalancetable(seeTable4.1),withabasisof1moleeachof
carbonmonoxideandwater,whichthenreacttoequilibrium.Usextorepresentthenumber
ofmolesreacting,thusgivingthevaluesinthetable.
TABLE4.1 SolutionforEquilibriumofWater–GasShiftReaction
Species Start End y
i
CO 1 1−x (1−x)/2
H O 1 1−x (1−x)/2
2
CO x x/2
2
H x x/2
2
Total 2 2 1
```

---

## Стр. 67

```text
P1:OTA/XYZ P2:ABC
JWBS084-c04 JWBS084-Finlayson May30,2012 8:39 PrinterName:YettoCome Trim:7in×10in
52 CHEMICALREACTIONEQUILIBRIA
TABLE4.2 SpreadsheetforEquilibriumofWater–GasShiftReaction
1 G H I J K
2 Species Start End MoleFraction
3 CO 1 0.075861 =H3-conv 0.03793
4 H O 1 0.075861 =H4-conv 0.03793
2
5 CO 0 0.924139 =H5+conv 0.46207
2
6 H 0 0.924139 =H6+conv 0.46207
2
7 Total 2 2 =SUM(I3:I6) 1
8 conv 0.924139
9 Eq. 7.35E-09 =148.4-I5∗I6/(I3∗I4)
Step2 PutthemolefractionsintoEq.(4.12)andsimplify:
(x/2)(x/2) x2
148.4= = (4.13)
[(1−x)/2][(1−x)/2] (1−x)2
You can easily solve this equation by taking the square root, giving x = 0.924. In
morecomplicatedcases,itwouldnotbepossibletosolveitsoeasily.Instead,youwould
have to solve a nonlinear equation numerically to find the value of x. When there are
multiple reactions, which also may be in equilibrium, there will be several equations to
solvesimultaneously.Thus,beingabletosolvemultiplenonlinearequationsisusefulwhen
dealingwithreactionsatequilibrium.
SolutionUsingExcel
TosolvefortheequilibriuminEq.(4.13)usingExcel,youputtheequationinonecell,put
aguessofxinanothercell,anduse“GoalSeek”or“Solver”tomakethefirstcellzeroby
changingx.Sincethetotalnumberofmolesdoesnotchange,youcanchangeEq.(4.12)to
oneinvolvingmoles:
y y (n /n )(n /n ) n n
148.4= CO2 H2 = CO2 t H2 t = CO2 H2 (4.14)
y y (n /n )(n /n ) n n
CO H2O CO t H2O t CO H2O
Thecalculationsareconvenientlydoneinaspreadsheet,andthefinalresultsareshown
inTable4.2.Letusseehowtoconstructthisspreadsheet.
Step1 ColumnHistheinitialmolesofeachspecies.
Step2 ColumnIiscomputedaccordingtotheequationdisplayedinColumnJ.
Step 3 Then, the equilibrium equation (4.14) is calculated in cell I9, according to the
formuladisplayedincellJ9.
Step4 Finally,youuseGoalSeek(ifitconverges)orSolver(morelikelytoconverge)to
makecellI9zerobyvaryingcellI8.Ifyouhavedifficultygettingconvergence,trychanging
thevalueofthenumberofmolesreacting(conv)toavalueclosertowhereyouthinkthe
```

---

## Стр. 68

```text
P1:OTA/XYZ P2:ABC
JWBS084-c04 JWBS084-Finlayson May30,2012 8:39 PrinterName:YettoCome Trim:7in×10in
CHEMICALEQUILIBRIUMEXPRESSION 53
TABLE4.3 EquilibriumofWater–GasShiftReactionwithNonstoichiometricInput
1 G H I J K
2 Species Start End MoleFraction
3 CO 1 0.01164 =H3-conv3 0.00364
4 H O 1.8 0.81164 =H4-conv3 0.25364
2
5 CO 0.3 1.28836 =H5+conv3 0.40261
2
6 H 0.1 1.08836 =H6+conv3 0.34011
2
7 Total 3.2 3.20000 =SUM(I3:I6) 1.00000
8 conv3 0.98836
9 Eq. -9.168E-07 =148.4-I5∗I6/(I3∗I4)
answer is. If the iteration goes off to oblivion (1024!), you need to reset the spreadsheet
by not accepting the result (with Goal Seek) or “return to initial values” (with Solver).
(The formulas listed in column J are displayed by entering them in a cell, preceded by
theapostrophesymbol.Inordertopreparethespreadsheettocomputethemolefractions,
thefirstcell(K3)issetto=I3/$I$7.Then,theformulacaneasilybecopieddowntoget
I4/$I$7,etc.;seeAppendixAformoreinformation.)
Onceyouhavepreparedthespreadsheet,itiseasytochangetheconditions,eitherthe
equilibriumconstantorthestartingmolesofvariousspecies.Foranothercase,withsome
CO and H initially, you get the results shown in Table 4.3. Note that you can get more
2 2
hydrogenbyaddingwatertotheinitialcomposition.Thisisonewaytohelpthehydrogen
economy.
SolutionUsingMATLAB
TosolvefortheequilibriuminEq.(4.13)usingMATLAB,youcreateanm-filethatwill
calculate
x2
f(x)=148.4− (4.15)
(1−x)2
for any x. Then, you use “fsolve” or “fzero” or “fminsearch” to find the x that makes
f(x)=0.
Step1 Constructanm-filethatevaluatesthefunction,givenx.Thenameisequil_eq.mand
itislistedinthefollowing.Fortestingpurposes,youleaveoffthe“;”ofthecommandsthat
involvecomputation. Save thisfunctioninyourdesiredworkspace.(Notethatthevalues
forthe“in”parametershavebeensetarbitrarilyforthetest.)
% equil_eq
function y=equil_eq(x)
COin = 1.1;
H2Oin = 1.2;
CO2in = 0.1;
H2in = 0.2;
Kequil = 148.4;
CO = COin - x
H2O = H2Oin - x
```

---

## Стр. 69

```text
P1:OTA/XYZ P2:ABC
JWBS084-c04 JWBS084-Finlayson May30,2012 8:39 PrinterName:YettoCome Trim:7in×10in
54 CHEMICALREACTIONEQUILIBRIA
CO2 = CO2in + x
H2 = H2in + x
y = Kequil - CO2∗H2/(CO∗H2O)
Thism-fileactslikeanyfunction:giveitanxanditcomesbackwiththevalueofy.
Step 2 To test this function, you evaluate it for a specific value of x. Issue the following
commandinthecommandwindow.
equil_eq(0.9)
Theresultis
CO = 0.2000
H2O = 0.3000
CO2 = 1
H2 = 1.1000
y = 130.0667
ans = 130.0667
Thisisthecorrectanswer.
Step3 Oncethecheckismade,youcanadd“;”totheendofeveryline.Notethattotestthe
functionyouhadtodothreethingscorrectly:(1)tellMATLABthenameofthefunction
(equil_eq),(2)besurethefunctionwasintheworkingdirectory(orsomeplaceMATLAB
wouldlook),and(3)provideavalueofx.
Step4 ToruntheproblemshowninTable4.1,youchangethefunctiontothefollowing.
% equil_eq
function y=equil_eq(x)
COin = 1.;
H2Oin = 1.;
CO2in = 0.;
H2in = 0.;
Kequil = 148.4;
CO = COin - x;
H2O = H2Oin - x;
CO2 = CO2in + x;
H2 = H2in + x;
y = Kequil - CO2∗H2/(CO∗H2O);
Step5 Youthenissuethenexttwocommandstofindtheanswer.
format long
fzero(’equil_eq’,0.5)
ans = 0.92413871189774
Asexpected,thisisthesameanswerasyoufoundusingExcel.Theinitialconcentrations
canbechanged,too.Becausethecheckwasforvariousvalues(not0sand1s),youhave
```

---

## Стр. 70

```text
P1:OTA/XYZ P2:ABC
JWBS084-c04 JWBS084-Finlayson May30,2012 8:39 PrinterName:YettoCome Trim:7in×10in
CHEMICALEQUILIBRIUMEXPRESSION 55
checkedthecodeforanysetofparameters.Infindingthesolution,MATLABwillaccess
thefunctionmanytimes.ThestrategyforfindingthesolutionisbuiltintoMATLAB,but
you need to provide the function name and an initial guess. MATLAB does the rest (the
hardpart).TosolvetheproblemshowninTable4.3,withdifferentstoichiometry,youcan
use the same program. Here, the program is changed slightly to illustrate the use of the
globalcommand.
% equil_eq_global
function y=equil_eq_global(x)
global COin H2Oin CO2in H2in Kequil
CO = COin - x;
H2O = H2Oin - x;
CO2 = CO2in + x;
H2 = H2in + x;
y = Kequil - CO2∗H2/(CO∗H2O);
% run equil_eq_global
global COin H2Oin CO2in H2in Kequil
COin = 1
H2Oin = 1
CO2in = 0
H2in = 0
Kequil = 148.4
x=fzero(’equil_eq_global’,0.5)
Step 1 Here, you use the global command in run_equil_eq_global, setthe variables, and
repeat the global command in the function equil_eq_global. Then those variables are
accessibletothefunction(seeAppendixBforadditionalinformation).
Step2 Leaveoffthe“;”intherunningprogram,sothedataarerepeatedintheoutput.
Step 3 When using the global command, you must be sure to use the global command
in the command window (or a run_program that runs in the command window), set the
variables after the global statement, and then repeat the global statement in the func-
tion. If you do not follow these three rules, MATLAB will inform you that it was asked
for an undefined variable or function, and give you the m-file and line number where
itappears.
Step4 Whenyourunthisprogram,theresultsarethesameasbefore,whichchecksyour
modification to use the global option. To solve the problem in Table 4.3, you change the
inputvalueinrun_equil_eq_globaltobe1,1.8,0.3,and0.1,respectively.Theansweris
x = 0.98835845820682
Inthiscase,MATLABcouldnotfindasolutionwhenstartingfromaguessof0.5.After
someexperimentation,usingaguessof0.99workedandgavetheanswerprovidedabove.
Intheseexamples,youprovidedthedataeitherbyinsertingthemintothefunctionitself,
whichwascalledbyadriverprogram,orbyusingtheGlobaloption.Anotheroptionisto
```

---

## Стр. 71

```text
P1:OTA/XYZ P2:ABC
JWBS084-c04 JWBS084-Finlayson May30,2012 8:39 PrinterName:YettoCome Trim:7in×10in
56 CHEMICALREACTIONEQUILIBRIA
transferthoseparametersinthecallingargumentsofthefunction.Thefunctionischanged
to
% equil_eq_global2
function y=equil_eq_global2(x,param)
CO = param(1) - x;
H2O = param(2) - x;
CO2 = param(3) + x;
H2 = param(4) + x;
Kequil = param(5);
y = Kequil - CO2∗H2/(CO∗H2O);
andthecallingprogramischangedto
% run equil_eq_global2
COin = 1
H2Oin = 1
CO2in = 0
H2in = 0
Kequil = 148.4
param = [COin H2Oin CO2in H2in Kequil]
x=fzero(@(x) equil_eq_global2(x,param), 0.5)
Notehowtheparametersaretransferred—asavector.Theninthefunction,theindividual
termsareobtainedfromthevectorsothatitiseasiertochecktheequation.Naturally,the
resultisthesame.
CHEMICALREACTIONEQUILIBRIAWITHTWOORMOREEQUATIONS
In most real cases, multiple reactions can take place, and several of them may be in
equilibriumatthesametime.ThenyouwillhavetwoequationslikeEq.(4.14)thatdepend
upontwovariables;youmustchoosethevariablestosatisfybothequations.MATLABis
ideallysuitedtosolvingsuchproblems.
MultipleEquations,FewUnknownsUsingMATLAB
Supposeyouwanttosolvethefollowingtwoequations:
10x +3y2 =3
(4.16)
x2−exp(y)=2
There are two main ways to solve multiple equations in MATLAB. The first way is to
use the “fsolve” command. The second way is to use the optimization routines and the
“fminsearch”command.Bothareillustratedhere.
Method1Usingthe“fsolve”Command Thestepsarecreateanm-file,checkit,callthe
appropriateMATLABfunction,andchecktheresults.
```

---

## Стр. 72

```text
P1:OTA/XYZ P2:ABC
JWBS084-c04 JWBS084-Finlayson May30,2012 8:39 PrinterName:YettoCome Trim:7in×10in
CHEMICALREACTIONEQUILIBRIAWITHTWOORMOREEQUATIONS 57
Step1 Createanm-fileandcallitprob2.m.
%filename prob2.m
function y2 = prob2(p)
% vector components of p are transferred to x and y
% for convenience
% in remembering the equation
x = p(1)
y = p(2)
% the components of the two equations are calculated
y2(1) =10∗x + 3∗y∗y - 3
y2(2) = x∗x - exp(y) - 2
Step2 Testthefileprob2.mwithp(1)=1.5andp(2)=2.5.Ifyoutestedwithvaluesof
1.0and1.0thereareseveralchancesforerror.Forexample,ifalineissupposedtobex∗x
butonlyxiswritten,thenusingavalueof1.0forxgivesthesamevalueforxandx∗xand
you will not detect the error. Using the same value for x and y [or p(1) and p(2)] has the
same pitfall: if you inadvertently typed x in place of y in the m-file, then you would not
detecttheerrorwiththesevalues.
p = [1.5 2.5]
>>feval(‘prob2’,p)
y2 = 30.75 -11.9325
These values agree with the hand calculations, so the functions are computed correctly.
Nowyouput“;”aftereverylineinthecodeinordertosuppressthedisplayedoutput.
Step3 Fromthecommandmode,youcallthe“fsolve”programwithaninitialguess,p0.
>>p0 = [0 0]
>>z = fsolve(‘prob2’,p0)
>>z = -1.4456 -2.4122
Step4 Becauseyoudonotknowhowaccuratetheresultsare,youshouldcheckthemby
evaluatingthefunction.
>>ans = feval(‘prob2’,z)
ans = -1.0120e-04 5.1047e-06
Method 2 Using the “fminsearch” Function In MATLAB the “fminsearch” function is
usedtofindtheminimumofafunctionofseveralvariables.Youfirstcreateanm-filethat
calculatesthefunction,andtheninvokethe“fminsearch”functiontominimizeit.
Step1 Tosolvethesameproblem,createaslightlydifferentm-fileandcallitprob3.m.
Youcandothismosteasilybyopeningprob2.m,changingit,andsavingitwiththenew
name:prob3.m.
%filename prob3.m
function y2 = prob3(p)
% vector components of p are transferred to x and y
```

---

## Стр. 73

```text
P1:OTA/XYZ P2:ABC
JWBS084-c04 JWBS084-Finlayson May30,2012 8:39 PrinterName:YettoCome Trim:7in×10in
58 CHEMICALREACTIONEQUILIBRIA
% for convenience in remembering the equation
x = p(1)
y = p(2)
% the components of the two equations are calculated
f1 =10∗x + 3∗y∗y - 3
f2 = x∗x - exp(y) - 2
y2 = sqrt(f1∗f1 + f2∗f2)
Step 2 Check the function as you did before. In fact, because you already checked the
m-file“prob2.m”youonlyhavetocheckthaty2iscalculatedcorrectlyfromf1andf2.The
commandisinvokedbyfirstsettingtheinitialguess(thisalsosetsthelengthofthevector
ofindependentvariables,thatis,ittellsMATLABhowmanyparametersithastoadjust).
>>p0 = [1.5 2.5]
>>feval(‘prob3’,p0)
f1 = 30.75
f2 = -11.9325
ans = 32.984
Thesevaluesagreewiththehandcalculations,sothefunctionsarecomputedcorrectly.
Step 3 Next, replace the “;” in the m-file and run the problem from an initial guess of
[11].
>>p0 = [1 1];
>>xvec = fminsearch(‘prob3’,p0)
Theresultsare
xvec = -1.4456 -2.4121
Step 4 You still do not know how accurate these results are. Check by evaluating the
functionafteryouhave removed the“;”fromthelinescalculating f1andf2sothatthey
willbedisplayedwhenthefunctioniscalled.
>>ans = feval(‘prob3’,xvec)
f1 = -1.0120e-04
f2 = 5.1047e-06
VariationsinMATLAB
Step 5 If these values are not small enough, you should reduce the tolerance using the
options variable. The standard tolerance is 10−4. To see the effect, though, you must get
moresignificantdigitsbyusingthe“formatlong”command.
>>format long
>>options=optimset(‘TolFun’,1e-12)
>>xvec = fminsearch(‘prob2’,p0,options)
xvec = -1.44555236880465 -2.41215834803936
```

---

## Стр. 74

```text
P1:OTA/XYZ P2:ABC
JWBS084-c04 JWBS084-Finlayson May30,2012 8:39 PrinterName:YettoCome Trim:7in×10in
CHAPTERSUMMARY 59
Step6 Toseehowwelltheequationsaresolved,youtakeoutthe“;”fromthefileprob3.m
andsaveit.
>>feval(‘prob3’,xvec)
f1 = 1.4531e-12
f2 = -9.0994e-13
ans = 1.7145e-12
Thus, you have made the functions zero to at least 10 digits. (The numbers you get will
notbeidenticaltothese,becausethenumbersaresosmalltheyarecorruptedbyround-off
error.)
Step7 Tofindinformationaboutotheroptions,type
>>help fminsearch
which tells you to use the options: Display, TolX, TolFun, MaxFunEvals, and MaxIter.
Then
>>help optimset
tellsyouhowtosetthoseparameters.
ChemicalReactionEquilibriaUsingAspenPlus
YoucanalsousetheprocesssimulatorAspenPlustosolvechemicalreactionequilibrium
problems.IthasahugeadvantageoverExcelandMATLAB:AspenPluscontainstheGibbs
free energies of many chemicals, and it can calculate them as a function of temperature.
Thus,thedatagatheringaspectoftheproblemishandledforyou.Yourjobistocompare
theresultsandthepredictedK valueswithexperimentalinformation.
The reactor module with Gibbs free energy is RGibbs. You can set up the problem in
thesamefashionasshowninChapter3(p.35),exceptthatyouchooseReactors,andthen
choosetheRGibbsreactor.IntheexampleshowninTable4.4,theNRTLmodelischosen
forpropertyevaluation.ThisisoneoftheequationsofstaterecommendedbyAspen:under
Tools,selectPropertyMethodSelectionAssistant,forchemicals,nothighpressure.
Byusingthemolefractions,youcanfindtheequilibriumconstantused,whichis137.5.
ThisisslightlydifferentfromtheoneusedinEq.(4.13),whichmakesaslightchangein
theanswer.FortheproblemillustratedinTable4.1,AspenPlusobtainedaCOmolarflow
rateof0.076versus0.079usinganequilibriumconstantof148.4.FortheprobleminTable
4.3,AspenPlusobtainedaCOmolarflowrateof0.013versus0.012andahydrogenflow
rate of 1.087 versus 1.088. The chief difference between the calculations is due to the K
value.AspenPluspredictsthatvaluefromtheGibbsfreeenergy,whilethevalueusedin
Eq.(4.13)wasobtainedbyreadingoffagraph.
CHAPTERSUMMARY
In this chapter, you have derived the equations governing chemical reaction equilibrium
andseenhowthekeyparameterscanbeestimatedusingthermodynamics.Youhavesolved
```

---

## Стр. 75

```text
P1:OTA/XYZ P2:ABC
JWBS084-c04 JWBS084-Finlayson May30,2012 8:39 PrinterName:YettoCome Trim:7in×10in
60 CHEMICALREACTIONEQUILIBRIA
TABLE4.4 EquilibriumofWater–GasShiftReactionat500Kand1atm(a)Feedwith
ReactantsOnly,and(b)FeedwithReactantsandProducts
(a) (b)
S1 S2 S1 S2
Temperature(◦C) 226.8 226.8 Temperature(◦C) 226.8 226.8
Pressure(bar) 1.013 1.013 Pressure(bar) 1.013 1.013
Vaporfraction 1 1 Vaporfraction 1 1
Massflow(kg/h) 46.026 46.026 Massflowkg/hr 73.842 73.842
Volumeflow(cum/h) 81.964 82.059 Volumeflow(cum/h) 131.091 131.223
Enthalpy(Gcal/h) −0.081 −0.09 Enthalpy(Gcal/h) −0.153 −0.163
Density(kg/cum) 0.562 0.561 Density(kg/cum) 0.563 0.563
Moleflow(kmol/h) Moleflow(kmol/h)
CO 1 0.079 CO 1 0.013
H O 1 0.079 H O 1.8 0.813
2 2
CO 0 0.921 CO 0.3 1.287
2 2
H 0 0.921 H 0.1 1.087
2 2
Molefraction Molefraction
CO 0.5 0.039 CO 0.313 0.004
H O 0.5 0.039 H O 0.563 0.254
2 2
CO 0 0.461 CO 0.094 0.402
2 2
H 0 0.461 H 0.031 0.34
2 2
Vaporphase Vaporphase
Volumeflow(cum/h) 81.964 82.059 Volumeflow(cum/h) 131.091 131.223
Compressibility 0.999 1 Compressibility 0.998 0.999
HeatCapRatio 1.346 1.294 HeatCapRatio 1.324 1.291
theresultingproblemsusingExcel,MATLAB,andAspenPlus.Youhavealsolearnedto
solvemultipleequationsusingMATLABwhenthereareseveralreactionsinequilibrium.
PROBLEMS
4.1 Methanolisformedbyreactingcarbonmonoxidewithhydrogen.(Thismightbean
1
on-boardgenerationofhydrogenforthehydrogeneconomy.)Withthereaction
CO+2H ↔CH OH (4.17)
2 3
theconditionatequilibriumis
p y 1
K = CH3OH = CH3OH (4.18)
p p p2 y y2 p2
CO H2 CO H2
Whenthecarbonmonoxideandhydrogenenterthereactorina1:2ratio,findthe
equilibriumconversionwhenthepressureis50atmand K =0.0016.First,(a)use
p
Excel;then,(b)useMATLABtosolvetheproblem.
4.2 Findthemolarflowratesofallspeciesoutofanequilibriumreactorwhentheinlet
1
values of nitrogen, hydrogen, and ammonia are 1.1, 3, and 0.2. The equilibrium
```

---

## Стр. 76

```text
P1:OTA/XYZ P2:ABC
JWBS084-c04 JWBS084-Finlayson May30,2012 8:39 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 61
constantis0.05at589K:
p y 1
K = NH3 = NH3 (4.19)
p p1/2p3/2 y1/2y3/2 p
N2 H2 N2 H2
forthereactionwrittenas 1N + 3H ↔NH .Use220atmforthepressure.First,
2 2 2 2 3
(a)useExcel;then,(b)useMATLAB.
4.3 Redo Problem 4.1 using Aspen at 256.9 ◦C. Since the pressure is high for this
1
chemical system, use the RK–Soave equation of state, which is one of the options
suggestedbyAspen.HowdotheresultscomparewiththoseofProblem4.1?
4.4 RedoProblem4.2usingAspen.Sincethepressureishighforthischemicalsystem,
1
usetheRK–Soaveequationofstate,whichisoneoftheoptionssuggestedbyAspen.
HowdotheresultscomparewiththoseofProblem4.2?
4.5 Theexampleofawater–gasshiftreactorwasdoneatafixedtemperature.Usually,
2
thisreactioniscarriedoutadiabatically,andthetemperaturerisestowhatitneeds
tobeforanadiabaticoperation.Theresultofthatisthattheequilibriumconversion
is less. Thus, a common method of performing this reaction is to use two reactors
(Stephenson, 1966, p. 126). Let the reaction proceed adiabatically in the first one,
then cool the gases, and then go into a second adiabatic reactor. Do this for the
same problem shown in Table 4.4, using Aspen Plus, but have the first reaction
be an adiabatic one rather than isothermal one. Then use a heat exchanger to cool
to 342.9◦C and go into another adiabatic reactor. How does the overall conversion
comparewiththeexampleinTable4.4?
4.6 Asteamreformertakesmethaneandreactsitwithwatertoformcarbondioxideand
1
hydrogenbythereaction:
CH +H O⇔CO+3H (4.20)
4 2 2
Inaddition,thewater–gasshiftreactionoccurs:
CO+H O⇔CO +H (4.21)
2 2 2
Theoverallreactionisendothermic,though,sothatthepartialoxidationreactionis
usedtoincreasethetemperature:
(cid:5) (cid:6)
CH + 3 O ⇒CO+2H O (4.22)
4 2 2 2
ModelthereformerwiththesereactionsusingtheRGibbsblockinanadiabatic
mode. The oxidation reaction should proceed to completion and the other two re-
actions will be at equilibrium at the exit temperature. Take the input as (kmol/h)
methane, 10,000; water, 5000; oxygen stream 5800 (99% oxygen, 1% nitrogen),
530 C, 20 bar. One must be careful when operating such an autothermal reformer
because you may have an explosive mixture in a contained space. You do have an
advantage,though,becausewhenyoustartupthereactoryoucanusemoreoxygen
tocausethereactortoreachitsoperatingtemperaturefaster.
```

---

## Стр. 77

```text
P1:OTA/XYZ P2:ABC
JWBS084-c04 JWBS084-Finlayson May30,2012 8:39 PrinterName:YettoCome Trim:7in×10in
62 CHEMICALREACTIONEQUILIBRIA
4.7 A process to make hydrogen uses gas from a reformer; the gas is fed to a reactor
2
where the water–gas shift reaction takes place [Eq. (4.11)]. Under usual operating
conditions,thestreamleavingthereactorisinequilibriumattheoutlettemperature
(orclosetoit).Thefeedratetothispartoftheprocessis(lbmol/h)CO:1260,H :
2
932, CO : 140, steam: 1972 at 177◦C and 1.36 atm. The stream goes to a reactor,
2
andtheoutputofthereactorisinchemicalequilibriumat377◦C.Theequilibrium
constantat377◦Cis15.6.Findtheequilibriumcompositionleavingthereactorusing
(a)Excel,then(b)MATLAB,andthen(c)usingAspenPluswiththeRGibbsblock.
Sincethepressureislow,anidealgasequationofstateisappropriate.
4.8 Ethylchlorideismadebyreactingethylenewithhydrogenchloride:
1
C H +HCl⇔C H Cl (4.23)
2 4 2 5
Startwithanequimolaramountofethyleneandhydrogenchlorideanddetermine
the equilibrium composition at 350◦F and 250 psig using Aspen Plus with the
RK–Soaveequationofstate.
4.9 Findtheequilibriumconversionforamixtureofsulfurdioxide,oxygen,andsulfur
2
trioxideat700Kand2atm.
(a) StartingmixtureofSO :O ::1:3,usingidealthermodynamicssinceonlygases
2 2
arepresent.
(b) Increasethetemperatureto900K.
(c) UseastartingmixtureofSO :O ::1:1/2at900K.
2 2
(d) Discussthesimilaritiesanddifferencesofparts(a)–(c).
4.10 Ethyleneismakebyheatingethaneatahightemperature.Theinputtothereactoris
2
100%ethane.
(a) Determine the equilibrium composition of ethane, ethylene, and hydrogen at
1100Kand1atmusingAspenPlus:
C H ⇔C H +H (4.24)
2 6 2 4 2
(b) Addinasecondreactionandincreasethetemperatureto1367Kanddetermine
theequilibriumcomposition:
C H ⇔C H +H (4.25)
2 4 2 2 2
Sinceonlygasesarepresentandthepressureislow,anidealgasisappropriate;
also,usetheRK–Soaveequationofstateforcomparison.
4.11 In a steam reformer, steam is added to methane and two (or more) reactions take
2
place:
CH +H O⇔CO+3H endothermic
4 2 2
(4.26)
CO+H O⇔CO +H exothermic
2 2 2
The composition out of the reformer is based mainly on chemical equilibrium
(Marsh et al., 1994, p. 165). Determine the equilibrium composition under the
following conditions using Aspen Plus. First, (a) 750◦C, 14 bar, steam/methane =
```

---

## Стр. 78

```text
P1:OTA/XYZ P2:ABC
JWBS084-c04 JWBS084-Finlayson May30,2012 8:39 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 63
3; then, (b) 650◦C, 14 bar, steam/methane = 2. Since the pressure is over 10 atm,
usetheRK–Soaveequationofstate.
4.12 SolveProblem4.10withExcelwhentheequilibriumconstantis1.76at1100K.
1
4.13 Use MATLAB to solve Problem 4.10 with both reactions at 1367 K. The two
2
equilibriumconstantsare37.6and0.769.
4.14 UseMATLABtosolveProblem4.11whentheequilibriumconstantsare47.17atm
2
and1.309atm.
NumericalProblems
4.15 SolveEq.(4.16)usingtheNewton–Raphsonmethod.
1
4.16 SolveProblem4.1usingtheNewton–Raphsonmethod.
1
```

---

## Стр. 79

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
5
MASS BALANCES WITH
RECYCLE STREAMS
Engineerswhodesignandrunchemicalplantsusemassbalancestodecidewhichprocesses
arecost-effective.Chemicalengineeringstudentsaretaughtintheirfirstcoursetolookat
the entire system as well as the individual pieces of equipment. If you know the mass
flowsofachemicalprocess,includingtheinputflowsandoutputflows,youcanestimate
theeconomicviabilityofthatprocessbyaddingupthesellingpriceoftheproducts,and
subtractingthecostoftherawmaterialsandwastetreatment.Ifthatnumberisnotpositive,
theprocessisnotcost-effective.Youwanttofindthatoutbeforeyouhavespenttoomuch
time designing it. Then, you can try to make it economically viable, perhaps by using
anotherchemicalreactionpathway,oranewseparationschemeforpurifyingtheproduct.
Often, the raw material cost is 70% of the cost of the product, which makes the mass
balanceveryuseful.Also,massbalancesallowyoutofindtheenergycostsintheprocess,
providedyoucancalculatetheenthalpyofeachstream.Sincethermodynamicsallowsyou
tocalculatetheenthalpy,youcanestimatetheenergycost.
Mostprocessesinvolvearecyclestream.Thereasonisthatallthereactantsdonotreact,
andbusinessescannotaffordtothrowtherestaway.Furthermore,anyleftovershavetobe
disposed of in an environmentally friendly manner, which costs money. Thus, engineers
take the unreacted reactants and put them back in the start of the process and try again.
Thismakesthemassbalancesabitmorecomplicated,anditleadstoiterativemethodsof
solution,whicharedescribedinthischapter.BothExcelandAspenPlusareusedtosolve
mass balances with recycle streams. Situations in which the energy balances affect the
massbalancearetreatedinChapters6and7,becausethesearebestdoneusingaprocess
simulatorsuchasAspenPlus.
IntroductiontoChemicalEngineeringComputing,SecondEdition.BruceA.Finlayson.
©2012JohnWiley&Sons,Inc.Published2012byJohnWiley&Sons,Inc.
65
```

---

## Стр. 80

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
66 MASSBALANCESWITHRECYCLESTREAMS
InstructionalObjectives: Afterworkingthroughthischapter,youwillhave
1. Learned how to model processes using mass balances only, in Excel and Aspen,
includingreactorsandseparators.
2. Obtainedexperiencewiththeprogramsthatsolvenonlinearequations:howtoinclude
theminthecalculation,theireffectonconvergencetoasolution,andwhichoptions
workbestinspecificcases.
MATHEMATICALFORMULATION
Themathematicalformulationofmassbalancesisreallyquiteeasy.Thissectiondevelops
the equations for three simple units, which you then combine in myriad ways. Once you
can do the mass balance for a simple unit, with the help of Excel you can do the mass
balanceforaprocesscombiningthosesimpleunits.Equationsaregivenhereforamixer,
separator,andreactor,andthenthoseequationsareusedinExceltoperformmassbalances
onprocesses.
Amixer(calledMIXR)addsalltheflowsinandtransfersthemtotheoutputstream,as
illustratedinFigure5.1.Themass(ormole)balanceisthatthemassoutequalsthesumof
themassesin.Thisistrueforeachchemicalcomponent,andhenceforthetotalmass,too.
Itismorecommontomakemolebalances,sincechemicalreactionsoccurusingmoles,but
theconversionfrommasstomolesandbackagainiseasy.Themassbalanceequationsfor
theMIXRunitare
N(cid:2)STRM
nout = nj (5.1)
i i
j=1
where nj is the flow rate of component “i” in the jth stream, and nout is the flow rate of
i i
component“i”intheoutletstream.Ifyouknowtheflowratesin,youcaneasilycalculate
theflowratesout.
Thesecondunitisaseparator,calledSEPR.Thereisoneinputstreamandtwo(ormore)
outputstreams,asillustratedinFigure5.2.Youcanspecifythefractionofeachcomponent
going into the unit that goes out the overhead stream. (Note that you need to have some
conventions here; clearly identify to which output streamthe fractional flow refers.) Call
FIGURE 5.1 MIXRunit.
```

---

## Стр. 81

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
MATHEMATICALFORMULATION 67
FIGURE 5.2 SEPRunit.
thatfractionsf ,andcallitthesplitfractiongoingtotheoverheadstream.Themassbalance
i
foreachcomponent“i”is
n2 =ninsf , n1 =nin(1−sf ) (5.2)
i i i i i i
If you know the split fractions of each component, and the flow rate in, you can easily
calculatetheflowratesoutofstream1and2foreachcomponent.
The final unit is a reactor, called REAC, illustrated in Figure 5.3. This time there is
onlyoneinputstreamandoneoutputstream,butareactionoccurs.Naturally,youneedto
specifythereactionandtheconversioninsomeway.Youcanspecifythereactionusingthe
stoichiometricequationforthereaction
aA+bB→cC+dD (5.3)
IfN molesofAreact,then(b/a)N molesofBalsoreactandform(c/a)N molesofCand
(d/a)N moles of D. You specify the amount reacting by giving a conversion for A (i.e.,
50%oftheAreacts).Theconversioniscalledα.Youdohavetobecarefultospecifythe
conversion based onthelimitingreagent, which intheillustrationisA.Iftherewere not
enoughBtoreactwithA,thentheconversionofAislimited.Ifitistoohigh,itwouldgive
anegativeconcentrationofB.Theequationforeachofthecomponentsis
b
nout =nin−ninα, nout =nin− ninα
A A A B B a A
(5.4)
c d
nout =nin+ ninα, nout =nin+ ninα
C C a A D D a A
NoteinparticularthattheequationsforcomponentsB,C,andDdependupontheamount
ofAentering,sincethatishowtheconversionisspecified.
FIGURE 5.3 REACunit.
```

---

## Стр. 82

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
68 MASSBALANCESWITHRECYCLESTREAMS
Allthese equations can be programmed easily in Excel. Itis the combination of them
to represent the mass balances in a process with recycle that becomes challenging. Here
aresomeexamplesinwhichtheindividualunitsarecombinedinanExcelspreadsheetto
makemassbalancesforanentire(butsimple)process.
EXAMPLEWITHOUTRECYCLE
Astreaminarefineryisat100psiaand75◦Fandcontainsthefollowing:
lbmol/h
Propane 100
i-Butane 300
n-Butane 500
i-Pentane 400
n-Pentane 500
Total 1800
Your task is to separate this stream into five streams, each of which is a relatively pure
streamofonecomponent.
Step1 Youneedtodecidewhatphysicalmechanismtouse(distillation,absorption,mem-
branes, etc.) and the operating parameters of the equipment. For the first example, you
can use the SEPR unit above as a simplistic model of any of these units. The chemicals
arelistedinorderoftheirboilingpointswiththelowestboilingpointsfirst.Thus,choose
distillationasthepreferredseparationmethodandthedistillationtrain(seeFigure5.4)will
distillthemoffonebyone.
FIGURE 5.4 Distillationtrain.
```

---

## Стр. 83

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
EXAMPLEWITHOUTRECYCLE 69
FIGURE 5.5 Simplisticdistillationtrain.
Step 2 You can simplify this by taking out all the energy exchange units, as shown in
Figure5.5.
Step 3 Next, you prepare an even simpler flow sheet, using specified split fractions, as
showninFigure5.6.InChapters6and7youwilllearntoestimatethosesplitfractionsand
tomodelthedistillationtowersmoreexactly.
Each unit, SEPR-x, involves a simple mass balance in which you specify the fraction
of the feed that you want to go out the overhead and out the bottom stream. You do this
foreachspecies.Thecalculationproceedsfromlefttoright,andtheresultsareshownin
Table5.1.
Step4 Noiterationisnecessaryinthisexample.Thefinalstepistochecktheresults.You
can add up the input and output streams for each component in each unit and determine
that the mass of each species is conserved. You can also check to see that you used the
appropriate split fractions. Then, and only then, should you accept the results. This was
FIGURE 5.6 DistillationtrainmodeledusingsimpleSEPRunits.
```

---

## Стр. 84

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
70 MASSBALANCESWITHRECYCLESTREAMS
TABLE5.1 RecoveryFractionsinDistillationTrain
StreamNo. 1 2 3 4 5 6 7 8 9
SplitFraction SEPR-1 SEPR-2 SEPR-3 SEPR-4
C3 0.99 1 1 1
i-C4 0.005 0.995 1 1
n-C4 0 0.005 0.995 1
i-C5 0 0 0.005 0.995
n-C5 0 0 0 0.005
lbmol/h
C3 100 99 1 1 0 0 0 0 0
i-C4 300 1.5 298.5 297 1.5 1.5 0 0 0
n-C4 500 0 500 2.5 497.5 495 2.5 2.5 0
i-C5 400 0 400 0 400 2 398 396 2
n-C5 500 0 500 0 500 0 500 2.5 497.5
a very simple example, so easy that you could have done it on the back of an envelope.
However,ifthesimpledistillationunitswerereplacedbyrealdistillationcolumns,inwhich
vapor–liquid data were used, the calculations would have been much more difficult and
timeconsuming.
EXAMPLEWITHRECYCLE;COMPARISONOFSEQUENTIALAND
SIMULTANEOUSSOLUTIONMETHODS
Consider a simple process in which the reactor can only convert 40% of the feed to it
(perhapsduetoequilibriumconstraints),buttheseparationofreactantAandproductBis
completeandtheunreactedAisrecycled.TheprocessisillustratedinFigure5.7.
Step1 Onewaytosolvethisproblemistodoasequentialsolution.Youstartwiththefeed,
and solve the mass balance for the mixer, labeled MIXR. Since you do not yet know the
amountofAinstreamS5,assumeitiszeroandgoon.ThenthereisonemoleofAfedto
thereactor,40%ofitreacts,andtheunreactedpartisrecycledintostreamS5.
FIGURE 5.7 Processwithrecycleand40%conversionperpass.
```

---

## Стр. 85

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
RECYCLE;COMPARISONOFSEQUENTIALANDSIMULTANEOUSSOLUTIONMETHODS 71
TABLE5.2 MassBalancewithRecycle,SolvedUsingSequentialMethod
Recycle
Iteration Feed, Recycle IntoReactor, Outof (atEndof
Number S1 (Guess),S5 S2 Reactor,S3 Iteration),S5
1 1 0 1 0.6 0.6
2 1 0.6 1.6 0.96 0.96
3 1 0.96 1.96 1.176 1.176
4 1 1.176 2.176 1.3056 1.3056
5 1 1.3056 2.3056 1.38336 1.38336
10 1 1.4848835 2.4848835 1.4909301 1.4909301
15 1 1.4988245 2.4988245 1.4992947 1.4992947
20 1 1.4999086 2.4999086 1.4999452 1.4999452
Step 2 Now repeat the process. This time when doing a mass balance on the mixer, you
haveavalueinstreamS5,soyoucanuseit.Youcontinuethisprocess,workingthrough
theprocessoverandover.After20iterations,thevalueofAintherecyclewhenyoustart
aniteration(1.4999086)isclosetothevaluewhenyouendtheiteration(1.4999452).You
can then stop. The solution is shown in Table 5.2; note that some of the rows have been
hidden(seethebookwebsite).
Manyprocesssimulatorsusethisprocedurebecauseitisquiteeasytoimplement.You
only need to have a module or subroutine for a mixer, a reactor, and a separator, and the
equations for each of these are quite simple. One problem that arises, though, is that the
procedure takes many iterations to converge if the conversion is low. And, if there are
interlockingrecyclestreams,convergencemaynotoccuratall.However,itisaquitegood
scheme,andyoucanapplyitusingaspreadsheet.
The other solution technique finds an algebraic solution. Look at Table 5.3. Assign a
variable name, R, to the unknown amount of A in stream S5. Work through the same
processonce;whenyoufinish,theamountofAintherecycle(whichyoucalledR)must
beequaltotheamountofAcomingoutofthelastunitandgoingintotherecyclestream.
Theequationrepresentingthatis
R =0.6 ∗ (1+ R) (5.5)
SolvingEq.(5.5)gives R=1.5.
Thesolutionisthesameasthatfoundwiththesequentialmethod,butyouobtainedit
inoneiteration.Theonlyproblemisthatyouhadtodoitanalytically,whichusuallyisnot
possible.However,youcanwritethemassbalanceequationsinageneralformandcreatea
largesetoflinearornonlinearequationstobesolvedsimultaneouslyonthecomputer.The
difficultyliesinthecomplexityoftheunits.Themixer,simplereactor,andsimpleseparator
leadtosimpleequations,butheatexchangers,distillationunits,andplugflowreactorsdo
TABLE5.3 MassBalancewithRecycle,SolvedUsingSimultaneousMethod
Feed Recycle(Guess) IntoReactor OutofReactor Recycle(atEndofIteration)
1 R 1+R 0.6∗(1+R) 0.6∗(1+R)
```

---

## Стр. 86

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
72 MASSBALANCESWITHRECYCLESTREAMS
not. In return for your work, though, you get enhanced convergence properties, since the
simultaneousmethodwillconvergewhenthesequentialmethoddoesnot.Inalaterchapter
youcanexaminesomeofthetrickschemicalengineersusetomakethesequentialmethod
workmoreoften.First,letuslearntosolveproblemswithrecycleusingExcel.
EXAMPLEOFPROCESSSIMULATIONUSINGEXCELFOR
SIMPLEMASSBALANCES
ThenextexampleillustratestheuseofExceltosolvemassbalancesforaprocessconsisting
ofafeedstream,amixerinwhichthefeedstreamismixedwiththerecyclestream,areactor,
followedbyaseparatorwheretheproductisremovedandthereactantsarerecycled.Inlater
examplesandproblems,therewillbeinertsandpurgestreams,andsoon,butthisproblem
usesastoichiometricfeed.Thereactorislimitedbychemicalequilibriumconsiderations,
whichcomplicatesthesolution.
Theprocesstakeshydrogenandnitrogen(ina3:1)ratiotomakeammonia.Thereactoris
limitedbyequilibrium;youwillpreparethespreadsheetinstagestoaidintroubleshooting.
Thus,firstprepareaspreadsheetasshowninFigure5.8,using25%conversionperpassin
thereactor.
Step1 Themixertakesstreams1and6andaddsthemandputsthemintostream2.For
example,D14=C14+H14.
Step2 ThenitrogenreactingisgivenbyE14=−$E$19∗D14.CellE15issettothreetimes
CellE14(hydrogenusesthreetimesthenitrogenreacting),andCellE16issettonegative
twotimesthenitrogeninCellE14.Inthiscolumn,thesignsarenegativeforreactantsand
positiveforproducts.Thespreadsheetclearlyshowsthatthestoichiometryiscorrect.
Step 3 Stream 5 takes 0.5% of the nitrogen and hydrogen and 98% of the ammonia:
G14=0.005∗F14;G15=0.005∗F15;G16=0.98∗F16.
FIGURE 5.8 Ammoniaprocesswith25%conversionperpassinthereactor.
```

---

## Стр. 87

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
EXAMPLEOFPROCESSSIMULATIONUSINGASPENPLUSFORSIMPLEMASSBALANCES 73
Step4 Therestgoesoutstream6:H14=F14−G14,andsoon.Youcaneasilycheckthe
molebalancearoundtheseparator.
Step5 Turnontheiterationfeatureforthecircularreferenceandtheproblemissolved.
EXAMPLEOFPROCESSSIMULATIONUSINGASPENPLUSFOR
SIMPLEMASSBALANCES
To perform this simulation in Aspen, without calculating any energy effects, open As-
pen Plus and go to Data/Setup. Open the Setup box on the left and choose Simulation
Options. Unclick the box that says Perform heat balance calculations. When filling out
the information in Aspen Plus, you may have to put in temperatures and pressures, but
they will not be used until you authorize the heat balance calculations. For this process,
chooseaMixer,StoichiometricReactor(RStoic),andComponentSeparator(SEP).Insert
theinformationonthefeedtotheprocess.Forthereactor,choosethatblock,thenchoose
Reactions,andthenNew.Definethestoichiometryofthereactionandtheconversionofa
specifiedcomponentasshowninFigure5.9.FortheComponentSeparator,chooseanout-
putstreamandprovidethefractionofeachcomponentgoingoutthatstream.Thenrunthe
problem,gettingtheresultsshowninTable5.4.Naturally,theyarethesameasfoundusing
Excel. Problem 5.9 provides a more complicated example of a process with interlocking
recycle streams. It was used early in the days of process calculations to test convergence
techniques.
FIGURE 5.9 Stoichiometryforreactor.
```

---

## Стр. 88

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
74 MASSBALANCESWITHRECYCLESTREAMS
TABLE5.4 AmmoniaProcesswith25%ConversionperPassintheReactor
1 2 3 4 5
Temperature(◦C) 25 25 25 25
Pressure(bar) 1.013 1.013 1.013 1.013 1.013
Vaporfraction
Moleflow(kmol/h) 400 1580.376 1383.332 202.956 1180.376
Massflow(kg/h) 3406.112 13491.587 13491.587 3406.112 10085.475
Volumeflow
Enthalpy(Gcal/h)
Moleflow(kmol/h)
N 100 394.089 295.567 1.478 294.089
2
H 300 1182.266 886.7 4.433 882.266
2
NH 0 4.021 201.066 197.044 4.021
3
EXAMPLEOFPROCESSSIMULATIONWITHEXCELINCLUDING
CHEMICALREACTIONEQUILIBRIA
Next,thereactorconversionischangedtobetheequilibriumconversion,whichmaynot
be25%.Theequilibriumequationis
1 3 p y 1
N + H ⇔NH , K = NH3 = NH3 (5.6)
2 2 2 2 3 p p1/2p3/2 y1/2y3/2 p
N2 H2 N2 H2
TheflowsheetandspreadsheetforthiscaseisshowninFigure5.10.ThevalueofK andp
p
areputintoCellsF26andF27,andthemolefractionsofthestreamcomingoutofthereactor
1 B C D E F G H
2
3 6
4
5
6 6 6
7
8
9 1 Mixer 2 Reactor 4 Separator 5
10
11 3
12
13 1 2 3-Reacting 4 5 6
14 Nitrogen 100.00 134.83 –99.82 35.00 0.18 34.83
15 Hydrogen 300.00 404.48 –299.47 105.01 0.53 104.48
16 Ammonia 0.00 4.07 199.65 203.72 199.65 4.07
17 Total 400.00 543.38 –199.65 343.73 200.35 143.38
18
19 Conversion 0.74039191
20 Reacting Mole fraction out of reactor
21 Nitrogen 0.1018 =F14/$F$17
22 Hydrogen 0.3055 =F15/$F$17
23 Ammonia 0.5927 =F16/$F$17
24 Total 1.0000
25
26 Kp 0.05
27 p 220
28 Equation 1.4432E-07 =F26-F23/((F21*F22^3)^0.5*F27)
FIGURE 5.10 Ammoniaprocesswithequilibriumconversioninthereactor.
```

---

## Стр. 89

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
PROCESSSIMULATIONWITHEXCELINCLUDINGCHEMICALREACTIONEQUILIBRIA 75
TABLE5.5 InputforCavettProblem5.9
Temperature(◦F) 120 Moleflow(lbmol)
Pressure(psia) 49 N 358.2
2
Vaporfraction 0.572 CO 4965.6
2
Moleflow(lbmol) 27340.6 H S 339.4
2
Massflow(lb/h) 1.87E+06 Methane 2995.5
Volumeflow(cu−) 1.97E+06 Ethane 2395.5
Enthalpy(MME) −2421.884 Propane 2291
i-Butane 604.1
n-Butane 1539.9
i-Pentane 790.4
n-Pentane 1129.9
n-Hexane 1764.7
n-Heptane 2606.7
n-Octane 1844.5
n-Nonane 1669
n-Decane 831.7
n-Undeca 1214.5
27340.6
areobtainedbytakingthemolesofaspeciesinstream4anddividingbythetotalmoles
instream4:F21=F14/$F$17.Thosemolefractionscanbeuseddirectlyinthechemical
equilibrium equation, as shown in Cell F28. This is simpler than deriving a chemical
equilibriumequationinvolvingthemolarflowrates.Noticethatastheconversionchanges,
themolebalancechanges.Thisinturnchangesthemolefractions,whichnolongersatisfy
thechemicalequilibriaequation.Thus,youshoulduseSolvertosetF28tozerobychanging
cellE19,wherethefinalresultisshown.(Note:GoalSeekdidnotworkforthisproblem.)
GoalSeekisavailablefromathirdpartyfortheMicrosoftoperatingsystemandisincluded
intheMacintoshversion.ThereverseholdsforSolver.ThesolutionshowninFigure5.10
wasobtainedusingtheMicrosoftoperatingsystemandfirstusingtheEvolutionarySolver
with 0.5 ≤ conv ≤1 to get close (10−4). Then the “GRG Nonlinear” option was used to
refinetheanswer.Theonlyremainingcheckistotakethefinalmolefractionsandcompute
the chemical equilibrium equation yourself. If it is satisfied, then you have the correct
solution. When using Excel, sometimes the iterations involving a circular reference do
not converge. You can use CTRL-Z to reset the spreadsheet or use the undo key in the
upperleft: .Anothermethodtoavoiddifficultiesistosavethespreadsheetasabackup
beforeturningoniteration.When“Solver”or“GoalSeek”arebeingused,anditdoesnot
converge,itaskswhetheryouwishtoreverttotheinitialguess;youwouldchooseyes.
DidtheIterationsConverge?
Inthisexample,youhavetwoiterations—onebecauseofthecircularreferenceduetothe
recycle streams and one because of the nonlinear chemical equilibrium equation. Some
computers cannot handle both of these complications together. If you need to iterate by
hand,followthesesteps.
Step 1 In effect you used the spreadsheet to do the molar balances, and you set conv
yourself.Thespreadsheetshowsthevalueoff(conv)foryourchoiceofconv,butitdoes
themolarbalanceanyway.
```

---

## Стр. 90

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
76 MASSBALANCESWITHRECYCLESTREAMS
Step 2 If f(conv) is not zero, you can change conv and do it again. Keep this up until
f(conv) is small enough to satisfy you. Once you are close, “Solver” should have no
problemconvergingtoatighttolerance.Whatyouaredoingisreplacingaproblemwith
two iteration loops with a problem in which you supply one of the numbers, and the
computer solves the other iteration loop. Then you change your number until the other
equationissatisfied.
Extensions
Ideally you would have calculated the phase equilibrium in the separator, too. Then you
wouldhavethreeinteractingiterations,anditwouldbetherareproblemthatExcelcould
solve.Thedifficultyisthatduringtheiterations,thevaluesmaybephysicallyunrealistic.
Then,theequilibriumrelationortheRachford–Riceequationgivesevenmoreunrealistic
values. Programs such as Aspen Plus can realize this and take precautionary steps to
avoidit.Astheflowsheetgetsmoreandmorecomplicated,andinvolvesmoreandmore
thermodynamics,thepowerofAspenPlusiswelcome;seeChapters6and7forexamples.
CHAPTERSUMMARY
Inthischapter,youlearnedhowtowritethemassbalanceequationsforsimpleunitsandthen
combinethemintoacomplicatedprocesstopology.Yousawthatthereweretwomethods
tosolvetheseequations,andExcelusedessentiallythesequentialmethodbecauseofthe
circularreference.Youlearnedtohandleseveralcomplications:recyclestreams,chemical
reactionequilibrium,phaseequilibrium,andpurgestreams.
CLASSEXERCISES
Divideintoteamsoftwotofourstudents.Workthroughaspreadsheet(Tables5.1,5.2,and
5.4; Figures 5.8 and 5.10), with each person of a team taking a unit, showing where the
parametersareforthatunitandcheckingtheresults.Aretheycorrect?Workthroughthe
wholeprocess.Alternatively,yourinstructorcanprepareaflowsheetanddatasetshowing
theresults,butwithsomeerrorsforyourteamtofind.
CLASSDISCUSSION(AFTERVIEWINGPROBLEM5.10
ONTHEBOOKWEBSITE)
Whathappenedtothemassbalanceswhenyouintroducedapurgestream?(Youcanrun
it without carbon dioxide, too.) What happened to the mass balances when vapor–liquid
equilibrium was required? Did the ratio of nitrogen to hydrogen in the recycle stream
change? Why or why not? What if you had to solve the Rachford–Rice equation in the
separator, the chemical equilibrium equation in the reactor, and set the purge fraction to
maintainamaximummolefractionofcarbondioxideintheinlettothereactor.Couldyou
dothatallinExcel?Woulditconverge?Speculate.
```

---

## Стр. 91

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 77
PROBLEMS
Note: All the problems can be solved using Excel or Aspen (with the mass balance only
option).Theinstructorcanspecifythepreferredmethod,orbothforcomparison.
5.1 TheprocessformakingbenzeneisdescribedbelowandillustratedinFigure5.11.The
1
complete process is described in 5.2. Project below; here the process is simplified.
(TorayIndustries,Inc.andUOPProcessDivision,1975,andOtanietal.,1968.)The
process converts toluene (feedrate of 100 mol/h) to benzene and xylenes by dispro-
portionation(alsocalledtransalkylation).Thereactionandconversionperpassis
2C H ⇔ C H +C H 58%conversion/pass
7 8 6 6 8 10 (5.7)
toluene benzene xylenes
The output from the reactor contains all the components; benzene is removed and
thentolueneisrecycled.Inthefirstsplitter,thebenzenestreamcontains99.5%ofthe
benzene fed to the splitter and 0.1% of the toluene and none of the xylene. In the
second splitter, the toluene recycle stream contains all the benzene, 99.5% of the
toluene and 0.1% of the xylene fed to the splitter. Perform a mass balance. What is
theoverallconversionoftoluenetoxylene?
Toluene
recycle
Benzene
Xylenes
Toluene Mixer Reactor Splitter Splitter
FIGURE 5.11 Simplifiedbenzeneprocess.
5.2 Project. The process for making benzene is illustrated in Figure 5.12, and you are
tomake the mass balance. (Toray Industries,Inc.and UOP Process Division, 1975,
and Otani et al., 1968.) The process converts toluene (feedrate of 100 mol/h) to
benzeneandxylenesbydisproportionation(alsocalledtransalkylation).Thexylenes
alsodisassociatetoformtolueneandtrimethylbenzene.Thesereactionsoccurwitha
FIGURE 5.12 Benzeneprocess.
```

---

## Стр. 92

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
78 MASSBALANCESWITHRECYCLESTREAMS
catalystinthepresenceofhydrogen,withatypicalratioof7:1hydrogentotoluene
feedtothereactor.Thehydrogenalsoreactswithtoluenetoformbenzeneandmethane
orwithxylenestoformbenzeneandmethane.Themolarconsumptionofhydrogen
isabout10%ofthatoftoluene.
Thereactionsandtheirconversionperpassare
2C H ⇔ C H + C H 58%conversion/pass
7 8 6 6 8 10 (5.8)
Toluene Benzene Xylenes
2C H ⇔ C H + C H 1%conversion/pass
8 10 7 8 9 12 (5.9)
Xylenes Toluene Trimethylbenzene
C H + H ⇔ C H + CH 0.14percentconversion/pass
7 8 2 6 6 4 (5.10)
Toluene Hydrogen Benzene Methane
C H + 2H ⇔ C H + 2CH 28%conversion/pass
8 10 2 6 6 4 (5.11)
Xylenes Hydrogen Benzene Methane
Theoutputfromthereactorcontainsallthecomponents,andthehydrogenandtoluene
arerecycled,themethaneisremovedfromtheprocess,andthebenzeneandxylenesare
removedfromtheprocess.Thevaporpressuresofthecomponentsat20◦Carebenzene,
75mmHg;toluene,22;xylenes,4.8–6.6;trimethylbenzene,1.1.Aseparationsystem
isusedthatremovesthehydrogenandmethanefirst,thenseparatesthebenzene,then
the toluene, and then the trimethylbenzene. The hydrogen and methane should be
somewhat separated (to recover the hydrogen, which is recycled) and the toluene is
recycled.Intheseparators,usesplitsof99.9%ofthelightcomponentoutthetopand
only0.1%ofthenextheaviercomponent.Usesplitsof100%forcomponentslighter
than the light key and 0% for components heavier than the heavy key. Use “Goal
Seek”or“Solver”toadjustthehydrogenmakeupfeedtoinsuretheproperamountof
hydrogenenteringthereactor(necessaryforthecatalyst).
5.3 Revise the process modeled in Problem 5.2 by using split fractions of 99% and
1
1%insteadof99.9%and0.1%inalltheseparators.Howdothetotalflowschange?
Wouldtheequipmenthavetobelarger?Woulditcostmore?Istheseparationcostless?
Answerthesequestionsqualitativelynow;whenyoufinishyourchemicalengineering
studiesyouwillbeabletoanswerthemquantitatively.
5.4 Ethyl chloride is manufactured in an integrated process; see Figure 5.13 (Stirling,
1
1984,p.72).Completethemassbalanceforthisprocess.Ethanereactswithchlorine
to make ethyl chloride and hydrogen chloride, and ethylene reacts with hydrogen
chloridetoformethylchloride:
C H +Cl ⇔C H Cl+HCl (5.12)
2 6 2 2 5
C H +HCl⇔C H Cl (5.13)
2 4 2 5
Theprocessisfedwiththreestreams:ethane,ethylene,andchlorine.Thefeedstreams
contain100mol/hofeach:ethane,ethylene,chlorine.Theethane/ethylenestreamalso
```

---

## Стр. 93

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 79
FIGURE 5.13 Ethylchlorideprocess.
contains1.0%acetyleneandcarbondioxide.(Forthisproblem,justuse1.0%carbon
dioxide.)Thefeedstreamsaremixedwithanethylenerecyclestreamandgotothe
firstreactor(chlorinationreactor)wheretheethanereactswithchlorinewitha95%
conversionperpass.Theproductstreamiscooledandethylchlorideiscondensedand
separated. Assume that all the ethane and ethyl chloride goes out in the condensate
stream.Thegasesgotoanotherreactor(hydrochlorinationreactor)wherethereaction
withethylenetakesplacewitha50%conversionperpass.Theproductstreamiscooled
tocondensetheethylchloride,andthegases(predominatelyethyleneandchlorine)
are recycled. A purge or bleed stream takes off a fraction of the recycle stream
(use1%).
5.5 Project. Vinyl chloride monomer is the raw material to make polyvinyl chloride
(PVC),whichisproducedingreatquantities.WhenPVCwasinvented(asahighly
elasticpolymerbyaUniversityofWashingtongraduate,WaldoL.Semon,PatentNo.
1,929,435)thevinylchloridewasmadebyreactingacetylenewithhydrogenchloride.
Aprocessthatusescheaperrawmaterialsisnowused(CowferandGorensek,1997),
andasimplificationofitisgiveninFigure5.14.Completethemassbalanceforthis
process.
Theethylene(100mol/h)andchlorine(103mol/h)streamisfedtoadirectchlo-
rinationreactorwherethereaction
C H +Cl ⇔ClC H Cl (5.14)
2 4 2 2 4
takes place with essentially 100% conversion of the limiting reagent (ethylene).
The selectivity to ethylenedichloride is 99% with the main by-product (and
FIGURE 5.14 Vinylchlorideprocess.
```

---

## Стр. 94

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
80 MASSBALANCESWITHRECYCLESTREAMS
the only one considered here) as 1,1,2-trichloroethane, formed in the following
reaction:
C H +2Cl ⇔C H Cl +HCl (5.15)
2 4 2 2 3 3
Theethylene andoxygen streamfedtotheoxychlorination reactoris50%ethylene
and100mol/htotal.Itismixedwithahydrogenchloriderecyclestream(whichhas
somechlorine)andsenttoanoxychlorinationreactor,wherethereaction
C H +2HCl+1O ⇔ClC H Cl+H O (5.16)
2 4 2 2 2 4 2
takesplacewithaconversionof96%forethyleneandethylenedichlorideselectivities
of95%.Hereyoucanassumethebyproductisall1,1,2-trichloroethane.
Theoutputfromthedirectchlorinationreactorissenttoadistillationtowerwhere
the heavy components are distilled off. The light components are sent to a furnace,
whereapyrolysisreactiontakesplace:
2C H Cl ⇔2C H Cl+2HCl (5.17)
2 4 2 2 3
Thefeedtothefurnacemustbeverypure(99.5%ethylenedichloride)toachievegood
cracking. The output is quenched. The liquid is the vinyl chloride product and the
vaporishydrogenchloride,whichisrecycledtotheoxychlorinationreactor.
Thefeedtotheoxychlorinationreactoris100mol/hethyleneand50mol/hoxygen.
The output is cooled to remove the liquid (mostly water). A vent is used to remove
lightgases.Theremaindergoestoadistillationcolumnwhereethylenedichlorideis
theheavycomponent(andissenttothefurnace)andthelightcomponentsarerecycled
totheoxychlorinationreactor.
5.6 Modify Problem 5.5 by using air instead of oxygen as feed to the oxychlorination
1
reactor.Makeamassbalanceoftherevisedprocess.
5.7 Synthetic ethanol is made by vapor-phase hydration of ethylene as shown in Figure
2
5.15.MakeamassbalanceofthisprocessusingExcel:
C H +H O→C H OH (5.18)
2 4 2 2 5
Water and ethylene is mixed with a recycle stream and sent to a reactor where
the reaction in Eq. (5.21) takes place (5% conversion of ethylene per pass). The
ethylene feed is 100 mol/h and is 97% ethylene but also contains acetylene (2.9%)
FIGURE 5.15 Ethanolprocess.
```

---

## Стр. 95

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 81
and inert gases (0.1%). The acetylene reacts with water, too, forming acetaldehyde
(50%conversionofacetyleneperpass):
C H +H O→CH CHO (5.19)
2 2 2 3
The reactor effluent is cooled to remove the liquids (ethanol, acetaldehyde, water).
The gases (ethylene, acetylene, and inert gases) are recycled, but a purge stream is
neededtoremovetheinertgases.
Assumeperfectsplits.Adjustthefractionpurgedtokeeptheratioofinertgasto
ethyleneinthestreamfedtothereactorat0.04,andfeedenoughwatertotheprocess
tomakethemolarratioofwatertoethylene0.6inthestreamintothereactor.Separate
theliquidsintorelativelypurecomponentstreams,firstremoving60%ofthewater,
then the acetaldehyde, and then purifying the ethanol to 93% ethanol by removing
water. In the acetaldehyde separation, remove 99% of the acetaldehyde and 1% of
ethanol and water. (Hint: This problem has two constraints. In Excel you can use
“GoalSeek”or“Solver”tosatisfyoneofthemandadjusttheothervariableyourself,
followed by another use of “Goal Seek” or “Solver.” Repeat this process until both
constraintsaresatisfied.)
5.8 Consideraprocesstomakeacetaldehydebydehydrogenationofethanoloverasilver
2
catalyst(Aguilo´andPenrod,1976),asillustratedinFigure5.16.Theethanolfeedrate
is350mol/h.
Thefollowingdesignconstraintsmustbesatisfied:
1. Ethanoldecomposestoformacetaldehydeandhydrogen:
C H OH→C H OH+H (5.20)
2 5 2 3 2
2. Theequilibriumlimitisabout35%conversionperpass,sothatarecyclestream
isnecessary.
3. Acetaldehyde reacts to form a number of side-products, including ethyl acetate,
aceticacid,andbutanol;onlyethylacetateisconsideredhere:
C H OH→ 1C H −CO−OCH (5.21)
2 3 2 2 5 3
4. Theconversionperpassisabout2%forthereactioninEq.(5.21).
FIGURE 5.16 Acetaldehydeproductionbydehydrogenationofethanol.
```

---

## Стр. 96

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
82 MASSBALANCESWITHRECYCLESTREAMS
5. Thefirstsplittermustseparatethereactoreffluenttoremovehydrogen;150mol/h
ofwaterisadded.
6. Thesecondsplittermustseparatetheacetaldehyde.
7. Thethirdsplittermustremovetheethylacetateandwaterandrecycletheethanol.
Makeamassbalancewiththefollowingseparations:
1. Ninety-ninepercentofthehydrogenand0.1%oftheothercomponentsgoesout
theoverheadofthefirstsplitter.
2. Ninety-ninepercentoftheacetaldehyde,100%ofthehydrogen,and0.5%ofthe
othercomponentsgoesouttheoverheadofthesecondsplitter.
3. Ninety-ninepercentoftheethanoland1%oftheothercomponentsgoesoutthe
overheadofthethirdsplitter.
5.9 CavettProblem.Chemicalplantsoftentimeshaverecyclestreams;itcansometimes
2
be difficult to solve the mass and energy balances because iteration is required. As
discussedinChapter7,tearstreamscanbeidentified;youtheninsertyourexpected
value of that stream and begin the computations. Hopefully, your guess is good
P1
FL1
S1
R1
AD1
FL2
FEED
R2
R3
AD2
S2
FL3
FL4
S3
P2
FIGURE 5.17 Cavettproblem(Cavett,1963;RosenandPauls,1977).
```

---

## Стр. 97

```text
P1:OTA/XYZ P2:ABC
JWBS084-c05 JWBS084-Finlayson May26,2012 13:54 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 83
enough that the calculations converge as they proceed from unit to unit, and then
aroundagain.Oneoftheearlyproblemsusedtotestconvergenceschemesiscalled
theCavettproblemafterthepersonwhoformulatedit.
The flowsheet isshown inFigure 5.17. Therearefour flash unitsoperated atthe
followingconditions:
FL1 100◦F,800psi
FL2 120◦F,270psi
FL3 96◦F,49psi
FL4 85◦F,13psi
The feed rate to the first unit is given in Table 5.5. These chemicals are typical
ofthoseinaRefinery,sotheChao–Seaderthermodynamicsisappropriate.Perform
a study of the convergence methods in Aspen Plus: Wegstein, Direct, Broyden, and
Newton.Solvetheproblemwitheachone,notingthenumberofiterations,themaxi-
mumerror/tolerance,andwhethertheprogramsaiditconverged.Betweeneachchoice
ofconvergencemethods,useRun/Reinitializesothattheproblemstartsfromscratch
atthebeginning.
```

---

## Стр. 98

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
6
THERMODYNAMICS AND SIMULATION
OF MASS TRANSFER EQUIPMENT
Masstransferisonesubjectthatisuniquetochemicalengineering.Typicalmasstransfer
problems include diffusion out of a polymer to provide controlled release of a medicine,
diffusion inside a porous catalyst where a desired reaction occurs, or a large absorption
columnwhereonechemicalistransferredfromtheliquidphasetothegasphase(orvice
versa).Themodelsofthesephenomenainvolvemulticomponentmixturesandcreatesome
toughnumericalproblems.
In Chapters 3 and 5, you have already seen separations achieved with flash units,
wherethepressureisloweredandthevaporandliquidoutputhavedifferentcompositions.
Such separation works when the chemicals have widely differing boiling points or are
otherwise easy to separate. When that is not the case, engineers must use distillation.
Otherphenomenausedforseparationincludeabsorption,liquid–liquidextraction(moving
achemicalfromoneliquidphasetoanotherone,withimmiscibleliquids),andadsorption
(used for identification in chromatography and for separation in chemical plants). This
chapterprovidessimpleexamplesofsomeofthoseprocesses.Yourcoursesinmasstransfer,
separations,thermodynamics,anddesignstudytheseprocessesingreaterdetail.Inaddition,
mass transfer involving diffusion and flow (like in microfluidic devices) is covered in
Chapters10and11.
When modeling mass transfer equipment, there are two key points to remember: (1)
thermodynamics is important and (2) convergence is difficult. The corollary is that you
havetocompareyourthermodynamicpredictionswithexperimentaldata.Also,youmay
startwithidealthermodynamicsandgetasolution.Thissolutioncanthenbeusedasthe
initial guess when the thermodynamic model is more realistic. Process simulators do not
alwayswork,becausefromiterationtoiterationtheconditionsmaybeunphysical,soyou
needtobeflexibleabouthowyouapproachaproblem.
IntroductiontoChemicalEngineeringComputing,SecondEdition.BruceA.Finlayson.
©2012JohnWiley&Sons,Inc.Published2012byJohnWiley&Sons,Inc.
85
```

---

## Стр. 99

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
86 THERMODYNAMICSANDSIMULATIONOFMASSTRANSFEREQUIPMENT
InstructionalObjectives: Afterworkingthroughthischapter,youwillhave
1. Learnedtomakereasonablechoicesofthermodynamicmodels.
2. Obtained experience modeling distillation columns, using both short-cut methods
andplate-to-platecalculations.
3. Learnedtomodelpackedbedabsorptioncolumns.
4. LearnedtouseAspenPluswithsensitivityblocksanddesignspecificationblocksso
thattheprogramcanvaryparameterstomeetyourobjective.
THERMODYNAMICS
Beforedoingprocesscalculations,itisnecessarytochooseamodeltodescribethether-
modynamic properties of the system (called Physical Property Methods in Aspen). The
chosen method must account for the forces acting on the molecules of the mixture. It is
important to distinguish between specific classes: neutral and nonpolar molecules (such
as alkanes), polar molecules (such as water and alcohols), and ionic systems. The forces
between these molecules include electrostatic forces between charged particles in ionic
systems or permanent dipoles. These develop because, for example, the two ends of the
moleculemayhaveoppositesignseventhoughthemoleculeisneutraloverall.Itmayalso
happen because atoms are sharing electrons (as in the HCl molecule, where chlorine has
sevenelectronsandsharesonewithhydrogen,buttheelectronsinthehydrogenorbitare
affectedmorestronglybythesevenelectronsinthechlorineorbit.Dipole–dipoleinterac-
tionsareproportionaltothesquareofthedipolemomentofeachspecies,butdipole–dipole
forcesfalloffmuchfasterwithseparationdistancethanCoulombforces(Koretsky,2004).
Induced dipoles can occur if the mixture is placed in an electric field, in which case
induction forces are important. The normal forces of attraction (dispersion forces) and
repulsion are always there, and in some systems loose chemical bonds can be formed
(hydrogen bonds). Statistical thermodynamics (Sandler, 2011) is useful for developing
thesemodels.
Thevirialequationofstateforavapor
pvˆ B(T) C(T)
=1+ + +··· (6.1)
RT vˆ vˆ2
canbederivedinanumberofwaysfromstatisticalmechanics,andthenumericalvaluesof
thevirialcoefficientscanbeobtainedasintegralsoverthevariousintermolecularforces.As
thepressureisincreased,moreandmoretermsareneededintheexpansion.Itispossible
todevelopmixingrulesforvapormixtures,too,basedonthetypeofforcesincluded.This
suffices for vapors, but the virial equation of state for liquids converges too slowly. It is
then necessary to use radial distribution functions, deduced from scattering experiments,
statisticalmechanicaltheoryofintegralequations(withnumericalsolutions),ormolecular
level computer simulations using Monte Carlo methods or molecular dynamics (Sandler,
2011).Althoughthemodelparametersarenotusuallydeterminedapriori,thestructureof
equations is used with adjustable constants that are chosen to fit experimental data. This
point emphasizes again that your choice of thermodynamic model must be validated in
someway,andcomparisonwithexperimentaldataisthegoldstandard.
```

---

## Стр. 100

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
THERMODYNAMICS 87
Someoftheoptionsforliquidsare(Sandler,2006)asfollows:
OptionOne:Iftheliquidsolutionisideal,theactivitycoefficientis1.0.
OptionTwo:TheMargulesone-constantmodelsareforliquidmixtureswithchemicals
that have similar sizes, shapes, and chemical nature. The two-constant Margules
equationexpandsthatfordissimilarmolecules.
Option Three: The van Laar model (and regular solution theory by Scatchard–
Hildebrand) assumes that the mole fraction around a molecule is the same as the
molefractionofthemixture.Butitdoesaccountforthefactthattheinteractionof
moleculeawitha,andbwithb,isdifferentfromtheinteractionofmoleculeawith
b. It works best for nonpolar compounds (like hydrocarbons) and compounds with
similarmolecular weights, and itmay work for weakly polar compounds. The Van
LaaroptionsarelessrecommendedinAspenPlus;theyaresimplertousethanthe
others, but less successful in general. In Aspen Plus the ease of use is immaterial
sincesomeoneelsehascreatedtheprogram.
Option Four: The Wilson equation removes the restriction in the van Laar model and
permitsthemolefractionaroundthemoleculetodependonthesizeandenergyofthe
molecule,notjustthemolefractionofthemixture(thisisalsotrueforthenonrandom
two liquid (NRTL) and UNIFAC models discussed later). It is more robust, and it
worksforpolarcompoundsandcanhandleazeotropes,butnottwoliquidphases.It
worksforalcoholsandalkanesandrequirespair-interactionparameters,whichmust
bedeterminedfromdata.Itusesmolarvolumesofthedifferentchemicals,sowhen
they are not equal, this is a good method. It also uses binary interaction energies,
and the parameters determined by fitting binary experimental data are also used in
multicomponentmixtures.
OptionFive:TheNRTLequationisevenmorerobust,anditworksforpolarcompounds
and can handle azeotropes as well as two liquid phases. This method includes the
effectofnonrandomnessandshort-rangeorderaswellasdifferencesduetomolecular
orientation.
Option Six: The UNIQUAC model is perhaps the best of the correlative equations. It
is based on statistical mechanics and uses information on molecular volumes and
surfaceareas,whichmakesitapplicabletomoleculesofdifferentsizes.Theactivity
coefficients are calculated as the sum of two contributions. The first is a size and
shapecontributionwithparametersgenerallyobtainedbyconsideringeachmolecule
to be a collection of functional groups (e.g., −CH and −CH OH), and adding up
3 2
the volumes and surface areas of the groups. All this information is in the Aspen
Plus database, and the calculation is done by Aspen Plus. The second contribution
in the UNIQUAC model is from the interactions between the molecules. The two
parameters for each binary pair of molecules in this contribution are obtained by
fittingexperimentaldata.TheUNIQUACmodelworksforpolarcompoundsandcan
handleazeotropesaswellastwoliquidphases.
OptionSeven:TheUNIFACmodelisacompletelypredictivemodelthatisespecially
usefulwhennoexperimentaldataareavailable.ItisbasedontheUNIQUACmodel,
butcarriestheideaofgroupcontributionsfurtherbycalculatingthevaluesofparam-
etersintheinteractionpartoftheUNIQUACmodelfromfunctionalgroup-functional
groupinteractions(unlikefrommolecule–moleculeinteractionsinUNIQUAC).The
functional group interaction parameters, obtained by correlating thousands of sets
```

---

## Стр. 101

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
88 THERMODYNAMICSANDSIMULATIONOFMASSTRANSFEREQUIPMENT
ofdata,areinAspenPlus.Asageneralrule,UNIFACpredictionsarelessaccurate
thanUNIQUACandothermodelsdiscussedearlierthathaveparametersobtainedby
correlatingdataforeachsystemofinterest,butitisvaluableforpredictionswhenno
dataareavailable.TheUNIFACmodelworksforpolarcompoundsandcanhandle
azeotropesaswellastwoliquidphases.
OptionEight:TheElectrolyteNRTLisgenerallyapplicabletoelectrolytesystems.Itis
commonlyusedforacidgassystemsbecauseinorganicamines,inorganiccarbonates,
andotherionsareinvolved.
What method should you use? Aspen Plus recommends using Peng–Robinson or
Redlich–Kwong–Soaveforhydrocarbonsandlightgasesundermoderateconditions.These
are Peng–ROB and RK–Soave in Aspen Plus. The equation of state will be used for all
thermodynamicpropertiesofbothgasesandliquidsexceptforliquiddensity.Toseedetails
of the equations of state and the list of properties needed to define them (which Aspen
Plus already has included), click on the help menu and type the abbreviation into the
searchwindow.
Ifthemixturecontainspolarcomponents,thenitisnecessarytouseWilson,NRTL,or
UNIFACpropertymethodsfortheliquid.Thesecanbecombinedwitheitheranidealgas
(WILSON,NRTL,orUNIQ-2)orRedlich–Kwong(WILS–RK,NRTL–RK,UNIFAC,or
UNIQ–RK).Thisworksforlow-to-moderatepressures.Asaroughruleofthumb,chemi-
calswithdipolemomentsof0.2Dandbelowcanbeconsiderednonpolar.Ifthepressure
is higher (say greater than 10 atm) then the recommended methods are Redlich–Kwong
orPeng–RobinsonwiththeWong–Sandler(1992)mixingrules(RKSWSorPRWS).Fig-
ure 6.1 is a simplified decision tree that applies to most of the examples and problems
in this book. If the chemicals are polar and electrolyte, one must use a special model for
electrolytes,ELECNRTL.
≥1 NRTL
UNIQUAC (or UNIFAC)
Yes Number of
liquid
phases
NRTL
1
UNIQUAC (or UNIFAC)
Wilson
Polar
p < 10 atm?
Nonelectrolyte
No
PRWS
RKSWS
FIGURE 6.1 Decisiontreeforchoosingthermodynamicmodels.
```

---

## Стр. 102

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
THERMODYNAMICS 89
TABLE6.1 MethodsforChoosingThermodynamicModels
Tools/PropertyMethodSelectionAssistant
Tools/NISTThermodynamicDataEngine
Help/InSearchWindow:GuidelinesforChoosing
GuidelinesforChoosingaPropertyMethod
GuidelinesforChoosingaPropertyMethodforPolar,NonelectrolyteSystems
GuidelinesforChoosinganActivityCoefficientPropertyMethod
AspenPlushashundredsofchoicesforthermodynamicmodels.Althoughtheguidelines
given earlier will suffice in many cases, there may be times when the comparison to
experimentaldataisnotgood.ThenthefeaturesinAspenPluscanbeusedtoexploreother
optionsassummarizedinTable6.1.
GuidelinesforChoosing
A convenient decision tree is available in Aspen Plus; enter Guidelines for Choosing a
Property Method into the Search window, and figures as in Figure 6.1 will appear. The
decisions you have to make are the ones shown in Figure 6.1 as well as: Real or pseu-
docomponents?;Interactionparametersavailable?;Vaporphaseassociation?;andDegree
ofpolymerization.
PropertyMethodSelectionAssistant
Another aid is the Property Method Selection Assistant, under Tools; see Figure 6.2. If
youselect“Specifycomponenttype”yougetawindowlistingofthreegroups:Chemical,
FIGURE 6.2 PropertymethodselectioninAspenProperties.
```

---

## Стр. 103

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
90 THERMODYNAMICSANDSIMULATIONOFMASSTRANSFEREQUIPMENT
TABLE6.2 EquationsofStateRecommendedforDifferentProcesses
Oilandgasproduction(OILGAS):Peng–RobinsonwithBoston–Mathiasalphafunction(PR–BM)
orRedlich–Kwong–SoavewithBoston–Mathiasalphafunction(RKS–BM).
Refinery—mediumpressure(REFINERY):Peng–Robinson,Redlich–Kwong–Soave;Chao–Seader,
Graysonareolderonesdevelopedspecificallyforrefineries.
Refinery—hydrogen-richapplications(REFINERY):Peng–Robinson,Redlich–Kwong–Soave.
Graysonisanolderonedevelopedspecificallyforrefineries.
Gasprocessing—hydrocarbonseparations(GASPROC):Peng–RobinsonwithBoston–Mathias
alphafunction(PR–BM),Redlich–Kwong–SoavewithBoston–Mathiasalphafunction
(RKS–BM),Peng–Robinson,Redlich–Kwong–Soave.
Gasprocessing—acidgasabsorption(CHEMICALANDELECTROLY):ElectrolyteNRTL.
Petrochemicals—aromaticsandetherproduction(PETCHEM):Wilson,NRTL,UNIQUAC.
Chemicals—phenolplants(CHEMICAL):Wilson,NRTL,UNIQUAC.
Chemicals—ammoniaplant(CHEMICAL):Peng–Robinson,Redlich–Kwong–Soave,SR–Polar
(Schwartzentruber–Renon).
Chemicals—inorganicchemicals(CHEMICALANDELECTROLY):ElectrolyteNRTL.
Coalprocessing—combustion(COALPROC):Peng–RobinsonwithBoston–Mathiasalphafunction
(PR–BM),Redlich–Kwong–SoavewithBoston–Mathiasalphafunction(RKS–BM),orthe
combustiondatabank.
Hydrocarbon,andSpecial.(1)IfyouchooseChemicalSystem,thefirstquestioniswhether
thepressureisabove10bars.Ifso,youaredirectedtouseequationsofstatewithadvanced
mixing rules, such as the Wong–Sandler method described earlier. If not, the program
recommends using NRTL, Wilson, UNIQUAC, or UNIFAC for liquid activity methods;
severalcautionsareprovidedforspecificsystemsthatcangivetrouble(carboxylicacids,
electrolytes, HF, etc.). (2) If you choose Hydrocarbon system, then additional choices
involvewhetherpetroleumassaysandpseudocomponentsareinvolved,andwhethervac-
uum conditions are used. Several reasonable choices of thermodynamic models are then
displayed. Even then, you should try each of those choices and compare the results to
experimentaldata.WhilethatmaynotbepossiblewhenlearningtouseAspenPlus,ifyou
andyourcompanyputmoneyonthetable,youbettertestthethermodynamics.
Itisalsoworthwhiletoseewhatmethodsarerecommendedforthetypeofprocessyou
aremodeling;inthescreenshowninFigure6.2,chooseSpecificprocesstype.Apartiallist
ofprocessesisshowninTable6.2.IfonechoosesChemical,anewscreengiveshintsfor
specificchemicalsystemsaswellasasummaryofhelpcommands.
ThermodynamicModels
To get general information about the equations of state and the liquid activity coefficient
property methods, search on “Liquid Activity Coefficient Property Methods” or on the
abbreviationoftheequationofstate.Table6.3showssomeofthecombinationsofequations
ofstateandliquidthermodynamicmodels.Thislisthighlightsthemost-usedequationsof
state.Withallthesechoices,andlimitedknowledgeofyoursystem,youwilllikelywant
tousetherecommendedoptionsandmakepredictionsofvapor–liquidequilibriumusing
Aspen Plus to compare those predictions with experimental data. Chapter 3 presents an
exampleofsuchacomparisonfortheethanol–watersystem.
```

---

## Стр. 104

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:MULTICOMPONENTDISTILLATIONWITHSHORTCUTMETHODS 91
TABLE6.3 PairsofEquationsofStateandLiquidActivityCoefficientModels
(AbbreviatedList)
PropertyMethod GammaModel EquationofState
NRTL NRTL Idealgaslaw
NRTL–RK NRTL Redlick–Kwong
UNIFAC UNIFAC Redlich–Kwong
UNIFAC–LL UNIFAC Redlich–Kwong
UNIQ-2 UNIQUAC Idealgaslaw
UNIQ–RK UNIQUAC Redlich–Kwong
WILS-2 Wilson Idealgaslaw
WILS–RK Wilson Redlich–Kwong
PropertyMethod EquationofState Exceptfor
PENG–ROB Peng–Robinson Liquidmolarvolume
RKSWS Redlich–Kwong UNIFACforexcessHelmholzfreeenergy
PRWS Peng–Robinson Wong–Sandlermixingrules
EXAMPLE:MULTICOMPONENTDISTILLATION
WITHSHORTCUTMETHODS
Considerasingle-distillationcolumnasshowninFigure6.3.Short-cutmethodshavebeen
developed that allow you to see the splits that can be achieved at different pressures,
with different reflux ratios, and with a different number of stages. It is often useful to
do a short-cut distillation calculation first, before doing the more rigorous plate-to-plate
calculations,becausethepreliminarycalculationsgiveyouanideaofwhatisreasonable.
Themethodsarebasedontherelativevolatilityofthechemicals,andrequireyoutoidentify
2
1 B1
3
FIGURE 6.3 Distillationcolumn.
```

---

## Стр. 105

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
92 THERMODYNAMICSANDSIMULATIONOFMASSTRANSFEREQUIPMENT
TABLE6.4 IdentificationofLightandHeavyKey
Chemical BoilingPoint(◦C)at1atm
Propane −42.1
i-Butane −11.9
n-Butane −0.5
i-Pentane 27.9
n-Pentane 36.1
two components that will be essentially separated (to the extent you specify). If you line
upallthecomponentsintheorderoftheirboilingpoints,anddrawalinebetweentwoof
them,themorevolatilecomponentiscalledthelightkeyandthelessvolatilecomponent
iscalledtheheavykey.
For this example, you choose the first column in the process shown in Figure 5.4. In
AspenPlus,youusethemoduleDSTWUfortheshortcutmethod;youalsouseRK–Soave
as the physical property method, because it is a good one for hydrocarbons. The feed is
100 lb mol/h of propane, 300 lb mol/h of i-butane, and the other chemicals as listed in
Table5.1,at138psiaand75◦F.Thecolumnoperatesat138psiawitharefluxratioof10
(awildguessinitially,confirmedbecausethecolumnworked).Remember,theminimum
number of stages goes together with infinite reflux, so if your column does not work,
increasetherefluxratio.
First,you specifythesplityouwouldlike.Todothis,you needtheconcept ofalight
keyandheavykey.First,linethechemicalsupinorderoftheirboilingpoints,fromlowto
high.(Note:thisillustrationassumesthatthethermodynamicsareideal,soRaoult’sLaw
applies.) Because you are using distillation, if most of the propane is to go out the top
stream, a little of the i-butane will, too; very small fractions of the other species will go
outthetopstream.Youwantmostofthei-butanetogooutthebottom.Thus,youdrawa
linebetweenpropaneandi-butaneinTable6.4.Thecomponentabovethelineisthelight
keyandthecomponentbelowthelineistheheavykey.Thedistillationcolumnisbasedon
those two components, and the other components are split according to thermodynamics
asdescribedlater.Inthiscase,propaneisthelightkey,andyouwant99%ofittogoout
thetopstream;i-butaneistheheavykey,andyouwant1%ofittogooutthetopstream.
Inashortcutmethod,correlationsareusedtorelatetherefluxratio,minimumrefluxratio,
number of stages, minimum number of stages and the relative volatilities. The equations
are available on the book website, but here it suffices to say that the results are based on
correlationsbutareoftenquitegood,especiallyforhydrocarbons.
YoucanuseAspenPlustosolvethisproblemusingtheDSTWUblock.
Step 1 The flowsheet is shown in Figure 6.3, and you enter the components and feed
conditions in the usual manner (see other examples in Chapters 2–5 and Appendix C).
UsingtheTools/PropertyMethodSelectionAssistant,process=refinerygivessuggestions
forthethermodynamicmodel:BK10,Chao–Seader,andPENG-ROB.Thethermodynamics
model chosen was the PENG-ROB. The parts specific to the distillation column are the
blockparameters.ShowninFigure6.4isthescreenwhereyouselecttheblockparameters.
You choose the light and heavy keys (propane and i-butane), the splits desired (99% and
1%), the pressure of the column (138 psia),a total condenser, and the desired number of
stages(10).
```

---

## Стр. 106

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:MULTICOMPONENTDISTILLATIONWITHSHORTCUTMETHODS 93
FIGURE 6.4 BlockinputinformationforDSTWUblock.
Step2 Figure6.5showsthesolutionwithstreaminformation.Youcancheckpartsofthis
output.Lookfirstatthemolebalances.Indeed,99%ofthepropaneand1%ofthei-butane
wentoutthetopstream.Theothercomponentsareheavier,andyouwouldexpectthemto
besplitinsuchawaythatonlyasmallfractiongoesoutthroughtheoverheadstream;this
isindeedthecase.Youalsogetthebubblepointsofthedistillateandbottomproduct(not
shown):82.0◦Fforthedistillateand200.9◦Fforthebottomproduct.Theseareclosetothe
valuesshowninChapter5,whichshouldgiveyouconfidenceinthethermodynamicsused
inthecalculations.
FIGURE 6.5 MulticomponentdistillationwithDSTWU.
```

---

## Стр. 107

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
94 THERMODYNAMICSANDSIMULATIONOFMASSTRANSFEREQUIPMENT
FIGURE 6.6 BlockresultsforDSTWUblock.
Step3 Youalsowanttoknowtheparametersofthedistillationcolumn,whichareobtained
bychoosingtheblockforthecolumnandthenclickingtheResultstab,givingFigure6.6.
Note that the minimum number of stages is 16, the minimum reflux ratio is 3.14, the
actual reflux ratio is 3.66, and the actual number of stages is 32. In this case, your guess
of 10 stages was too small and the program modified it for you. If you had entered 32
stages,theprogramwoulduseexactly32stages.Youcouldhavespecifiedtherefluxratio
instead,andAspenPluswouldcomputethenumberofstages.Thefeedisonthe16thstage
(fromthetop).
Notethattheratioofrefluxratiotominimumrefluxratiois3.66/3.14=1.17,whichis
acommonandeconomicalone.However,duringtheenergycrisisinthe1970s,engineers
foundthataratioof1.1wasmoreeconomical,althoughthedistillationtowerwasharderto
control.Thisisoneofthechoices(numberofstagesorrefluxratio)thatyouwillmakeas
achemicalengineerthataffectstheeconomicsoftheprocess.Thecostofthecolumnand
theheatingandcoolingcostmustbeexaminedtofindtheminimumcost.Inthiscase,the
reboilerdutyis15.3×106Btu/handthecondenserdutyis2.7×106Btu/h.Sinceheating
ismoreexpensivethancooling,themajoroperatingcostisthecostofthesteamtoheatthe
reboiler.Ifenergyissellingfor$6permillionBtu,youwouldhaveanoperatingcostfor
thiscolumnof$61perhour,orabout$540,000peryear.
Yourchoiceofthermodynamicmodeldoesmakeadifference.Table6.5showsresults
fromthreesimulations,allwithexactly26stages,usingdifferentmodels.Theresultsdiffer,
butsinceAspenPlusrecommendstheChao–SeaderandRKS–BMmodels,wechoosethem
ratherthantheRK–Soave.
Difficultiescanarise.Ifyoumisidentifythelightandheavykey(sayreversingthem),
you may get a negative number of stages. If you identify a light and heavy key that has
another component that boils between them, that other component will be split in some
way, which may not meet your desired specifications. If the thermodynamics is nonideal
andtheboilingpointsarenotsufficienttoguaranteethevolatility(i.e.,activitycoefficients
```

---

## Стр. 108

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
MULTICOMPONENTDISTILLATIONWITHRIGOROUSPLATE-TO-PLATEMETHODS 95
TABLE6.5 ComparisonofDifferentThermodynamicModels
ThermodynamicModel RK–Soave RKS–BM Refinery/Chao–Seader
Minimumnumberofstages 10.9 16 15.6
Actualnumberofstages 22 32 31
Minimumrefluxratio 1.0 3.14 2.85
Actualrefluxratio 1.3 3.66 3.34
areimportant),thenyoumayspecifythelightandheavykeycorrectlyaccordingtotheir
boilingpoints,butthesimulationmayactasiftheywerenotspecifiedcorrectly.
MULTICOMPONENTDISTILLATIONWITHRIGOROUS
PLATE-TO-PLATEMETHODS
Theshortcutdistillationmethodgivesreasonableanswerstostraightforwardproblems,but
distillationscanhavemultiplefeedstreamsormultipleproductstreams.Theremightevenbe
azeotropeswithinthecolumn.Tohandlecomplicationslikethat,andtogetbetteraccuracy,
youwillwanttousearigorousplate-to-platemethodthattakesavaporstreamandliquid
stream,equilibratesthem,andsendsoffavaporandliquidstreamwithdifferentcomposi-
tions.Thisiswhathappensoneachplate,ortray,onthecolumn.Suchamethodisalarge
computationalproblem,anditrequiresspecifyingthenumberofplates,ortrays,orstages,
inadvance.Agoodstartingpointisthenumberofstagessuggestedbytheshortcutmethod.
Thenextsimulationisforthesamecolumn,butusingtheRadFracblockinAspenPlus.
The feed is the same, the pressure is 138 psia, and the PENG-ROB property method is
used.Thisexampleuses32stages,andyourunAspenPlustoseewhatthesplitis.(Note
thatyoucannoteasilysetthesplitandfindthenumberofstagesorrefluxrationeededto
achieveit.)Settherefluxratioto3.7andenterthefeedonthe13thstage.
The output is shown in Table 6.6, and only 62% of the propane goes out the top
stream;alongwith5%ofthei-butane.Thecondenserisat99.5◦Fandhasaheatdutyof
TABLE6.6 StreamTableforMulticomponentDistillationwithRadFrac,
RefluxRatio=3.7
1 2 3
Temperature(◦F) 75 99.5 174.2
Pressure(psia) 138 138 138
Vaporfraction 0 0 0
Moleflow(lbmol/h) 1800 100 1700
Massflow(lb/h) 110232.9 4937.957 105294.9
Volumeflow(cuft/h) 3051.494 157.948 3303.065
Enthalpy(MMBtu/h) −120.833 −5.67 −108.691
Moleflow(lbmol/h)
Propane 100 62.336 37.664
i-Butane 300 14.829 285.171
n-Butane 500 3.064 496.936
i-Pentane 400 19.771 380.229
n-Pentane 500 0 500
```

---

## Стр. 109

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
96 THERMODYNAMICSANDSIMULATIONOFMASSTRANSFEREQUIPMENT
(a)
(b)
FIGURE 6.7 MulticomponentdistillationwithRadFrac,refluxratio=3.7.(a)Condenserresults;
(b)reboilerresults.
−3.3 × 106 Btu/h, and the reboiler is at 174.2◦F and has a heat duty of 9.8 × 106 Btu/h
(seeFigure6.7).Toseetheflowratesoneachstage,choosetheblock,thenProfiles.Above
thefeed,theliquidflowratevariesbetween330and470lbmol/h,andbelowit,theflow
ratevariesbetween2920and2940lbmol/h.AlthoughDSTWUassumesthesamenumber
ofmolesoneachplateortray,RadFraccalculateswhatactuallyoccurs.
Sincethedesiredseparationisnotachieved,youmustruntheproblemagainwithmore
stages (40) and a higher reflux ratio (11). The results are in Table 6.7. The separation
is slightly better than required (99.2%). This, of course, changes the temperatures of the
condenser and reboiler because they are at the bubble points of the mixtures, and these
changewithcomposition.Thecondenserisat77◦Fwithaheatdutyof−7.0×106 Btu/h,
and the reboiler is at 177◦F and with a heat duty of 14.3 × 106 Btu/h. Above the feed
stream, the liquid flow rate varies between 920 and 1200 lb mol/h, and below it the flow
rateisabout3520lbmol/h.
```

---

## Стр. 110

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:PACKEDBEDABSORPTION 97
TABLE6.7 MulticomponentDistillationwithRadFrac,RefluxRatio=11
1 2 3
Temperature(◦F) 75 77.3 177
Pressure(psia) 138 138 138
Vaporfraction 0 0 0
Moleflow(lbmol/h) 1800 100 1700
Massflow(lb/h) 110232.9 4421.785 105811.1
Volumeflow(cuft/h) 3051.494 143.763 3327.539
Enthalpy(MMBtu/h) −120.833 −5.206 −109.003
Moleflow(lbmol/h)
Propane 100 99.135 0.865
i-Butane 300 0.363 299.637
n-Butane 500 0.018 499.982
i-Pentane 400 0.484 399.516
n-Pentane 500 0 500
EXAMPLE:PACKEDBEDABSORPTION
If a gas contains a contaminant you would like to remove, one way is to bring the gas
intocontactwithaliquidthatcanabsorbit;thisisoftendoneinanabsorptioncolumn,as
illustratedinFigure6.8.Here,youtakeanairstreamcontainingacetoneataconcentration
of2%;youwanttoloweritsconcentrationto0.4%byusingwaterinacolumn.InAspen
7
ADSORB
6
4
8
FIGURE 6.8 Absorptioncolumn.
```

---

## Стр. 111

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
98 THERMODYNAMICSANDSIMULATIONOFMASSTRANSFEREQUIPMENT
Plus,youcanuseRadFrac.TogetthisformofthepictureforRadFrac,openuptheoptions
fortheRadFracblockbyclickonthedownwardpointingarrow.Theonlydifferencefrom
distillation towers is that you will not have a condenser or reboiler, and there are two
inputs,oneateachend.Beforemakingthatmodel,youhavetodecideonanappropriate
thermodynamicmodel.Figure6.9showsexperimentaldata,alongwiththepredictionsof
AspenPlususingtheWILS-2thermodynamicmodel,whichisWilsonwithanidealgas.
(a)
(b)
FIGURE 6.9 Vapor–liquid diagram for acetone–water: (a) experimental data at 1.01 × 105 Pa
(OthmerandMorley,1946);(b)calculationsat1atmusingWILS-2thermodynamics.
```

---

## Стр. 112

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:PACKEDBEDABSORPTION 99
(a) (b)
FIGURE 6.10 AbsorptioncolumnparametersinAspenPlus.(a)Feedstreams;(b)productstreams.
This is one of the recommended models suggested by Aspen using the Tools/Property
MethodSelectionAssistant...for“Specifycomponenttype”and“chemicalsystem,”not
high pressure. The experimental data were obtained by choosing the blue and red NIST
TDEbuttonandlookingatTxydata.TheoneplottedisVLE036duetoOthmerandMorley
(1946),andreasonableagreementexistsforthisverynonlinearsystem.
Usea12-stagecolumnandhavetheairstreamenteronstage12andthewaterstream
enters on stage 1, as shown in Figure 6.10. (The stages are numbered from the top.) The
feedstreamsarebothtakenas80◦Fand14.7psia.Table6.8showsthefeedratesoftheair
andwaterstream.
Acetone has been transferred from the air stream to the water stream, and the mole
fractionoftheairstreamleavingis0.406%.Notealsothattheair,whichwasdryentering,
isnowwet,withwatervaporformingabout3.5%ofthegasstream.Asmallamountofair
isdissolvedinthewater,too.Inacompletesystem,ofcourse,thewatereffluentistaken
toanothercolumnwheretheacetoneisremovedandthewaterisrecycled.Thenthewater
streamissaturatedwithairandcontainssomeacetoneaswell.
Absorber/stripper combinations are used to remove a chemical from a stream. For
example,carbondioxideisoftenabsorbedintomonoethanolamine(MEA);thesteamthen
issenttoastrippingcolumnatadifferentpressureandthecarbondioxideisremovedout
thetop.TheMEAissentbacktotheabsorbertobeusedagain.Suchunitsareubiquitous
inrefineries,buttheyaredifficulttosimulatebecauseoftherecycleandthefactthatthe
TABLE6.8 AcetoneRemovalStreamTable
Substream:Mixed 4 6 7 8
Moleflow(lbmol/h)
Acetone 3.527396 0 0.7288636 2.798533
Water 0 176.3698 6.117179 170.2526
Air 172.8424 0 172.596 0.2463896
Totalflow(lbmol/h) 176.3698 176.3698 179.4421 173.2976
Totalflow(lb/h) 5208.816 3177.352 5149.347 3236.821
Totalflow(cuft/h) 69485.12 51.28876 70657.21 52.37885
Temperature(◦F) 80 80 79.70766 59.21119
Pressure(psia) 14.7 14.7 14.7 14.7
Vaporfraction 1 0 1 0
Liquidfraction 0 1 0 3
```

---

## Стр. 113

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
100 THERMODYNAMICSANDSIMULATIONOFMASSTRANSFEREQUIPMENT
absorberitselfmaynotconverge.ExamplesaregiveninAspenExamples(seeAppendix
C),andmostoftheabsorbersusingaminesinvolverate-basedversionsofRadFrac.Agood
strategyistonotconnecttherecyclestream,butadjustconditionssothattheoutputfrom
thestripperisaboutequaltotheabsorberamineinputstream.
EXAMPLE:GASPLANTPRODUCTSEPARATION
Consider the gas plant product separation process described in Figure 5.4. The pressures
intheunitshavebeenchosensotheoverheadstreamscanbecooledwithcoolingwaterat
80◦F.Thus,thedesignerlookedatthevaporpressureofeachcomponentbeforefixingthe
pressures.Thetemperaturesofthereboilersarebasicallyatthebubblepointofthebottom
stream,andthiswillbeanoutputofthecomputerprogram.
UseAspenPlusandmodeleachdistillationcolumnusingtheDSTWUmodelasshown
in Figure 6.11. First, specify the split of key components: for the light component you
want 99% out the top and for the heavy component you want 1% out the top. The other
componentswillbesplitaccordingtotheshortcutmethod[TheFenskeequation,Eq.(6.3)
onthebookwebsite.]
ChoosethethermodynamicpropertymethodasRefinery/Chao–Seader.Choosethepres-
suresofthecolumnstoagreewiththegasplantinFigure5.4.Eachcolumnhas26stages,
andthetemperaturesshowninTable6.9aretheresultofthermodynamicspredictedwith
AspenPlus.TheseareveryclosetothoselistedinFigure5.4.
Aspen Plus also gives information such as the number of stages, minimum reflux ra-
tio, and heat duties in the reboiler and condenser. With the information shown engineers
can calculate the capital cost of the equipment (sometimes using rules of thumb to ac-
count for instrumentation, pumps, valves, etc.). You can also calculate at least some of
the operating cost, the raw material cost and product value, and the cooling and heating
cost. For distillation towers at normal temperatures, the heating cost per unit of energy
is about 10 times the cooling cost when using cooling water. If refrigeration is used
to cool the condensers, that energy cost is even more expensive that the cost of steam.
Experienced designers know that, and that is why the pressures are chosen so that cool-
ing water can be used in the condensers. The conditions of the columns are given in
Table6.10.
5 6
7 8
B1 B2 B3 B4
1
2 3 4
9
FIGURE 6.11 Gasplantseparationinadistillationtrain.
```

---

## Стр. 114

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
noitarapeStnalPsaGmorfstluseR
9.6ELBAT
9
8
7
6
5
4
3
2
1
611
9.99
7.08
9.97
28
6.441
7.831
9.002
57
)F◦(erutarepmeT
02
02
63
15
831
63
15
831
831
)aisp(erusserP
0
0
0
0
0
0
0
0
0
noitcarfropaV
906.894
589.104
631.794
30.003
42.201
495.009
37.7931
67.7961
0081
)h/lombl(wofleloM
908.47953
309.33982
892.65982
737.42471
778.3554
317.80946
10.56839
57.982111
26.348511
)h/bl(woflssaM
862.169
735.867
166.118
141.805
437.841
606.6971
106.5562
308.5943
10.6213
)h/tfuc(woflemuloV
793.63−
384.03−
215.13−
319.91−
743.5−
705.56−
332.69−
611.111−
940.521−
)h/utBMM(yplahtnE )h/lombl(wofleloM
0
0
0
1
99
0
0
1
001
enaporP
0
100.0
969.2
30.492
3
100.0
79.2
792
003
enatuB-i
0
849.4
518.984
899.4
42.0
849.4
267.494
67.994
005
enatuB-n
69.3
40.293
4
0
0
693
004
004
004
enatneP-i
946.494
699.4
253.0
200.0
0
646.994
899.994
005
005
enatneP-n
101
```

---

## Стр. 115

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
102 THERMODYNAMICSANDSIMULATIONOFMASSTRANSFEREQUIPMENT
TABLE6.10 ConditionsinDistillationColumnsinGasPlantSeparation
Column B1 B2 B3 B4
Minimumrefluxratio 2.93 9.5 1.9 7.9
Actualrefluxratio 3.43 10.8 2.2 8.9
Minimumnumberofstages 12.9 31.1 11.3 36.8
Numberofactualstages 26 62.3 26 73.5
Feedstage 13.7 33.4 13.6 39.2
Reboilerheatingrequired 11.5×106 23.8×106 13.4×106 40.0×106
Condensercoolingrequired 2.9×106 28.8×106 14.2×106 41.3×106
EXAMPLE:WATERGASSHIFTEQUILIBRIUMREACTORWITH
SENSITIVITYBLOCKANDDESIGNSPECIFICATIONBLOCK
Next,weconsideranequilibriumreactorandletthetemperaturechange.Wehavesolved
foranadiabaticreactor(Table4.4),sonextsolveforonewithheating,thendoasensitivity
calculation,andfinallysolveitwithadesignspecification.InChapter8,thesameproblem
issolvedusingrateequations.
1. Reactor with Heating: Open the same file used to produce Table 4.4. Change the
inlettemperatureto25◦C;inthereactorsetup,setthetemperatureto226.85◦C;see
Figure6.12.Thesolutiongivesamolefraction0.079forCOandH O,aswasfound
2
forTable4.4.ButifwelookattheReactorResultswefindweneed0.00499Gcal/h,
or0.0209GJ/h.Thismuchenergymustbesuppliedtokeeptheoutlettemperatureat
226.85◦C.
2. Sensitivity Block: Change the reactor setup to use heat duty instead of temperature
initsspecifications.Althoughtheheatdutywillbechangedinthesensitivitycalcu-
lation,itisagoodideatogiveitaprospectivevalue,here0.001Gcal/h,asshownin
Figure6.13.ThenopenModelAnalysisTools/Sensitivityanddefineanewanalysis
calledHEAT.OpentheInputunderthatanddefinetwoflowsheetvariables,FRAC-
TIONandTEMPasshowninFigure6.14.Thesearedefinedbyputtinginthename
FIGURE 6.12 Reactorwithheating.
```

---

## Стр. 116

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:WATERGASSHIFTEQUILIBRIUMREACTOR 103
FIGURE 6.13 Reactorsetupforsensitivitycalculations.
anddoubleclickingit.Avariabledefinitionwindowcomesup;forFRACTION,the
windowisshowninFigure6.15.ThisisthemolefractionofCOintheexitstream,
S2.TEMPisthetemperatureofstreamS2,whichisdesiredforthesensitivitytable.
Next,clickontheVarytabandfillinthewindowasshowninFigure6.16.Byplacing
your cursor on each arrow and looking down the selections, you can obtain what
is shown there. The calculation will be done using heat duties from 0.001 to 0.008
Gcal/h.Finally,clickontheTabulatetabandchooseFRACTIONforcolumn1and
TEMPforcolumn2oftheTable.Theparameterbeingvariedwillalsobelistedin
the table. The table is shown in Figure 6.17; it can also be copied and pasted into
Excel. Now we have a solution for a variety of outlet temperatures along with the
heatdutyneededtocometothattemperature.Thistakesintoaccountboththeheat
capacityofthevarioussubstancesaswellastheheatofreaction
3. DesignSpecifications:Thenextsimulationshowshowtosetadesignspecification.
Inthiscase,wewillchoosethedesiredmolefractionofCOintheoutputstreamS2
FIGURE 6.14 Inputforsensitivityblock.
```

---

## Стр. 117

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
104 THERMODYNAMICSANDSIMULATIONOFMASSTRANSFEREQUIPMENT
FIGURE 6.15 Variabledefinitionforsensitivityblock.
andlettheprogramfigureoutwhattheheatingdutyisforthatoutcome.Thisisdone
usingtheFlowsheetingOptions/DesignSpecoption.ClickonDesignSpecandcreate
anewone,calledDS-1.DefinetheInputasshowninFigure6.18inthesameway
usedforthesensitivityanalysis(b)intheprecedingtext.Thespecificationsaresetin
theSpectab,asshowninFigure6.19:FRACTIONistobesetto0.07,withatolerance
of0.001.Theparametertobevariedisthesameasinthesensitivityexample,namely
FIGURE 6.16 Varyaparameterinsensitivityblock.
```

---

## Стр. 118

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:WATERGASSHIFTEQUILIBRIUMREACTOR 105
FIGURE 6.17 Tablefromsensitivitycalculations.
FIGURE 6.18 Designspecificationinput.
FIGURE 6.19 Designspecifications.
```

---

## Стр. 119

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
106 THERMODYNAMICSANDSIMULATIONOFMASSTRANSFEREQUIPMENT
FIGURE 6.20 Resultsusingthedesignspecificationblock.
theheatduty.Themanipulatedvariablelimitsarefrom0.001to0.008withastepsize
of0.0005.TheresultsunderDesignSpecareshowninFigure6.20.ThestreamS2
hasamolefractionof0.070andatemperatureof305.7,usingheatdutyof0.006966
Gcal/h.
CHAPTERSUMMARY
ThischapterintroducesyoutothemanythermodynamicmodelsavailableinAspenPlus.
Aspen Plus was used to solve a variety of distillation problems, with either short-cut
methods (DSTWU) or plate-to-plate methods (RadFrac). You also learned how to solve
gasabsorptionproblemsusingAspenPlus.Finally,youlearnedhowtousethesensitivity
optionanddesignspecoptioninAspenPlus.
CLASSEXERCISE
Divideintogroupsoftwotofourstudents.Workthrougheachoftheexamples,witheach
person on the team taking a unit, showing where the parameters are for that block and
checkingtheresults.(1)Tables6.6and6.7;(2)Table6.8andFigure6.8;(3)Tables6.9and
Figure6.11.Alternatively,yourinstructorcanprepareaflowsheetanddatasetshowingthe
results,butputinsomeerrorsforourgrouptofind.
PROBLEMS(UsingAspenPlus)
6.1 ModelcolumnB2inFigure6.11usingashortcut,DSTWUblockwiththeconditions
1
oftheinletstreamasshowninTable6.9,stream2,butwithapressureof51psia.
6.2 Model column B2 in Figure 6.11 using a detailed model, RadFrac. (Hint: use the
1
results from problem 6.1 to choose key operating parameters.) Prepare a report
comparing the output when using DSTWU and RadFrac to model the distillation
column.Whatinformationwasneededforeach?Howdotheresultscompare?
6.3 (a) Model column B3 in Figure 6.11 using a shortcut, DSTWU block with the
2
conditions of the inlet stream as shown in Table 6.9, stream 3, but with a pressure
```

---

## Стр. 120

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
PROBLEMS(UsingAspenPlus) 107
of 36 psia. (b) Then model the same column using RadFrac. How do the results
compare?
6.4 (a) Model column B4 in Figure 6.11 using a shortcut, DSTWU block with the
2
conditions of the inlet stream as shown in Table 6.9, stream 4, but with a pressure
of 20 psia. (b) Then model the same column using RadFrac. How do the results
compare?
6.5 Model Example 3 in Perry’s Chemical Engineering Handbook (Perry and Green,
2
2008,pp.13–35,Figures13–37)using(a)DSTWUand(b)RadFrac.
6.6 Results for the gas plant are given in Tables 6.9 and 6.10. Which separations are
1
themostexpensive?Ifyouwerethedesigner,wherewouldyouwanttospendyour
time?
6.7 Carbondioxidefromafermentationprocesscontainsonemolepercentethylalcohol.
1
Thealcoholneedstoberemovedbycontactwithwaterat35◦Cand1atm.Thegas
flowrateis400lbmol/handthewaterstreamis620lbmol/handcontains0.02mol%
alcohol. Determine the compositions out of the absorption column if you model it
with10stagesusingRADFRAC.
6.8 Naturalgascontainsmostlymethanebutalsosmallamountsofotherchemicalsthat
1
are valuable in themselves. In a refrigerated absorption process, the natural gas is
cooled to −40◦F at 865 psia and sent to an absorber, which uses dodecane as the
absorbing media, with a flow rate of 10,000 lb mol/h. Determine the fraction of
each of the chemicals absorbed in a tower with 30 stages with the input shown in
Table6.11.
TABLE6.11 InputforProblem6.8
Component FlowRate(lbmol/h)
Methane 700,000
Ethane 27,000
Propane 11,000
i-Butane 3,200
n-Butane 2,800
i-Pentane 1,200
n-Pentane 770
Hexane 820
6.9 Figure5.15showsanethanolprocess.Thelastunitisadistillationtowertoremove
2
waterfromamixtureofwaterandethanol.Notethatthemixtureformsanazeotrope.
Thefeedstreamis100lbmol/hofa50–50molarmixtureofwaterandethanolat
80◦Fand1atm.
1. Simulateadistillationtowertocreatetheazeotropicmixture(93%ethanol).Use
the WILS-2 option for the thermodynamic model (see Figures 3.5 and 3.6 for
the data). Model the column using the DSTWU short-cut model with recovery
fractionsof0.85and0.15forethanolandwater,respectively.Startwith10stages
andletDSTWUfigureouthowmanystagesareneeded.
```

---

## Стр. 121

```text
P1:OTA/XYZ P2:ABC
JWBS084-c06 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
108 THERMODYNAMICSANDSIMULATIONOFMASSTRANSFEREQUIPMENT
2. UseRadFracwiththenumberofstagesandrefluxratesetbytheoutputfromthe
DSTWUmodel.
6.10 An air stream with flow rate of 14,515 kmol/h and composition of 0.781 nitrogen,
2
0.210oxygen,and0.009argonistobedistilledatlowtemperatureandhighpressure.
Taketheinputtothedistillationcolumnat−138.1◦Cand32bar.
1. Experimentaldata(T–xydiagram)at−150.5◦CcanbeobtainedusingtheNIST
TDE system. Verify that the PENG-ROB equation of state does a good job of
representingthisdata.
2. Using Aspen Plus, simulate a distillation column using the shortcut module,
DSTWU.Forthermodynamics,usethePeng–Robinsonoption,assuggestedby
Aspen.Use35stages,nitrogenasthelightkey,recovery(outtop)of0.85,oxygen
astheheavykey,recovery(outtop)of0.05.Whatistheminimumrefluxratio?
Whatistheactualrefluxratio?Whatistheminimumnumberofstages?Allthese
quantities are useful when using a more complicated distillation model. Since
thisprocessisataverylowtemperature,themostexpensivepartoftheprocess
istherefrigeration,thatis,theheatdutyofthecondenser,sonotethat.
3. Form a group and have each person examine the effect of changing one of the
operationalchoices:numberofstages,refluxratio,fractionoflightkeyandheavy
key,andthermodynamicchoice,suchasNRTL–RK,andreporttheresults.These
guidelinescanthenbeusedwhensimulatingtheentiregasificationplant.
6.11 SolvethesameProblem6.10usingtheRADFRACmoduleinAspenPlus.Use50
2
stages, feed on stage 30, distillate rate of 10,000 kmol/h, and a reflux ratio of 30.
Sometimes it helps to get a solution by starting out with a higher reflux ratio, or
morestages,andthenchangingthemtotheonesyouwant.Howdoestheseparation
compare with the shortcut method in Problem 6.10? Is one column sufficient to
obtainarelativelypureoxygenstream?Whatcouldyoudotoimprovethepurityof
theoxygenstream?Rememberthatthecostofrefrigerationisasignificantcostin
thisprocess,andthatgoesupwithrefluxratio.
```

---

## Стр. 122

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
7
PROCESS SIMULATION
Processsimulationisusedtodeterminethesizeofequipmentinachemicalplant,theamount
ofenergyneeded,theoverallyield,andthemagnitudeofthewastestreams.Becausethe
results of process simulation depend upon thermodynamics and transport processes, the
mathematical models are complicated and would be time-consuming to solve without a
computer. This chapter illustrates the use of a process simulator, Aspen Plus, to model a
planttomakeammonia.
The problems solved in Chapters 5 and 6 are simple problems with many numerical
parametersspecified.Youmayhavewonderedwherethosenumberscamefrom.Inareal
case,ofcourse,youwillhavetomakedesignchoicesanddiscovertheirimpact.Inchemical
engineering,asinreallife,thesechoiceshaveconsequences.Thus,youmustmakemassand
energybalancesthattakeintoaccountthethermodynamicsofchemicalreactionequilibria
and vapor–liquid equilibria as well as heat transfer, mass transfer, and fluid flow. To do
thisproperlyrequireslotsofdata,andtheprocesssimulatorsprovideexcellentdatabases.
Chapters 2–4 discussed some of the ways thermodynamic properties are calculated. This
chapter uses Aspen Plus exclusively. You will have to make choices of thermodynamic
models and operating parameters, but this will help you learn the field of chemical
engineering. When you complete this chapter, you may not be a certified expert in using
AspenPlus,butyouwillbecapableofactuallysimulatingaprocessthatcouldmakemoney.
First, the chapter lists the possible unit operations in the Aspen Plus Model Library,
becausetheprocessisaconnectedsetoftheunits.Thenanexampleprocessisillustrated
that makes ammonia from nitrogen and hydrogen. You will be able to get both the mass
balancesandtheenergybalancesfortheprocess.Withthisinformationyoucanfigurethe
sizeofmostoftheequipmentneeded,andhenceitscost.Youcanalsofiguretheoperating
cost for heating, cooling, compression, and other tasks. The process involves a recycle
stream,too,whichmeansyouwillneedtoiterate.Thechapterendswithadescriptionof
IntroductiontoChemicalEngineeringComputing,SecondEdition.BruceA.Finlayson.
©2012JohnWiley&Sons,Inc.Published2012byJohnWiley&Sons,Inc.
109
```

---

## Стр. 123

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
110 PROCESSSIMULATION
factorsthatmaycontrolwhetheryougetasolutionatall,suchasconvergenceacceleration
techniquesandtearstreams.
InstructionalObjectives: Afterworkingthroughthischapter,youwillhave
1. BecomefamiliarwithmodelsofdifferenttypesofequipmentinAspenPlus.
2. Learnedtodrawaflowsheet,convertingphysicalunitsintooneormoreunitmodules.
3. Learnedwhichparametersmustbespecifiedandwhichonesaresolvedfor.
4. Understood the vagaries of getting the whole simulation to converge, with large
recyclestreamsandmultipleinteractingrecyclestreams.
5. Learnedtotesttheresultstoverifyconvergence.
6. Learned to figure costs and optimize the process and control the process to meet
specifications.
7. Learnedhowtoaddsimpleuser-definedprogramsinFORTRANtounitmodels(in
AppendixC).
MODELLIBRARY
Whenengineersdesignaprocess,theychoosedifferentmodulestorepresentthedifferent
units.YoucanviewthesebyclickingontheiconsatthebottomoftheAspenPlusscreen.
If the icons are not displayed, choose the View/Model Library menu option. When you
clickonaunit,thewordsshownatthebottomofthescreengiveabriefdescriptionofthe
module. Some of the module choices are described in Table 7.1. In Aspen Plus, click on
thedownwardpointingarrowtoseedifferentconfigurationsofeachmodule.
Yourtaskistocombinetheseunitswithconnectingstreamsintoaprocess,whichcan
thenbesimulatedonthecomputer.
EXAMPLE:AMMONIAPROCESS
Consider the ammonia process, as illustrated in Figure 7.1. The feed to the process is
nitrogen, hydrogen, and a small amount of carbon dioxide (left over from the process to
makethehydrogen).Theprocessfeedismixedwitharecyclestream,heatedtothereactor
temperature, and sent to the reactor. The feed to the reactor is roughly a 3:1 mixture of
hydrogen and nitrogen, with some ammonia, too. The reaction is limited by equilibrium
considerations, so the conversion is not known. You must determine it by solving the
equilibrium equation (using RGibbs). In this example, the pressure is high because that
favorsthereaction.Thetemperatureisalsohighinordertogetafastreaction,eventhough
thislimitstheconversioninthereactor.Theoutputfromthereactoriscooledandsenttoa
vapor–liquidseparator(thisexampleusesFlash2),wherethetemperatureislowered.Thus,
mostoftheammoniacondensesandisremovedasaliquid.Thevaporisrecycledandissent
throughacompressortogetthepressurebacktothedesiredpressure.Asmallpartofthe
recyclestreamisbledoffasapurgestreamtopreventthebuildupofimpurities.Tomodelthe
ammoniaprocess,wewill(1)developthemodel(yourengineeringjudgmentisnecessary),
(2)solveit(notatrivialstep),(3)examinetheresults,(4)testthethermodynamicmodel
(whichinsuresyoursolutionisreal),(5)introduceutilitycosts(andrawmaterialcostsif
desired)todeduceoperatingexpenses,and(6)savetheresults.
```

---

## Стр. 124

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
TABLE7.1 SelectedMajorBlocksAvailableinAspenPlus
1. Mixers/splitters
a. Mixer—combineseveralstreamsintoonestream
b. FSplit—splitonestreamintotwoormorestreamsbasedonsplitfraction,flow,flowofa
component,etc.
c. SSplit—dividesastreamintosubstreams
2. Separators
a. Flash2—rigorousvapor–liquidsplitorvapor–liquid–liquidsplit
b. Flash3—rigorousvapor–liquid–liquidsplitwiththreeoutletstreams
c. Decanter—separatetwoliquidphases
d. Sep—usesplitfractionsofeverycomponent
e. Sep2—separationbasedonflowsandpurities
3. Heatexchangers
a. Heater—heaters,coolers,condensers,firedheaters
b. HeatX—co-andcounter-currentheatexchangers
c. MHeatX—multistreamheatexchanger,especiallyusedinLNGorasacoldbox
d. HXFlux—heattransfercalculationmodel,includingfurnace
4. Columns
a. DSTWU—shortcutdistillationusingWinn–Underwood–Gillilandequationsand
correlations
b. Distl—Edmistershortcutdistillation
c. RadFrac—rigoroustwophaseandthreephase,absorber,stripper,distillationcolumnsusing
stages
d. Extract—liquid–liquidextraction
e. MultiFrac,SCFrac,PetroFRAC,BatchSEP—specializedunitsforspecificapplications
5. Reactors
a. RStoic—stoichiometricfractionalconversionorextentofreaction
b. RYield—nonstoichiometric—basedonyielddistribution
c. REquil—rigorousequilibriumusingGibbsfreeenergyanduser-specifiedreactions
d. RGibbs—rigorousequilibriumusingGibbsfreeenergyminimizationwithdeterminationof
allpossiblereactions,includingmultiphaseones
e. RCSTR—continuousstirred-tankreactor,specifyvolume
f. RPlug—plugflowreactor,specifylengthanddiameteroftube
g. RBatch—batchreactor,specifycycletimes
h. TheRCSTR,Rplug,andRBatchreactorsrequirechoosingareactionsetandbuildingupa
reactionrateexpression.
6. PressureChanges
a. Pump
b. Compr—compressor
c. MCompr—multistagecompressor
d. Valve
e. Pipe—withconstantdiameterandrise
f. Pipeline—withmultiplesegmentsofpipe
7. Manipulators—includingDesignSpecBlockandCalculatorBlock
8. Solids,multiplechoices—Crystall,Crusher,Cyclone,Filter,CCD(washer),etc.
9. Usermodels—youprogramtheseinFORTRANtotakeinputtemperature,pressure,andflow
rateofeachcomponentandcalculateconditionsofoutletstreams
10. Conceptualdesign—interfacetoAspenDistillationSynthesis
```

---

## Стр. 125

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
112 PROCESSSIMULATION
8
PURGESPL
COMP
PURGE
7
9
REACT
MCOMP MIXR 4 HXER2 FLASH
HEATER 5
1 8 6
2 HEATER
NH3
FIGURE 7.1 Ammoniaprocess.
DevelopmentoftheModel
Inthisexample,youwilltakeaninputstreamtotheprocess(at80◦Fand300psia)of
Nitrogen 100lbmol/h
Hydrogen 300lbmol/h
Ammonia 0
Carbondioxide 1lbmol/h
The inlet stream is compressed to 4000 psi with a multistage isentropic compressor. The
streamismixedwiththerecyclestreamandheatedto900◦F,thereactortemperature.Inthe
reactor, there is a pressure drop of 30 psi,and the temperature and component flow rates
aresetbyminimizingtheGibbsfreeenergyunderconditionsofnoheatduty.Theoutletis
cooledto80◦Fandtheliquid–vaporphasesareseparated.Thevaporphasegoestorecycle,
and0.01%ofitisusedaspurge.Arecyclecompressorthencompressestherestfrom3970
to4000psia.Inarealprocess,theheattransfertopreheatthefeedtothereactorusesthe
effluentfromthereactor,usuallyinsidethesamevessel.Inprocesssimulators,though,itis
usefultobeginasshowninFigure7.1tohelpconvergence.Nonrandomtwoliquid(NRTL)
thermodynamicswaschosenandisjustifiedaposteriori.
TheidentificationofcomponentsisshowninFigure7.2.
FIGURE 7.2 Componentsforammoniaprocess.
```

---

## Стр. 126

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:AMMONIAPROCESS 113
FIGURE 7.3 Partialflowsheetsummary.
ItisusefultochecktheconnectionsbetweentheunitsbyusingtheFlowsheetoptionSec-
tion/GLOBAL,asshowninFigure7.3.Anystreamsthatwereinadvertentlynotconnected
toaunitwillshowupherebecausetheSectionboxwillbered.
The operating parameters for the MCOMP compressor is shown in Figure 7.4. Both
compressorshaveadischargepressureof4000psia,andtherecyclecompressoronlyhas
one stage. The operating parameters for the fired heater are 900◦F and 4000 psia (see
Blocks/HEATER/Input).Thedatafortheheatexchangerissimilar,withpressureof3370
psia.YoucanseethereactorspecificationsinFigure7.5.
The specifications for the vapor–liquid separator and simple splitter are shown in
Figure7.6.InAspenPlus,youcanspecifydifferenttemperatureandpressureintheoutlet
than in the inlet. This may be useful in a first simulation when you are not as interested
intheactualheatingandcoolingrequired,butthisexamplekeepstheunitconditionsthe
sameasthestreamenteringtheunitsonoheattransferorcompression/expansionoccurs.
TheoutletconditionsfortheMIXRblockare900◦Fand4000psia.
FIGURE 7.4 SpecificationsforcompressorunitMCOMP.
```

---

## Стр. 127

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
(a)
(b)
FIGURE 7.5 Specifications for the reactor, unit REACT: (a) operating conditions of reactor;
(b)productsofthereaction.
(a)
(b)
FIGURE 7.6 Specificationsfortheseparatorandsimplesplitter,unitsFLASH,andPURGESPL:
(a)FLASHspecifications;(b)PURGESPLspecifications.
```

---

## Стр. 128

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:AMMONIAPROCESS 115
SolutionoftheModel
Nowthattheprocessisfullyspecified,youcansolveit.Becausethereisarecyclestream,
begin the calculations with the first unit, the compressor. The output from that unit is
combined with the recycle stream, which initially is zero. Follow the stream through the
restoftheprocessuntilitcomputestherecyclestream.Thisrecyclestreamisnowdifferent
from its previous value. Thus, the program does another iteration, and it continues until
thereisnofurtherchange.Figure7.7showssomeoftheinformationAspenPlusprovides
abouttheconvergence.
Figure 7.7a indicates that the sequential module is used for iteration. Unit MCOMP
is calculated only once, since the exact input to that unit is known. Then units HEATER
through MIXR are calculated in turn. Thus, convergence is achieved when the input to
the MIXR unit agrees with the output from it. If they are the same, convergence has
been achieved. If not, more iterations are necessary. This simulation used the Wegstein
methodofacceleratingconvergence.Figure7.7aindicatesthattheiterationshavenotfully
converged after 30 iterations, and the mass balance error is in Block MIXR. It gives the
totaldiscrepancyas1.3029invs.1.3033out,forarelativedifferenceof0.03percent.This
difference is so small that you could accept the results. After the 30 Wegstein iterations
the flow rates for N , H , NH , and CO coming into (out of) the MIXR were 269.499
2 2 3 2
(269.599), 838.580 (838.514), 56.562 (56.582), and 3.122 (3.123) lb mol/h, respectively.
If you change to the Direct method (Convergence/Conv Options), it converges about the
same. After the Wegstein method, if you change to the Newton method there is a very
slightimprovement(0.023%),after147passes.SeethesebylookingattheMIXRBlock
andStreams(Figure7.7b).
Thefinalmassandenergybalanceareshowninthestreamtable,Table7.2.Bychecking
themassbalancesaroundeachunit,youcanseethattheybalance.Theoverallconversion
(100 moles of nitrogen to 197.8 moles of ammonia) is reasonable. The rest of the raw
materialsarelost.Mostofthecarbondioxidegoesoutintheammoniasoperhapsthepurge
streamwasnotnecessary.
ExaminationofResults
You can learn several things by looking at “Results” under each “Block.” First, look
at Figure 7.8, which is for the MCOMP unit. Two stages were specified in MCOMP
becausethecompressionratiowasbig:4000/300=13.3.Foridealconditions,youcanuse
thermodynamicstoshowthattheoptimalconfigurationhasequalcompressionratioswith
interstagecoolingbacktotheinlettemperature,becausethisresultsinlesstotalhorsepower.
Thesquarerootof13.3is3.65,whichisthecompressionratioused.Thetemperatureout
of the first stage was set at 300◦F since the stream eventually needs to be heated before
goingintothereactor,andthepressureafteronestageis1095psia.
In the Results menu of the fired heater and heat exchanger, the heat duties of each
exchangeraregiven,whichpermitsestimationofthecapitalcost.Theheatdutiescanbe
combined with the enthalpies of the process streams to verify an energy balance. Notice
alsothattheratioofhydrogentonitrogenintherecyclestreamisnot3:1.Thisisbecause
thermodynamics dictates that the solubility of hydrogen and nitrogen in the ammonia is
different,andhydrogenbuildsup.Inthereactor,nitrogenisthelimitingreagent,and73%of
thenitrogenfedtothereactorreacts.Thus,theconversionperpassis73%,basedonnitro-
gen.Ifyoulookattheproduct,though,197.8lbmolofammoniaaremadefrom100lbmol
```

---

## Стр. 129

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
116 PROCESSSIMULATION
(a)
(b)
FIGURE 7.7 Convergenceofthemassbalanceafter30iterationswithWegsteinmethodandthen
the Newton method: (a) information about iterations; (b) flow rates at beginning of one iteration
(stream3)andattheendofthatiteration(streams2and9).
```

---

## Стр. 130

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
ssecorPainommArofecnalaBygrenEdnassaM
2.7ELBAT
egruP
HN
9
8
7
6
5
4
3
2
1
3
08
08
2.18
08
08
08
009
009
9.603
6.967
08
)F◦(erutarepmeT
0793
0793
0004
0793
0793
0793
0793
0004
0004
0004
003
)aisp(erusserP
1
0
1
1
1
197.0
1
1
1
1
1
noitcarfropaV
770.0
101.302
916.667
916.667
696.667
797.969
797.969
536.7611
536.7611
104
104
)h/lombl(wofleloM
786.0
608.1543
457.6686
457.6686
144.7686
52.91301
52.91301
52.91301
62.91301
221.0543
221.0543
)h/bl(woflssaM
521.0
871.59
5.4421
359.9421
870.0521
652.5431
628.2183
212.8654
344.1762
219.6241
709.9087
)h/tfuc(woflemuloV
0
328.5−
225.1−
925.1−
925.1−
153.7−
318.0
474.5
923.0
158.1
261.0−
)h/utBMM(yplahtnE )h/lombl(wofleloM
710.0
451.1
526.861
526.861
246.861
697.961
697.961
517.862
617.862
001
001
N 2
450.0
511.3
563.935
563.935
914.935
435.245
435.245
192.938
92.938
003
003
H 2
600.0
238.791
805.65
805.65
415.65
643.452
643.452
905.65
905.65
0
0
HN 3
0
1
21.2
21.2
21.2
21.3
21.3
21.3
21.3
1
1
OC 2
noitcarfeloM
22.0
600.0
22.0
22.0
22.0
571.0
571.0
32.0
32.0
942.0
942.0
N 2
407.0
510.0
407.0
407.0
407.0
955.0
955.0
917.0
917.0
847.0
847.0
H 2
470.0
479.0
470.0
470.0
470.0
262.0
262.0
840.0
840.0
0
0
HN 3
300.0
500.0
300.0
300.0
300.0
300.0
300.0
300.0
300.0
200.0
200.0
OC 2
117
```

---

## Стр. 131

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
118 PROCESSSIMULATION
FIGURE 7.8 Compressorspecifications,unitMCOMP.
ofnitrogenand300lbmolofhydrogen.Becausetherawmaterialscanbeconvertedintoa
maximumof200lbmol,theoverallyieldoftheprocessis197.8/200or98.9%.
EvenmoreinformationcanbeobtainedusingtheView/Reportmenu.Thisgivesdetails
aboutindividualblocks.TheView/Historymenugivesinformationabouttheconvergence
andwhatcalculationshavebeendone.TheView/InputSummaryliststheparametersyou
haveset.
TestingtheThermodynamicModel
ThethermodynamicscanbetestedusingtheresultsfromTable7.2.Thereactoreffluentis
inequilibrium.Takethemolefractionsofstream5andcomputetheK-value:
y 1
K = NH3 (7.1)
p (y y3 )1/2 p
N2 H2
Withvaluesofy =0.175,y =0.559,y =0.262,p=270atm,theK-valueis0.0056.
N2 H2 NH3
Stephenson(1966)givesameasuredvalueof0.006attheseconditions.Thus,thechemical
reactionequilibriumissatisfactorywhenusingthePENG-ROBthermodynamicmodel.
Anothertestofthethermodynamicsiswhetherthesolubilityofhydrogenandnitrogenin
theliquidammoniaiscorrect.Lookingattheexittotheflashunit,theamountofhydrogen
is 3.115 lb mol for 197.8 lb mol ammonia. Solubilities are usually expressed in cc (at
STP) per gram of liquid. In this case, those numbers are 20.7 and 7.7 for hydrogen and
nitrogen,respectively.DatabyWiebeandTremeame(1933,1934)givevaluesat270atm
(interpolatedbetween200and400atm)of26.4and27.6.Thus,thehydrogenisclose,but
thenitrogenisoff.Thisisaverydifficultsystemtosimulate;manyotherequationsofstate
didnotleadtoaconvergentresult.Vapor–liquidequilibriaislessusefulinthiscasesince
theamountofhydrogenandnitrogenintheammoniaissosmall.
UtilityCosts
Thecostofrawmaterialsisusuallythemajoroperatingcost,butfollowingthatinimpor-
tance is the cost of utilities. Aspen Plus provides a convenient way to obtain the cost of
utilitiesintheentireprocess.YoubeginbyopeningtheUtilitiesfolderintheDataBrowser
(orusetheData/Utilitiesmenu).Thereareseveralpossibleformsofutilities;chooseNew,
selectwaterandfillouttheform:energypriceof$0.6/MMBtu,Heating/CoolingValueof
45 Btu/lb, Inlet and Outlet Temperatures of 75 and 120◦F. Since water is being used as
```

---

## Стр. 132

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:AMMONIAPROCESS 119
a coolant, it is also necessary to select the Consistency Check/Ignore. (Otherwise errors
willbeindicated,althoughtherearenotanyerrors.)Thenchoosegasandfillouttheform:
$4/MMBtu.Chooseelectricityandassignapriceof5cents/kwh.
The next step is to tell the computer which blocks are going to use utilities. Select
BlockHXER(thecoolerafterthereactor),andselectWATER.FortheBlockCOMPselect
ELECTRICITY.FortheBlockMCOMP,selectSetupandthentheSpecsTab.Atthebottom
youcanspecifytheutilitiesasELECTRICITY.Sinceacountercurrentheatexchangeris
used,nogasisusedtoheatthefeedtothereactor.Nowtheutilitieshavebeenspecifiedto
AspenPlus.
After the mass and energy balances are computed, the program calculates how much
cooling water and natural gas is needed, and its cost. That information can be accessed
fromtheDataBrowser/Results/OperatingCostSummary/withtheUtilityCostSummary
Tab,asshowninFigure7.9.Thecostofthenaturalgasisalmostone-halfmilliondollars
peryear.Bycombiningtheheaterandcoolerbeforeandafterthereactor,thiscostcanbe
reduced.Thecostofelectricityforthecompressorsis$300,000peryear.
Thiscompletestheexample.Thestepsareasfollows:
Step1 Developmentofthemodel,includingaprovisionalchoiceofthermodynamicmodel
andequipmentspecifications.
Step2 Solutionofthemodelbydoingthecalculationsiteratively.Convergenceacceleration
techniquesaresometimesnecessary.
Step3 Examinationofresults.
Step4 Testingthethermodynamicmodel(maybedoneasstep2).
Step5 Obtaintheutilitycosts.
Step 6 Summarizing the results using View/Report, View/History, and View/Input Sum-
mary,savethestreaminformationtoExcelandtheflowdiagramasafigure.
FIGURE 7.9 Summaryofutilitycost.
```

---

## Стр. 133

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
120 PROCESSSIMULATION
GreenhouseGasEmissions
AspenPluswillalsocalculatethegreenhousegasemissionsforaprocessandthecostof
thecarbontax.InSetup/SimulationOptions/Calculations,choosethestandardyouwishto
use;hereweusewhatAspencallsUSEPA(2009).Alsosetthecarbontax;for$50perton,
put in 2.5 cents/lb. Then when the simulation is finished, choose Results/CO Emission/
2
and you get the summary. For the ammonia process treated here there is carbon dioxide
going inandout,whichbalance, andthecarbon taxisextremely smalland duetoround
offerrorintheiterations.Forotherprocesses,thecarbontaxwillbemoreimportant.
CONVERGENCEHINTS
To understand the convergence process used in most simulators, consider the process
showninFigure7.10.Chapter5discussesthesequentialandsimultaneousmethods.The
sequential method is simple, but it might not converge. Thus, convergence acceleration
techniques are used to improve the chances of convergence; two of those are described
here [Wegstein (1958) and Broyden (1965, 1970) methods (Perry and Green (2008)].
Simultaneous methods are called equation oriented (EO) methods in Aspen Plus. Take a
singlecomponentforillustration;inFigure7.10,youwouldknowtheflowrateinthefeed
stream. The mass balance on the mixer takes the flow rate of streams 1 and 6 and adds
themtobecomestream2.Thereactorchangestheamount,andthentheseparatorseparates
thestreamintotwostreams.Oneofthoseistherecyclestream.Usually,youdonotknow
stream 6 when you start the calculation; in the first iteration you often take it as zero, or
someotherassumedvalue.Afterreachingtheseparator,youhaveanewpossiblevaluefor
stream6.Writethisprocessasanequation:
x = f(x) (7.2)
Inthisform,xistheflowrateofthechemicalintherecyclestream,andf(x)isthevalue
of the flow rate of the chemical in the output of the separator, obtained after doing the
calculation once around the loop. You have solved the problem when these two values
agree.Tomakethisaniterativeprocess,callxnthevalueofxafterniterations.
xn+1 = f(xn) (7.3)
This iterative process is simple to apply, since the function f(x) is really a series of
functionsevaluatedoneaftertheother,andeachstepisamassbalanceononesimpleunit.
6
6
1 Mixer 2 Reactor 4 Separator 5
3
FIGURE 7.10 Processwithrecyclestream.
```

---

## Стр. 134

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
CONVERGENCEHINTS 121
Itmaynotconverge,however.Inordertospeeduptheconvergence,theWegsteinmethod
isveryeffective.Themethodcalculatesaprovisionvalueofxˆn+1andthenusesthelasttwo
iteratestocalculatea“modified”value,whichisthenusedasthenewvalueinplaceofxˆn+1:
xˆn+1 = f(xn), xn+1 =qxn +(1−q)xˆn+1, where
b xn −xˆn+1 (7.4)
q =− , b=
1−b xn−1−xn
Wegstein(1958)foundthattheiterationsconvergeddifferentlydependingonthevalueofq.
q<0 Convergenceismonotone
0<q<0.5 Convergenceisoscillatory
0.5<q<1 Directmethoddivergesinoscillatorymanner,
Wegsteinmethodconverges
1<q Divergesmonotonically
The derivation of the Wegstein method begins with Eq. (7.2), written as a new function
F(x)asshowninEq.(7.5).
F(x)= x − f(x) (7.5)
Applythesecantmethodtothisfunction.ThesecantmethodistheNewtonmethodwitha
numericalversionofthederivativebasedonthelasttwoiterations(seeAppendixE):
F(xn−1)−F(xn) (cid:2) (cid:3)
0= F(xn)+ (x ∗ )n+1−xn (7.6)
xn−1−xn
Butyoualsoknowthat
F(xn)= xn − f(xn)= xn −xn+1
(7.7)
F(xn−1)= xn−1− f(xn−1)= xn−1−xn
Combiningtheseequationsgives
xn−1xn+1−(xn)2
(x ∗ )n+1 = (7.8)
xn−1−2xn +xn+1
whichisthesameastheWegsteinmethod,Eq.(7.4).Sometimesconvergenceisenhancedby
applyingWegsteinonlyeverysomanyiterationsratherthaneachiteration.TheWegstein
iteration method is the default method in Aspen Plus, but there are others, including
the direct method (Eq. 7.3), Broyden’s method, and Newton’s method. While Wegstein’s
method works on one variable at a time, Broyden’s method works on all the variables at
once using a matrix that is adjusted iteration by iteration. In the direct method, Eq. (7.3)
isusedasitstands.Intheammoniaprocess,whenusingtheWegsteinmethod,thelackof
convergence was apparent in the MIXR unit, even though this is the last unit calculated.
Thisisbecauseafterthecalculationxn+1isreplacedby(x∗)n+1usingEq.(7.8).Thus,itis
importanttonotetheorderofcalculationintheiterations.
```

---

## Стр. 135

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
122 PROCESSSIMULATION
TABLE7.3 OverallIterationErrorsforAmmonia
ProcessUsingWegsteinandDirectMethods
IterationNumber Error-Wegstein Error-Direct
1 1.00E4 1.00E4
2 1.00E4 1.00E4
3 1.47E4 6.72E3
4 −2.50E3 −3.22E3
5 −8.79E2 −2.58E3
10 5.58E2 −6.48E2
15 −5.62E0 −9.40E1
20 3.31E1 3.06
25 2.60E1 9.70
30 1.64E1 11.1
Another term used when discussing iteration methods is the tear stream. This is the
streamthatisguessed(orsettozero)whensteppingthroughtheprocessthefirsttime.In
Figure7.10,ifyoucomputeinthefollowingorder:mixer,reactor,separator,thenstream6
isthestreamyoumustassumeandcheck—itisthetearstream.Ifyoucomputeintheorder:
reactor,separator,mixer,thenstream2isthetearstream.YouapplytheWegsteiniteration
methodtothetearstream.Ofcourse,ifthecalculationsaresimple,aswouldbethecase
ifallphysicalpropertiesarespecifiedandtherearenoenergybalances,thenyoucanuse
a spreadsheet. It may be so fast that you do not care whether 10, 100, or 1000 iterations
areneeded.
Sometimes it is convenient to have the calculations made one unit at a time. This can
be done using the Run/Step menu or CTRL-F5 or by clicking on the open triangle (see
FigureC.5inAppendixC).Itmayalsobenecessarytoreinitialize,thatis,setthevariables
totheirvaluesatthestartofthesimulation.Thisisusefuliftheiterationsdonotconvergeand
theanswerisnotreasonable.Justrerunningtheproblemwillstartfromtheunreasonable
answer. To put the variables back to their beginning value, use Run/Reinitialize or the
reinitializebutton(seeFigureC.5inAppendixC).Theprogressofiterationscanbeseen
clearlyifyouexpandtheResults/StreamstoincludeallthestreamsandthenclicktheStep
buttonoverandover.
For the ammonia process, the errors at each iteration (when starting from zero) are
showninTable7.3.Theerrorsdecreaserelativelyrapidlybutthendecreasemoreslowly.
UsingtheNewtonmethodafterWegsteinprovidedaconvergedsolution.
OPTIMIZATION
AspenPlushasthecapabilityofoptimizingafunctionthatyoudefine.Anexampleisgiven
herethatisverysimple,butitillustratestheprocess.Takeasingleunit,thereactorinthe
ammoniaprocess.ThereactorRGibbsisusedandtheproductionofammoniaismaximized
withrespecttothereactorpressure.Inthisexample,thereactorisunitREAC,withinput
stream1andoutputstream2.Theinputis100lbmol/hnitrogenand300lbmol/hhydrogen
at900◦Fand270atm.
```

---

## Стр. 136

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
OPTIMIZATION 123
FIGURE 7.11 Definitionofthevariable.
Step 1 In the Data Browser, open Model Analysis Tools and the Optimization folder.
Select New in the Object manager; change the name, if desired, and click OK. Here, it
isCONV.
Step2 OpentheOptimizationCONV.Initiallythiswindowhasnoentries;selectNewand
defineavariablenamethatwillbeinvolvedintheoptimization(anynameisacceptable).
Here,itisCONV.
Step 3 A window appears to define CONV. Complete it as shown in Figure 7.11. Se-
lect in turn the type, Mole-Flow; Stream: 2 (the output stream of this simple example);
Component:Ammonia.
Step4 ClickontheObjectivesandConstraintsTab;youwishtomaximizeCONV.
Step5 NextclickontheVarytabinordertodefinewhichvariabletochange.Figure7.12
shows the choice of Block-Var for Block B1 (the reactor in this simple example), and
indicatesthatthepressureistobevaried,betweenthelimitsof2000and6000psia.
Step6 Solvetheproblembyrunningtheprogram.ThefinalresultsareshowninFigure7.13;
selectResultsSummary/Streamstoseethis.
Note that you only get the final results, but do not know how sensitive the result is
to the reactor pressure. In this case, though, the pressure is at the maximum allowed in
```

---

## Стр. 137

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
124 PROCESSSIMULATION
FIGURE 7.12 Parameterstovary.
Figure7.12,asexpected.YoucanusetheSensitivityoptionintheModelAnalysisTools
tofindtheconversionasafunctionofpressure.Itoperatesinasimilarway,butprovides
more information. To see this, take out the optimization option in the previous example
andreplaceitwiththeSensitivityoption.ThescreensaresimilartoFigures7.11through
7.12.InSensitivity/CONV/Input,choosetheTabulateTab.AddNew,CONVasthesecond
column.Afterrunningthemodel,selectModalAnalysisTools/Sensitivity/CONV/Results.
ThenonegetstheammoniaoutputforavarietyofpressuresasshowninFigure7.14.
FIGURE 7.13 Optimizationresults.
```

---

## Стр. 138

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
INTEGRATEDGASIFICATIONCOMBINEDCYCLE 125
FIGURE 7.14 Sensitivityresults.
INTEGRATEDGASIFICATIONCOMBINEDCYCLE
Prosperity frequently depends on the availability of cheap energy. Two countries, United
States and China, have significant deposits of coal within their respective borders (Chu,
2009).One-halftheelectricityintheUnitedStatesisgeneratedbyburningcoal(National
AcademyofEngineering,2008).Yetburningcoalcauseslargeemissionsofcarbondioxide,
a greenhouse gas. Thus, both countries are the largest emitters of carbon dioxide in the
world. There are ways to change that, and one of them is to use integrated gasification
combined cycle (IGCC). The technology is not new—Eastman Chemical has designed,
built and operated IGCC processes for many years (since 1983) (Hess, 2006). But new
advances in part of the process make them cheaper, and if there is a penalty for emitting
carbon to the atmosphere, they become especially attractive compared with just burning
thecoal.
Thestepsintheprocessaresimple:burnthecoalwithlimitedoxygensothatyoumake
syngas,withlotsofhydrogenandcarbonmonoxide.Infact,itisbettertoseparatetheair
streambeforehandintoanoxygenstreamandnitrogenstream,sincethatreducescostslater
for the emission control—the amount of nitrogen is huge so if it is not there the process
issmaller.TheairisseparatedinanAirSeparationUnit(ASU).Thecoalandoxygenare
combinedinagasifiertomakethesyngasstream.Thisstreamcontainssomesolidmaterial
(particulates),includingflyash,whichmustberemoved.Next,thewatergasshiftreactor
```

---

## Стр. 139

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
126 PROCESSSIMULATION
makesmorehydrogen;intheprocessthesulfurisconvertedtohydrogensulfide,whichis
thenremoved.Thecarbondioxideisremovedinanacidgasremovalprocess(thishappens
everydayinarefinery,soitisnotnew).ItcanbestoredundergroundinaCarbonCapture
and Sequestration step. What is left is a hydrogen-rich fuel that is sent to a gas turbine
whereitburns.Aftercombustion,thehydrogenisintheformofwater.Duringthiswhole
process,someunitsareveryhotandneedtobecooled.Thecoolingfluid(startingoutas
water,turningintosteam)usedtodothatissenttoasteamturbinewhereadditionalenergy
isextracted.Thisstepaddsabout7–10percentagepointstotheefficiency.
Inadditiontotheflyashandsulfurcompounds,thereareemissionsofNO ,particulate
x
matterandmercurytobeconsidered.Coalscomeindifferentvarieties,sothattheprocess
willbetunedsomewhattomeettherequirementsofaspecifictypeofcoal.Forexample,
thecoalinIndiaoftenhasahighashcontent(PrasadandGautam,2004),andthisaffects
the temperature in the gasifier and the flyash removal step. The sulfur content may very
from0.5to7wt.%;ashcontentmayvaryfrom1to40wt.%;chlorinecontentmayvaryby
afactorof20(Cooper,2010).Furthermore,asimilarprocesscanbeusedwithbiofuelsas
theinputinsteadofcoal.Thus,itisworthwhiletolearntodesignanIGCCprocess.
The material fed to the process—air and coal—basically goes straight through the
process with no recycle. Thus, many of the single units can be examined individually
without reference to other parts of the process, and that is done in Chapters 2–6. It is
importanttomodelthethermodynamicscorrectly,andthisaspectisconsideredinChapters
2–6,also.Whiletherawmaterialsandresultingproductsdonotinvolverecyclestreams,the
processistiedtogetherwithheatexchangers,sincethewater/steamisrecycled.Adetailed
report of this process and others is available (National Energy Technology Laboratory,
2007).Here,weutilizetheprocessinAspenforProblems7.9–7.10.
CELLULOSETOETHANOL
Ethanol has been made from biomass since the time of the pharaohs in Egypt. Early in
the twenty-first century there was a push to develop an industry doing this in the United
States.Partofthepushwasforenergyindependence—tohaveafuelthatdidnothavetobe
imported.Farmersgroupswereallformakingethanolfromcorn,thegovernmentsubsidized
itandestablishedfuelstandardsthatrequiredsomeethanol,butchemicalengineerswere
wary.Theyknewsomeoftheproblems:unlessdonecarefully,theprocessusedmoreenergy
thanwasinthefinalproduct.Still,therewaslesscarbondioxideemittedtotheatmosphere
in a complete life cycle since the growing of the biomass used carbon dioxide to offset
the carbon dioxide formed during combustion of ethanol. It was also found that growing
cornrequiredagreatdealofwater,2.3–8.7millionliterspermegawatthour,versus90–190
liters per megawatt hour for petroleum extraction and oil refining (Service, 2009). Later,
theuseofcornforethanolcausedfoodpricestoincrease.
Another option was being looked at too: making ethanol from cellulosic feedstocks,
thestalks,leaves,andwoodofplants.Anothertwistwastomake“drop-in”fuelsinstead
of ethanol. The idea was to develop chemical processes that made hydrocarbons that are
similartothosealreadyusedinpowerplants,trains,andautomobiles(Anonymous,2010;
Weekman,2010).Thisavoidstheproblemofhavingtoreplacetheentiregasolinepipeline
system in the United States, since ethanol corrodes the current pipelines. It also allows
fuelsforaviationanddiesel,whereethanolcannotbeused.Enzymescanbedevelopedto
tweakthereactionstomakethemostdesirablehydrocarbonsandtomakemoreofthem,
thusincreasingtheoverallefficiency.
```

---

## Стр. 140

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
CELLULOSETOETHANOL 127
Theproductionofdrop-infuels(Anonymous,2010)usesenzymesandbacteriatoturn
sugarintostraight-chainalcohols,C12–C16,whicharethemaincomponentofdieselfuel.
Furthermore, if butanol is made rather than ethanol, the corrosion problems are reduced
sincebutanoldoesnotabsorbwaterasreadilyasethanolandithasfourcarbonatomsfor
each oxygen atom, rather than the two in ethanol. This is where the energy comes from.
Whilethisisalsoasmallmarket,theUSNavyprojectsthatby2020halfoftheirfuelwill
befromrenewablesources(Anonymous,2010).
There are a variety of processes that can use biomass: gasification, pyrolysis, and
fermentation. Grains and cellulosic material is usually processed using hydrolysis and
fermentation.Vegetableoilsandalgaeuseaprocessofesterificationandpyrolysis,whereas
wood and stalks can be gasified (Regalbuto, 2009; Weekman, 2010). We focus here on
fermentation,primarilyofcellulosicmaterials.
Therawmaterialforcellulosicfeedstocksisquitevaried:trees,cornstover,andswitch-
grass,amongothers.Theeconomicsofmovingthatmaterialdictatethataplantcaneco-
nomicallycollectmaterialfromaradiusofabout50miles(Ladischetal.,2010).Thus,we
immediately lose one of the hallmarks of chemical engineering processes—the economy
ofscale.Thenextproblemisthatdifferentsourcesoffeedstockshavedifferentchemical
composition,sothateachprocessmustbetunedforthefeedstockbeingused.Sometimes
enzymesareengineeredtohandleaspecificfeedstock,too.Thefeedstockcontainsvariable
amountsofcellulose(33–44%),xylan(15–21%),arabinan,mannan,andgalactan(collec-
tively0–5%),acetyl(2–5%),lignin(18–29%),ash(1–10%),andothermaterial.Xylanisa
complexpolysaccharidefoundinplantcellwalls.Arabinanisamonosaccharide,mannan
isaplantpolysaccharide,andgalactanisapolymerofgalactosefoundinhemicellulose.
Theprocessinvolvesanumberofstepsinseries:
1. Feedstockpreparation:First,thefeedstockispreparedtoeliminatedirtandmetals.
2. Pretreament: Then it goes to a pretreatment process that cooks the material in hot
waterorsteam,acidorbase,inordertoopentheplantcellwalltoexposethecellulose
toenzymesthathydrolyzethesemacromolecules.
3. Hydrolysisproducesbothfive-carbonandsix-carbonsugars.
4. Fermentation:Thenthestreamgoestofermentationunitswherethesugarsaremade
intoethanol.
5. Distillationanddryingprocessesprovidedryethanol.
Whiletheprocessismostlystraightthrough,thereisasignificantenergyload,andthis
isreducedviamanyrecyclestreamsinvolvingwaterandsteamandsolidsforcombustion.
Infact,thereisagreatdealofwatercirculatingthroughouttheprocess,whichaddstothe
expense.Thelignincanbeusedasaboilerfuel,forexample.Ladischetal.(2010)estimate
thatthemaximumyieldofethanolfromcornstoveris95gal/drytonbiomass.Usingthe
densityofethanol(6.58lb/gal),thisgivesanethanolproductofonly625lb/dryton,oronly
31%.Since40%ofthefeedstockiswater,thatmeansthatoftheweightofwetfeedstock,
only about 18% by weight leaves as product. This limitation makes the development of
enzymesparticularlyimportantsothattheprocesscanbeasefficientaspossible.
Here,aprocessdevelopedbytheNationalRenewableEnergyLaboratoryandtheHarris
Groupwillbeusedtoillustratemanyfeatures(Adenetal.,2002;Aspen,2011).Themass
balances can easily be made using Excel, and they can be done in Aspen, too, using the
mass-balance-onlyoption.TodotheenergybalancesinExcelwouldbetootedious,since
therearesomanycomponents.TodoenergybalancesinAspenrequiresthatonedevelop
```

---

## Стр. 141

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
128 PROCESSSIMULATION
the appropriate thermodynamics for each chemical, including the solids. Frequently, this
is done using user-generated information, which must then be inserted into the Aspen
simulation.Forthisreason,hereweonlyconsiderthemassbalances.
The report is Aden et al. (2002). The Aspen Model is at http://devafdc.nrel.gov/
biogeneral/Aspen_Models/. Download the BKP file (the Aspen backup file), the input
file,andthespreadsheet.
CHAPTERSUMMARY
This chapter listed many of the possible units in the Model Library of Aspen Plus. The
ammonia process illustrated the procedures (and computer windows) you used to set the
process conditions and examine the results. The thermodynamics choices can be verified
by comparison with data reported in the literature. Sometimes the calculations do not
converge,andthenusemethodsforacceleratingconvergence:Wegstein,direct,Broyden,
Newton. Some experimentation may be necessary and your choices should be guided by
an understanding of how the iterations proceed through the process and from iteration
steptostep.Twoprocesseswereintroduced:IGCCandethanolfromcellulose.Whilethe
problemsforthoseprocessesaresimplified,theyareprocessescurrentlybeingworkedon
bychemicalengineers.
CLASSEXERCISE
Divide into teams of two to four students. Work through a spreadsheet (Table 7.2), with
each person of a team taking a unit, showing where the parameters are for that unit and
checkingtheresults.Aretheycorrect?Doesthemassbalance?Doestheenergybalance?
Workthroughthewholeprocess.Alternatively,yourinstructorcanprepareaflowsheetand
datasetshowingtheresults,butwithsomeerrorsforyourteamtofind.
PROBLEMS
InProblems7.2–7.8reporttheGreenhouseGasEmissions,too.
7.1 DeriveEq.(7.8)fromEqs.(7.6)and(7.7).ShowthatEq.(7.8)isthesameasEq.(7.4).
1
7.2 Simulatethebenzeneprocess(Problem5.1)usingAspenPlus.Takethefeedatroom
1
temperature and 1 atm. Compress it to 35 atm. Preheat the feed to the reactor to
550◦C and cool the effluent. Model the reactors as RStoic reactors, and model the
separationsusingdistillationtowers.Youwillhavetodecideonthenumberofstages
andrefluxratio,andusingDSTWUfirstmightbeuseful.
7.3 Project.Simulatethebenzeneprocess(Problem5.2)usingAspenPlus.Takethefeed
atroomtemperatureand1atm.Compressitto35atm.Preheatthefeedtothereactor
to550◦Candcooltheeffluent.ModelthereactorsasRStoicreactors,andkeepthe
hydrogen/methaneseparationsassimplesplitters;modeltheotherseparationsusing
distillationtowers.Youwillhavetodecideonthenumberofstagesandrefluxratio,
andusingDSTWUfirstmightbeuseful.
```

---

## Стр. 142

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 129
7.4 Project. Simulate the ethyl chloride process (Problem 5.4) using Aspen Plus. The
feedstreamsareatroomtemperatureand20psiaandtheyarecompressedto95psia.
Preheatthefeedtothereactorto800◦Fandcooltheeffluent.Modelthereactorsas
RStoicreactors.Taketheeffluentfromthefirstreactor,coolit,andsendtheliquid
to the product stream. Compress the gases to 265 psia, and heat them to 350◦F
(if needed). Lower the pressure and cool the effluent from the second reactor and
separatetheliquidandvapor.Recyclethevaporandsendtheliquidtotheproduct
stream.Youwillhavetodecideonthecoolingtemperaturetouseinthevapor–liquid
separators.
7.5 Project.Simulatethevinylchlorideprocess(Problem5.5)usingAspenPlus.Take
the feed at room temperature and 20 psia. Operate the direct chlorination reactor
at 65◦C and 560 kPa. A distillation column removes the trichloroethane and the
rest of the stream is sent to the furnace. Heat the stream to 1500◦F, so pyrolysis
takesplace.Cooltheeffluentfromthefurnace,andrecyclethevapor(mostlyHCl).
Sendtheliquid(vinylchlorideandethylenedichloride) toadistillationcolumnfor
separation.Youwillhavetodecideonthenumberofstagesandrefluxratio,andusing
DSTWU first might be useful. The oxychlorination reactor operates at 200◦C and
1400kPa.Washtheeffluentfromtheoxychlorinationreactorwithwatertoremove
contaminantsandthenremovethewaterandlightgasesinadistillationcolumn.The
ethylenedichloridemustbedry(<10ppm)beforegoingtothefurnace.Thestream
thengoestoadistillationcolumnwheretheethylenedichlorideispurified(>99.5%)
beforeitissenttothefurnace.Sincethefurnaceoperatesat560kPa,thepressureis
reducedbeforereachingthefurnace.
7.6 HowdoestheprocessinProblem7.5changeifthefurnaceisrunatthehighpressure
1
(1400kPa)?
7.7 Project. Simulate the ethanol process (Problem 5.7) using Aspen Plus. The feed
streamsareatoneatmosphereandroomtemperature,butthereactoroperatesat960
psiaand570◦F.Thus,youmustheatthereactorfeed,andafterthereactionoccurs
youmustcooltheproduct.Thefirstsplitterisavapor–liquidseparator(youchoose
thetemperaturethatwillseparateethanolfromethylene),andtheremainingsplitters
aredistillationcolumns.Youwillhavetodecideonthenumberofstagesandreflux
ratio,andusingDSTWUfirstmightbeuseful.
7.8 ModifytheprocessinProblem7.7touseacounter-currentheatexchanger(andtrim
1
heater)toheatthereactorfeedandcoolthereactorproduct.
7.9 Obtainaccesstothefollowingfileseitherfromyouradministratororfromthearea
2
(usually):
LocalDisk(C@/ProgramFiles(x86)/AspenTech/AspenPlusv7.2/GUI/App/IGCC.
Your system may be different, so the x86 and v7.2 are adjustable. There is a
pdf file entitled Aspen Plus IGCC Model. There is also an Aspen model that can
beloaded.Theprocessincludesalmost40chemicalsandseveralsubprocesses.The
subprocessesareasfollows:
Sizing:topreparethecoal
ASU:toseparateairintonitrogenandoxygen
GASFR:thegasifiers
```

---

## Стр. 143

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
130 PROCESSSIMULATION
CLEANING:tocleanthegas
CLAUS:toprocessthehydrogensulfidetomakeelementalsulfur
POWER: to collect all the steam in the process to use it in a turbine or in the
process
WGS:thewatergasshiftreactorandseparators
METHANZ:themakemethanol
NH :tomakeammonia
3
Ifyouopentheprocessandlookattheflowsheet,eachofthesesubprocessesisina
squarebox,andtheprocessunitsareinside.Thus,thereareblocksinsidetheblocks.
Thesubprocessblockscanbeexaminedbydoubleclickingonthebox.Ifyoulook
atafewofthem,youwillseewhatacomplicatedprocessitis.Examinetheprocess
andanswerthefollowingquestions:
1. Whatthermodynamicchoicesaremade?Aretheythesameinallsubprocesses?
2. The process involves solids at the beginning. Look at the components and see
howthesolidsarespecified.
3. Whatistheobjectiveofeachsubprocess,basedontheinputandoutput?
4. What blocks are used? Are they a priori blocks that can be calculated, or must
youchoosesomeparametersthatyoumightnotknowunlessyouareanexpert
in the field? (ex. A simple splitter (SEP block) will separate components of a
streaminthemanneryouspecify,butyouneedtochoosethesplit.Bycontrast,a
flashunitordistillationcolumnwilldeterminethesplitbasedonchemistryand
physicswithoutaprioriknowledge.
7.10 Consider the two-stage water–gas shift reactor for the IGCC process. The flow
2
rate of the syngas is taken proportional to that from the Aspen model (stream
SG-A) (kmol/h): nitrogen, 1126; water, 1700; carbon monoxide, 1686; hydrogen,
1134; carbon dioxide, 0. First, compare the mole fraction of this stream (from a
coal gasification process) with that from a methane reformer (Problem 4.6). Note
particularlythepresenceofnitrogenhere(muchlessinthemethanereformerbecause
air has been separated so that only oxygen is involved) and the mole fraction of
hydrogen.Whywouldtherebemorehydrogenfrommethanereformingthanfrom
coalgasification?BothreactorsaremodeledusingtheRGibbsblock.Theinputtothe
firstreactorissetat400◦Cand20bar,basedonthesuggestionsofPlatonandWang
(2010).Theoutputfromthefirstreactoriscooledto200◦C;steamisaddedtoenhance
theconversion.PlatonandWangsuggestasteam/drymolarratioof0.4goinginto
thesecondreactor.Addasteamflowgoingintothesecondreactor,too,andadjust
itsothattheratioof0.4isachieved.ThiscanbedoneusingtheDesignSpecblock.
7.11 Project. A one-stage process to form acetaldehyde from ethylene and oxygen is
givenbelow.Thefeedstreamis100lbmol/hofethyleneand50lbmol/hofwater
at20psiaand80◦F.Thereactionis
(cid:4) (cid:5)
C H + 1 O →CH CHO
2 4 2 2 3
andtheconversionperpassistakenas95%.Theoutputiscooledto80◦Fandthe
gases are removed in a stripper (use a version of RADFRAC without a condenser
orreboiler),thewater–acetaldehydestreamisseparatedinanotherRADFRAC,and
```

---

## Стр. 144

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 131
finally, light gases are removed from the acetaldehyde stream. The gases from the
stripperarerecycled,and1%ofthemarepurged.(Thisisnotstrictlynecessaryfor
theprocessasdescribed,butwouldbenecessaryiftherewerelightimpuritiesinthe
oxygen inlet stream.) You will have to experiment with the number of stages and
distillateratesandrefluxratios.
7.12 Examine the Aspen example for a biodiesel process. (See Aspen examples in Ap-
2
pendix C for directions to find this.) Identify the main sections of the process.
Lookatmajorinput/outputstreams:oil,methanol,FAME(fattyacidmethylesteror
biodiesel),andglycerol.Whatisthemassflowrateofproductglyceroltoproduct
FAME? Lots of glycerol is generated by the process. Suggest some ways glycerol
canbeused.
ProblemsInvolvingCornStoverandEthanol
Theprocessmodeledhereisamassbalanceonlyversionofthisprocesstomakeethanol
from corn stover. The nomenclature adheres as much as possible to that in the original
document. You should download the Aspen version and examine both the pdf report,
especially Appendix F (process flow diagrams) and the Aspen model itself. Also see the
spreadsheet. See the appendix for how to view sections of the process in Aspen. Also,
save the input report, which provides additional details. There is not exact agreement
betweenthepdfdocument,AppendixF(whichshowsactualprocessunits),andtheAspen
model (where several modules may represent one process unit), but the stream numbers
are usually the same. The mass balances on the pdf document are not the same as those
intheExcelspreadsheet,becausethevariousdocumentsrepresenttheprocessatdifferent
time during development over several years. Likewise the input file may be different
from what is shown in the pdf document. Despite some inconsistencies, all versions of
the process are generally the same. The numbers used here to define the process are
representative; in many cases, they must be determined by experiment. In particular, the
Aspen model has a Process Section 400, which is used to produce enzyme (in the 1999
version); it has been eliminated in the later versions (pdf); instead, the enzyme will be
purchased.Thisisanareaofactiveresearch,sothispermitspurchaseofthebestmaterialat
thetime.
The process to change corn stover into ethanol involves many different chemicals. To
simplify the process, the polymers xylan, arabinan, mannan, and galactan are combined
andusedsimplyasxylan.Inaddition,wehaveleftoutanumberofcomponentsthatare
small and are not involved in the reactions. In addition, we consider mass balances only.
Streamscancontainbothliquidsandsolids;thus,itisnecessarytolearnhowtodothisin
Aspen.Whileversion7.2requiresthesolidsbeinaseparatestream(CISOLIDS),version
7.3 allows many of them to be in the liquid stream (MIXED), here we will use them
inaseparatestreamtoillustratetheprocedure.Aspenhascertainrestrictionsforamass-
balance-onlysimulation,whicharedescribedintheAspenindex(insert“massbalanceonly
simulations”intothesearchwindow).Inparticular,itisnecessarytoturnoffthecalculation
of energy balances by unchecking the box “Perform Heat Balance Calculations” in the
Simulationoptionsform.Also,itisconvenienttodeveloptheflowsheetinsections,which
can be plotted and examined by themselves. The method to do that is demonstrated in
AppendixC.
```

---

## Стр. 145

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
132 PROCESSSIMULATION
100Process—FeedstockStorageandHandling
Cornstoverarrivesinbales,98,039kg/hat15%moisture.Itiswashed,andthedirtywater
iscleanedinaclarifierandthickener.Thewashedstoverhasmetalsremovedmagnetically
andisthenshredded.Someofitmustbestoredforfutureuse,sincethedeliveryofmaterial
isnotyear-round.Theshreddedmaterialis30–40%moisture.
200Process—PretreatmentandHydrolyzateConditioning
The hydrolysis reactions convert most of the hemicellulose in the feedstock to soluble
sugars; here, all combined in xylose. Glucan is converted to glucose using sulfuric acid.
Aceticacidisalsoliberatedfromthehemicellulosehydrolysis.Followingthepretreatment
reactor,thestreamisflashcooled,whichvaporizesalargeamountofwaterandsomeacetic
acid. The solids are washed and pressed to separate the liquid portion, which contains
sulfuric acid. Lime is added to the liquid to raise the pH to 10. After a delay, the stream
isneutralizedandgypsumprecipitates.Thegypsumisfilteredoutandthehydrolyzateis
mixedwiththesolids(cellulose)andwaterbeforesendingontothenextarea.
Section A201. The mass-balance-only process begins with the input to the 200 process,
stream105asindicatedinTable7.4.ThefirstpartisA201,theprehydrolysissection.The
flowrateisabout40%waterbymass;someofitisaliquidandsomeisasolid.2104kg/h
TABLE7.4 InputtoProcess(kg/h)
105
kg/h FromFeedHandling MolecularWeight
Liquids
Ethanol 22 46.0684
Water 45,002 18.0153
Glucose 180.1560
Xylose 150.1300
Aceticacid 232 60.0520
Lacticacid 90.0779
Sulfuricacid 98.0785
Carbondioxide 44.0095
Oxygen 31.9988
Nitrogen 28.0134
Othersolublesolids 7,417 193.0000
Totalliquids 52,673
Solids
Cellulose 31,187 162.1410
Xylan 22,924 132.1147
Lignin 21,806 –
Gypsum 172.1720
CaO 56.0774
Totalsolids 75,917
Totalflow 128,590
```

---

## Стр. 146

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 133
TABLE7.5 ReactionsOccurringintheEthanolProcess
Reaction FractionalConversionBased
Number Reaction onNonwaterSubstance
M202HI
3 H O+Cellulose(Cisolid)→Glucose 0.07
2
6 H O+Xylan(Cisolid)→Xylose 0.9
2
T209
H SO +CAO(Cisolid)+H O→Gypsum 1
2 4 2
ConversionbasedonH SO
2 4
T224
H SO +CAO(Cisolid)+H O→Gypsum 1
2 4 2
ConversionbasedonH SO
2 4
T310
3 H O+Cellulose(Cisolid)→Glucose 0.9
2
F301-6F
7 Glucose→2Ethanol+2CO 0.9
2
11 Glucose→3AACID 0.015
12 Glucose→2LACID 0.002
16 3Xylose→5Ethanol+5CO 0.8
2
F300CONT
1 Glucose→2LACID 1
2 3Xylose→5LACID 1
F300F
7 Glucose→2Ethanol+2CO 0.95
2
11 Glucose→3AACID 0.015
12 Glucose→2LACID 0.002
16 3Xylose→5Ethanol+5CO 0.85
2
ofsulfuricacid(stream212)iscombinedwith98,256kg/hofwater(stream211)inamixer
(A201).Thedilutesulfuricacid(stream214)iscombinedwithstream105inM202MIX
whereitisheatedto100◦C;whilewewouldnotworrynowabouttheenergytransfer,the
combinedstreamis214A.Thisstreamiscombinedwith11,507kg/hoflow-pressuresteam
(stream215)inM202LO,whereitisheatedto100◦Candthepressureisraisedto39.26
atm. The output (stream 215A) is fed to the reactor (M202HI) along with high-pressure
steam (stream 216, 37,234 kg/h). There are several different reactions taking place, and
theRStoicmodulecanbeusedtomodelthemassbalance, asdisplayedinTable7.5.Be
careful, though, since the balances are on mass and the reactions occur on a mole basis.
Theoutput,stream217,isfedtoaflashunit(T203)at1atm.Forthismass-balance-only
model,thesplitfractions(thefractionofthefeedstreamgoingoutthetopstream218as
vapor) are ethanol 78%, water 27%, acetic acid 2.9%. This completes the prehydrolysis
SectionA201.
Section A203. (It is more convenient to consider this section before Section 202.) The
Lime Addition Section, A203, takes stream 240 from section 202 and adds lime (stream
227,2395kg/h);allthesulfuricacidreactswiththelimeinT209toformgypsumandthe
ouputisstream228.ThisgoestounitT-224,areacidificationtank.Sulfuricacidisadded
```

---

## Стр. 147

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
134 PROCESSSIMULATION
(1185kg/h)andallthelimereactswithsulfuricacidtoformgypsum.Theoutputisstream
239,whichissenttoS-222(SSplit)toremovethegypsum.Thesolidstream(229)contains
99.5%ofthesolidsand0.4%oftheliquids;therestisintheliquidstream(230),whichis
recycledtoSectionA202.
Section A202. In the solid–liquid separation section, water is added in stream
252 (125,000 kg/h) and stream 253 (75,000 kg/h with 1000 kg/h ethanol. In the real
process,thiswatercomesfromtheligninseparationprocess,whichisnotmodeledhere.
Meanwhile,stream220fromtheprevioussectionissplitintotwostreamsinunitS205A
(SSplit):stream221is78%ofitandstream225istherest.Streams225and252arecom-
binedinS205MIXtoformstream254.Stream254issenttounitS205B(SEPunit)thatis
afiltrationunit;theoutputisdeterminedfromexperimentaldata:stream256contains75%
ofthewaterand90%oftheotherliquidcomponents.Stream255Acontainsallthesolid
components,plustherestoftheliquidcomponents.Steams221and256arecombinedin
MIXRtoformstream240,whichissentontotheLimeAdditionSection,A203.Stream
255Aiscombinedwithair(964kg/hofoxygenand3703kg/hofnitrogeninstream259)
andsenttotheS205FLSH unit.Theairstreamand404 kg/hwater come outof thisunit
asagasstream(260)andtheremainderisaliquidasstream255.Stream255iscombined
in unit C202 with stream 253 and stream 230 from the Lime Addition (A203); this is
thusarecyclestream.Theoutputisstream250,whichissenttotheSaccharificationand
FermentationSection,A300.Thiscompletesthesection.
A300Process—SaccharificationandCofermentation
Section A300. Saccharification (or hydrolysis) of cellulose to glucose uses cellulase en-
zymes,anditworksbestathightemperatureswheretheenzymeactivityishigh.Thus,the
saccharificationisperformedfirst.ThenextsectionoftheA300processusesfermentation
toconvertthesugarstoethanol.Thisisdoneusingbacteriaasabiocatalyst.Theenzymes
and bacteria are specially made to enhance production; here, the conversion is taken as
from the NREL study, and the conversions were based on experimental data; see pages
27–28ofthereportforinformationaboutthespecificcompounds.
InProcessSectionA300,stream250fromProcessSectionA202isfedtoavessel(T310).
ThisvesselinAspenactuallyrepresentsaseriesoffivestirredtanksthataredesignedto
allowtheenzymestogrow(overaperiodof36hours).ThereactionsforT310arelistedin
Table7.5;mostofthecelluloseisconvertedtoglucose.Ninetypercentoftheoutputfrom
T310issentdirectlytothefermenters,FEMMIX,instream302.Therestissenttoanother
reactorunit.TheseedtrainoffivereactorsismodeledasunitF301-6F(RStoic),withthe
conversions shown in Table 7.5. The output is flashed (F301-6FL) to remove the carbon
dioxide and oxygen formed in the reactors. In addition, 3% of the ethanol, 0.22% of the
water,and0.2%oftheaceticacidgooutasvapor.Theliquidfromtheflashdrumgoeson
tobecombinedinthemixerFEMMIXwiththepreviousstream302.
Threepercentofstream304Aissplitofftosendtoacontaminationreactor(F300CONT).
Inthatunittheglucoseandxyloseareallconvertedtolacticacidwith100%conversion.
Theotherstream(97%of304A)goestoafermenter(F300F)whereanumberofreactions
takeplace(Table7.5).Theoutputfrombothreactorsissenttoaflashunittoreleasegases
(allthecarbondioxideandoxygenand2.8%oftheethanol,0.2%ofthewater,and1.1%
oftheaceticacid.Theliquidstream(306)fromtheflashunit(F300FLSH)goesontothe
nextsectionforpurification.
```

---

## Стр. 148

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 135
A500Process—Distillation,Dehydration,Scrubber,Evaporator,SolidsSeparation
SectionA500. Stream306isfedtoadistillationcolumn(D501,SEP)todistillmostofthe
water(andremovethedissolvedcarbondioxide).Thiscolumnactswithasidedraw,which
is an ethanol–water mixture. For purposes of this model, remove all the carbon dioxide,
0.24%oftheethanoland0.005%ofthewateroutthetopinstream508.Thisstreamgoes
toascrubber.Thesidedraw(stream510)takes99%oftheethanolfedtothecolumn,10%
of the water, and 5% of the acetic acid; this stream goes to the rectification process. The
remainder goes out the bottom, stream 518. This stream goes to a series of evaporators;
these are not modeled here, but some of the output from the evaporator goes to a lignin
separationprocess(A505,notmodeled),andsomeoftheoutputfromthatprocessbecomes
stream516;itis97%water.Ultimately,waterfromtheligninseparationplantisrecycled
asstreams252and253,whicharespecifiedhere.
Therectificationprocesstakesstream510,addsrecyclestream521fromthemolecular
sieve process, and distills it in unit D502. The overhead from this unit (stream 511) is at
theethanol–waterazeotrope,whichis0.826molefractionethanolat27psiaand92.4◦C.
The rest of that stream is water. The bottoms (stream 516) contains everything else, but
negligibleamountsofethanol,anditisrecycled.Sincewearespecifyingtheoutputstream
ofD502,weusetheSEP2unittomodelthis.
Theethanol–waterazeotrope,stream511,issenttoamolecularsieveprocess(T507-8)
for drying. This is an adsorption unit that requires regeneration periodically. During the
regeneration, ethanol and water are generated, and this is sent back to the rectification
columnasstream521.Thisstreamcontains20%oftheethanolfedtothedehydrationunit
and 95% of the water in stream 511. The very dry ethanol output (stream 515) is sent to
storage.Thatistheproductoftheprocess.
Theflowratesintoeachsectionaregivensothateachsectioncanbedoneasahomework
problem.Theoutputscanthenbecomparedwiththeotherinformation.Theentireprocess
isaProject.BothproblemsandtheprojectcanbedoneinExcelorinAspenPlus.Foreach
section,comparetheeaseofcalculationandthetransparencyoftheflowsheetbetweenthe
twoprograms.ComparetheresultswiththeresultsoftheNRELprocess.
7.13 SimulateSection201in(a)AspenPlus;(b)Excel.Flowratestotheprocess(kg/h):
1
ethanol, 22; water, 45002; acetic acid, 232; other soluble solids, 7417; cellulose,
31187;xylan,22924;lignin,21806.Stream215is11,507kg/hofsteam;stream216
is37,234kg/hofsteam.
7.14 Simulate Section 202 in (a) Aspen Plus and (b) Excel. Flow rates to Section 202,
1
stream 220: ethanol, 5; water, 137,928; glucose, 2426; xylose, 23445; acetic acid,
225;sulfuricacid,2104;othersolublesolids,7417;cellulose,29004;xylan,2292;
lignin, 21806. Stream 230 is ethanol, 5; water, 222430; glucose, 2363; xylose,
22837;aceticacid,219;othersolublesolids,7225;cellulose,113;xylan,9;lignin,
85;gypsum,37.Stream252is125,000kg/hofwaterandstream253is1000kg/h
of ethanol and 75,000 kg/h of water. The air stream is 964 kg/h of oxygen and
3703kg/hofnitrogen.
7.15 SimulateSection203in(a)AspenPlus;(b)Excel.FlowratestoSection203:ethanol,
1
5;water,224092;glucose,2372;xylose,22929;aceticacid,220;sulfuricacid,2058;
other soluble solids, 7254; cellulose, 22623; xylan, 1788; lignin, 17009; the lime
addition(stream227)is2395kg/handthesulfuricacidsteamisadjustedtoreactall
thelime.
```

---

## Стр. 149

```text
P1:OTA/XYZ P2:ABC
JWBS084-c07 JWBS084-Finlayson May26,2012 14:1 PrinterName:YettoCome Trim:7in×10in
136 PROCESSSIMULATION
7.16 SimulateSection300in(a)AspenPlus;(b)Excel.FlowratestoSection300:ethanol,
1
1005;water,335862;glucose,2416;xylose,23353;aceticacid,224;sulfuricacid,
46; other soluble solids, 7388; cellulose, 6494; xylan, 513; lignin, 4882; gypsum,
37.
7.17 SimulateSection500in(a)AspenPlus;(b)Excel.FlowratestoSection500:ethanol,
1
14775;water,334468;glucose,259;xylose,3126;aceticacid,352;lacticacid,905;
sulfuricacid,46;othersolublesolids,7388;cellulose,649;xylan,513;lignin,4882;
gypsum, 37. The model for unit D502 must achieve a certain concentration in the
overhead—theazeotropewithwaterandethanol.UseaSEP2blockforthisunit.For
thisblock,setthesplitfractionoftheoverheadto1.0forethanol,and0.0forallthe
othercomponentsexceptwater.Thewindowhasaplaceforasecondspecification.
Forthewater,setthattoamolefractionof0.174.Thentheamountofwatersentto
theoverheadwillbeadjustedtogivethatmolefractioninamixtureofethanoland
water, and the rest of the water, and the other components, will go out the bottom
stream.
7.18 Project. Do the entire process using either Excel or Aspen Plus. Compare the
resultswiththeresultsoftheNRELprocess.Inyourreport,showanoverallmass
balance, indicate the amount of water fed to the process and the ratio of water to
ethanolproduced.UsingthestoichiometryinTables7.4–7.5,calculatethemaximum
amountofethanolthatcanbeproducedandtheefficiencyofyourprocess.
```

---

## Стр. 150

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
8
CHEMICAL REACTORS
Ethane flowing through a cylindrical tube can be heated to the point that it reacts into
hydrogen and ethylene, the precursor to polyethylene. Many reactors, though, require a
catalysttospeedupthereaction.Thewater–gasshiftreactormakeshydrogenbyusinga
cylindrical tube that is filled with catalyst and past which the gas flows. One feature that
setschemicalengineersapartfromotherengineeringdisciplinesistheirabilitytohandle
chemicalreactions,theprocessofconvertingoneormorechemicalsintootherchemicals
that are more valuable. Thus, chemical engineers need to understand chemical reactions
andshouldbeabletomodelequipmentinwhichthechemicalreactionstakeplace—that
is,chemicalreactors.Sometimesreactorsareassimpleasacylindricaltube,withreactants
fedinoneendandproducts(andunreactedreactants)comingouttheotherend.Reactants
maybeplacedinavesselandstirredtocreatenewchemicals.
Real-life complexities challenge engineers as they design chemical reactors. In some
reactors,thereactionrateisslow.Whenthishappens,youneedtohaveabiggerreactorto
achieveaspecifiedproductionrate,anditmaybetoobigtobeeconomical.Then,youlook
for a catalyst that speeds up the reaction but retains its existence after the reaction. The
tubeispackedwithcatalyst,andreactantsflowaroundthecatalyst.Oftentimesthereaction
is exothermic and the reactor gets hot. The energy must be removed somehow, and heat
transfermustbeincludedinthecalculations.Sometimesthereactionoccursinsideaporous
catalyst,perhapsanaluminapellet(Al O )withcatalystcoatingtheinternalsurface.Then
2 3
itmaybenecessarytoincludeheatandmasstransfereffectsinsidethepellet.
Whenitisnecessarytoincludetheseeffects—slowreactionrates,catalysts,heattrans-
fer, and mass transfer—it can make an engineering problem extremely difficult to solve.
Numerical methods are a must, but even numerical methods may stumble at times. This
chapter considers only relatively simple chemical reactors, but to work with these, you
mustlearntosolveordinarydifferentialequationsasinitialvalueproblems.
IntroductiontoChemicalEngineeringComputing,SecondEdition.BruceA.Finlayson.
©2012JohnWiley&Sons,Inc.Published2012byJohnWiley&Sons,Inc.
137
```

---

## Стр. 151

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
138 CHEMICALREACTORS
This chapter begins with reactor models described in mathematical terms. You will
learn how to solve ordinary differential equations by using MATLAB®. Then, after you
have mastered this new skill, you will solve several chemical reactor problems by using
MATLAB.SometimestheseproblemscanbesolvedusingComsolMultiphysicsandAspen
Plus, too, as the chapter discusses next. A few problems use Excel to solve ordinary
differential equations. The reason is that all the other programs have guaranteed error
control.AlthoughitispossibletosolvesimpleordinarydifferentialequationswithExcel,
itbecomescumbersomeiftheproblemisdifficult,andyouwouldnotknowtheaccuracy
ofyoursolutionwithoutextraeffort.Somereactorsoperatinginsteadystateareexpressed
asalgebraicequations,andbothExcelandMATLABareusedtosolvethoseequations.
InstructionalObjectives: Afterworkingthroughthischapter,youwillbeableto
1. Model chemical reactors that are stirred tanks, plug flow reactors, including non-
isothermalones.
2. SolvesuchproblemsusingMATLAB,ComsolMultiphysics,AspenPlus,andExcel,
forcomparison.
3. Solvereactorproblemsinwhichtherearemolechangesand/ormasstransferlimita-
tions.
4. Appreciatetheneedforspecialintegrationtechniqueswhentheequationsarestiff.
5. Introduce complicated reaction rate expressions into Aspen Plus when modeling
reactors.
MATHEMATICALFORMULATIONOFREACTORPROBLEMS
Adifferentialequationforafunctionthatdependsononlyonevariableiscalledanordinary
differentialequation.Theindependentvariableisfrequentlytime,t,butforreactors,itcan
alsobelengthdownaplugflowreactor.Anexampleofanordinarydifferentialequationis
dy(t)
= f(y), y(0)= y (8.1)
0
dt
Thegeneralsolutiontothedifferentialequationincludesmanypossibilities;theengineer
needstospecifyinitialconditionstospecifywhichsolutionisdesired.Ifallconditionsare
availableatonepoint[asinEq.(8.1)]thentheproblemisaninitialvalueproblemandcan
be integrated from that point on. If some of the conditions are available at one point and
othersatanotherpoint,thentheordinarydifferentialequationsbecometwo-pointboundary
value problems (see Chapter 9). Initial value problems as ordinary differential equations
ariseincontroloflumpedparametermodels,transientmodelsofstirredtankreactors,and
generallyinmodelswherethereisnodiffusionoftheunknowns.
Example:PlugFlowReactorandBatchReactor
Consider a plug flow reactor—a cylindrical tube with reactants flowing in one end and
reacting as they flow to the outlet. A mole balance is made here for the case when the
operation is steady. Let F be the molar flow rate of a chemical, which changes dF in a
smallpartofthetube;takethevolumeofthatsmallparttobedV.Therateofreactionis
```

---

## Стр. 152

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
MATHEMATICALFORMULATIONOFREACTORPROBLEMS 139
expressedasthemolesproducedperunitoftimeperunitofvolume.Ifachemicalspecie
reacts,thentherforthatspecieisnegative.Thus,theoverallequationforasmallsection
ofthetubeis
dF
dF =rdV or =r (8.2)
dV
Themolarflowratecanberelatedtothevelocityinthetube:
F =uAc (8.3)
Inmanycases,thevelocityandcross-sectionalareaofthetubeareconstant.Thenyoucan
write
dF =uAdc, dV = Adz (8.4)
IfyouputtheseintoEq.(8.2)anddividebydzyouget
dc
u =r, plugflowreactor (8.5)
dz
Normally, r is a function of c, and this is an ordinary differential equation for c(z). In
addition,youneedtoknowtheinitialvalueoftheconcentration,thatis,
c(0)=c (8.6)
0
Ifthereactorcontainsacatalyst,thenthereactionrateisexpressedasthemolarrateof
changepermassofcatalyst,r(cid:2).Onemustthenmultiplyitbythemassofcatalystperunit
volume,butotherwisethesituationisthesame:
dc
dF =ρ r (cid:2) dV and u =ρ r (cid:2), catalyticplugflowreactor (8.7)
B B
dz
Inabatchreactor,letNbethemolesofachemical;themolarchangeofachemicalisthe
reactionrate(molarchangeperunittimeperunitvolume)timesthevolumeandthetime:
dN =rVdt (8.8)
Thiscanbeputintoadifferentialequation,too:
dN
=rV (8.9)
dt
Ifthevolumeofthebatchreactorisconstant,then
N
c= (8.10)
V
andtheequationbecomes
dc
=r, batchreactor (8.11)
dt
```

---

## Стр. 153

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
140 CHEMICALREACTORS
Thisequationissimilartotheequationforaplugflowreactor,withthetimet takingthe
place of the variable z/u. You can also introduce catalyst into the batch reactor, in which
casethereactionraterisreplacedbyρ r(cid:2).Inaddition,youneedaninitialconditiontogo
B
withEq.(8.11),c(t=0)=c .Thestructureoftheproblemisthesameasthatforaplug
0
flowreactor,andifyoucansolveone,youcansolvetheother.So,thereissomeeconomy
ofeffort.
Manychemicalsareinvolved,andyouneedareactionrateforeachreactionoccurring.
Thus, use {c} for all the chemical concentrations and {r} for all the reactions. If the
j i
reactionis
aA+bB→cC+dD (8.12)
thentherateofreactionofBisb/atimestherateofreactionofA,andtheratesofreaction
ofCandDare−c/aand−d/atimestherateofreactionofA.Theimportantpointisthatthe
rate of reaction is an algebraic function of the concentrations, temperature, and pressure.
Eachreactionrateneedstobeknownspecificallyforthereactioninquestion.
Example:ContinuousStirredTankReactor
Anothertypeofreactorisknownasacontinuousstirred-tankreactor(CSTR).Thisreactor
isavesselwithaninletstreamandanoutletstream,andthecontentsareconstantlybeing
stirred.Engineersoftenassumethatthisreactorissowellmixedthattheconcentrationis
thesameeverywhere.Themolebalanceonthisreactoris
F −F =rV (8.13)
out in
where V is the volume of the reactor. The molar flow rates are related to the volumetric
flowrates,Q,asfollows:
F = Qc (8.14)
Whenthevolumetricflowratesareconstant,Eq.(8.13)becomes
Q(c −c )=rV, CSTR (8.15)
out in
Inawell-mixedreactor(CSTR),theconcentrationgoingoutthereactoristhesameasthe
concentrationinthereactor.Sincetherateexpressionisafunctionofc,itisafunctionof
c .ThenEq.(8.15)becomesanalgebraicequationinonevariable(here)forc .Youcan
out out
solvethisusingeitherExcelorMATLAB.
USINGMATLABTOSOLVEORDINARYDIFFERENTIALEQUATIONS
SimpleExample
In MATLAB, you define the problem by means of a function, called an m-file. You then
tellMATLABtosolvethedifferentialequation.Thus,youneedtoprepareanm-filethat
definestheequationandthencallthesubroutine“ode45”todotheintegration.Thismethod
mayseemmysteriousatfirstbecauseyoucallasubroutine,whichinturncallsyourm-file.
```

---

## Стр. 154

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
USINGMATLABTOSOLVEORDINARYDIFFERENTIALEQUATIONS 141
Youdonotdirectlycallyourm-filewhensolvingthedifferentialequation.Thisprocessis
illustratedusingasingle,simpledifferentialequation:
dy
=−10y, y(0)=1 (8.16)
dt
Integratethisequationfromt=0tot=1.Theexactsolutioncanbefoundbyquadrature
andis
y(t)=e −10t (8.17)
Step1 TouseMATLAB,youfirstconstructanm-filethatdefinestheequation.
% filename rhs.m
function ydot=rhs(t,y) %compute the rhs of eqns.for any input
%values t, y
ydot = -10*y %compute rhs
Step2 Thentotestthefunction,issuethecommand
q = rhs(0.2,3)
ydot = -30
q = -30
When y = 3, the value of the right-hand side should be −30, so the m-file is correct.
In more complicated cases, you might remove all the “;” from the rhs.m so intermediate
resultsareprinted.Thissimplifiesyourtaskwhencheckingtheprogram.Nowadd“;”to
allcommandsinrhs.morelseyouwillgetlotsofoutput.
Step3 Nextcreateanm-filethatprovidesthescripttoruntheproblem.Thesecommands
canalsobetypedinthecommandwindow,butwhenyouhaveseveralcommandsthatyou
willuseoverandover,itismoreconvenienttocreateascriptthatcanrunallthecommands
withonemessagefromyou.
% filename simple.m
y0(1)=1.; % set the initial condition to 1.
tspan=[0 1]; % integrate from t = 0 to t = 1
[t,y]=ode45(@rhs,tspan,y0) % call the routine ode45
plot(t,y,’r’) % plot the solution
xlabel(‘t’) % label the x-axis
ylabel(‘y’) % label the y-axis
TheresultsgiveatableofvaluesfortandyandFigure8.1.
t = 0 0.0050 0.0100 0.0157 ... 0.9475 0.9738 1.0
y = 1.0 0.9510 0.9044 0.8601 ... 0.000076 0.000059 0.000046
Step 4 The validity of your solution depends upon several things. First, you check the
m-file“rhs”anddeterminethatitgivesthecorrectresultwhenyouinsertvaluesfortand
y.Youalwayshave todothischeck toshowthatyour workiscorrect.Youdepend upon
MATLAB to do its job correctly. You can easily check that it uses the initial and ending
timescorrectlyfromtheoutputandcanseethattheinitialconditionfor yiscorrect,too.
```

---

## Стр. 155

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
142 CHEMICALREACTORS
1
0.8
0.6
0.4
0.2
0
0 0.2 0.4 0.6 0.8 1
t
y
FIGURE 8.1 SolutiontoEq.(8.16)usingMATLAB.
You can always solve a problem for which you know the solution, and you try to make
thatproblemasmuchlikeyourproblemaspossible.Inthiscase,youdonotneedtouse
numericalmethodsforthetest,becauseyouhaveanexactsolution.Thus,youcancompare
thenumericalresulttotheanalyticalresult(theyarethesame)anddeterminethatMATLAB
did its job correctly. In cases without an analytical solution, you check your m-file “rhs”
andthendependonMATLAB(andtheaccuracychecks).Notethatinthetabulatedvalues
shownearlier,theincrementsbetweentimepointsare0.005atthestartofthecalculation
and 0.0272 at the end of the calculation. The integration routine adjusts the time step to
insurethataspecifiedaccuracyismet.Youcanalsodecreasethenumericalerrorbysetting
aparameter(errortolerance)toimprovetheresult(seeAppendixB).
Useofthe“Global”Command
In the aforementioned example, you solved the problem when the right-hand side was
−10y,andyousimplyusedthevalue10intheprogram.Therearetwootherwaystoset
thisvalue,usingthecommand“global”orbypassingkasaparameter.Youmightwantto
writethisas−kyandsolvetheproblemforseveralvaluesofk.Becausethefunctiononly
knowswhatissetinsidethefunction,orwhatgetstransferredtoit,youneedtolearnhow
totransferinformationfromtheworkspaceintothefunction.Youwillneedtomakethose
changestothecodeusedearlier.Ifyouusethe“global”command,putthevariablename
in both the workspace and the m-file and assign its value in one place or the other. Then
thatvalueisaccessiblefromeitherthem-fileortheworkspace.
Step1 Here,youwillsetthevalueofkintheworkspace,orcallingprogram,andthenit
willbeavailableinthem-file.
% filename simple2.m %compute the rhs of Eq. (8.16)
global k
k=10; % set k to 10; it is now available to any
% m-file that has the
```

---

## Стр. 156

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
USINGMATLABTOSOLVEORDINARYDIFFERENTIALEQUATIONS 143
% global k statement in it.
y0=1; % set the initial condition to 1
tspan=[0 1]; % integrate from t = 0 to t = 1
% call the routine ode45; use the m-file called rhs2,
[t,y]=ode45(@rhs2,tspan,y0)
plot(t,y) % plot the solution
Step2 Next,addtheglobalcommandtothem-file,calledrhs2.(Noteyouaddedanumerical
identifiertoboththecallingprogramandthem-filetohelpkeepthemstraight.)
% filename rhs2.m
function ydot=rhs(t,y)
% compute the rhs of Eq. (8.16) for any input
% values t, y
global k % The m-file can access the numerical
% value of k, if
% it has been set to global and given a
% value elsewhere
disp(k) % display the numerical value of k
% use this only when testing the function rhs2
ydot = -k*y; % compute rhs
Naturally,youexpectthesameresults,whichyoucanverifybyrunningthenewcode.
Step3 Checkthecodeasdonebefore,withoneaddition.Itishelpfulthefirsttimeyourun
thecodetoprintthevariablesinsidethefunctiontomakesuretheyareaccessible.Ifnot,
MATLAB will tell you that the variable is not defined. Alternatively, use the debugging
techniquesdescribedinAppendixB.
PassingParameters
Stillanotherwaytointroducek intothefunctionistouseitasaparameterinthecalling
argument.
% filename simple3.m
k=10; % set k to 10
y0=1; % set the initial condition to 1
tspan=[0 1]; % integrate from t = 0 to t = 1
options = [] % the OPTIONS = [] is a place holder
% The symbol [] is made as [] without a space.
% call the routine ode45;
% use the m-file called rhs3,
[t,y]=ode45(@rhs3,tspan,y0,options,k)
plot(t,y) % plot the solution
Nowthefunctionis
% filename rhs3.m
function ydot = rhs(t,y,k)
% compute the rhs of eqns. for any input values t, y
```

---

## Стр. 157

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
144 CHEMICALREACTORS
disp(k) % display the numerical value of k; use only for
% testing of rhs3
ydot = -k*y; % compute rhs
Thisprogramgivesthesameresultsasgivenbysimple1.mandsimple2.m.
Example:IsothermalPlugFlowReactor
Inthissection,youwillsolvetheequations foranisothermalplugflowreactor.Thefirst
problem is very simple and is patterned after a problem on the California Professional
EngineersLicenseExamination(Fogler,2010).Hereitismodified.Youtakeareactorin
whichcomponentsAandCarefedinequimolaramounts,andthefollowingreactiontakes
place:
2A→B (8.18)
Youassumethatthereactiontakesplaceintheliquidphaseandthatthevolumetricflowrate
remainsconstantevenwhenreactionoccurs.TheequationsareEq.(8.5)foreachspecies:
dC
u j =r , j =1,...,3 (8.19)
j
dz
where C is the molar concentration of the jth species, u is the velocity, z is the distance
j
downthetubefromtheinlet,andr istherateofreactionofthejthspecies,inmolesper
j
volumetime.Heretherateofreactionistakenassecondorder:
RateofformationofB=kC2 (8.20)
A
wheretheunitsofkarevolumepermoletime.Theequationsforallthreespeciesarethen
dC dC dC
u A =−2kC2, u B =+kC2, u C =0 (8.21)
dz A dz A dz
Attheinletyoutake
C (0)=2kmol/m3, C (0)=0, C (0)=2kmol/m3 (8.22)
A B C
andwetakeu=0.5m/s,k=0.3m3/kmols,andthetotalreactorlengthasz=2.4m.
Step1 TheMATLABprogramrequiresyoutowriteafunctionthatdefinestheright-hand
side.Theinputparameterstothefunctionaretheconcentrationsofallspecies.(a)Thus,to
solvetheproblemyouusethevariables
y =C , y =C , y =C (8.23)
1 A 2 B 3 C
```

---

## Стр. 158

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
USINGMATLABTOSOLVEORDINARYDIFFERENTIALEQUATIONS 145
(b)Thefunctionalsoneedsthevelocity,u,andtherateconstant,k.Thedistancefromthe
inlet, z, takes the place of time and is the independent variable. (c) The rates of reaction
arethenevaluated,andthefunctionreturnsthenumericalvalueoftheright-handside.The
codeforthefunctionis
% rate1.m
% This function gives the right-hand side for a simple
% reactor problem which is isothermal.
function ydot=rate1(VR,y)
% y(1) is CA, y(2) is CB, y(3) is CC
% k = 0.3 and u = 0.5
CA=y(1);
rate = 0.3*CA*CA;
ydot(1) = - 2.*rate/0.5;
ydot(2) = + rate/0.5;
ydot(3) = 0.;
ydot = ydot';
Step2 Youtestthism-filebycallingitwithspecificvaluesfory,j=1,2,3toensurethat
j
itiscorrect.Usingy(j)fory issuethefollowingcommands.
j,
y(1) = 0.2; y(2) = 0.3; y(3) = 0.4; rate1(0.1,y)
Youget
ans = -0.048, 0.024, 0
which agrees with hand calculations. This is a very important step because this is where
youaddvalue.MATLABwillintegratewhateverequationsyougiveit,rightorwrong,and
onlyyoucanensurethattheprogramhassolvedtherightequations.
Step 3 Next, write a code that serves as the driver. This code must (a) set any constants
(heretheyarejustputintothefunctionrate1forsimplicity),(b)settheinitialconditions
andtotalreactorlength,and(c)calltheodesolver.
% run_rate1.m
% This is the driver program to solve the simple flow reactor
example.
y0 = [2 0 2] % set the initial conditions
zspan = [0 2.4] % set the total volume of the reactor
[z y] = ode45(@rate1,zspan,y0) % call the ode solver
plot(z,y(:,1),'*-',z,y(:,2),'+-',z,y(:,3),'x-') % plot the result
xlabel('length (m)')
ylabel('concentrations (kgmol/mˆ3)')
legend('A', 'B', 'C')
```

---

## Стр. 159

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
146 CHEMICALREACTORS
2
1.5
1
0.5
0
0 0.5 1 1.5 2 2.5
Length (m)
)3m/lomgk(
snoitartnecnoC
A
B
C
FIGURE 8.2 DifferentplotofsolutiontoproblemposedbyEqs.(8.21)–(8.22).
Step4 Eachcurveislabeledwithadifferentsymbolintheplotcommand,andthecurves
areeasytodistinguish(seeFigure8.2).Theplotcommandgivenearlierwillmakethethree
curveshavedifferentcolors,butthosearenotvisibleinthisblackandwhiteversion.Now
thatyouhaveavalidatedcode,youcanvarytheparameterstoseetheireffect.
Example:NonisothermalPlugFlowReactor
Mostreactionshaveheateffects,andthismeansthatreactormodelsmustbeabletomodel
the heat transfer as well as the mass balances. The following example models a simple
reactoroxidizingSO toformSO (YoungandFinlayson,1973).Aftersomemanipulation,
2 3
theequationsare
dX dT
=−50R (cid:2), =−4.1(T −T )+1.02 ×104R (cid:2) (8.24)
surr
dz dz
wherethereactionrateis
X[1−0.167(1−X)]1/2−2.2(1−X)/K
R (cid:2) = eq (8.25)
[k +k (1−X)]2
1 2
lnk =−14.96+11,070/T, lnk =−1.331+2331/T
1 2
lnK =−11.02+11,570/T (8.26)
eq
with the parameters: T =673.2, T(0)=673.2, X(0)=1. The variable X is the con-
surr
centrationofSO dividedbytheinletconcentration,1–Xisthefractionalconversion,andT
2
isthetemperatureinkelvin.ThefirstequationisthemolebalanceonSO ,andthesecond
2
istheenergybalance.Thefirsttermontheright-handsideofEq.(8.24)representscooling
atthewall;thesecondtermthereistheheatofreaction.
```

---

## Стр. 160

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
USINGMATLABTOSOLVEORDINARYDIFFERENTIALEQUATIONS 147
These equations are appropriate when radial and axial dispersion are not important.
Axial and radial dispersion are actually important in this case, as discussed by Young
and Finlayson (1973), but the simpler case is a good vehicle for seeing how to include
temperatureeffectsintheproblem.Thereactionrateequationshowsthatequilibriumcan
bereached(thenR(cid:2) =0),andtheequilibriumconstantdependsonthetemperature.Thus,
theconversiondependsintimatelyonthetemperature.
Step1 TheMATLABprogramrequiresyoutowriteafunction(m-file)thatcalculatesthe
right-handsideofEq.(8.24),giventheinput,z,X,andT,whicharetheaxiallocationin
thereactorandtheconversionandtemperatureatthataxiallocation,respectively.Thus,(a)
tosolvetheproblemyouusethevariables
y(1)= X, y(2)=T (8.27)
Theaxiallocation,z,andthevariablesy(1)andy(2)willbeavailabletothefunction.(b)You
firstmovey(1)intoX andy(2)intoT (forclarityintheprogram)andthen(c)evaluatethe
rateofreaction.(d)Finally,youcalculatetheright-handsidesofthedifferentialequations
andputtheminthevectorydot,whichistheoutputfromthefunction.
% rateSO2.m for SO2 reaction
function ydot = rateSO2(z,y)
% X is concentration SO2 divided by the inlet concentration
X = y(1);
% T is temperature in degrees K
T = y(2);
k1 = exp(-14.96+11070/T);
k2 = exp(-1.331+2331/T);
Keq = exp(-11.02+11570/T);
term1 = X*sqrt(1-0.167*(1-X));
term2 = 2.2*(1-X)/Keq;
denom = (k1+k2*(1-X))ˆ2;
rate = (term1-term2)/denom;
ydot(1) = -50*rate;
ydot(2) = -4.1*(T-673.2) + 1.02e4*rate;
ydot = ydot'; % converts ydot to a column vector (required)
Analternativeforthelastthreelinesis
term1 = -50*rate;
term2 = -4.1*(T-673.2) + 1.02e4*rate;
ydot = [term1;term2] % ydot is a column vector
Step2 Youtestthism-filebysettingtheinputvariablesandcallingthem-file.
y(1) = 0.2; y(2) = 573.2;
rateSO2(0.1,y)
ans = −0.001148 410.235
```

---

## Стр. 161

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
148 CHEMICALREACTORS
This agrees with hand calculations, so the m-file is correct. (To make the comparison
easier,youcanremovethesemicolonsfromrateSO2.Afterchecking,thesemicolonsare
addedagain.)Youmustmakethischecktobesureyouhavesolvedthedesiredproblem.
Step3 Next,youwritethecodeasthedriver.Thiscodemustsettheconstants,settheinitial
conditions for conversion and temperature, decide how far down the reactor to integrate,
andthencalltheodesolver.
% run_SO2.m
% set the dimensionless initial conditions
y0 = [1 673.2]
% set the integration range
zspan = [0 1]
% call the solver
[z y] = ode45(@rateSO2,zspan,y0)
% plot the result
plot(z,y(:,1),'r-')
xlabel('dimensionless axial position')
legend('fraction converted')
pause
plot(z,y(:,2),'g-')
xlabel('dimensionless axial position')
legend('temperature (K)')
The results are shown in Figure 8.3. The concentration and temperature are plotted in
separate graphs because they have such different magnitudes. Now you can change the
parameterstoseetheireffect.Changetheinlettemperatureto800Kandseewhathappens.
USINGCOMSOLMULTIPHYSICSTOSOLVE
ORDINARYDIFFERENTIALEQUATIONS
ComsolMultiphysicsistreatedindetailinChapters9–11andAppendixD,butitcanalsobe
usedtosolvereactorproblems.TheadvantageofComsolMultiphysicsisthatyouprogram
with a graphical user interface, so computer errors are less likely. It is still necessary to
checkyourwork,though.Althoughtheapplicationsinthischapterareallone-dimensional
(to compare with MATLAB solutions), it is easy to solve two-dimensional problems,
as described in more detail in later chapters. We show here how to solve the same three
problemsalreadysolvedusingMATLAB:thesimpleexponential,Eq.(8.16);theisothermal
flowreactor,Eqs.(8.21)–(8.22);andthenonisothermalreactor,Eqs.(8.24)–(8.26).
SimpleExample
Theproblem(8.16)canberestatedas
du
=−10u, u(0)=1, f(u,u ,u ,t)≡ut +10 ∗ u =0 (8.28)
t tt
dt
```

---

## Стр. 162

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
USINGCOMSOLMULTIPHYSICSTOSOLVEORDINARYDIFFERENTIALEQUATIONS 149
1
0.9
0.8
Fraction converted
0.7
0.6
0.5
0.4
0.3
0.2
0 0.2 0.4 0.6 0.8 1
Dimensionless axial position
(a)
750
740
730
Temperature (K)
720
710
700
690
680
670
0 0.2 0.4 0.6 0.8 1
Dimensionless axial position
(b)
FIGURE 8.3 SolutiontoproblemposedbyEqs.(8.24)–(8.26).(a)Fractionconverted;(b)tem-
perature.
WewishtosolvethisinitialvalueproblemusingComsolMultiphysics;sincethereareno
spacedimensions,theinitialvalueproblemisdesignatedasazero-dimensionproblem—
zerospacedimensions.
Step1(ChoosetheProblem) OpenComsolMultiphysicsandchoose“0D”intheModel
Wizard and click the next arrow (blue, at the top of the Settings window). Then click
Mathematics to expand the folder, expand the “Global ODEs and DAE interface folder,”
```

---

## Стр. 163

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
150 CHEMICALREACTORS
1
0.8
0.6
0.4
0.2
0
0 0.2 0.4 0.6 0.8 1
t
u
FIGURE 8.4 SolutiontoEq.(8.16)usingComsolMultiphysics.
andselect“GlobalODEsandDAEs(ge)”;clickthenextarrow.TheSettingswindowwill
havealistofoptions;select“TimeDependent”andthenclicktheFinishflag.
Step2(DefinetheEquation) Openthe“GlobalODEs”node(clickonthetrianglebefore
it)andclickon“GlobalEquations.”Inthesettingswindow,enteru,ut+10∗u,1.Thissays
thevariableiscalledu,theequationisEq.(8.28),andtheinitialconditionis1.0.
Step 3 (Solve the Problem) Click on the arrow before “Study 1” to expand the node
and then click on Step 1: “Time Dependent.” Change the Times from range (0:0.1:1) to
(0:0.01,1).Rightclickon“Study1.”
Step 4 (Plot the Solution) The plot should appear automatically. If not, choose Results
underModelBuilder;rightclicktoget“1DPlotGroup.”Ifthatalreadyexists,chooseit.
Clickon“1DPlotGroup”andintheSettingswindowchange“TimeSelection”fromAll
to“Fromlist”toseethelistoftvalues.Clickon“PlotGroup1”andsettheaxisandplot
settings.YouwillgetFigure8.4,whichisthesameasobtainedusingMATLAB,Figure8.1.
Step5(SavetheFigure) Tosavethefigure,clickonthecamera,clickonBrowse,givethe
figureaname,clickSave,andthenOK.
Example:IsothermalPlugFlowReactor
Theproblemissolvedintheoriginalcoordinates[molarflowratesandreactorvolumeIn
Eq.(8.2)sincethoseareconvenientlyincludedinComsolMultiphysics:
dF dF dF
A =−2kC2, B =kC2, C =0 (8.29)
dV A dV A dV
Step 1 (Choose the Problem) Open Comsol Multiphysics and select “0D” in the
Model Wizard; click the next arrow. Then select “Chemical Species Transport/Reaction
```

---

## Стр. 164

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
USINGCOMSOLMULTIPHYSICSTOSOLVEORDINARYDIFFERENTIALEQUATIONS 151
2
1.5
1
0.5
0
0 0.5 1 1.5 2 2.5
t
etar
wolf
raloM
F
C
F B
F
A
FIGURE 8.5 SolutiontoproblemposedbyEq.(8.21)–(8.22)usingComsolMultiphysics.
Engineering (RE)” and click the next arrow. Finally, choose “Stationary Plug Flow” and
click the Finish flag. If you do not have the Reaction Engineering Module, choose the
“GlobalODEs.”
Step2(DefinetheEquation) Clickon“ReactionEngineering”intheModelBuilder;in
the Settings window set the reactor type to plug flow and make the mixture for a liquid.
Keeptheflowratevas1asasimplificationinthisexample.ThenthemolarflowrateF =
A
vC =C .Rightclick“ReactionEngineering”again;thistimechooseReaction.Setthe
A A
chemicalreactionto2A⇒B,irreversible.TheprogramwillautomaticallyaddSpecies:A
and Species:B to “Reaction Engineering.” Set the forward rate constant kf to 0.6; set the
reactionratetokf_1∗c_Aifitisnotdoneautomatically.GotoSpecies:Aandsetthereaction
rateto−2∗r_1.ForSpecies:Bsetitto+r_1.Rightclickthe“ReactionEngineering”node
andaddaspecies,C.Theratesofreactionforthisspeciesarezero.Openthe“SpeciesFeed
Stream”nodeforeachspeciesandsetthevaluestoF_A=2,F_B=0,F_C=2.
Step 3 (Solve) Under Study 1, choose “Stationary Plug Flow” and change the range of
solution from 0:0.1:1 to 0:0.1:2.5. Solve the problem by choosing “Study 1” and right
clicking;choose=.
Step4(PlottheSolution) Theplotshouldappearautomatically.Ifnot,choose“Results”
underModelBuilder;rightclick“1DPlotGroup.”Ifthatalreadyexists,chooseit.Right
clickon“1DPlotGroup”andchooseGlobal.ThenclicktheploticonintheSettingspanel.
Youcanchangethelabelsforthex-andy-axishereunder“PlotSettings.”They-axislabel
ischangedto“Molarflowrate.”YouwillgetFigure8.5.
Step 5 (Save the Figure) To save the figure, click on the camera, click on Browse, give
thefigureaname,clickSave,andthenOK.YouseethatthesolutionshowninFigure8.5
looksthesameasobtainedusingMATLAB,Figure8.2.
Example:NonisothermalPlugFlowReactor
ConsidernexttheproblemposedbyEqs.(8.24)–(8.26).Becausetherearetwovariables,
youneedtwoequations.
```

---

## Стр. 165

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
152 CHEMICALREACTORS
FIGURE 8.6 Variables.
Step1(ChoosetheProblem) OpenComsolMultiphysicsandchoose“0D”intheModel
Wizardandclickthenextarrow.ThenclickMathematicstoexpandthefolder,expandthe
“GlobalODEsandDAEinterfacefolder,”andselect“GlobalODEsandDAEs(ge)”;click
thenextarrow.TheSettingswindowwillhavealistofoptions;select“TimeDependent”
andthenclicktheFinishflag.
Step 2 (Define Equation) Under the “Model 1” node, right click Definitions and select
Variables. In the settings window, create the Variables as shown in Figure 8.6. Expand
“GlobalODEsandDAEs”andclickon“GlobalEquations.”Setthetwoequationsasshown
inFigure8.7,whichagreewithEq.(8.24).TheinitialconditionsonXandTaresethere,too.
Step3(Solve) ExpandtheStudy1node,chooseTimeDependentandnotethattherange
ofsolutionisfrom0to1,asdesired.RightclickonStudy,=.
Step 4 (Plot) The plot should appear automatically. If not, choose Results under Model
Builder;rightclicktogetthe“1DPlotGroup.”Ifthatalreadyexists,chooseit.Clickonthe
arrowbefore“1DPlotGroup”andchooseGlobal.Thencreatetheexpressions toplotas
showninFigure8.8.Theresults(X,T,Rate,andK )areallscaledsothattheyappearon
eq
Figure8.9.The“x-AxisData”ischangedtoExpression,andsettot,sothatthedescription
can be changed to length. Since there are no units in this problem, click on “Plot Group
1”andremovethe“(s)”fromthex-axislabel.Itisusefultoseewhatpartofthereactoris
doing the most work and to see how the equilibrium constant changes with temperature,
whichchangeswithaxialposition.
FIGURE 8.7 Equations.
```

---

## Стр. 166

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
REACTORPROBLEMSWITHMOLECHANGESANDVARIABLEDENSITY 153
FIGURE 8.8 ExpressionstoplottoobtainFigure8.9.
REACTORPROBLEMSWITHMOLECHANGESANDVARIABLEDENSITY
The examples shown earlier are for liquid streams or dilute gaseous streams where the
densitydoesnotchangedrastically.Sometimesthedensitydoeschange,though,andsuch
problemsarenotmuchhardertosolvenumericallythantheirconstant-densitycounterparts.
ThegoverningequationisEq.(8.2),hereexpressedasadifferentialequation:
dF
j =r , j =1,...,3 (8.30)
j
dV
R
F isthemolarflowrateofthejthspecies,V isthevolumeofreactor(fromtheinlet),and
j R
r is the rate of reaction of the jth species. Let us take the same reaction, Eq. (8.18), and
j
reactionrate,Eq.(8.20).Puttingthesetogethergivesthedifferentialequationstobesolved:
dF dF dF
A =−2kC2, B =+kC2, C =0 (8.31)
dV A dV A dV
R R R
Theequationsaredifferentialequationsforthemolarflowrates,F ,F ,andF butthe
A B C
ratesofreactionareexpressedinconcentration,C .Itispossibletoderivetheconcentration
A
800
700
T
600
500
400
K
eq
300
200
300*X
100
3000*rate
0
0 0.2 0.4 0.6 0.8 1
Length
FIGURE 8.9 ResultsforSO reactor,Eqs.(8.24)–(8.26).
2
```

---

## Стр. 167

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
154 CHEMICALREACTORS
of each chemical from the molar flow rates, and this section illustrates how to do that in
MATLABandComsolMultiphysics.Inagasphase,thetotalconcentrationisgovernedby
theperfectgaslaw,althoughmorecomplicatedequationsofstatearepossible:
p
C = (8.32)
T
RT
Thus,atanypointinthereactor,ifyouknowthepressureandtemperature,youcanfindC .
T
Thepressureisdeterminedbyfluidmechanicsandthepressuredrop,andthetemperature
is determined by the energy equation. Then the concentration of a chemical is the mole
fractiontimesthetotalconcentration,forexample
C = x C , andthemolefractionis
j j T
F (8.33)
x = j , j =A,B,orC
j F +F +F
A B C
Ifthetemperatureandpressureareconstant,thetotalconcentrationisthetotalconcentration
attheinlet,whichistakenhereas5kmol/m3.Thus,theflowrateis
F +F +F = V˙C (8.34)
A B C T
Theproblemissummarizedhereas
dF dF dF
A =−2kC2, B =+kC2, C =0
dV A dV A dV
R R R
F (0)=2kmol/s, F (0)=0, F (0)=2kmol/s (8.35)
A B C
F
C = A C
A F +F +F T
A B C
The MATLAB program requires you to write a function (m-file) that calculates the
right-handside,giventheinput,whicharetheflowratesofallspecies.Thus,tosolvethe
problemyouwouldusethevariables
y(1)= F , y(2)= F , y(3)= F (8.36)
A B C
The function will have available to it the accumulated reactor volume V , and the local
R
valueofy(j),j=1,...,3atthesamereactorvolume.Youthencalculatetheconcentrations
atthatreactorvolumeusingEq.(8.37):
y(1)
C = C (8.37)
A y(1)+y(2)+y(3) T
The rates of reaction are then evaluated, and the function returns the numerical value of
theright-handside.YoucancompletethisexamplebydoingProblem8.7attheendofthe
chapter.
ThesameconsiderationsapplywhenusingComsolMultiphysics.Thevariablesbeing
solved for are now F , F , F . In Variables/Expressions/ you define equations for new
A B C
variables ca, cb, and cc representing Eq. (8.37), and then use the same reaction rate
```

---

## Стр. 168

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
CHEMICALREACTORSWITHMASSTRANSFERLIMITATIONS 155
expression(intermsofca).Therestofthesolutionproceedsasbefore:
ca=CT∗F /(F +F +F )
A A B C
cb=CT∗F /(F +F +F ) (8.38)
B A B C
cc =CT∗F /(F +F +F )
C A B C
CHEMICALREACTORSWITHMASSTRANSFERLIMITATIONS
When a reaction occurs on a catalyst particle, it is necessary for the reactants to get to
the catalyst. Sometimes this transfer is hindered by mass transfer, and then the concen-
tration near the catalyst is not the same as it is in the bulk stream. This phenomenon is
demonstrated with the problem posed in Eqs. (8.21)–(8.22), except that now the rate of
reactionisevaluatedataconcentrationthatisnearthecatalyst.TheconcentrationC isthe
s
concentrationonthesurface,expressedasthekmolofaspeciespervolumeofthecatalyst.
In your Chemical Reactor Design courses, you will learn various ways to represent this
concentration.Theneteffect,however,isthatEq.(8.21)ischangedtoEq.(8.39):
dC dC dC
u A =−2k C2 , u B =+k C2 , u C =0 (8.39)
dz
s A,s
dz
s A,s
dz
YouwillbesolvingforC (z),butyoucannotevaluatetherateofreactioninEq.(8.39)
A
becauseyoudonotknowC .Youneedamassbalancerelatingtherateofmasstransferto
A,s
thecatalysttotherateofreaction.OneformofthatisEq.(8.40),wherek isamasstransfer
m
coefficient in units of m/s, determined from correlations derived in fluid mechanics and
masstransfercourses,aisthesurfaceareaexposedpervolumeofthereactor(m2/m3),and
k isarateofreactionrateconstant(herem3/kmols).Otherformulationsarepossible,too:
s
k m a(C A −C A,s )=k s C2 A,s (8.40)
Looking closely at Eqs. (8.39)–(8.40) you can see that to solve the differential equations
in Eq. (8.39) you must solve Eq. (8.40) at every position z. Thus, this is a problem that
combinesordinarydifferentialequationswithnonlinearalgebraicequations.
MATLAB easily handles these kinds of problems. Basically, you call a routine to in-
tegrate the ordinary differential equations (e.g., ode45). You construct a right-hand side
function (m-file) to evaluate the right-hand side. The input variables are z and the three
concentrations, and the output variables are the three derivatives. Take C and solve
A
Eq. (8.40) using either “fzero” or “fsolve.” Then you have C at this location, z. You
A,s
canevaluatetheratesofreactioninEq.(8.39)andputthemintheoutputfromthem-file.
Step1 Youfirstconstructanm-filetoevaluateEq.(8.40).
% mass_rxn.m
% this m-file evaluates the mass transfer equations
% with a reaction
function y=mass_rxn(CAs,CA)
global k km
% the first entry is the guess of CAs and
% the second entry is the fluid concentration
y = km*(CA-CAs)-k*CAs*CAs;
```

---

## Стр. 169

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
156 CHEMICALREACTORS
Step2 Testthisfunctionbyusingthefevalfunction.
global k km
k = 0.3; km = 0.35
feval(@mass_rxn,0.6,0.5)
ans = -0.143
Thisiscorrect.
Step3 Next,testtheuseofthe“fzero”command.
CAguess = 0.5; CA = 0.5;
OPTIONS=[]
CAs = fzero(@mass_rxn,CAguess,OPTIONS,CA);
Theresultis0.37771,whichiscorrect.
Step 4 Next, construct an m-file, “rate1_mass.m”, to evaluate the right-hand sides of
Eq.(8.39).Thism-fileisalmostthesameasthatshownfollowingEq.(8.23),exceptthat
a global command is used so the parameters can be changed easily. The only significant
changetothism-filefromthatusedearlieristheuseof“fzero”tofindCAs,andthenusing
CAsratherthanCAtoevaluatetherateofreaction.
% rate1_mass.m
% This function gives the right-hand side for a
% reactor problem which is isothermal but has
% mass transfer effects
function ydot=rate1_mass(VR,y)
global k vel km
% y(1) is CA, y(2) is CB, y(3) is CC
CA=y(1);
% solve the mass transfer problem
% the first entry is the guess of CAs and
% the second entry is the fluid concentration
OPTIONS=[];
CAguess = CA;
CAs = fzero(@mass_rxn,CAguess,OPTIONS,CA);
rate = k*CAs*CAs;
ydot(1) = - 2.*rate/vel;
ydot(2) = + rate/vel;
ydot(3) = 0.;
ydot = ydot';
Step 5 The last m-file is the one to run the problem, which you do using the value
k a=0.2.Theonlychangestotheprogramrun_rate1followingEq.(8.23)are(a)theuse
m
of“global”tosettheparametersand(b)changingthenameoftheright-handsidefunction
fromrate1torate1_mass.
% run_rate1_mass.m
% This is the driver program to solve the simple flow reactor
% example.
```

---

## Стр. 170

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
CHEMICALREACTORSWITHMASSTRANSFERLIMITATIONS 157
global k vel km
k = 0.3; vel = 0.5; km = 0.2;
% set the initial conditions
y0 = [2 0 2]
% set the total volume of the reactor
zspan = [0 2.4]
% call the ode solver
[z y] = ode45(@rate1_mass,zspan,y0)
% plot the result
plot(z,y(:,1),'*-',z,y(:,2),'+-',z,y(:,3),'x-') % or plot(z,y)
xlabel('length (m)')
ylabel('concentrations (kgmol/mˆ3)')
legend('A', 'B', 'C')
Step6 Asacheck,yourunthisprogramwhilechangingthe“rate1_mass.m”programto
use
%CAs = fzero(@mass_rxn,CAguess,OPTIONS,CA);
rate = k*CA*CA;
insteadof
CAs = fzero(@mass_rxn,CAguess,OPTIONS,CA);
rate = k*CAs*CAs;
This has the effect of removing the mass transfer limitation, and the result should be
the same as shown in Figure 8.2, and it is the same. The code is returned to its proper
form, and the program “run_rate1_mass” calculates the output (see Figure 8.10). With
mass transfer resistance included, the outlet concentration of B is 0.61. When there was
no mass transfer limitation, the outlet concentration of B was 0.85. Thus, the reactor is
not able to produce as much product, and a bigger reactor is required. This same type of
2
1.5
1
0.5
0
0 0.5 1 1.5 2 2.5
Length (m)
3 )
m/lomgk(
snoitartnecnoC
A
B
C
FIGURE 8.10 SolutiontoEqs.(8.39)–(8.40)whenmasstransferisimportant.
```

---

## Стр. 171

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
158 CHEMICALREACTORS
problemcanarisewithmultipleconcentrationsorwithoneconcentrationandtemperature.
Thenyouwouldneedtoreplacethe“fzero”commandwiththe“fsolve”command(from
theOptimizationToolbox).Youmightneedtoexperimenttoprovidegoodinitialguesses
fortheconcentrationsandtemperatures,becauseEq.(8.40)wouldbeturnedintoasetof
nonlinearalgebraicequations,andthesolutionisverysensitivetothetemperaturevariable.
PLUGFLOWCHEMICALREACTORSINASPENPLUS
Thewater–gasshiftreactionwasstudiedinChapters4and6asanequilibriumreactor.Here
thesamereactorismodeledinAspenPlususingapackedbedwithakineticexpression,as
aplugflowreactor,butstillusingareactoratconstanttemperature.Thereactionis
CO+H O→CO +H (8.41)
2 2 2
Iftherateofreactionisr(mol/minm3)thenthefollowingequationcanbewrittenforeach
species.Thepositivevalueisusedfortheproductsandthenegativevalueisusedforthe
reactants:
dF
i =±r (8.42)
dV
ThereactionrateisobtainedfromChoiandStenger(2003)andKolavennuetal.(2006):
(cid:2) (cid:3)
p p
r =k exp(−E/RT) p p − CO2 H2 (8.43)
0 CO H2O
k
eq
Theparametersare
(cid:2) (cid:3)
4577.8
K =exp −4.33 (8.44)
eq
T
and
(cid:2) (cid:3)
mol 47.53kJ/mol
k exp(−E/RT)=6.195×108 − . (8.45)
0 atm2m3min RT
Thereactoristobeisothermalat450Kand1atm(1.013bar).Thus,themolefractionis
thesameasthepartialpressureinatmospheres.Thefeedratetothereactoris33kmol/min
(1992 kmol/h) half carbon monoxide and half water. A reactor volume of 0.25 m3 is
considered.Undertheseconditionsthereactionconstantis
mol kmol
k exp(−E/RT)=1882 =0.0314 (8.46)
0 m3/min m3/s
OpentheprogramandusetheunitRPLUGinReactors,withstreaminS1,andstream
out as S2. Insert the chemicals, and choose Peng–Robinson equation of state since that
is suggested as a good one (see Chapter 6). For stream S1, use 16.5 mol/min for carbon
```

---

## Стр. 172

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
PLUGFLOWCHEMICALREACTORSINASPENPLUS 159
monoxideand16.5mol/minforwater,asavaporat1.013bar(1atm)and450K.Inthere-
actorblock,inSpecifications,chooseReactoratconstanttemperature,atinlettemperature.
UndertheConfigurationtab,choosealengthof25mandadiameterof0.1129m;thenthe
cross-sectionalareais0.01m2 andthereactorvolumeis0.25m3.UndertheReactiontab,
createanewreactionsetbyrightclickingthe“availablereactionsets.”Itcreatesareaction
set R-1 and asks you what type of equation you wish to use. Since the reaction kinetics
is given in the form of Langmuir–Hinshelwood–Hougen–Watson (LHHW) formulation,
choose LHHW. Next,go totheReactions node and open it:thereaction setR-1isthere.
ClickonNewandcreatethestoichiometryofthereactioninthepop-upwindow.
Nowcomesthedifficultpart:definingthekineticswiththeproperunits.Clickthekinetic
tab.Makethereactingphaseavapor.ItishelpfultolookatthehelpdisplayforLangmuir,
whichissummarizedhere.Thereactionrateexpressionforafour-componentsystemisin
theform
(Kineticfactor)(drivingforceexpression)
Rate= (8.47)
(Adsorptionexpression)
Theformoftheseis
(cid:4) (cid:5) (cid:6) (cid:4) (cid:5)(cid:7)
T n E 1 1
Kineticfactor=k exp − − (8.48)
T R T T
0 0
We can make this agree with our expression by taking n = 0, T = 450, E = 0 and
0
k=0.0314.Enterthosevalues.Theunitsofkhavetobeinkmol/sm3,whicharealready
calculated. Next, consider the driving force expression; click on the Driving Force box.
Makethereactingphasevaporandmakemolefractionbetheconcentrationbasis.Ifitwere
somethingdifferentthevalueofkwouldhavetobeadjusted.Thetermisgoingtobe
(cid:8)N (cid:8)N
Drivingforce=k C α i −k C β i (8.49)
1 i 2 i
i=1 i=1
Forourcasewewant
y y
Drivingforce= y y − CO2 H2 (8.50)
CO H2O
K
eq
Sincetheconcentrationbasisismolefraction,theCsinEq.(8.49)aremolefractions.The
firstkis1.0andthesecondoneis1/K .Thestandardformoftheseksis
eq
B
lnk = A+ +ClnT +DT (8.51)
T
Thus,fork ,wewantA=B=C=D=0.Wealsowantforterm1(thefirsttermindriving
1
force)tohavea=1forbothCOandH O.Weachievethisbymakingsurethe“Enterterm”
2
says term1, choosing CO and H O and setting their coefficients to 1, keeping the others
2
zero,andkeepingallfourconstantsaszeroasshowninFigure8.11.Thenchange“Enter
term” to term2, the second term in Eq. (8.49). This time we set the coefficients of CO
2
andH to1,keepingtheothersaszero,andsettingk=1/K .Thus,wesetA=4.33and
2 eq
```

---

## Стр. 173

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
160 CHEMICALREACTORS
(a)
(b)
FIGURE 8.11 Drivingforce:(a)term1;(b)term2.
B=−4577.8.Finally,wesettheAdsorptionExpressionto1.0.Theadsorptiontermis
(cid:8)N
Adsorptionterm=1+ k C α i (8.52)
i i
i=1
Since we want this term to be one, we make all the k a small number. To do this we
i
activatecoefficientsforterms2through5andsetA =−1000.Onewaytocheckwhether
i
this has all been done correctly is to calculate the rate of reaction at the inlet conditions
and compare it with the computed result (as the slope of the mol/min vs. volume curve).
```

---

## Стр. 174

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
CONTINUOUSSTIRREDTANKREACTORS 161
FIGURE 8.12 Molefractionprofilesinwater–gasshiftreaction,usingAspenPlus.
NotethatinAspenonedoesnotneedtoworryaboutthefactthatthetotalnumberofmoles
changes(ifitdid)downthereactor—itishandledautomatically.
Theproblemcanthenbesolved.Thestream2givestheoutputconditions(450K,1atm,
0.127kmol/hofCO),butwealsowanttheprofilewithinthereactor,whichisavailablefrom
theReactorBlock/Profiles.ThetabulatedvaluesofmolefractionareshowninFigure8.12.
Thesearechangedtoconversion,whichisplottedinFigure8.13.Thesearenominallythe
sameasderivedinMATLAB.AspenPlushasanadvantageinthatitcalculatestheenergy
balanceandwillworkwithoutmuchadditionaleffortevenifthetemperatureischanging.
CONTINUOUSSTIRREDTANKREACTORS
Equation (8.15) gave the mass balance for a CSTR. A similar equation can be written
as an energy balance. This example considers a CSTR in which a first-order reaction
occurs, but the temperature also changes due to the heat of reaction. The equations to be
solvedare
Q
(1−c) =c exp[γ(1−1/T)]
V
R
(8.53)
Q
(1−T)=−β c exp[γ(1−1/T)]
V
R
Theleft-handsidesaretheflowratetimesaconcentrationortemperaturedifferencebetween
theinputandoutput,divided bythevolume.Theequations havebeen normalized bythe
inlet concentration and temperature. The right-hand sides are the rate of reaction and the
rateofenergygenerationduetoreaction,respectively.
```

---

## Стр. 175

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
162 CHEMICALREACTORS
1
0.8
0.6
0.4
0.2
0
0 5 10 15 20 25
Volume − (m) 3
noisrevnoC
FIGURE 8.13 Conversioninwater–gasshiftreaction,usingAspenPlus.
ThecasedescribedbyEq.(8.53)isforanadiabaticreactor.Whenthereactorisadiabatic,
theequationscanbecombinedbymultiplyingthefirstequationbyβ andaddingittothe
secondequation;thentheright-handsidevanishes:
β(1−c)+(1−T)=0 (8.54)
ThisequationcanbesolvedforT:
T =1+β(1−c) (8.55)
Nowthemassbalancecanbeconsideredasingleequationinoneunknown(c):
Q
(1−c)=c exp[γ(1−1/{1+β−βc})] (8.56)
V
R
SolutionUsingExcel
ThefirstsetofparametersusedisQ/V =8.7,β =0.15,γ =30.Thesimplespreadsheet
R
is shown in Figure 8.14; the cells are named and the names are used in the expressions.
Youcanuseeither“GoalSeek”or“Solver”tofindthevalueofcthatmakesthefunctionzero.
beta 0.15
gamma 30
flowvel 8.7
conc 0.731073
T 1.040339=1+beta*(1-conc)
rate 2.339659=conc*EXP(gamma*(1-1/T))
func on 0.000006=flowvel*(1-conc)-rate
FIGURE 8.14 SpreadsheetsolvingEq.(8.56).
```

---

## Стр. 176

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
CONTINUOUSSTIRREDTANKREACTORS 163
SolutionUsingMATLAB
MATLAB allows you to extend the method to more complicated situations when Excel
doesnotwork.
Step1 First,constructanm-filethatrepresentsEq.(8.56).
% rate_T
function fn=rate_T(c)
global beta gamma flowvol
T = 1 + beta*(1-c)
rate = c*exp(gamma*(1-1/T))
fn = flowvol*(1-c)-rate
Step2 Testitusingthecommands
>> global beta gamma flowvol
>> beta = 0.15; gamma = 30; flowvol = 8.7;
>> rate_T(0.5)
T = 1.0750
rate = 4.0547
fn = 0.2953
ans = 0.2953
Theansweriscorrect.
Step3 Tosolvetheproblem,typethefollowingcommandsintothecommandwindow.
>> fzero(@rate_T,0.5)
ans = 0.73107565193641
ThisisthesamesolutionasthatobtainedusingExcel,asexpected.
CSTRwithMultipleSolutions
For a different set of parameters, the CSTR can have more than one solution. For this
problem,thesolutionsliebetween0and1,becausetheconcentrationhasbeennormalized
bytheinletvalue,wherethenormalizedconcentrationis1.0,andthereactionusesupthe
material.Thesolutionyougetdependsupontheinitialguessofc.UseExceltosolvethe
problemwhenQ/V =25,β =0.25,keepingγ =30.Successivetrialsledtotheresults
R
showninTable8.1.
TABLE8.1 MultipleSolutionstoEq.(8.56)
WhenQ/V =25,β=0.25,γ =30
R
InitialGuessofc FinalResult
0 0.0863
0.5 0.5577
1.0 0.9422
```

---

## Стр. 177

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
164 CHEMICALREACTORS
Solutions to Multiple Equations Using MATLAB When two or more variables must be
found, as in Eq. (8.53), a solution can be found to make both the equations zero without
rearrangingtoproduceEq.(8.56).
Step 1 You can use the following MATLAB m-file along with the “fsolve” command
(availableintheOptimizationToolbox).
% rate_T2
function fn=rate_T2(y)
global beta gamma flowvol
c = y(1);
T = y(2);
rate = c*exp(gamma*(1-1/T));
fn(1) = flowvol*(1-c)-rate;
fn(2) = flowvol*(1-T)+beta*rate;
Step2 Testthem-filewiththefollowingcommands.
>> global beta gamma flowvol
>> beta = 0.15; gamma = 30; flowvol = 8.7;
>> feval(@rate_T2,[0.5 1.1])
ans = -3.29556351331856 0.27683452699778
Thisansweriscorrect.
Step3 Theninthecommandwindow,issuethefollowingcommands.
beta = 0.25; gamma = 30; flowvol = 25;
fsolve(@rate_T2,[0.0 1.25])
Withthisinitialguess,theprogramreturnsthefirstanswershowninTable8.1.Withan
initial guess of [0.5 1.125], it returns the second answer. With an initial guess of [1 1] it
returnsthethirdanswer.Suchproblemswouldnotalwaysconverge,andtheconvergenceis
harderforlargerβ andγ.Astheconvergencebecomesharder,itismoreandmorecrucial
toprovideareasonablestartingguess.
TRANSIENTCONTINUOUSSTIRREDTANKREACTORS
Reactorsdonotalwaysrunatsteadystate.Infact,manypharmaceuticalproductsaremade
in a batch mode. Such problems are easily solved using the same techniques presented
earlierbecausetheplugflowreactorequationsareidenticaltothebatchreactorequations.
Even CSTRs can be run in a transient mode, and it may be necessary to model a time-
dependent CSTR to study the stability of steady solutions. When there is more than one
solution,oneormoreofthemwillbeunstable.Thus,thissectionconsidersatime-dependent
```

---

## Стр. 178

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
TRANSIENTCONTINUOUSSTIRREDTANKREACTORS 165
CSTRasdescribedbyEq.(8.57):
dc(cid:2)
V = Q(c (cid:2)−c (cid:2) )−Vk c (cid:2) exp(−E/RT (cid:2) )
dt(cid:2) in 0
[φ(ρC ) +(1−φ)(ρC ) ]V
dT(cid:2)
=−(ρC ) Q(T (cid:2)−T (cid:2) ) (8.57)
p f p s dt(cid:2) p f in
+(−(cid:7)H )Vk c(cid:2)exp(−E/RT(cid:2))
rxn 0
Thevariablesareasfollow:
V =reactorvolume
Q=volumetricflowrate
c(cid:2)=concentration
T(cid:2)=temperature
t(cid:2)=time
k =reactionrateconstant
0
E=activiationenergy
φ=voidfraction
ρ =density
C =heatcapacitypermass
p
wheresubscriptfforfluid,sforsolid;−(cid:7)H istheheatofreactioninenergypermole.
rxn
Thenondimensionalformoftheseequationsis
dc
=(1−c)−cDaexp[γ(1−1/T)]
dt
(8.58)
dT
Le =(1−T)+βcDaexp[γ(1−1/T)]
dt
Theparametersaredefinedas
(cid:4) (cid:5)
c(cid:2) T(cid:2) Qt(cid:2) V E
c = , T = , t = , Da = k exp −
c(cid:2) T(cid:2) V Q 0 RT(cid:2)
in in in
(8.59)
φ(ρC ) +(1−φ)(ρC ) (−(cid:7)H )c(cid:2)
Le= p f p s, β = rxn in
(ρC ) (ρC ) T(cid:2)
p f p f in
TheparameterLeisaLewisnumber,anditincludestheheatcapacityofthesystem.The
DaisaDamko¨hlernumberandincludestherateofreaction.Theparametersaretakenas
β =0.15, γ =30, Da=0.115Le=1080, c(0)=0.7, T(0)=1 (8.60)
Step 1 To integrate these equations using MATLAB, you need an m-file to compute the
right-handside,andthenanm-filetocall“ode45.”Theright-handsidefunctionis
% rate_limit.m
% solve for particle with limit cycle
function ydot=rate_limit(t,y)
```

---

## Стр. 179

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
166 CHEMICALREACTORS
global beta gamma Damk Lewis Tin
c = y(1);
T = y(2);
rate = c*Damk*exp(gamma*(1 - 1/T));
ydot(1) = 1 - c - rate;
ydot(2) = Tin - T + beta*rate;
ydot(2) = ydot(2)/Lewis;
ydot = ydot';
Step2 Aftercheckingthiscodeyoucanrunitusingthefollowingm-file.
% run_rate_limit
global beta gamma Damk Lewis Tin
beta = 0.15; gamma = 30; Lewis = 1080 ; Damk = 0.115
Tin = 1
tic
[t y]=ode45(@rate_limit,[0 2],[ 0.7 1.0])
toc
plot(t,y(:,1),'*-k',t,y(:,2),'o-k')
xlabel('time')
legend('concentration','temperature')
TheresultisshowninFigure8.15.Itlooksasifsteadystateisachievedbythetimethat
t=2.However,thisisnottrue.Integratetot=1000andlookattheresultsinFigure8.16.
Itstillhasnotreachedsteadystate.Thereasonisthatthetemperaturerespondsmuchmore
slowlythandoestheconcentration.Thus,theconcentrationcomestoasteady-statevalue
appropriate to the current temperature, but then the temperature keeps changing and the
concentration must change to keep up. Notice the very rapid change of c from the initial
valueof0.7toabout0.875showninFigure8.17.Thisisbecausethevalueofc=0.7was
notappropriate foratemperature of 1.0.Inmathematical terms,thetimeresponse ofthe
1.05
1
0.95
Concentration
0.9 Temperature
0.85
0.8
0.75
0.7
0.65
0 0.5 1 1.5 2
Time
FIGURE 8.15 TransientCSTR,uptot=2,elapsedtime=0.0061s.
```

---

## Стр. 180

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
TRANSIENTCONTINUOUSSTIRREDTANKREACTORS 167
1.05
1
0.95
0.9
0.85
0.8 Concentration
Temperature
0.75
0.7
0.65
0 200 400 600 800 1000
Time
FIGURE 8.16 TransientCSTR,uptot=1000,elapsedtime=0.19s.
twovariablesisverydifferent(theeigenvaluesoftheequationarewidelyseparated),and
thesystemiscalledstiff.SeeAppendixEformorediscussionaboutstiffequations.
MATLABhassomesolversespeciallysuitedtostiffproblems.Youmerelychangefrom
“ode45”to“ode15s.”Whenintegratingtot=1000,yougetFigure8.17,butitonlytakes
0.016 seconds. Thus, the solution is 12 times faster. Since steady state still has not been
reached, integrate to t = 40,000. Figure 8.17 shows that steady state has been reached.
Nowthecomputationtimesare7.5sfor“ode45”and0.026secondsfor“ode15s,”giving
“ode15s” a speed-up factor of over 290. The difference is made more dramatic if you
removethe[ty]=infrontofthecalltoode45andode15s.Thenthesolutionisplottedas
itiscalculated,andthedifferenceinspeedisveryapparent.
NextchangetheparameterLefrom1080to0.1andintegratetot=100using“ode15s.”
1.05
1
0.95
Concentration
0.9 Temperature
0.85
0.8
0.75
0.7
0.65
0 1 2 3 4
Time x 104
FIGURE 8.17 TransientCSTR,uptot=40,000,elapsedtime=0.026s.
```

---

## Стр. 181

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
168 CHEMICALREACTORS
2.5
2
1.5
1
0.5
0
0 20 40 60 80 100
Time
FIGURE 8.18 TransientCSTR,Le=0.1,integrationtot=100.
Step1 Thecodeisshownbelow.
% run_rate_limit
global beta gamma Damk Lewis Tin
beta = 0.15; gamma = 30; Lewis = 0.1; Damk = 0.115; Tin = 1
tic
[t y]=ode15s('rate_limit',[0 100],[ 0.7 1.0])
toc
plot(t,y(:,1),'-k',t,y(:,2),'-k')
xlabel('time')
pause
plot(y(:,1),y(:,2),'-k')
xlabel('concentration')
ylabel('temperature')
ThesolutionisshowninFigure8.18.Thepatternseemstoberepeatedoverandover.
If the temperature is plotted versus the concentration at the same time, the repeated
pattern is very apparent (see Figure 8.19). This problem exhibits what is called a limit
cycle.Thisisalsoaniceproblemtorunwithoutthe[ty]=infrontoftheode15s;thenyou
seethesolutiondevelopbeforeyoureyes.
CHAPTERSUMMARY
Inthischapterequationswerederivedfordifferentreactors:plugflow,batch,andCSTR.
You learned how to integrate ordinary differential equation using MATLAB, and then
applied those skills to reactor problems in plug flow reactors (both isothermal and non-
isothermal).YoualsolearnedtodothesamethingusingComsolMultiphysics,AspenPlus,
and,forsimpleproblems,Excel.
Complications arose when the moles or total concentration changed, or when mass
transfer effects were important, and you learned how to incorporate those complications.
```

---

## Стр. 182

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 169
2.5
2
1.5
1
0 0.2 0.4 0.6 0.8
Concentration
erutarepmeT
FIGURE 8.19 LimitcycledisplayofFigure8.18.
Finally,CSTRswerestudiedusingbothMATLABandExcelincaseswherethesolutionis
steady,wheremultiplesteadysolutionsexist,andyoulearnedtouseMATLABwhenthe
solutionistime-dependentandtheproblemisstiff,leadingtolimitcycles.
PROBLEMS
8.1 Solve for the concentration distribution in a plug flow reactor governed by the
1
followingequations.(a)UseMATLABand(b)useComsolMultiphysics:
dc
Q =−R(c), c(0)=c (8.61)
in
dV
R
kc
R(c)≡ , Q =50, c =2, V =2000=totalvolume,
c+υ in
k =0.198, υ =3.8. (8.62)
8.2 Solve for the concentration distribution in a plug flow reactor with the following
1
reaction rate expression and parameters. (a) Use MATLAB and (b) use Comsol
Multiphysics:
kc
R(c)≡ , Q =2.2,c =1, V =50=totalvolume,
(1+K c)2 in
1
k =2, K =4. (8.63)
1
8.3 ACSTRisgovernedbythefollowingequation
1
Q(c−c )=−VR(c) (8.64)
in
(a) Solveforcwhen
kc
R(c)≡ ,Q =50,c =2,V =2000,k =0.198,ψ=3.8.
c+υ in
```

---

## Стр. 183

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
170 CHEMICALREACTORS
(b) Solvewhen
kc
R(c)≡ ,Q =2.2,c =1,V =50,k+2,K =4.
(1+K c)2 in 1
1
8.4 The problem posed by Eqs. (8.21)–(8.22) can be solved for a CSTR, too. In that
1
case,theequationismultipliedbythecross-sectionalareaofthepipetoobtain
dC dC dC
u A =−2k C2 →uA A =−2kC2 → Q A
dz s A dAz A dV
R
=−2kC2 A → Q(C A −C A,in )=−2VkC2 A (8.65)
Takethecross-sectionalareaas0.001m2 andsolveforthesameconditionsasin
Eq.(8.22).
8.5 Thegrowthrateforcellsinabioreactorcanfollowavarietyofgrowthequations.
1
Monod kinetics is represented by Problem 8.3(a). A substrate-inhibition growth
rateisgivenby(seeShuler(1988))
μ S
Growthrate= m (8.66)
K +S+S2/K
s I
whereμ isthemaximumspecificgrowthreactionrate;K isthemonodconstant,
m s
K is the inhibition constant, and S represents the substrate concentration (the
I
materialbeingreacted).TheequationgrowingcellsinaCSTRis
μ S
Q(S−S )=−V m (8.67)
in K +S+S2/K
s I
Innondimensionalformthisis
σ
(σ −1)=−Da ,
ω+σ +εσ2
where
Vμ K S
Da = m, ω= s, ε = in (8.68)
QS S K
in in I
SolvethisproblemforDa=1.19,ω=3.5610−3,ε=2.53.(Hint:lookformultiple
solutions.)SeeSchmidt(2005)andFogler(2010)foradditionalinformationabout
biologicalreactors.
8.6 Solve the same Problem 5 with the CSTR replaced by a plug flow reactor. The
1
equationsarethen
dσ σ
=−Da , z =0→3, σ(0)=1 (8.69)
dz ω+σ +εσ2
8.7 SolveEq.(8.35)usingMATLABforatotalvolumeof1.2m3,k =0.3m3/(kmol
1
s),atotalconcentrationof5kmol/m3.
```

---

## Стр. 184

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 171
8.8 Ammoniaundergoesareactionwithoxygeninthepresenceofaplatinumcatalyst
1
to form nitric oxide and water. The reaction is carried out in a microreactor (see
Chapter11),whichresultsinaconstanttemperature.Thereactionis
NH + 5O →NO+ 3H O (8.70)
3 2 2 2 2
The reaction occurs on the surface of a tube in the microreactor as governed by
the following rate of reaction (in gmol/cm2) (Pignet and Schmidt, 1975). The
partialpressuresareintorrandthetotalpressureismaintainedat0.115torr(asan
approximation).Therateisingmol/cm2s:
r = A , A≡3.4×10 −8exp(21,700/RT)p p1/2
NH3 B×C NH3 O2
B
≡1+8×10−2exp(4400/RT)p1/2 (8.71)
O2
C ≡1+1.6×10−3exp(25,500/RT)p
NH3
The inlet stream contains ammonia and oxygen with partial pressures of 0.046
and 0.068 torr, respectively, and the flow rate is 100 L/h. Solve the problem
for a temperature of (a) 473 K; (b) 673 K and compare the results. The micro-
reactor channel is 40 × 300 μm, and its length is 1 cm. The governing
equationsare
dF
i = Pvr , F(0)= F (8.72)
dz
i NH3 i i0
wherev isthestoichiometriccoefficientofithspecies;Pistheperimeterincm;F
i i
istheflowrateofithspeciesingmol/s;F istheflowrateofithspeciesatinletin
i0
gmol/s.
Inaddition,
(cid:9)N
F
F = F, y = i , p = y p (8.73)
T i i i i T
F
i=1 T
8.9 When an enzyme is immobilized on a surface, there may be a mass transfer
1
resistancethatlimitstheconcentrationofthereactingspeciesonthesurface.The
followingproblem(fromShuler,1988)findstheconcentrationofsubstrateonthe
surface when there is a reaction accompanied by mass transfer resistance. The
Michaelis–Mentenreactiononasurfaceisgovernedby
k S
rateofreaction= 0 (8.74)
S+K
m
The equation for reaction at a surface with mass transfer limitations approaching
thesurfaceis
εk S
k (S −S)= 0 (8.75)
L f S+K
m
```

---

## Стр. 185

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
172 CHEMICALREACTORS
wherek isthemasstransfercoefficient=10−3cm/s;K isthekineticconstant=
L m
10−4 mol/L; k is the kinetic constant = 5 × 10−4 mol/s mg enzyme; ε is the
0
enzymeloading=1.6×10−4 mgenzyme/cm2;S istheexternalconcentration=
f
10−4–10−2 mol/L;Sistheconcentrationatsurfaceinmol/L.
SolveforSwhentheexternalconcentrationis(a)10−4mol/Land(b)10−2mol/L
8.10 The steady-state model for a nonisothermal CSTR representing a catalytic con-
1
verteris
QC (y −y)=αVr(y,T)
tot in
QC MˆC (T −T )=αV(−(cid:7)H )r(y,T)
tot pg in rxn
0.05k y
r = 1 , k =6.701010exp(−12556/T),K =65.5 exp(961/T)
T(1+K y)2 1 1
1
(8.76)
Thereactionrateexpressionisgivenforoxidizingcarbonmonoxideonacatalytic
surface.WhentheinletmolefractionCOisy =0.02,andtheinlettemperatureis
in
T =600K,findthesolutiontotheseequations.TheparametersareQ=0.06555
in
m3/s,C =0.0203kmol/m3,α=26,900m2/m3,V=610−4m3,Mˆ =30kg/kmol,
tot
rinkmol/m2s,C =1070J/kgK,−(cid:7)H =2.84108 J/kmol.
pg rxn
8.11 SolvetheprobleminEq.(8.53)butforaplugflowreactorinsteadoftheCSTR.
1
dc
Q =−c exp([γ(1−1/T)]), c(0)=1
dV
R
(8.77)
dT
Q =βc exp([γ(1−1/T)]), T(0)=1
dV
R
IntegratefromV /Q=0to0.115withβ =0.15,γ =30.Comparetheconversion
R
tothatachievedwithaCSTR.
8.12 RepeatProblem11butwithV /Q=0to0.3withβ =0.25,γ =30.
1 R
8.13 GrowthofcellsinatransientCSTRisgovernedby
1
dσ σ
=1−σ −Da , σ(0)=σ (8.78)
dt ω+σ +εσ2 0
Fortheparametersω=3.5625×10−3,ε=2.5216,Da=1.1905,integratetot=
24forthefollowinginitialconditionsforc :(a)1;(b)0;(c)0.146019;(d)0.142;
0
(e)0.150.Discuss.
8.14 Duringthecureofanepoxyinaprepregoperationtomakepolymericcomposites,
1
theextentofreaction,α,issometimesmodeledwiththeequation
dα
=(1+aαm)(1−α)n, α(0)=0 (8.79)
dt
wherea=3,m=0.5,n=0.7.Solvethisequationasafunctionoftime.
```

---

## Стр. 186

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 173
8.15 Problem8.10isconsideredasatransientCSTR.Theequationsgoverningitare
1
dy
εVC = QC (y −y)−αVr(y,T)
tot tot in
dt
(cid:10) (cid:11)
dT
V ερ C +(1−ε)ρ C = QC MˆC (T −T)+αV(−(cid:7)H )r(y,T)
g pg s ps tot pg in rxn
dt
(8.80)
Theadditionalparametersare
C =1070J/kgK, C =1000J/kgK, ε =0.68
pg ps
ρ =C Mˆ =0.609kg/m3, ρ =2500kg/m3
g tot s
Initiallytheinletmolefraction(ofcarbonmonoxide)is0.01andtheinlettemper-
atureis600K.Integratetheseequationsunderthefollowingconditions:
t <1s: y =0.01, T =600K
in in
1<t <2s:inletconditionsincreaselinearlyto
(8.81)
y =0.03, T =700K
in in
2<t s: y =0.03, T =700K
in in
ThismodelcanbeusedtostudytheentireFederalTestCyclecoveringmanyhours
ofoperationofthecatalyticconverter.
8.16 Project.Thewater–gasshiftreactionwasmodeledinthetextusingAspen.Model
itusing(a)MATLABand(b)Comsol.
8.17 The catalytic converter on your car is made from a honeycomb of ceramic, in
2
which the gases flow down a tiny tube (about 1 mm2 cross section). The catalyst
isdepositedonthewallsofeachtube,andthatiswherethereactiontakesplace.
Considerhereaverymuchsimplifiedmodel;inrealityonemustsolvefortheflow
of mass and energy in the tube (without reaction), transfer between the fluid and
thewall(usingmassandheattransfercoefficients)withreactiononthewall.The
solid temperature and fluid temperature are not generally the same, but for this
simpleexampleweassumetheyare.Thisessentiallyassumesthattheinterchange
of mass and heat between the fluid and solid is instantaneous. More information
and examples are available (Young and Finlayson, 1976a, 1976b; Finlayson and
Young,1979;seealsowww.faculty.washington.edu/finlayso).Theequationsarea
plugflowversionofproblem8.10:
dy dT
QC =−αr, QC MˆC =α(−(cid:7)H )r, y(0)= y , T(0)=T
tot tot pg rxn 0 0
dV dV
(8.82)
The parameters are the same as in problem 8.10. Integrate these equations using
MATLAB when the inlet mole fraction is 0.02 and the inlet temperature is 600,
550, and 500 K. If the temperature is low, does the converter work? This is the
essenceofthe“firsttwominute”problemforreducingautomobilepollution.Once
```

---

## Стр. 187

```text
P1:OTA/XYZ P2:ABC
JWBS084-c08 JWBS084-Finlayson May26,2012 14:11 PrinterName:YettoCome Trim:7in×10in
174 CHEMICALREACTORS
theconverteriswarm,thepollutionisveryslight.Ithasbeenestimatedthatover
95%ofthetotalpollutionfromanautomobilecomesoutduringthistimewhenthe
converteriswarmingup.
8.18 Project.Beltrami(2002)andGray(2006)postthefollowingproblemrepresenting
the dynamics of two competing populations of bacteria. The variables are the
populationdensitiesofeachspecies.Theterminparenthesescapthegrowthdueto
limitationsintheenvironment,andthelasttermrepresentsthenegativeeffectsof
competitionbetweenthespecies.Thefirsttermestablishesthepopulationdensity
ifonlyonespecieswerepresent.Thesecondtermisproportionaltothenumberof
interactions between the species and represents the decline in population density
duetocompetition:
(cid:12) (cid:13) (cid:12) (cid:13)
dx x dx x
1 =9x 1− 1 −2x x , 2 =6x 1− 2 −x x (8.83)
1 1 2 2 1 2
dt 9 dt 12
(a)Determineallfoursteady-statesolutions.(b)Integratefromthefollowingpoints
tosteadystate:(x ,x )=(3,1),(7,4),(0,0),(0.01,0),(5,2),(5.01,2).(c)Writethe
1 2
solutionasasteadysolutionplusaperturbationandlinearizetheequationsforsmall
perturbations.Theright-handsidecanthenberepresentedbyamatrix.Determine
theeigenvaluesforeachofthesteadystates.
NumericalProblems(SeeAppendixE)
8.19 Solvetheproblemonpage144forCAandCBusinganEulermethodprogrammed
2
inMATLAB.Comparetheexitconcentrationsasafunctionofmeshsize,usingat
leastthreemeshsizesdifferingbyafactorof2.
8.20 Solve the problem on page 146 for SO and temperature using an Euler method.
2 2
Comparetheexitconcentrationandtemperatureandpeaktemperatureasafunction
ofmeshsizefor50,100,and200steps.
8.21 SolvetheprobleminFigure8.14usingtheNewton–Raphsonmethod.
1
8.22 Project.SolvetheProblem8.19byusingthesecond-orderRunge–Kuttamethod
programmedinExcel.Solvethreetimes,eachwithadifferentstepsizein(cid:7)z:0.2,
0.1,0.05.Comparetheaccuracyasthestepsizedecreases:doestheerrordecrease
with(cid:7)z2?
```

---

## Стр. 188

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
9
TRANSPORT PROCESSES
IN ONE DIMENSION
Chemicalengineeringprocessesinvolvethetransportandtransferofmomentum,energy,
andmass.Momentumtransferisanotherwordforfluidflow,andmostchemicalprocesses
involve pumps and compressors,and perhaps centrifuges and cyclone separators.Energy
transferisusedtoheatreactingstreams,coolproducts,andrundistillationcolumns.Mass
transferinvolves theseparation of amixture of chemicals intoseparate streams,possibly
nearlypurestreamsofonecomponent.Thesesubjectswereunifiedin1960inthefirstedition
oftheclassicbook,TransportPhenomena(Birdetal.,2002).Thischaptershowshowto
solvetransportproblemsthatareonedimensional,thatis,thesolutionisafunctionofone
spatialdimension;Chapters10and11treattwo-dimensional(2D)andthree-dimensional
(3D)problems.Theone-dimensional(1D)problemsleadtodifferentialequations,which
aresolvedusingthecomputer.
Diffusionproblemsinonedimensionleadtoboundaryvalueproblems.Theboundary
conditionsareappliedattwodifferentspatiallocations:atoneside,theconcentrationmay
be fixed and at the other side the flux may be fixed. Because the conditions are specified
attwodifferentlocationstheproblemsarenotinitialvalueincharacter.Itisnotpossible
to begin at one position and integrate directly because at least one of the conditions is
specified somewhere else and there are not enough conditions to begin the calculation.
Thus, methods have been developed especially for boundary value problems. There is a
baseballanalogythatillustratesthedifference.Ifyouareatbatandthereisnooneonbase,
youcanhitandrunasfastasyoucan.Thisislikeaninitialvalueproblem.Ifyouareatbat
andsomeoneisonthefirstbase,youcanhit,butthewayyourunisinfluencedbywhatthe
runneraheadofyoudoes.Thisislikeaboundaryvalueproblem.
This chapter illustrates heat transfer, diffusion, diffusion with reaction, and flow in
pipes,consideringsteadyandunsteadyprocesses.Mostoftheproblemsaresolvedusing
IntroductiontoChemicalEngineeringComputing,SecondEdition.BruceA.Finlayson.
©2012JohnWiley&Sons,Inc.Published2012byJohnWiley&Sons,Inc.
175
```

---

## Стр. 189

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
176 TRANSPORTPROCESSESINONEDIMENSION
Comsol Multiphysics, which is easy to use for these applications, but some are solved
withMATLABandExcel.Detailsofthefiniteelementandfinitedifferencemethods are
notgivenhere,butyouwillfindabriefdescriptioninAppendixE,alongwithreferences.
In essence, you represent the solution at a set of grid points (finite difference) or nodal
points(finiteelement).Thisisanapproximation,sotheanswerisonlyasgoodasthemesh
allowsittobe,andtheaccuracyisnotguaranteed.Thus,youhavetosolvetheproblemon
morethanonemeshtoensurethattheresultsdonotdependappreciablyonthemesh.The
solutionisexactonlyifyouuseaninfinitenumberofpoints,whichnoonehaseverdone.
However,youcanusuallymakeitasaccurateasneeded,andtheComsolMultiphysicsand
MATLABsoftwaremakesitveryeasytoresolvetheproblemonabettermeshsothatyou
can testthe accuracy. Afew numerical problems are provided that use Excel and require
diggingintothecomplexitiesofthenumericalmethods.
InstructionalObjectives: Afterworkingthroughthischapter,youwillbeableto
1. Modelheattransfer,diffusionandreaction,andfluidflowinone-dimensionalsitua-
tionslikethoseoccurringinyourtextbooks.
2. SolveboundaryvalueproblemsbyusingMATLAB,ComsolMultiphysics,andExcel,
forcomparison.
3. Solvelinearproblemsthatyoucancomparewithsolutionsinyourtextbooks.
4. Solve nonlinear problems that are not solvable with analytical methods and are
probablynotinyourtextbooks.
5. PracticeusingComsolMultiphysicsinpreparationforChapters10and11.
6. solveproblemsinwhichconvectiondominatesoverdiffusiontoillustratetheoscil-
lationsthatcanoccurandhowtominimizethem.
APPLICATIONSINCHEMICALENGINEERING—MATHEMATICAL
FORMULATIONS
HeatTransfer
Consider steady heat transfer across a slab of material that extends infinitely in two
directions and has thickness L. In the thin direction, x, the equation for steady heat
conductionis
(cid:2) (cid:3)
d dT
k(T) = Q
dx dx (9.1)
T(0)=T , T(L)=T
0 L
Thetemperature,T,isafunctionofposition,x.Noticethatoneconditionisatx=0andthe
otheratx=L.Thismakesitatwo-pointboundaryvalueproblem.Thethermalconductivity
kcandependontemperature,andwhenitdoes,theproblemisnonlinear.Therateofenergy
generationisQ.
```

---

## Стр. 190

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
APPLICATIONSINCHEMICALENGINEERING—MATHEMATICALFORMULATIONS 177
DiffusionandReaction
DiffusionacrossaflatslabisverysimilartoEq.(9.1):
(cid:2) (cid:3)
d dc
D =0
dx dx (9.2)
c(0)=c , c(L)=c
0 L
wheretheconcentration,c,isafunctionofposition,x.Thediffusivity,D,candependupon
concentration.Thisisalsoatwo-pointboundaryvalueproblembecausetheconcentration
isspecifiedatbothx=0andx=L.
Manychemicalreactionstakeplaceinsideacatalystpellet,whichisaporousmaterial
(suchasAl O impregnatedwiththecatalyst,usuallymetalsofvariouskinds).Theequation
2 3
forasphericalcatalystpelletwithradiusR is
p
(cid:2) (cid:3)
1 d dc
D r2 = R(c)
r2dr e dr
(9.3)
dc
(0)=0, c(R )=c
p R
dr
whereD isaneffectivediffusivityforthediffusionofmassinsidetheporouscatalyst.The
e
concentration,c,isafunctionofradialposition,r.Thereactionratecanhaveavarietyof
forms,alldependingonconcentration:
αc
R =c, R =c2, R = (9.4)
1+Kc
Inmostcases,thisproblemisnonlinear.Again,thisproblemisatwo-pointboundaryvalue
problem because the boundary conditions are at two different spatial positions. At r = 0
thereisnoflux(centerofthepellet),andatr=R theconcentrationtakesaspecifiedvalue
p
equaltotheexternalconcentration.
Whenthereisaheatofreaction,thetemperatureincreasesduetothereaction.Inthat
case, you have to also solve an energy balance on the catalyst pellet. A typical energy
balanceis
(cid:2) (cid:3)
1 d dT
k r2 =(−(cid:3)H )R(c,T)
r2dr e dr rxn
(9.5)
dT
(0)=0, T(R )=T
p R
dr
The temperature, T, is a function of radial position, r, and k is an effective thermal
e
conductivityand−(cid:3)H istheheatofreaction.Again,thereisnofluxatthecenter,and
rxn
thetemperatureattheouterboundaryissetatT .Nowthereactionratedependsonboth
R
concentrationandtemperature[andEq.(9.3)hastobewrittenwithR(c,T)].Suchproblems
canbeverydifficultduetotherapidchangeinthekineticconstantswithtemperature,and
theyprovideaseveretestofanynumericalmethod.
```

---

## Стр. 191

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
178 TRANSPORTPROCESSESINONEDIMENSION
r
2R v(r)
L
FIGURE 9.1 Fullydevelopedpipeflow.
FluidFlow
ConsidertheflowofaNewtonianfluidinapipe,asillustratedinFigure9.1.Thegoverning
differentialequationis(Birdetal.,2002)
(cid:2) (cid:3)
1 d dv (cid:3)p
rμ =−
r dr dr L
(9.6)
dv
(0)=0, v(R)=0
dr
where r is the radial position from the center of the pipe of radius R, v is velocity in the
axialdirection,μistheviscosity,(cid:3)pisthepressuredropalongthepipe,andListhelength
over which the pressure drop occurs. The boundary conditions are at different locations,
makingitatwo-pointboundaryvalueproblem.ThesolutiontothisproblemisEq.(9.7):
(cid:2) (cid:3)
1 (cid:3)p R2 r2
v = 1− (9.7)
μ L 4 R2
When solving the problem analytically, it is also possible to use a boundary condition at
r=0thatsaysthevelocityisfinite.Bothconditionsgivethesameresult,andinfactone
canbederivedfromtheother.Notethat(cid:3)pisapositivenumber.
Inpipeflow,theaveragevelocityisdefinedbyEq.(9.8):
(cid:4)Rp
v(r)rdr (cid:5)Rp (cid:5)1
2 r
<v >= 0 = v(r)rdr =2 v(r (cid:2) )r (cid:2) dr (cid:2), where r (cid:2) = (9.8)
(cid:4)Rp R2
p
R
p
rdr 0 0
0
Note the rdr in the integrand, which is necessary because cylindrical polar coordinates
are used. The relationship between the average velocity and the pressure gradient can be
obtainedbyintegratingEq.(9.7)usingEq.(9.8);itistheHagen–Poiseuillelaw.Thepeak
velocityistwicetheaveragevelocityinpipeflow:
(cid:2) (cid:3)
1 (cid:3)p R2 (cid:3)p D2
<v >= = (9.9)
μ L 8 L 32μ
```

---

## Стр. 192

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
APPLICATIONSINCHEMICALENGINEERING—MATHEMATICALFORMULATIONS 179
When the flow is between two wide, flat plates instead of inside a cylinder, Eq. (9.6)
becomes
(cid:2) (cid:3)
d dv (cid:3)p
μ =−
dx dx L
(9.10)
dv
(0)=0, v(H)=0
dx
Theplatesaretakenatadistance2Hapart.Thesolutionis
(cid:2) (cid:3)
1 (cid:3)p H2 x2
v = 1− (9.11)
μ L 2 H2
Nowtheaveragevelocityis
(cid:4)H
v(x)dx (cid:5)H (cid:5)1
1 x
<v >= 0 = v(x)dx = v(x (cid:2) )dx (cid:2), where x (cid:2) = (9.12)
(cid:4)H H H
dx 0 0
0
andtherelationshipbetweenaveragevelocityandpressuredropis
1 (cid:3)p H2
<v >= (9.13)
μ L 3
Thepeakvelocityis1.5timestheaveragevelocityforflowbetweenparallelplates.These
formulasareprovidedherebecausetheyprovideagoodbenchmarkagainstwhichtocheck
anynumericalsolutionbyintegratingoverboundaries.
Whenthefluidisnon-Newtonian,itmaynotbepossibletosolvetheproblemanalytically.
Forexample,fortheBird–Carreaufluid(Birdetal.,1987,p.171)theviscosityis
η
η= (cid:6) (cid:2)
dv
0 (cid:3)
2
(cid:7) (1−n)/2 (9.14)
1+ λ
dr
Theviscositydependsontheshearrate,dv/dr.Newparametersareintroducedthatmust
bedeterminedfromexperiments:η ,λ,andn.Nowtheboundaryvalueproblemis
0
(cid:2) (cid:3)
1 d dv (cid:3)p
rη =−
r dr dr L
(9.15)
dv
(0)=0, v(R)=0
dr
Itisnotpossibletosolvethisequationanalyticallyforv,exceptforspecialvaluesofη.For
problemssuchasthis,numericalmethodsmustbeused.Ifyousetη=μyougetthesame
problemdefinedearlierforaNewtonianfluid.
```

---

## Стр. 193

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
180 TRANSPORTPROCESSESINONEDIMENSION
UnsteadyHeatTransfer
Considerthefollowingheattransferproblemcorrespondingtoheattransferinaslab,
∂T ∂2T
=α (9.16)
∂t ∂x2
The temperature depends both on time, t, and on position, x. The coefficient of thermal
diffusionis
k
α = (9.17)
ρC
p
Theslabisinsulatedattheleft(x=0)andhasthetemperaturevalueofzeroattheother
side(x=L)
∂T
(x =0)=0, T =0 at x = L (9.18)
∂x
whiletheinitialtemperaturedistributionis
T(x,0)= f(x) (9.19)
YouthusstartwithT (x,0)andfindT (x,t)asafunctionofxfrom0toLandtfrom0to
infinity.
INTRODUCTIONTOCOMSOLMULTIPHYSICS
Inthischapter,step-by-stepinstructionsareprovidedforthese1Dproblems.Manyfeatures
ofComsolMultiphysicsarenotusedorneededuntilyousolve2Dand3Dproblems,and
thesefeaturesareexplainedinChapters10and11andAppendixD.Fortheboundaryvalue
problemstreatedhere,wegenerallyfollowthesesteps:
1. OpenComsolMultiphysicsandchoosethedimensionsoftheproblem(here1)and
thephysicsmoduleswewishtosolve.
2. Establishourpreferences.
3. Createthegeometry.
4. Insertthevariablesthatdefinetheproblemandsettheboundaryconditions.
5. Createamesh.
6. Solvetheproblem.
7. Examinethesolution;herewelimitourselvestoplotsandintegralsofthesolution.
The icons shown inFigure 9.2areones thatareused frequently intheseexamples. They
areworthremembering.
```

---

## Стр. 194

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:HEATTRANSFERINASLAB 181
next finish show geometry/mesh build plot expressions range of parameters
FIGURE 9.2 Iconsusedforsetup:next,finish,show;geometry/mesh:build;plot:expression,plot;
rangeofparameters.
EXAMPLE:HEATTRANSFERINASLAB
SolutionUsingComsolMultiphysics
Considertheproblemofheattransferinaslabwithnointernalheatgenerationbutwitha
thermalconductivitythatvarieslinearlywithtemperature—Eq.(9.1)withk=1+T.
(cid:8) (cid:9)
d dT
(1+T) =0
dx dx (9.20)
T(0)=0, T(1)=1
TheboundaryconditionsaretakenasT =0atx=0andT =1atx=1.
Step 1 (Open and Choose Physics) Open Comsol Multiphysics and choose 1D in the
ModelWizardandclickthenextarrow.Thenclickonthearrowbefore“HeatTransfer”to
openthatfolder.Choose“HeatTransferinSolidsht”andclickthenextarrow.TheSettings
windowwillhavealistofPresetoptions;selectStationaryandthenclicktheFinishflag.
ThenodesattheleftofthescreenarecalledtheModelBuilderandtheyprovideaguideto
thenecessarysteps(Figure9.3).
Step2(SetPreferences) WewillinturnusetheModel1,Study1,andResultsnodes.Note
theiconsatthetop,right.Thesecondonefromtheleftisto“show”additionalthings,and
wechoose“Discretization”and“EquationView.”Intherootnodewecanchooseasystem
ofdimensionsinthesettingswindow;choose“none.”
Step3(Geometry) OpentheModel1nodebyclickingonthearrowtothelefttoexpand
thisnode(Figure9.4).ThenrightclickontheGeometrysubnodeandchooseInterval.The
defaultintervaliszerotoone,whichiswhatwewant,soweacceptitbyclickingonthe
“build”iconatthetopofthesettingswindow.
Step 4 (Define the Problem) Withthe Model 1 node open, click on the arrow to the left
of the Heat Transfer node and choose Heat Transfer in Solids. Then click on the arrow
FIGURE 9.3 Outlineofmodelbuildernodes.
```

---

## Стр. 195

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
182 TRANSPORTPROCESSESINONEDIMENSION
FIGURE 9.4 Outlineofmodel1nodes.
beforeitandintheSettingswindowsetthethermalconductivityto1.0(fortestingfirst).
RightclickonHeatTransferandchooseTemperature.Choosetheleftnodeinthegraphics
window, use + in the settings window to add itto the box in the settings window. Leave
thevalueat0.Dothisagainfortherightendandsetthevalueto1.
Step 5 (Create a Mesh) Choose Mesh, and the Settings window for Size will appear.
Accept them by clicking the Build icon. Sixteen nodes will be identified in the Graphics
window.Ifyouforgetthisstep,itwillbeperformedautomaticallyforyouwhenyousolve
theproblem.
Step6(SolvetheProblem) ChooseStudyandrightclick=.AplotofT(x)shouldappear
intheGraphicsWindow.
Step7(ExaminetheSolution) Ifitdoesnot,ortocreateanothergraph,rightclickResults
andchoose1DPlotGroup.Rightclick1DPlotGroupandchooseLineGraph.Aplotof
T(x) should appear in the Graphics Window. The solution is a straight line from (0,0) to
(1,1),asitshouldbe.TheheatfluxisplottedbycreatinganotherLineGraph,butthistime
changing the expression for the y-Axis Data. Choose the expression button, select Heat
Transfer,thenConductiveHeatFlux,thenthexx-componentofheatflux(thereisonlyan
x-component in this problem though). The heat flux is a constant −1. If a plot does not
appear,clicktheploticon.
Step 8 (Solve the Real Problem) Go back to the Heat Transfer in Solids subnode and
change the thermal conductivity to 1 + T. Choose Study and right click =. Examine the
solution in the same way. The temperature is shown in Figure 9.5 and the heat flux is
shown in Figure 9.6. The temperature departs slightly from a straight line. The heat flux
hassomeweird-lookingoscillationsbetween−1.5015and−1.497,buttheseareanartifact
ofthenumericalmethod.Thisisbecausethetemperatureisapproximatedusingquadratic
functionsonfiniteelements,butthederivative(proportionaltoheatflux)isnotcontinuous
acrosselementboundaries.Ifyouclickon1DPlotGroup,thenAxisintheSettingswindow,
youcanchecktheManualboxandsettheaxislimitsfortheyto−2→0;onthatscalethe
oscillationsarescarcelynoticeable.
Step9(CalculateAverages) Youcancalculatetheaveragetemperature.Openthearrowthe
leftofResultsrightclickDerivedValues;rightclickDerivedValuesandchooseIntegration
andthenLineIntegration.IntheSettingswindow,notethatthevariablebeingintegrated
```

---

## Стр. 196

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:HEATTRANSFERINASLAB 183
1
0.8
0.6
0.4
0.2
0
0 0.2 0.4 0.6 0.8 1
x
erutarepmeT
FIGURE 9.5 SolutiontoEq.(9.20).
isT.Click=andlookattheResultsicon(Figure9.7,belowthegraph)toseethevalue:
0.55556.Thisisthevalueoftheaveragetemperature.Youcancheckthatthisistheaverage
byusingIntegrationinsteadofAverageandintegrateT and1separately:
(cid:10)
(cid:5)1 (cid:5)1
Tdx dx =0.55556 (9.21)
0 0
Step 10 (Plot the Thermal Conductivity) You can plot the thermal conductivity by right
clickingonResults;choose1DPlotGroup.ThenrightclickonitandchooseLineGraph.
In the Settings window, click on the expression button and choose heat transfer/thermal
−1.495
−1.496
−1.497
−1.498
−1.499
−1.5
−1.501
−1.502
0 0.2 0.4 0.6 0.8 1
x
xulf
taeH
FIGURE 9.6 Heatfluxinproblem,Eq.(9.20).
```

---

## Стр. 197

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
184 TRANSPORTPROCESSESINONEDIMENSION
FIGURE 9.7 Messages/log/results.
conductivitytoplot.RemovetheunitsfromtheSettingswindowiftheyappear.Theplot
lookslikeFigure9.5exceptwiththey-axisgoingfrom1to2(1+T).
SolutionUsingMATLAB
ThesameproblemcanbesolvedusingMATLAB.First,wewritetheproblemintheform
dq dT
=0,q =−k ,k =1+T,T(0)=1,T(1)=0 (9.22)
dx dx
Thevariabley(1)willrepresentT andthevariabley(2)willrepresenttheheatfluxq.Thus,
theequationbecomes
dy(1) y(2) dy(2)
=− , =0,y(1)=0atleft,y(1)−1=0atright (9.23)
dx k dx
Wedefinethefollowingfunctions(m-files)forthedifferentialequation
function dydx=heattr(x,y,alpha)
alpha = 1.;
k = 1+alpha∗y(1);
dydx(1) = -y(2)/k;
dydx(2) = 0;
dydx = dydx’;
andboundaryconditions(definedintermsoftheresidual,tobemadezero.
function res = heatbc(ya,yb)
res(1) = ya(1);
res(2) = yb(1)-1;
res = res’;
Theinitialguessisfoundusing
solinit=bvpinit(linspace(0,1,5),[0 1])
Thecommandlinspace(0,1,5)setsaspacefromx=0–1withfiveintervals.Theterm[01]
isalineardefinitionofaninitialguess.Thenthesolutionisfoundandplottedusing
sol = bvp4c(@heattr,@heatbc,solinit)
x=linspace(0,1);
y = deval(sol,x);
```

---

## Стр. 198

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:REACTIONANDDIFFUSION 185
plot(x,y(1,:));
xlabel(’x’)
ylabel(’Temperature’)
title(’BVP using MATLAB’)
ThetemperatureplotisofcoursesimilartoFigure9.5.Theheatflux,y(2,:)isconstantat
−1.5; it is determined better since the heat flux itself is a variable, which is smooth. In
Comsol Multiphysics (in the form given), the heat flux is a derivative of the temperature
andanydiscontinuitiesinslopeareprominent.
EXAMPLE:REACTIONANDDIFFUSION
Thenextexampleisareaction-diffusionprobleminasphericaldomain.Thereactionrate
expression is a nonlinear function of concentration, of a type that is appropriate for the
Michaelis–Mentenreactioninbiologicalsystems.Thenondimensionalformoftheproblem
isinEq.(9.24),anditissolvedforα=5,K =2:
(cid:2) (cid:3)
1 d dc αc dc
r2 = , (0)=0,c(1)=1 (9.24)
r2dr dr 1+Kc dr
FollowthesestepstosolvethisprobleminComsolMultiphysics.Sincetheproblemis
insphericalgeometry,weexpandthetermstoget
(cid:2) (cid:3)
1 d dc d2c 2dc αc
r2 ≡ + =
r2dr dr dr2 r dr 1+Kc
(9.25)
d2c 2dc αc
or− = −
dr2 r dr 1+Kc
ThedescriptionsoftheComsolMultiphysicsstepsareabbreviatednowsincetheyfollow
thefirstexampleclosely.Youneedtorememberhowtorightclickandclickthearrowto
expand the menu. For convenience, a pdf version of the first example is available on the
bookwebsite.
Step 1 (Choose the Problem) In Comsol, the 1D option will be appropriate for planar
geometry;the1D,axisymmetricoptionisappropriateforcylindricalgeometry.Sincewe
wantsphericalgeometry,wewillchoosethe1Doptionandaddthetermsneededtomake
theequationagreewithEq.(9.24).Selectfromthefirstmenu1D,next;TransportofDiluted
Species,next;andStationary,finish.Setthepreferences;besuretochoose“Discretization.”
Step2(DefinetheGeometry) OpenModel1andrightclickonGeometry;chooseIntervals.
Thedefaultintervalis(0,1),whichwekeep;clickBuild.Theindependentvariableiscalled
xratherthanr,butwecouldchangeitifdesired.
Step3(DefinetheProblem) OpenModel1andclickonTransportofDilutedSpecies.If
the domain is not listed in the Selection box, click on the domain and the +, or change
Selectionfrom“Manual”to“AllDomains.”Youcanalsotakeconvectionoutoftheproblem
```

---

## Стр. 199

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
186 TRANSPORTPROCESSESINONEDIMENSION
byunselectingtheConvectionbox,orkeepthevelocityaszero,sincethereisnovelocity
inthisproblem.NearthebottomofthesettingspanelisthepanelforDependentVariables.
Clickit,andnotethattheconcentrationiscalledc.UnderTransport,selectDiffusionand
change the diffusivity to 1 in the Settings panel (the problem is dimensionless). Go back
and right click Transport and choose Reactions; select the domain and + to add it to the
Domainbox.SetR to−rate.[Whytheminussign?ChecktheequationinTransportand
C
compareitwithEq.(9.25).]RightclickonDefinitionsandchoosevariables.Definealpha
as5andK as2.Theninsertthename“rate”anddefineitasalpha∗c/(1+K∗c).Alsoclick
onTransportofDilutedSpeciesandtheDiscretizationtab(remembersettingDiscretiztion
inthePreferences?).ChangeLineartoQuadratic.
Step 4 (Add the Spherical Terms) This is where we also have to add in the added term
arisingfromthesphericalcoordinates:(2/r)(dc/dr).Whentheindependentvariableisxand
thedependentvariableisc,thefirstderivativeintheprogramiscx.Thus,weneedtoadd
(2/x)∗cxtotheright-handsideoftheequation,whichistheR term.Addthatsothatthe
C
ratetermis−rate+(2/x)∗cx.
Step 5 (Set the Boundary Conditions) To set the boundary conditions, right click on
TransportandchooseConcentration.Thenclickonpoint2(theright-mostpoint),click+
toaddittothebox,clickSpeciesc,andsetthevalueto1.SelecttheNoFluxbuttonand
noticethattheboundary1isstillusingthatboundaryconditionbutboundary2hasbeen
overridden.Thus,theboundaryconditionsarecorrect.
Step6(SettheMesh) IntheModelBuilder,rightclickonMeshandchooseBuildAllto
createthemesh.Alternatively,selectMeshandthenintheSettingswindowchooseBuild.
The default mesh uses 16 points and the points are added to the plot of the geometry (or
sometimesnot).
Step 7 (Solve the Problem) Right click Study and choose = to solve the problem. If an
erroroccurs,clickontheErrornodeintheModelBuildertoseewhattheproblemisand
trace it down. The plot appears automatically; see Study 1/Solver Configurations/Solver
1/StationarySolver1/Problems1/Error.
Step8(ExaminetheSolution) Sincetheproblemisdimensionless,andthedefaultapplies
dimensionstotheplot,selectthe1DPlotGroupNodeandclickthex-axisandy-axislabels
totakeoutthedimensionsorchangethemtootherwords.ClickontheTitletochangeit
tosomethingmoremeaningful[solutiontoProblem(9.25)]andclicktheploticontoredo
the plot. To save the plot, choose the camera and follow the instructions. The solution is
showninFigure9.8.
ParametricSolution
Itisinstructivetosolvethisproblemformultipleparameters,α,andyoucandothatusingthe
parametricsolver.Ifyouhadnotalreadyusedavariablename,alpha,inPhysics/Subdomain
Selection,youwouldhavetouseavariablenamenow.
Step 1 (Define the Problem) Go back and right click on Global Definitions and choose
Parameters.Insertalpha,use5fornow.ThengotoDefinitionsundertheModelandremove
```

---

## Стр. 200

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:REACTIONANDDIFFUSION 187
1
0.95
0.9
0.85
0.8
0.75
0.7
0 0.2 0.4 0.6 0.8 1
r
noitartnecnoC
FIGURE 9.8 ConcentrationinsphericaldomainwithMichaelis–Mentenreaction.
alpha.Note:Ifyouareusingtheparametricsolver,theparametermustbedefinedinGlobal
Definitions.
Step 2 (Define the Parametric Sweep) Right click on Study, choose Parametric Sweep.
Choosethe+signtoaddaparameter;theAddwindowcomesup.Sincealphaisdefined
inGlobalDefinitions,itisalreadythereasaParametername;selectitandclickOK.Inthe
Settingspanel,alphaislistedasaparametername;settheParametervaluestogofrom0
to20instepsof2.ThiscanbedoneusingtherangesymbolorbysettingParametervalues
torange(0,2,20).
Step3(SolvetheProblem) RightclickonStudy=andaplotappears (Figure9.11).To
seethelegend,selectLineGraph1underthe1DPlotGroupintheModelBuilder/Results;
open Legends and click on the Show legends box. Back up to 1D Plot Group and select
whereyouwouldlikethelegend;herelowerright.ClickonthePloticontogettherevised
plot.Thetitlehasbeenchangedtoidentifyitasaplotofconcentrationfordifferentreaction
rateconstants.
Step4(ExaminetheSolution) Toseetherate,rightclickonResultsandchoose1DPlot
Group. A new node, 1D Plot Group 2 will be created. Set the title, x-axis, and y-axis to
whatyouwouldlike.Thenrightclickonthe1DPlotGroup2andselectLineGraph1;add
the domain to the Selection box by clicking it in the Graphics window and using +, and
changetheexpressiontorate.ClickonShowlegends,andclicktheplotbuttontoseethe
plot.Clickonthecameratosavetheplot.
Figure9.9indicatesthattheconcentrationdecreasesfromtheouterpartofthesphereto
theinnerpartofthesphereandthatthisdecreaseismoredramaticwithlargervaluesofα.
Thisisbecausetherateofreactionisfasteranddiffusioncannotkeepup,thusdecreasing
theconcentration. Figure 9.10shows therateofreaction asafunction ofposition and α.
For small values of α, the rate is the same at all positions, but as α increases the rate of
reactionvariesbyafactoroftwoormorefromthecentertotheouterboundary.
```

---

## Стр. 201

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
188 TRANSPORTPROCESSESINONEDIMENSION
1
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0 0.2 0.4 0.6 0.8 1
r
noitartnecnoC
0
4
8
12
16
20
FIGURE 9.9 Solutionsforseveralvaluesofα.
EXAMPLE:FLOWOFANEWTONIANFLUIDINAPIPE
ThisexampleconsidersflowinapipeforaNewtonianfluid,Eq.(9.6).Youwillsolvethis
problembyusingComsolMultiphysicswith(cid:3)p=2.8×105Pa,μ=0.492Pas,L=4.88,
R = 0.0025 m. You must expand the differential equation because the 1D, axisymmetric
optionforPoisson’sEquationdoesnotincludeallthetermsforcylindricalgeometry.(This
limitationisremovedin2Dand3Dproblems,butherea1Dsolutionsuffices.)So,rewrite
Eq.(9.6)as
d2v 1 (cid:3)p 1dv
=− −
dr2 μ L r dr
(9.26)
dv
(0)=0, v(R)=0
dr
7
6
5
4
3
2
1
0
0 0.2 0.4 0.6 0.8 1
r
etar
noicaeR
0
4
8
12
16
20
FIGURE 9.10 Rateofreactionasafunctionofx(r)andα.
```

---

## Стр. 202

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:FLOWOFANEWTONIANFLUIDINAPIPE 189
Step1(ChoosetheProblem) TosolveEq.(9.26),wemustselecttheequation.InComsol
Multiphysics,the1Doptionwillbeappropriateforplanargeometry;the1D,axisymmetric
optionisappropriateforcylindricalgeometry,whichiswhatwewant.Selectfromthefirst
menu: 1D, axisymmetric, next. The next screen indicates that there is no 1D option for
FluidFlow.Thus,wewilluseMathematics/ClassicalPDEs/Poisson’sEquation.Chooseit,
thenthenextarrow;thenStationary,andthefinishflag.LeavetheunitsasSI,butclickon
EquationsViewandDiscretization.
Step2(SettheVariables) WorkingdowntheModelBuilder,werightclickonDefinitions
andchoosevariables.DefinedpLas2.8e5/(0.492∗4.88)[alternativelyyoucouldinsertthe
pressuredrop,length,andviscosityhereanddefinedpLasdp/(mu∗L)].
Step3(DefinetheGeometry) RightclickonGeometryandchooseIntervals.Thedefault
intervalis(0,1),sochangeitto(0,0.0025);clickBuildAll.
Step 4 (Define the Problem) Click on Poisson’s Equation. Select the domain if it is not
highlighted in the Selection box. To see the equation being solved, choose Equation.
Unfortunately,thecylindricalgeometryisnotreflectedintheequation,butitisshownin
thegraphicswindow(withtheaxis).Nearthebottomofthesettingspanelisthepanelfor
DependentVariables.Clickit,andnotethatthedependentiscalledu;changeittov.Under
Poisson’sEquation,selectDiffusionandleavecas1intheSettingspanel.Makesurethe
domain is selected and appears in Domains. Set f to dpL + vr/r. Check the equation in
Poisson’sEquationandcompareitwithEq.(9.26).Thefactthatyouhavetoinsertthevr/r
isamistakeintheprogramthatisonlydiscoveredbycarefullycheckingtheresults.This
happensbecausePoisson’sequationusuallyreferstoplanargeometryonly.
Step 5 (Set the Boundary Conditions) To set the boundary conditions, right click on
Poisson’sEquationandchooseDirichletBoundaryCondition.Thenclickonpoint2(the
right-mostpoint)intheGraphicswindow,click+toaddittothebox,andkeepthevalue
of0.SelecttheZeroFluxbuttonandnoticethattheboundary1notapplicable,sincethe
programsatisfiesitwithoutinterventionbyusduetotheaxisymmetricgeometry.Thus,the
boundaryconditionsarecorrect.
Step6(SettheMesh) IntheModelBuilder,rightclickonMeshandchooseBuildAllto
createthemesh.Alternatively,selectMeshandthenintheSettingswindowchooseBuild
All.Thedefaultmeshuses16pointsandthepointsareaddedtotheplotofthegeometry
(ormaybenot).
Step 7 (Solve the Problem) Right click Study and choose = to solve the problem. If an
erroroccurs,clickontheErrornodeintheModelBuilder/Study1toseewhattheproblem
isandtraceitdown.
Step8(Examine theSolution) Theplotappears automatically (Figure 9.11).Tochange
theaxislabelsandtitle,selectthe1DPlotGroupNodeandclickthey-axislabelandchange
it to velocity (m/s). Click on the Title to change it to Velocity for Newtonian Fluid and
click the plot icon to redo the plot. To save the plot, choose the camera and follow the
instructions.
```

---

## Стр. 203

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
190 TRANSPORTPROCESSESINONEDIMENSION
0.2
0.15
0.1
0.05
0
0 0.5 1 1.5 2 2.5
Radius (m) x 10−3
)s/m(
yticoleV
FIGURE 9.11 VelocityprofileforfullydevelopedNewtonianflowinapipe.
Step 9 (Calculate the Average Velocity) To compute the average velocity, you need to
be careful to get the integrals in Eq. (9.8). Right click on the node Derived Values under
ResultsandchooseLineIntegration.Theninthesettingswindow,openthepanelIntegration
settings. A box there is clicked to have the integration be appropriate for cylindrical
geometry.Clickonthedomain(line),then+tochoosetheline.First,insertthevalue1.0
for the expression; click = . Look in the results for the tabular value, 1.9635e-5. This is
appropriateforintegrating2πrdr from0to0.0025.Nextinsertv fortheexpression.The
integralthistimeis1.779e-6.Theratiooftheseistheaveragevelocity,0.0906m/s.Note
thatthisisexactlyhalfofthepeakvelocity,whichisexpectedsincethatistrueoftheexact
solution. Alternatively, you can choose Line Average and avoid the division. Be careful,
though, because using Line Integration was how the error in Step 4 was discovered. It is
also possible to look at the velocity gradient (a straight line from zero at the center to a
maximumatthewall).Theshearstressistheviscositymultipliedbythevelocitygradient,
andthatislinearwithdistance,too,foraNewtonianfluid.
EXAMPLE:FLOWOFANON-NEWTONIANFLUIDINAPIPE
Next,youwillconsiderflowinapipewhenthefluidisanon-Newtonianfluid,inparticular
apolymermelt.TaketheviscosityasaCarreaufunction,Eq.(9.14).Theparametersused
hereareη =0.492,λ=0.1,andn=0.8.Theproblemisdefinedby
0
(cid:2) (cid:3) (cid:2) (cid:3)
1 d dv (cid:3)p d dv ηdu (cid:3)p
rη =− or η + =−
r dr dr L dr dr r dr L
(9.27)
dv
(0)=0, v(R)=0
dr
Step1(ChoosetheProblem) Tosolveproblem(9.27),startwiththesolutionforaNew-
tonianfluid.
```

---

## Стр. 204

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:FLOWOFANON-NEWTONIANFLUIDINAPIPE 191
0.35
0.3
0.25
0.2
0.15
0.1
0.05
0
0 0.5 1 1.5 2 2.5
Radius (m) x 10−3
)s/m(
yticoleV
FIGURE 9.12 Velocityprofileforfullydevelopednon-Newtonianflowinapipe.
Step 2 (Set the Variables) Change dpL to be just (cid:3)p/L, and include under Definitions
the viscosity, called eta. First, the program will be changed with eta defined as 0.492
(theNewtonianvalue)tobesurewehavesettheproblemupcorrectly.ThentheCarreau
functionwillbeinsertedforeta.
Step3(DefinetheProblem) TheGeometryisthesame,theboundaryconditionsarethe
same,andthemeshisthesame.Theonlychangeintheequationistouseetaforcinstead
of1.0andeta∗dv/rintheexpressionforf.
Step4(SolvetheProblem) RightclickonStudy=tosolvetheproblem.Wegetthesame
resultasbefore,sowearesuretheprogramiscorrect,oratleastascorrectasourprevious
solution.
Step 5 (Use the Carreau Expression for Viscosity) Now go back to Definitions in
the Model node, select the Variables node, and change the formula for eta to 0.492/
(1+(lambda∗vr)∧ 2)∧ ((1−t)/2);addvariablesoflambda=0.1andn=0.8.Rightclick
on Study =. Note that the independent variable is r, not x, and the first derivative of the
velocityvisvr.
Step6(SolvetheProblem) RightclickonStudy=tosolvetheproblem.Itworksbestif
yousettheinitialvalueofvelocity(underLaminarFlow)tosomethingotherthanzero.
Step7(ExaminetheSolution) ChangethetitletoVelocityfornon-NewtonianFluidand
click on the plot icon to change the plot. Click on the camera to save the plot, which is
showninFigure9.12.
Step 8 (Plot Solution Features) To plot the viscosity across the domain, right click on
Resultsandchoose1DPlotGroup.Thenchange(intheSettingspanel)thetitlesandlabels.
Rightclickon1DPlotGroup2andchooseLineGraph.Changethey-AxisDataExpression
```

---

## Стр. 205

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
192 TRANSPORTPROCESSESINONEDIMENSION
0.5
0.45
0.4
0.35
0.3
0.25
0 0.5 1 1.5 2 2.5
Radius (m) x 10−3
)s
aP(
atE
0.5
0.45
0.4
0.35
0.3
0.25
0 0.5 1 1.5 2 2.5
Radius (m) x 10−3
)s
aP(
atE
(a)
(b)
FIGURE 9.13 Viscosity,Eq.(9.14)forfullydevelopednon-Newtonianflowinapipe:(a)using
linearelementsforvelocity;(b)usingquadraticelementsforvelocity.
fromv toetaandtheUnittoblank.ClickonthePloticontoseetheplot(Figure9.13a).
Thisisanunusualplot,butitemphasizesthingsbothmathematicalandphysical.First,the
viscosityseemstobeconstantineachregion,whichcorrespondstoeachelement.Thatis
becausethevelocityisrepresentedasalinearfunctionintheelement,sothatthederivative
is constant in the element. The physical lesson is that the viscosity approaches the rest
viscositynearthecenterlineanddecreasestoitsminimumatthewall,whichiswherethe
shearrateisthelargest.
Step9(ImprovetheSolution) Toimprovetheplot,weneedtosolveitagain.Tochange
thetrialfunctions[thefunctionsrepresentingthesolutionv(r)],weneedtogobacktothe
```

---

## Стр. 206

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:TRANSIENTHEATTRANSFER 193
Model Builder at the top, choose the “Show” icon (see Step 1 in the reaction-diffusion
example). Select “Equation View” and “Discretization.” Now when we go back to the
Poisson’s Equation node, one of the options (near the bottom of the Settings window) is
“Discretization.”Currentlyitsays“Linear”;changeitto“Quadratic.”Resolvetheproblem
andchoosetheplotofviscosity.Nowwegetasmoothcurve(Figure9.13b)sincethevelocity
gradientcanvarywithinanelement.Anotheroptionwouldbetouselinearfunctionsfor
velocityandjustchooselotsofelements,sothatthecurvelookedsmooth.
Step10(CalculateAverageVelocity) TheaveragevelocityisgivenbyEq.(9.8);calculate
it the same way as for a Newtonian fluid. The average velocity increases from 0.091 to
0.168. The reason for this is shear thinning. The shear rate is zero at the centerline and
is a maximum (in absolute value) at the solid boundary. Because the viscosity decreases
as the shear rate increases [see Eq. (9.14)], the viscosity decreases as the radial position
increases,asseeninFigure9.15.Onehandywaytogetallthesolutionsforseveralpressure
drops (and avoid convergence problems) is to use the Parametric Sweep option (by right
clickingtheStudynode);seeSectionParametricSolution.Thevelocitiesvaryoverseveral
ordersofmagnitudeforthedifferentpressuredrops.Youcouldplotthevelocitydividedby
thepressuredroptoimproveyourgraph.Anevenbetteroptionwouldbetocomputethe
averagevelocityofeachsolution,andplotthevelocitydividedbytheaveragevelocity,all
onthesamegraph.
EXAMPLE:TRANSIENTHEATTRANSFER
Thenextexampleisatransientheattransferproblem:
∂T ∂2T
=α , α =2
∂t ∂x2
(cid:11) (9.28)
∂T (cid:11)
(cid:11)
(cid:11)
=0, T(1,t)=0, T(x,0)=1
∂x
x=0
SolutionUsingComsolMultiphysics
Step1(ChoosetheProblem) TosolveEq.(9.28),openComsolMultiphysics,choose1D,
next;HeatTransfer,thenHeatTransferinSolids,next;TimeDependent,finish.
Step2(DefinetheGeometry) RightclickonGeometryandchooseInterval.Thedefault
is(0,1),whichwekeep.ChooseBuildAll.
Step3(DefinetheProblem) IntheModel1node,chooseHeatTransfer;intheSettings
panel,lookattheequationthatComsolMultiphysicswillsolve.Severalofthetermsneed
tobesettozero:U andQ.ClickonHeatTransferinSolids,andchangetheparameters
trans
toUserdefinedandk=2,ρ =1,C =1.ThentheequationisthesameasEq.(9.28).
p
Step 4 (Set the Boundary Conditions and Initial Conditions) To set the boundary con-
ditions,rightclickonHeatTransferandchooseTemperature.Selecttheboundarypoint2
attheright-handsideofthediagramandthe+symboltoaddittotheSelection.Change
```

---

## Стр. 207

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
194 TRANSPORTPROCESSESINONEDIMENSION
thevaluefrom293.15to0.ClickontheThermalinsulationsubnodeandseethatboundary
point1hasthermalinsulation(whichwewant)andboundarypoint2hasbeenoverridden.
Tosettheinitialcondition,clickontheInitialValuesnodeandsetT to1.
Step5(SettheMesh) SelectthemeshandchooseBuildAll;notethatthenodalpointsare
displayedinthegraph.
Step6(SolvetheProblem) RightclickonStudy=togetthesolution.
Step 7 (Examine the Solution) Right click Data Sets and choose Parametric Extrusion
1D. The Settings window will list the times at which the solution will be plotted. Select
the1DPlotGroupandchangethePlotSettingstoreflectwhatwehaveactuallydone,x,T,
“SolutiontoProblem9.28”andclickontheploticontogetthenewplot.Togetthelegends
forthegraph,clickontheLineGraphnode,chooseLegends(nearthebottom)andclick
ontheShowlegendsbox.ThenreplottoobtainFigure9.14.Notethatitisnotpossibleto
havethetemperaturebeboth0(theboundarycondition)and1(theinitialcondition)atthe
pointx=1,t=0,andthisintroducesasmallperturbationnearthatpoint.Thisperturbation
quickly dampens out in time, though. It is really a manifestation of an improperly posed
mathematical problem rather than an incorrect method, because such a discontinuity is
impossibletocreatephysically.Thisgraphcanbecomparedwithgraphsinyourtextbook
tovalidatethecomputersolution.
Step8(Createa3DPlot) Toseeacolorful3Dplot,rightclickonResults,choose2DPlot
Group. Right click 2D Plot Group, choose Surface and make sure the data set chosen is
ParametricExtrusion1D.Rightclickagain onSurfaceandchooseHeightExpression.A
blackandwhiteversionofthecolorful3DplotisshowninFigure9.15.
1
0.8
0.6
0.4
0.2
0
0 0.2 0.4 0.6 0.8 1
x
erutarepmeT
0
0.1
0.2
0.3
0.5
0.7
0.9
FIGURE 9.14 Solutionofheattransferproblem,Eq.(9.28).
```

---

## Стр. 208

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:TRANSIENTHEATTRANSFER 195
1.0021
1
1
0.8
0.5 0.6
0.4
0
1
1
0.2
0.5
0.5
0 0
0
FIGURE 9.15 Solutionofheattransferproblem,Eq.(9.28)plottedin3D.
SolutionUsingMATLAB
MATLABcansolvepartialdifferentialequations(inonespatialdimension)oftheform
(cid:2) (cid:3) (cid:2) (cid:2) (cid:3)(cid:3) (cid:2) (cid:3)
∂u ∂u ∂ ∂u ∂u
c x,t,u, = x −m xm f x,t,u, +s x,t,u, (9.29)
∂x ∂t ∂x ∂x ∂x
Theparametermis0,1,or2,forplanar,cylindrical,orsphericalgeometry.Forthisproblem
weusec=1andm=0.Here,thevalueoff is2∗dT/dx.TheMATLABfunctiontranstemp
definesthedifferentialequation.
function [c,f,s] = transtemp(x,t,u,dTdx)
c = 1;
s = 0; %no source term
f = 2∗dTdx;
Theinitialconditionsaresetwiththefunctionictemp.
function T0=ictemp(x)
T0 = 1;
```

---

## Стр. 209

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
196 TRANSPORTPROCESSESINONEDIMENSION
Theboundaryconditionscanbe
(cid:2) (cid:3)
∂u
p(x,t,u)+q(x,t)f x,t,u, =0 (9.30)
∂x
Thefunctionf isalreadydefinedintranstemp.Here,attheleftwewant
p =0, q =1 (9.31)
Andattherightwewant
p =T, q =0 (9.32)
Thus,definethefunctionbctemp.
function [pl,ql,pr,qr]=bctemp(xl,Tl,xr,Tr,t)
pl = 0; % l for left boundary
ql = 1;
pr = Tr; % r for right boundary
qr = 0;
ThesolutionisobtainedwiththefollowingMATLABcommands.
xmesh = linspace(0,1,11)
tspan = linspace(0,1,11)
sol = pdepe(0,@transtemp,@ictemp,@bctemp,xmesh,tspan)
Twotypesofplotsarepossible:a3Dplotandalineplotatdifferentt;seeFigure9.16.
T = sol(:,:,1)
plot(xmesh,T(1,:,1),xmesh,T(2,:,1),xmesh,T(3,:,1),...
xmesh,T(4,:,1),xmesh,...
T(5,:,1),xmesh,T(6,:,1),xmesh,T(7,:,1),xmesh,T(8,:,1),...
xmesh,T(9,:,1),xmesh,T(10,:,1),xmesh,T(11,:,1))
xlabel(’x’)
ylabel(’Temperature’)
title(’Transient Heat Transfer with MATLAB)’)
pause
surf(xmesh,tspan,T)
In Eq. (9.29) the variable u can be a vector, which makes possible solution of coupled
partialdifferentialequations.
EXAMPLE:LINEARADSORPTION
Adsorptionisonewaytoremoveachemicalspeciesfromaflowingstream.Acylindrical
tube is packed with adsorbent material, oftentimes in the form of small spheres. The
adsorbent has the property that some materials adsorb while others do not. The flowing
streamgoesinandouttheintersticesbetweenthespheres,andcontactstheadsorbent.The
```

---

## Стр. 210

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:LINEARADSORPTION 197
1
0.8
0.6
0.4
0.2
0
0 0.2 0.4 0.6 0.8 1
x
(a)
(b)
erutarepmeT
0
0.2
0.4
0.6
0.8
1.0
1
0.8
0.6
0.4
0.2
0
1
0.8 1
0.6 0.8
0.4 0.6
0.4
0.2
0.2
0 0
FIGURE 9.16 Transienttemperature:(a)lineplot;(b)3Dplot.
chemicalthatisstronglyadsorbedisremovedfromtheflowingstreamandappearsonthe
solidadsorbent.Thenextexampleillustratesthatprocess.
Thedifferentialequationsgoverninglinearadsorptionaregivenbytwoequations,the
first a mass balance on the fluid phase and the second a mass balance on the stationary
phase:
∂c ∂c ∂n ∂n
φ +φV +(1−φ) =0, =k(γc−n) (9.33)
∂t(cid:2) ∂x(cid:2) ∂t(cid:2) ∂t(cid:2)
wherecisthefluidconcentration (molesper fluidvolume), nistheconcentration onthe
solid adsorbent (moles per solid volume), φ is the void fraction in the bed, V is the fluid
```

---

## Стр. 211

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
198 TRANSPORTPROCESSESINONEDIMENSION
velocity,t(cid:2)istime,x(cid:2)isdistancedownthebed,kisamasstransfercoefficient,andγ isthe
slope of the equilibrium line, n versus c. The initial conditions give the concentration in
fluidphasesandadsorbedphasesattimezero,whichinthisexamplearenoconcentration
atall:
c(x
(cid:2),0)=0,
n(x
(cid:2),0)=0
(9.34)
Theonlyboundaryconditionistheinletconcentration,heretakenas1.0:
c(0,t (cid:2) )=1 (9.35)
Theequationsaremadenondimensionalusingthefollowingvariables:
x(cid:2)k
x = , t =kt (cid:2) (9.36)
V
ThenEq.(9.33)is
∂c ∂c (1−φ) ∂n
+ + (γc−n)=0, =γc−n (9.37)
∂t ∂x φ ∂t
Thisproblemislinear,andananalyticalsolutionexists,butitisverycomplicatedtoevaluate
becauseitdependsonintegralsofBesselfunctions(Rheeetal.,1986).Numericalsolutions
arealsoavailableforcomparison(Finlayson,1992).WhenyouuseComsolMultiphysics,
itisnecessarytoaddsomediffusiontotheproblem,andyousolveanaugmentedequation
forconcentration.TheaddedterminvolvesaPecletnumber,definedintermsofaneffective
diffusioncoefficient:
∂c ∂c (1−φ) 1 ∂2c 1 φV2 Dk
+ + (γc−n)= , = , orPe= (9.38)
∂t ∂x φ Pe∂x2 Pe Dk φV
Step1(ChoosetheProblem) TosolveEq.(9.38),openComsol,choose1D,next;Transport
ofDilutedSpecies,next;TimeDependent,finish.
Step 2 (Set the Variables) Right click on Global Definitions and define the following
parameters:phi=0.4,gamma=2,Pe=1000.UndertheModel,rightclickDefinitions
andchooseVariables.Setraten=gamma∗c−nandrate=(1−phi)∗raten/phi.
Step 3 (Define the Geometry) Under the Model, right click on Geometry and choose
Interval.Thedefaultis(0,1),whichwekeep.ChooseBuildAll.
Step 4 (Define the Problem for c) It can take the form of Eq. (9.38). Select the down
arrow on Transport, and click Convection and Diffusion. Set the velocity to 1.0 and the
D to1/Pe.RightclickonTransportandchooseReactions.SetR to−rate.Comparethe
C C
equationformatinComsolwiththatinEq.(9.38)toseewhytheminusisnecessary.
```

---

## Стр. 212

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:CHROMATOGRAPHY 199
Step5(SettheBoundaryandInitialConditionsforc) RightclickonTransportandchoose
Inflow. Select boundary point 1, then the + so that 1 appears in the Boundary Selection.
Set the inflow concentration to 1.0. Right click on Transport again and choose boundary
point2andthenclick+.Accepttheboundarycondition,whichwillallowconvectionout
ofthedomain.ClickonInitialValuesandmakesuretheconcentrationiszero.
Step6(DefinetheProblemforn) Next,weaddtheequationforn,theamountofmaterial
adsorbed. Right click on Model 1, then choose “Transport of Diluted Species” again,
next; then choose “Transient,” finish. Select “Transport of Diluted Species 2” and check
theequation.Changethenameofthedependentvariableton.Clickon“Convectionand
Diffusion” and set D = 0. Right click on “Transport of Diluted Species 2” and choose
n
“Reactions.”SetR toraten.
n
Step7(SettheBoundaryandInitialConditionsforn) ClickonInitialValuesandverify
thatniszero.Wedonotchangetheboundaryconditionsfromnoflux,sincetheadsorbed
materialcannotgetoutexceptbyexchangingwiththemovingfluid.
Step 8 (Set the Mesh) Select the mesh and change the element size to “Extrafine” (in
anticipation that many nodes will be needed). Choose “Build All”; notice that the nodal
pointsaredisplayedinthegraph.
Step9(SolvetheProblem) RightclickonStudy=togetthesolution.
Step10(ExaminetheSolution) Selectthe1DPlotGroupandchangethePlotSettingsto
reflectwhatwehaveactuallydone,x,c,“SolutiontoProblem9.37”andclickontheplot
icontogetthenewplot.Togetthelegendsforthegraph,clickontheLineGraphsubnode,
chooseLegends(nearthebottom)andclickontheShowlegendsbox.Thenreplot,choose
the camera and save the figure. To see the plot of n, perform the same steps but plot n
ratherthanc.TheconcentrationinthefluidisshowninFigure9.17aandtheconcentration
adsorbedisshowninFigure9.17b.
Thesolutionisagoodrepresentationofthesolution,butthefront,wheretheconcentra-
tiondropsquickly,isnotassteepasitshouldbe(Finlayson,1992).Someoftheoscillations
apparentinthefigurearebecausethefiniteelementmethodisnotwellsuitedtoproblems
suchasthis,withconvectionbutnodiffusion.ComsolMultiphysicsaddssomestabiliza-
tionfeaturestosmooththeoscillationswithoutobscuringtheessentialdetails.Avarietyof
specializedmethodsareavailabletodothat,asdescribedinAppendixEandbyFinlayson
(1992).
Thisexampleusedalinearisotherm.Itiseasytochangetoanonlinearisotherm,since
theonlychangeisinStep2;chooseadifferentformulathatrepresentsanotherisotherm.
EXAMPLE:CHROMATOGRAPHY
In some columns, mass transfer is so fast that the concentration in the gas phase is in
equilibrium with the concentration on the solid adsorbent. In that case the problem is
slightlydifferent.Thiscaseisaprototypeofachromatographycolumn,whichcanbeused
toseparatechemicals.
```

---

## Стр. 213

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
200 TRANSPORTPROCESSESINONEDIMENSION
1.4
1.2
1
0.8
0.6
0.4
0.2
0
−0.2
0 0.2 0.4 0.6 0.8 1
x
n
1.2
1
0.8
0.6
0.4
0.2
0
−0.2
0 0.2 0.4 0.6 0.8 1
x
Solution to Eq. (9.37)
c
Solution to Eq. (9.37)
(a)
(b)
FIGURE 9.17 Solution of linear adsorption problem, Eq. (9.37), at times 0:0.1:1: (a) fluid
concentration;(b)solidconcentration.
TheequationisthefirstoneofEq.(9.33).Now,however,thesolidconcentrationisan
algebraicfunctionofthefluidconcentration,sincetheyareinequilibrium.Inthisexample,
youwilluseaLangmuirisothermwiththealgebraicexpression:
γc
n = (9.39)
1+Kc
WhenthisequationissubstitutedintoEq.(9.33)youobtain
∂c ∂c dn ∂c
φ +φV +(1−φ) =0 (9.40)
∂t(cid:2) ∂x(cid:2) dc∂t(cid:2)
```

---

## Стр. 214

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:CHROMATOGRAPHY 201
FortheLangmuirisotherm,theequationis
(cid:8) (cid:9)
dn ∂c ∂c dn γ
φ+(1−φ) +φV =0, = (9.41)
dc ∂t(cid:2) ∂x(cid:2) dc (1+Kc)2
Thenondimensionalformoftheproblemisobtainedusingt(cid:2)=tandx=x(cid:2)/V:
(cid:8) (cid:9)
(1−φ)dn ∂c ∂c dn γ
1+ + =0, = (9.42)
φ dc ∂t ∂x dc (1+Kc)2
In this example, you will solve the problem with an initial concentration of one between
x=0.25and0.75.Theinletconcentrationiszeroalways:
0, x <0.25
c(x,0)=1, 0.25≤ x ≤0.75 (9.43)
0, 0.75 < x
Step1(ChoosetheProblem) TosolveEq.(9.38),openComsolMultiphysics,choose1D,
next;TransportofDilutedSpecies,next;TimeDependent,finish.
Step 2 (Set the Variables) Right click on Global Definitions and define the following
parameters: phi = 0.4, K = 2, gamma = 0.1. Under the Model, right click “Definitions”
andchoose“Variables.”Setder=gamma/(1+K∗c)∧2andcoeff =1+(1−phi)∗der/phito
matchEq.(9.42).
Step 3 (Define the Geometry) Under the Model 1, right click on Geometry and choose
“Interval.”Thedefaultis(0,1),sochangeitto(0,2).Choose“BuildAll.”
Step4(DefinetheProblem) First,setuptheequationforc.Choose“TransportofDiluted
Species”andbesurethe“Convection”boxischecked.Clickon“ConvectionandDiffusion”
and set u to 1/coeff and D to 0.001. There is no diffusion in this problem, but the finite
C
element method requires some to get a solution. As the mesh is refined, the amount of
diffusion decreases. The signal to you is oscillations in the figures, which indicates that
eithermoreelementsormoreartificialdiffusionisneeded.
Step 5 (Set the Boundary and Initial Conditions) Right click on “Transport of Diluted
Species”andchoose“Inflow.”Selectboundarypoint1,thenthe+sothat1appearsinthe
“Boundary Selection.” Set the inflow concentration to zero. Right click on “Transport of
Diluted Species” again and choose “Outflow.” Select boundary point 2 and then click +.
Accepttheboundarycondition,whichwillallowconvectionoutofthedomain.Clickon
“InitialValues”makesurethatthedomainisincludedinthe“DomainSelection.”Wewant
the concentration to start as 0 from x = 0 to 0.25, then change to 1 until x = 0.75, then
changebacktozero.Thus,weuse1∗(x>0.25)–1∗(x>0.75).The(x>0.25)meansthe
valuemultiplyingitwillbeusedwhenx>0.25butnototherwise.Thus,theinitialvalue
willbezerountilx=0.25,then1,andfromx=0.75onitwillbezeroagainsinceboth
functionsareusedandareidenticalandsubtractedfromeachother.
```

---

## Стр. 215

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
202 TRANSPORTPROCESSESINONEDIMENSION
Step6(SettheMesh) Selectthemeshandchangetheelementsizetoextremelyfine(in
anticipationthatmanynodeswillbeneeded).ChooseBuildAll;notethatthenodalpoints
aredisplayedinthegraph.
Step7(SolvetheProblem) BeforesolvingtheproblemclickonStep1:TimeDependent
underStudy1.ChangetheTimestoseethesolutiontorange(0,1)sothattherewillbetwo
curves.Rightclickon“Study1”=togetthesolution.[Youcanuserange(0,0.2,1)toget
morecurves,butonlytwoareusedheretoalloweasiercomparisonwithFigure9.18b.]
Step8(ExaminetheSolution) Selectthe1DPlotGroupandchangethePlotSettingsto
reflectwhatwehaveactuallydone,x,c,“SolutiontoProblem9.42”andclickontheploticon
1
0.8
0.6
0.4
0.2
0
0 0.5 1 1.5 2
x
c
1.2
1
0.8
0.6
0.4
0.2
0
−0.2
0 0.5 1 1.5 2
x
MacCormack method with flux correction
c
(a)
(b)
FIGURE 9.18 Solution of chromatography problem, Eq. (9.42): (a) Comsol Multiphysics; (b)
MacCormackflux-correctedmethod(AppendixE).
```

---

## Стр. 216

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
PRESSURESWINGADSORPTION 203
togetthenewplot.Togetthelegendsforthegraph,clickontheLineGraphnode,choose
“Legends”(nearthebottom)andclickonthe“Showlegends”box.Thenreplot,choosethe
cameraandsavethefigure.TheconcentrationinthefluidisshowninFigure9.18a.
Nowthequestionarisesastotheeffectoftheaddeddiffusion.Ifwechangethediffusion
coefficient to 0.01, right click Study = , and look at the plot, we find that it is smoothed
outconsiderably.Ifwechangethediffusioncoefficientto0.0001,wefindtheoscillations
increase dramatically. Thus, the value of 0.001 seems to be enough to get a reasonable
solution, but not so much that it makes the solution incorrect. This is the meaning of the
term ‘streamline diffusion’, and here we are just introducing it ourselves. The solution
obtainedinComsolMultiphysicscanbecomparedwithFigure9.18b,whichisgenerated
withaspecializedmethodcalledMacCormackmethodwithFlux-correctiondescribedin
Appendix E. The Comsol Multiphysics solution is a reasonable solution if we ignore the
smalloscillations.
PRESSURESWINGADSORPTION
Hydrogenismadeeverydayinrefineries,anditisusedtomakeammoniaandmethanol.In
thefuture,moremaybeneededforautomobilefuelcells.Mostofthehydrogenisobtained
bypurifyingagasmixtureof60–90molpercenthydrogen(SircarandGolden,2010).The
primary method is pressure swing adsorption. The gaseous stream flows at high pressure
through a packed bed of adsorbent. The carbon dioxide, carbon monoxide, methane, and
nitrogenareadsorbedonthepacking,andquitepurehydrogenexits.Thisrequiresagood
adsorbent, such as activated carbon or a xeolite. Then the pressure is reduced and the
output,stillpurehydrogen,isdirectedtoanothervessel.Finallyastreamofhydrogenflows
in the reverse direction at the lowest pressure to remove the adsorbed gases. For this to
beefficient,processeslowerthepressureseveraltimessothatthereareseveralco-current
depressurizationsstepsandseveralcountercurrentdecompressionsteps(SircarandGolden,
2010).Inthisproblem,anextremelysimplifiedversionisconsidered.
Itisassumedthattheprocessisisothermalanddilutesothatthevelocitydoesnotchange
as the material adsorbs; these limitations are made strictly for simplification here, since
theyarenotusuallytrue(Ruthvenetal.,1994).Theequationsareanexpandedversionof
Eq.(9.37)sothattheactualnonlinearadsorptionprocesscanbemodeled.Foreachofthe
fourspeciestheequationsare
∂y ∂y ∂2y 1 RT ∂q¯
i +v i = D i − ρ i (9.44)
∂t ∂x ∂x2 φ p B ∂t
∂q¯ a p
i =k (q ∗−q¯ ), q ∗ = (cid:12)i i (9.45)
∂t i i i i 1+ n b p
j=1 j j
They isthemolefraction,vistheinterstitialvelocity,Disaneffectivediffusioncoefficient
i
(needed for stability), φ is the void fraction, R is the gas constant, T is the temperature,
pisthepressure,t isthetime,xisthedistancefromtheinlet,andk isthemasstransfer
i
coefficient.Theconcentrationoftheithspeciesontheadsorbantisq¯ andtheconcentration
i
inequilibriumwiththepartialpressurep isq∗.Theconstantsa andb areparametersin
i i i i
theadsorptionrelationwhichiswrittenasamulticomponentLangmuirformula.
```

---

## Стр. 217

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
204 TRANSPORTPROCESSESINONEDIMENSION
Whennondimensionalized,theequationsare
∂y ∂y 1 ∂2y ∂q¯
i + i = i −coeff i
∂t(cid:2) ∂x(cid:2) Pe∂x(cid:2)2 ∂t(cid:2)
(9.46)
∂q¯ k L a p y
i = i (q ∗−q¯ ), q ∗ = i(cid:12)T i
∂t(cid:2) v i i i 1+ p n b y
T j=1 j j
TherewillbefourTransportequationsforthefourcomponentsandfourTransportequations
(withoutvelocity)fortheconcentrationontheadsorbent.
Intherealprocess,thissteptakesplace,thenthepressureisreducedandthereisback
flow,thenthepressureisreducedsomemore.Onewouldneedtheadsorbentconcentration
attheendofonestepastheinitialconditionforthenextstep.Thenthestepswouldhaveto
berunoverandoveruntilacyclicconditionwasreachedinwhicheachstepwasthesame.
They will not be the same at the start, however, because we start with nothing adsorbed,
whereasinthecyclicoperation,therewillbesomething,anditwillbethesameeachcycle.
Thus,thisprocesscanbecomeverycomplicated;Problem9.29isonlyastart.
CHAPTERSUMMARY
Yousawhowtheequationsgoverningenergytransfer,masstransfer,andfluidflowwere
similar, and examples were given for 1D problems. Examples included heat conduction,
both steady and transient, reaction and diffusion in a catalyst pellet, flow in pipes and
betweenflatplatesofNewtonianornon-Newtonianfluids.Thelasttwoexamplesillustrated
an adsorption column, in one case with a linear isotherm and slow mass transfer and in
the other case with a nonlinear isotherm and fast mass transfer. Specific techniques you
demonstratedincludeparametricsolutionswhenthesolutionisdesiredforseveralvaluesof
oneparameterandtheuseofartificialdiffusiontosmoothtime-dependentsolutionswhich
havesteepfrontsarelargegradients.
PROBLEMS
Note: When solving boundary value problems in MATLAB, the differential equation is
evaluatedateachboundary,aswellaspointsbetween.Thus,forcylindricalandspherical
geometry,youneedtousel’Hopital’sruletoevaluatethedifferentialequation:
1dc d2c/dr2(0) d2c
lim = = (9.47)
r→0r dr dr/dr(0) dr2
ChemicalReaction
9.1 Achemicalreactorwithaxialdispersionisgovernedbythefollowingequations:
1
1 d2c dc c 1 dc dc
− = Da , − (0)=1−c(0), (1)=0 (9.48)
Pedx2 dx c+v Pedx dx
Solve for Da = 8, v = 3, and Pe = 15, 150, and 1500. (Hint: include streamwise
diffusionasneeded.)
```

---

## Стр. 218

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 205
9.2 The following equation governs diffusion and reaction of carbon monoxide in an
2
isothermal catalyst. Find the average reaction rate and compare the average with
the reaction rate if the concentration were everywhere the same as the external
concentration(herec=1).Theparametersareφ =32, Bi =10, α =20.Solve
m
using(a)Comsoland(b)MATLAB:
(cid:2) (cid:3)
1 d dc dc
r2 =φ2R(c), (0)=0,
r2dr dr dr
dc
− (1)= Bi (c(1)−1),
m
dr
c
R(c)= (9.49)
(1+αc)2
9.3 Thetransientreactionanddiffusioninapackedbedwithaxialdispersionisgoverned
1
bythefollowingequations.Beginwithaninitialconcentrationinthebedofzero.At
timezerostartflowingwiththeinletconcentration=1.0.Integratetosteadystate.
UsetheparametersPe=100,0≤x≤1,Da=2,v=2:
∂c ∂c 1 ∂2c c 1 ∂c
+ = −Da , − (0,t)=1−c(0,t),
∂t ∂x Pe∂x2 c+v Pe∂x
∂c
(1,t) =0,
∂x
c(x,0) =0 (9.50)
9.4 Bratu’s equation is an interesting boundary value problem that arises in a simpli-
1
fication of a combustion reaction within a cylindrical vessel (Frank-Kamenetskii,
1969;Linetal.,2008).Theproblemhasmorethanonesolutionforthesamecon-
ditions; thus, one must start from different initial guesses to find it. In addition,
time-dependent solutions can become unstable and jump from one steady solution
toanotherasaparameterchanges.Or,thesteady-statesolutionmaybeunstableand
notrealizable.Theequationsare
d2y
+λexp(y)=0, y(0)= y(1)=0 (9.51)
dx2
UseComsolMultiphysicstosolvethisproblemforλ=1.Trytofindmorethanone
solution.
ChemicalReactionandHeatTransfer
9.5 Achemicalreactorwithaxialdispersionofbothmassandenergyisgovernedbythe
1
followingequations:
1 d2c dc 1 dc dc
− = R(c,T), − (0)=1−c(0), (1)=0 (9.52)
Pedx2 dx Pedx dx
1 d2T dT 1 dT dT
− =βR(c,T), − (0)=1−T(0), (1)=0 (9.53)
Pe dx2 dx Pe dx dx
H H
```

---

## Стр. 219

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
206 TRANSPORTPROCESSESINONEDIMENSION
Thereactionrateexpressionis
R(c,T)=3.817c2exp(γ −γ/T) (9.54)
andtheparametersarePe=Pe =96,γ =17.6,β =−0.056.
H
9.6 The following equations govern diffusion and reaction in a catalyst with signifi-
1
cant heat effects. Solve for φ =1.1, γ =30 and β = 0, 0.01, 0.03, 0.07, 0.10,
0.12,0.15:
(cid:2) (cid:3)
1 d dc dc
r2 =φ2R(c,T), (0)=0, c(1)=1 (9.55)
r2dr dr dr
(cid:2) (cid:3)
1 d dT dT
r2 =−βφ2R(c,T), (0)=0, T(1)=1,
r2dr dr dr
R(c,T)=cexp[γ(1−1/T)] (9.56)
9.7 Solvethefollowingproblemforreactionandheattransferinaporouscatalystpellet
1
for the parameters: φ = 1.1, γ = 30, β = 0.15, Le = 1050 (see Hellinckx et al.,
1972),forasimplifiedformoftheproblem.Useinitialconditionsofc=0,T=0.8.
Integratefromt=0to1050:
(cid:2) (cid:3)
∂c 1 ∂ ∂c ∂c
= r2 −φ2R(c,T), (0,t)=0, c(1,t)=1 (9.57)
∂t r2∂r ∂r ∂r
(cid:2) (cid:3)
∂T 1 ∂ ∂T ∂T
Le = r2 +βφ2R(c,T), (0,t)=0,
∂t r2∂r ∂r ∂r
T(1,t)=1, R(c,t)=cexp[γ(1−1/T)] (9.58)
9.8 Solveproblem9.6withLe=0.1.Integratefromt=0to1.
1
9.9 Hlava´c˘ek et al. (1968) provide the following example of heat and mass transfer in
1
a porous catalyst that is a flat particle. The parameters are chosen so that multiple
solutions exist; thus one must start from different initial guesses to find them. In
addition,time-dependentsolutionscanbecomeunstableandjumpfromonesteady
solution to another as a parameter changes. Or, the steady-state solution may be
unstableandnotrealizable.Theequationsare
(cid:8) (cid:9)
d2y γβ(1−y)
=λyexp , y (cid:2) (0)=0,y(1)=1 (9.59)
dx2 1+β(1−y)
UseComsolMultiphysicstosolveforλ=0.05,0.1,and0.15.Findasmanysolutions
asyoucanforeachparameter,λ.Linetal.(2008)provideamethodtobesureall
thesolutionshavebeenfound.
```

---

## Стр. 220

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 207
MassTransfer
9.10 Solve the following diffusion problem with a variable diffusivity (appropriate for
2
somepolymers).Solveusing(a)Comsoland(b)MATLAB:
(cid:2) (cid:3)
∂c ∂ ∂c
= D , c(0,t)=1, c(1,t)=0, c(x,0)=0, D =e0.5c
∂t ∂x ∂x
(9.60)
HeatTransfer
9.11 Solvethefollowingheattransferproblemwithradiationincylindricalgeometry.The
1
parametersareG=2,Nu=10:
d2T 1dT dT dT
+ +G, (0)=0, − (1)= Nu[T4(1)−1] (9.61)
dr2 r dr dr dr
9.12 Solvethefollowingtransientproblemandintegratetosteadystate.Doyougetthe
1
samesolutionatsteadystateasfoundinProblem9.9?Solveusing(a)Comsoland
(b)MATLAB:
∂T ∂2T 1∂T ∂T
= + +G, (0,t)=0,
∂t ∂r2 r ∂r ∂r
∂T
− (1,t)= Nu[T4(1,t)−1], T(r,0)=1 (9.62)
∂r
9.13 Solve the following heat transfer problem. The parameters are ρ = 491 lb /ft3,
1 m
C =0.11Btu/lb ,R=0.4ft,h=30Btu/hft2◦F,k =3Btu/hft2◦F,T =120◦F,
p m 0
T =68◦F:
surr
(cid:2) (cid:3)
∂T k ∂ ∂T ∂T
ρC = r , (0,t)=0,
p ∂t r ∂r ∂r ∂r
∂T
−k (R,t)= h[T(R,t)−T ], T(r,0)=T (9.63)
∂r surr o
9.14 Solvethefollowingheattransferproblem.Theparametersareρ=491lb /ft3,C =
1 m p
0.11Btu/lb ,R=0.4ft,U=12.9Btu/hft2◦F,T =120◦F,T =68◦F.Compare
m 0 surr
theaveragetemperatureversustimewiththesolutionfoundinProblem9.13:
dT
ρC πR2L =−U2πRL(T −T ), T(0)=T (9.64)
p surr 0
dt
ElectricalFields
9.15 The following (nondimensional) problem governs the electric potential outside a
2
cylinderthatiskeptatpotential(cid:12) whereasthepotentialatadistanceLawayfrom
0
the center of the cylinder is kept at zero; L is taken as 10. The parameter κ is 0.8,
the applied potential is 2, and the radius of the cylinder is 1. Find the potential
```

---

## Стр. 221

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
208 TRANSPORTPROCESSESINONEDIMENSION
distributionaroundthecylinder.Solveusing(a)Comsoland(b)MATLAB:
d2(cid:12) 1d(cid:12)
+ =κ2(cid:12), (cid:12)(R)=(cid:12) , (cid:12)(L)=0 (9.65)
dr2 r dr 0
Parts (a) and (b) are applicable when the dependent variable remains small (lin-
earizedPoisson–Boltzmannequation).Solvetheproblemwiththeright-handside=
κ2sinh((cid:12)) (Kirby, 2010, pp. 206–208). Comment on the validity of the Debye
approximation.
9.16 The transient charge distribution in a semiconductor is governed by the following
1
partialdifferentialequation.Integratetheequationtosteadystatewithβ =1.5:
∂c ∂2c
= −βec, c(x,0)=0.5, c(0,t)=1, c(1,t)=1 (9.66)
∂t ∂x2
9.17 UseComsolMultiphysicstosolvetheproblem
1
d2(cid:12) d(cid:12)
=κ2sinh((cid:12)), (cid:12)(0)=2, (∞)=0 (9.67)
dy2 dy
usingκ =0.8.Useafinite,butlarge,domain.ShowthedifferencewhentheDebye
approximationisusedandtheright-handsideis=κ2(cid:12).
9.18 UseComsolMultiphysicstosolvetheBoltzmannproblembetweentwoflatplates
1
d2(cid:12) d(cid:12)
=κ2sinh((cid:12)) and (cid:12)(0.5)=2, (0)=0 (9.68)
dy2 dy
in a finite domain, 0 to 0.5, with zero slope at y = 0 (the center) and a boundary
conditionof2aty=0.5.Theκ =0.8.AlsodothisfortheDebyeapproximation,
withtheright-handsidereplacedby(cid:12).IstheDebyeapproximationvalid?
FluidFlow
9.19 SolvefortheflowofaNewtonianfluidinapipe,followingtheexample.Plottheshear
2
rate as a function of radial position. Calculate the average velocity. Plot the shear
stressasafunctionofradialposition.Solveusing(a)Comsoland(b)MATLAB.
9.20 Solvetheflowofanon-Newtonianfluidinapipe,followingtheexample,forpressure
2
dropsof10,103,105,107Pa.Theparametersareη =0.492Pas,λ=0.1s−1,and
0
n=0.8.Plotthevelocity,shearrateandshearstressasafunctionofradialposition.
Howdothesecurveschangeasthepressuredropisincreased?
9.21 AfiberspinningproblemisgovernedbythefollowingequationsfromMiddleman
1
(1977):
(cid:2) (cid:3)
d2u ρ du 1 du 2
= u + , u(0)=u , u(L)=u (9.69)
dx2 3μ dx u dx 0 L
```

---

## Стр. 222

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 209
Theratioofthetwovelocitiesisthedrawdownratio,
u
D = L (9.70)
R
u
0
Whenρ=0thesolutionforvelocityandradiusofthefiberis(Middleman,1977,
p.237)
(cid:2) (cid:3) (cid:2) (cid:3)
xlnD 1xlnD
u =u exp R , R(x)= R exp − R (9.71)
0 0
L 2 L
Solvetheproblemwithoutinertia(ρ =0)usingu =16.7cm/s,u =1666.7cm/s,
0 L
andL=300cm.
9.22 Solvethefiber-spinningproblem(9.21)withρ=0.96g/cm3andμ=5000poise.Is
1
inertiaimportant?HowdoesthefiberradiuscomparewiththesolutiontoProblem
(9.21)?
9.23 Solve the fiber-spinning problem for a non-Newtonian fluid with viscosity that
1
dependsonshearrate.Theproblemwithoutinertiais
(cid:2) (cid:3) (cid:2) (cid:3)
d du η du 2
η = , u(0)=u , u(L)=u ,
0 L
dx dx u dx
(cid:11) (cid:11)
(cid:11) (cid:11)
η= K(2×3(n−1)/2) (cid:11) (cid:11) du(cid:11) (cid:11) , K =5000 (9.72)
dx
Solveitforu =16.7cm/s,u =1666.7cm/s,L=300cm,andn=1to0.5using
0 L
theparametricsolver.
9.24 Berg(2010,p.712)discussessteadythermocapillaryflowinonedimension.Consider
2
ashallowtroughoffluid,withatemperaturegradientimposedfromlefttoright(hot
on the left); see Figure 9.19. First, we assume that the solution depends only on
the vertical distance, y, and that the trough is very long and very wide. Due to the
imposed temperature gradient on the surface, and the temperature dependence of
surfacetension,aforceisappliedonthetopthatrequiresthefluidtomovefromleft
toright.Toobeycontinuity,itmust(somewhere)alsomovefromrighttoleft.Thus,
theproblemis
(cid:8) (cid:9)
d2v dp dv dσ dT
μ = , v(h)=0, μ + =0 (9.73)
dy2 dx dy dT dx
y=0
x
y
T T
hot cold
FIGURE 9.19 Thermocapillaryflow.
```

---

## Стр. 223

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
210 TRANSPORTPROCESSESINONEDIMENSION
Thepressuredropiseliminatedbytheconditionthatthenewflowrate(lefttoright)
bezero:
(cid:5)h
vdy =0 (9.74)
0
Use Comsol Multiphysics to solve for the velocity profile when L = 10 cm, h =
1 mm, (cid:3)T = 40◦C, μ = 5 cP, and dσ/dT = 0.1 mN/mK. (Hint: you can program
itwithaspecificdp/dxandvaryituntilyougettheintegraltobezero;oryoucan
usetheparametricsolverandsolveforavarietyofvaluesofdp/dxandinterpolate
andextrapolate;oryoucanuseintegrationcouplingtocausethedp/dxtobechosen
suchthattheaveragevelocityiszero;seeAppendixD.)
9.25 When colloids flow under conditions of low volume fraction, the viscosity of the
1
solution is constant. When the volume fraction is larger, though, the particles of a
suspension of hard, noninteracting (i.e., nonaggregating) spherical particles, cause
theviscositytovarywiththedimensionlessshearrate,calledPecletNumber,Pe,as
follows(Berg,2010,p.626):
η(Pe)−η(∞) sinh −1(Pe)
= (9.75)
η(0)−η(∞) Pe
ThisisoftenapproximatedbytheCrossequation:
η(γ˙)−η(∞) 1
= (9.76)
η(0)−η(∞) 1+(Cγ˙)p
This is reminiscent of polymers with viscosity functions like Eq. (9.14). The C is
the“Crossconstant”andthepisthe“Crossexponent.”UseComsolMultiphysicsto
solvefor1Dflowofacolloidbetweentwoflatplatesthatare1cmapart,whenthe
constantsareη(0)=0.5,η(∞)=0.01,C=2,p=0.4underavarietyofpressure
dropsfrom1to1e6.
9.26 Kirby (2010, p. 259) suggests a change of variable for problems with high Peclet
2
numbers.Theproblem
(cid:11)
∂c
+Pe
∂c
=
∂2c
, c(0,t)=1,
∂c (cid:11)
(cid:11) (cid:11) =0, c(x,0)=0 (9.77)
∂t ∂x ∂x2 ∂x
x=1
wouldbeconvertedusingc=exp(γ)to
(cid:2) (cid:3) (cid:11)
∂γ ∂γ ∂ ∂γ ∂γ(cid:11)
e γ +Pee γ = e γ , γ(0,t)=0, (cid:11) (cid:11) =0,
∂t ∂x ∂x ∂x ∂x
x=1
γ(x,0)=−10. (9.78)
Thevalue−10issimplytakenasalargenegativenumber.UseComsolMultiphysics
tosolvethisproblemonthedomainx=0,1forPe=1000using30and60elements.
```

---

## Стр. 224

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 211
Comparethesolutionwiththatobtainedfortheoriginalproblembyusingthesame
numberofelements.
9.27 Thermal flow field fractionation involves mass transfer induced by temperature
1
gradients.Considertwoflatplateskeptatdifferenttemperatures.Considertwoflat
platesseparatedby5×10−5m,keptatdifferenttemperatures.Thefluidbetweenis
atwo-componentsystem.ThetheoryisbasedonequationsfromdeGrootandMazur
(1954)andBirdetal.(2002,p.770).Themassfluxofcomponentoneisgivenby
Eq.(9.79):
j =−ρD∇c−ρD c(1−c)∇T (9.79)
1 T
wherej isthemassflux,ρisthedensityofthesolution,Disthediffusioncoefficient
1
of the solute in the solvent, c is the mass fraction of the solute (component 1) in
the solvent (component 2), D is the thermal diffusion coefficient, and T is the
T
temperature.Ifthesoluteisdilute,thisreducesto
j =−ρD∇c−ρD c∇T (9.80)
1 T
Dividing by the average molecular weight of the mixture (assumed constant in a
dilute system) converts this to molar flux. The problem is to solve the following
equationforthedilutesystem:
∂T ∂c
ρC =k∇2T, =∇·[D∇c+D ∇T] (9.81)
p ∂t ∂t T
Theleftsurfaceisat308K,therightoneisat298K.Theinitialtemperatureis298
K and the initial relative mass fraction was 1.0. This is a dimensionless value, the
actualmassfractiondividedbyitself.
9.28 Flowthroughapartiallysaturatedsoilisoftendescribedmacroscopicallyusingthe
2
followingequation(foronedimension):
∂ ∂(ρq)
(ρφS)=− (9.82)
∂t ∂x
where ρ is the density (kg/m3), φ is the porosity of the rock/soil, and S is the
saturation, defined as the fraction of free space that is occupied by water. The
combination ρφS is the mass density per system volume. The mass flux is ρq in
unitsofmassofwaterperunittimeperunittotalcross-sectionalarea(kg/m2s);qis
thevolumetricflux(avelocity,m/s).Themassfluxisrelatedtothepressuregradient
byDarcy’slaw
(cid:2) (cid:3)
ρk ∂p
ρq =− −ρg (9.83)
μ ∂x
In this equation, k is the permeability (m2), μ is the viscosity of the liquid
(kg/ms), p is the pressure (Pa), and g is the acceleration of gravity (m/s2).
w
```

---

## Стр. 225

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
212 TRANSPORTPROCESSESINONEDIMENSION
Themassbalanceis
(cid:13) (cid:2) (cid:3)(cid:14)
∂S ∂ k ∂p
φ = −ρg (9.84)
∂t ∂x μ ∂x
Thesaturationandpermeabilitydependonthecapillarypressure.Here,weconsider
waterindrysoil,inwhichthevoidvolumenotfilledwithwaterisfilledwithairata
constantpressure.Thecapillarypressureisp = p − p,whichcanbereducedto
c air
p =−psincepairisconstant.Thesaturationtimederivativeisthen
c
(cid:13) (cid:2) (cid:3)(cid:14)
∂S dS ∂p dS ∂p ∂ k ∂p
=− sothat −φ = −ρg (9.85)
∂t dp ∂t dp ∂t ∂x μ ∂x
c c
Theequationismadenondimensionalusing
p k x t φLμ
p (cid:2) = , k = , x (cid:2) = , t (cid:2) = , t = ,
ρgL r k L t c k ρg
(cid:2)0 (cid:3) c 0
dS ∂p(cid:2) ∂ ∂p(cid:2) ∂k
− = k − r (9.86)
dp(cid:2) ∂t(cid:2) ∂x(cid:2) r∂x(cid:2) ∂x(cid:2)
c
The dependence of S and k on p is empirical and must be determined from
r c
measurements of the soil in question. The following formulae were developed to
model very dry soil of the type in Richland, Washington, where nuclear waste is
stored:
1 S−S 1
k = , r = (9.87)
r 1+(p(cid:2)L/B)λ 1−S 1+(p(cid:2)L/A)η
c r c
Forthissoiltheparametersarek =0.50πm,φ =0.485,S =0.32,A=231cm,
r r
B=146cm,η=3.65,λ=6.65.Solveaproblemforasoilofheight100cminitially
at p/ρg = −1000 cm (the lower the value the drier the soil). In nondimensional
terms, solve for x = 0 to 0.4 (the solution never gets past that point). Let the left
handside(top)beatp (cid:2) =−0.01(almostsaturated),theinitialconditionbep (cid:2) =
c c
−10(verydry)andhavezerofluxouttheright-handside.First,solvetheproblem
withoutgravityandthenincludegravity.
9.29 Solvethesimplifiedpressureswingadsorptionproblem,Eq.(9.46).Forthepurposes
2
ofthisproblem,reasonablevalueswillbetakenfortheparameters,andtheLangmuir
formulaforadsorptionofapurecomponentmodelsthatinSircarandGolden(2010).
First, plot the equilibrium concentration versus pressure for pressures from 0.1 to
100 atm. Next, solve the example problem, linear adsorption. Finally, change that
problemtoinvolveonenonlinearLangmuirisotherm.Runthattoverifythatthebasic
formatofyourmodeliscorrect.ThenaddseveralTransportequationssothatthere
arefourmolefractionsandfouradsorbentconcentrations.Fortheconcentrationon
thesolid,useadiffusivityofzeroandno-fluxboundaryconditionsateachend.Begin
the calculation with nothing adsorbed and integrate until t(cid:2) = 1 when the column
pressureis20atm.Lookatthegasmolefraction,theconcentrationontheadsorbant,
andthebreakthroughcurve(concentrationsattheexitversustime).ForCO ,CH ,
2 4
```

---

## Стр. 226

```text
P1:OTA/XYZ P2:ABC
JWBS084-c09 JWBS084-Finlayson May26,2012 14:43 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 213
CO, and H , the values of a are (mmol/g atm): 4, 1.6, 0.4, 0.03. The values of b
2
(atm−1)are0.188,0.172,0.068,0.Theinletmolefractionsare0.2,0.04,0.02,0.74.
SolvewithPe=1000,coeff=7.7andkL/v=0.05.
i
NumericalProblems(SeeAppendixE)
9.30 SolveProblem9.17usingafinitedifferencemethodinExcel.
1
9.31 SolveEq.(9.26)usingafinitedifferencemethodinExcelwiththeparametersused
1
toprepareFigure9.13.
9.32 SolveEq.(9.28)usingafinitedifferencemethodinspaceandtheEulermethodin
2
timefort=0to1.ProgramitinExcel.
9.33 Solvetheproblemofstart-upflowinapipeusingthefinitedifferencemethodinspace
2
andode45inMATLABfortime.UsetheparametersusedtocreateFigure10.13.
9.34 Investigatetheaccuracyofthefiniteelementmethodappliedtothereaction-diffusion
2
problem,Eq.(9.25)whenα=20andK=2.Todothis,startwithlineardiscretization
and solve the problem on increasingly dense meshes. Keep a record of the flux at
ther=1andthenumberofdegreesoffreedom.Thendothisagainwithquadratic
discretization,thenwithcubicdiscretization.
Whatistheexactsolution?Plotthefluxversusmeshsizeanddegreesoffreedom.
As an additional test, calculate the absolute value of the residual, too. This is the
differentialequationwiththefiniteelementsolutionputintoit.Thegoalistomake
itzero,butthiswilloccuronlyforaninfinitenumberofdegreesoffreedom.Forthis
problemtheresidualis
Residual=crr+2∗cr/r −alpha∗c/(1+K ∗c) (9.88)
Whenyouuselineardiscretizationthesecondderivativeswillnotbedefined.Inte-
gratetheabsolutevalueoftheresidualovertheentiredomain;theresidualwillbe
oscillatingaroundzerosotheabsolutevalueisnecessary.
```

---

## Стр. 227

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
10
FLUID FLOW IN TWO AND
THREE DIMENSIONS
Mostchemicalprocessesinvolvefluidsflowinginturbulentflow.However,polymermelts
(theprecursorstoplastics)aresoviscousthattheyflowinlaminarflow.Inmodernchem-
ical engineering, there are more and more applications in small devices in which lami-
nar flow prevails. In microfludics, these devices may be used for detection of biological
or chemical weapons (after the payload is dispersed into the air), for medical diagnos-
tics for cheap and rapid measurements, and for analytical tools used in process control.
There are even applications where whole chemical processes are done on a microscale.
This may be advantageous because the temperature can be carefully controlled (making
a certain reaction possible), or the conversion can be increased due to precise mixing
(minimizing waste products and recycle streams), or it may be advantageous to have
distributed manufacture for safety reasons. In microfluidics, the dimensions of the chan-
nels are 1 mm or less and the cross sections of the channels are square or rectangular
(so they are no longer called pipes), and the flow is laminar even in complex geome-
tries. Thus, it is worthwhile to learn how to solve laminar flow problems in complex
geometries.
Two methods are used in commercial computational fluid dynamics (CFD) codes: the
finitevolumemethodandthefiniteelementmethod.Toabeginner,itprobablymakeslittle
differencewhichmethodisused.Theauthorhasusedfiniteelementmethodsforfluidflow
forover35years,andthatisthemethodusedinComsolMultiphysics,whichistheCFD
programillustratedhere.
What does matter, though, is the difference between laminar and turbulent flow. A
commonmisconceptionisthatifyouseevortices(swirlingmotion),theflowisturbulent.
That is not necessarily true. In turbulent flow, there are fine-scale oscillations on time
IntroductiontoChemicalEngineeringComputing,SecondEdition.BruceA.Finlayson.
©2012JohnWiley&Sons,Inc.Published2012byJohnWiley&Sons,Inc.
215
```

---

## Стр. 228

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
216 FLUIDFLOWINTWOANDTHREEDIMENSIONS
scalesof0.1ms,andspatialfluctuationsonthescaleof30μm(30×10−6 m,or3%ofa
millimeter).Tomodelturbulentflow,oneoptionisdirectnumericalsimulation(DNS).In
DNS,theNavier–Stokesequationsareintegratedintimeonaverysmallspatialscale,with
millionsofnodes;thisisfundamental(noassumptionsaremade),butitisalsoverytime
consuming.ADNSsimulationforevensimpleproblems,suchasturbulentflowinapipe),
maytakehoursforanetworkofafewcomputerstosimulatewhathappensinsecondsin
reality.Thecomputerneedstosolveforthreefluctuatingvelocitiesonaverysmallspatial
scaleandasafunctionoftime.Toovercomethisproblem,commercialCFDcodesusek-ε
models, which introduce new variables representing the turbulent kinetic energy (k) and
rateofdissipation(ε),andaddequationstopredictthem.Thecommercialcodesthensolve
for the time-averaged velocities and use k and ε to represent the effect of the fluctuating
velocitieswithoutsolvingthefluctuatingvelocities.Theequationshaveseveralempirical
parameters that have been determined by comparison with experimental data, but these
parameterschangedependingonthetypeofflow,andsomeuncertaintyexistsinrealistic
situations.Thek-ε modelalsoinvolvessteepboundarylayersnearsolidsurfaces,andthe
CFDcodestrytotakethatintoaccountanalytically.Tosummarizethek-εmodel:itcontains
empiricismbutisrelativelyfasttocomputewith.Thereisanintermediatemethod—large
eddysimulation(LES)—whichismorereliablethanthek-ε modelsandusesparameters
from DNS studies, but it, too, involves lengthy calculations, somewhere between DNS
andk-ε.
Thischapterfocusesonfluidflow,leavingthecombinationoffluidflow,heattransfer,
and diffusion to Chapter 11. Examples of fluid flow include entry flow into a pipe, flow
in a microfluidic T-sensor, turbulent flow in a pipe, time-dependent start-up of pipe flow,
flowinanorifice,andflowinaserpentinemixer.Theexamplesdemonstratemanyofthe
techniquesthatareusefulintheprogramComsolMultiphysics.
InstructionalObjectives: Afterworkingthroughthischapter,youwillbeableto
1. Modellaminarfluidflowintwo-dimensional(2D)andthree-dimensional(3D)situ-
ations,includingaxisymmetricgeometries.
2. Seehowtomodelturbulentflow,whichdependsonthespecificmodulesofComsol
Multiphysicsinyourinstallation.
3. Settheoptionsyouneed:unitsanddiscretization.
4. Applyvariousboundaryconditions,includingperiodicboundaryconditions.
5. Handlevariableviscosity,dependinguponshearrate(non-Newtonianfluidandcol-
loids).
6. Makeavarietyofplots(velocity,streamlines,arrowplots,pressureplots)andcalcu-
latepropertiesofthesolution(averagevaluesatboundaries).
7. Use the parametric solver to compute a number of solutions with one parameter
changing.
8. Checkyoursolutionforcontinuityofflow.
9. Learntousecouplingvariablestosolveforafullydevelopedvelocityintwodimen-
sionsthatisusedforaninletvelocityina3Dproblem.
Inaddition,youwillbeintroducedtothefieldofmicrofluidics.
```

---

## Стр. 229

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
MATHEMATICALFOUNDATIONOFFLUIDFLOW 217
MATHEMATICALFOUNDATIONOFFLUIDFLOW
Navier–StokesEquation
TheflowequationsaretakenhereastheNavier–Stokesequations,withsomeextensionsto
purelyviscousnon-Newtonianfluids.Invectorform,theNavier–Stokesequationis
∂u
ρ +ρu·∇u=−∇p+μ∇2u (10.1)
∂t
This vector equation applies to the case when the gravitational term is absorbed into the
pressure.Italsotakesthedensityasconstant,leadingtoanincompressiblefluid:
∇·u=0 (10.2)
Forsteadyflows,theequationreducesto
ρu·∇u=−∇p+μ∇2u (10.3)
IncomponentnotationinCartesiangeometryandtwodimensions,theseequationsare
(cid:2) (cid:3) (cid:2) (cid:3)
∂u ∂u ∂u ∂p ∂2u ∂2u
ρ +u +v =− +μ +
∂t ∂x ∂y ∂x ∂x2 ∂y2
(cid:2) (cid:3) (cid:2) (cid:3)
∂v ∂v ∂v ∂p ∂2v ∂2v
ρ +u +v =− +μ + (10.4)
∂t ∂x ∂y ∂y ∂x2 ∂y2
∂u ∂v
+ =0
∂x ∂y
Because the program Comsol Multiphysics includes all these terms, you merely need to
definetheproblemyouwanttosolve.
When evaluating pressure, one complication in the finite element method is a mathe-
maticalconditionsayingthattheapproximatingfunctionsforpressurehavemorerestricted
choicesthanthoseforvelocity.ThisiscalledtheLBBcondition[namedafterLadyshen-
skaya,Brezzi,andBabuska(Greshoetal.,1998,p.593)],andthedesignersofthecomputer
programhavetakenitintoaccountforyou.Avarietyofconsistentmethodsofdiscretiza-
tionareincludedinComsolMultiphysics.Anotherfeatureofthefiniteelementmethodis
thatthecomputerproblemcangetverylarge.Oftenyouwillhavetomakecompromises
betweentheaccuracyyouwouldlikeandhowlongyouarewillingtowaitforasolution.
Withmoderncomputers,thisisnotasbigaproblemasitoncewas,butincomplicated3D
casesitisstillaconcern.Thus,oneaspectofyoursolutionmethodwillbemeshrefinement
toestimatetheaccuracy.
Thefiniteelementmethodintwoandthreedimensionsissimilartothefiniteelementin
onedimension,exceptthebookkeepingisharder.Butagain,ComsolMultiphysicsdoesthat
bookkeepingforus.Foronetypeofelement(thereareseveralchoices),thedomainofthe
problemiscoveredbysmalltriangles(intwodimensions)orsmalltetrahedrons(inthree
dimensions),andoneachtriangle(ortetrahedron)thedependentvariable(uorv velocity
or w) is approximated by a polynomial, even a straight line along the boundary. In two
```

---

## Стр. 230

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
218 FLUIDFLOWINTWOANDTHREEDIMENSIONS
dimensions,theapproximationisatriangularpatchlookinglikeageodesicdome.Engineers
andscientistshavedeterminedhowtomaketheapproximationsatisfytheequationsasbest
aspossible,butthatisbeyondthescopeofthisbook;seeAppendixEforabriefdescription
of the finite element method. When the solution is represented this way, you need to
recognizethatyouhaveintroducedanapproximation,andthesolutionisnobetterthanthe
mesh(orsetoftrianglesortetrahedrons)allows.Thus,youwillusuallysolvetheproblem
onmorethanonemesh,eachonemorerefinedthanthelast,toensurethattheresultsdo
notdependuponthemesh.
Non-NewtonianFluid
For purely viscous non-Newtonian fluids, the viscosity is a function of shear rate, as
illustratedinChapter9,andthesteady-stateequationmustbewrittenas
ρu·∇u=−∇p+∇·[η(∇u+∇uT)]
(cid:2) (cid:3) (10.5)
1
η= f (cid:6):(cid:6) , (cid:6)=∇u+∇uT
2
(cid:4)(cid:2) (cid:3) (cid:2) (cid:3) (cid:5) (cid:6) (cid:7)
1 ∂u 2 ∂v 2 ∂u ∂v 2
((cid:6):(cid:6))=2 + + + (10.6)
2 ∂x ∂y ∂y ∂x
Theexpressionfortheshearratein2Dflow,Eq.(10.6)isobtainedfromBirdetal.(2002,
p.849).TheexpressionforcylindricalgeometryisEq.(10.7):
(cid:4)(cid:2) (cid:3) (cid:2) (cid:3) (cid:5) (cid:6) (cid:7)
1 ∂v v2 ∂v 2 ∂v ∂v 2
((cid:6):(cid:6))=2 r + r + z + r + z (10.7)
2 ∂r r2 ∂z ∂z ∂r
NotethenotationisdifferentfromthatusedinComsolMultiphysics.Withthetransforma-
tion
∂v ∂v ∂v ∂v
v →u, v →v, r →ur, r →uz, z →vr, z →vz (10.8)
r z ∂r ∂z ∂r ∂z
thisis
(cid:8) (cid:9)
1((cid:6):(cid:6))=2 ur2+(u/r)2+(vz)2 +[uz+vr]2 (10.9)
2
TheshearrateisalsodefinedinComsolMultiphysics.Tofindoutwhatitiscalled,goto
Results,chooseaplot,chooseexpressions,andlookfor“shearrate.”Hereitismod1.spf.sr.
Thus,onecaneitherdefinetheshearrateasshowninEq.(10.9)orusemod1.spf.sr.
ThischaptergivesseveralillustrationsapplyingthefiniteelementmethodusingComsol
Multiphysics.Onedecisionyoumustmakeiswhethertosolvetheequationindimensional
form or nondimensional form. The dimensional form will solve one problem at a time,
whereas the nondimensional form will be solving an infinite number of problems each
simulation.Thenondimensionalformalsoallowsyou(forcesyou)toconsidertherelative
importance of different phenomena for your problem. Three-fourths of the problems in
```

---

## Стр. 231

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
NONDIMENSIONALIZATION 219
the classic transport book, Transport Phenomena (Bird et al., 2002) are formulated in a
nondimensional format, for example. On the other hand, if you are modeling a specific
device, as you would when working for a company, the more general nondimensional
formisnotasnecessaryandyoumayusethedimensionalform.Bothareillustratedhere,
butmostoftheexamplesareinanondimensionalformat.Shownbelowisthemethodto
make the problem nondimensional and instructions aregiven for doing this withComsol
Multiphysics,too.
NONDIMENSIONALIZATION
This section takes the dimensional Navier–Stokes equation, Eq. (10.10) and derives two
differentdimensionlessversions:
∂u
ρ +ρu·∇u=−∇p+μ∇2u (10.10)
∂t
Thevelocity,pressure,anddistancearemadedimensionlessbydividingthembyaconstant
standardforvelocity,pressure,anddistance.Thenondimensionalvariableisdenotedbya
prime:
u p x 1
u (cid:4)= , p (cid:4)= , x (cid:4)= , ∇(cid:4)=x ∇ oru=u u (cid:4), p=p p (cid:4), x=x x (cid:4), ∇= ∇(cid:4)
s s s s
u p x x
s s s s
(10.11)
The variables are substituted into the Navier–Stokes equation, Eq. (10.10); note that the
dimensionalstandardsareconstantsandcanbetakenthroughthedifferentials:
ρu ∂u(cid:4) ρu2 p μu
s + su (cid:4)·∇(cid:4) u (cid:4) =− s∇(cid:4) p (cid:4)+ s∇(cid:4)2u (cid:4) (10.12)
t ∂t(cid:4) x x x2
s s s s
OptionOne:SlowFlows
This option is especially useful for slow flows such as those that occur in microfluidics,
sincethentheinertialtermsaremultipliedbytheReynoldsnumber,whichissmallandthe
termcanoftenbeneglected.MultiplyEq.(10.12)byx2/μu togive
s s
ρx2∂u(cid:4) ρu x p x
s + s s u (cid:4)·∇(cid:4) u (cid:4) =− s s∇(cid:4) p (cid:4)+∇(cid:4)2u (cid:4) (10.13)
μt ∂t(cid:4) μ μu
s s
Choose the pressure standard so that the coefficient of the pressure gradient term is 1.0;
makeasimilarchoiceforthetimestandardtoget
p x μu ρx2 ρx2
s s =1, or p = s, s =1 or t = s (10.14)
μu s x μt s μ
s s s
```

---

## Стр. 232

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
220 FLUIDFLOWINTWOANDTHREEDIMENSIONS
ThenthenondimensionalNavier–Stokesequationis
∂u(cid:4) ρu x
+ Reu (cid:4)·∇(cid:4) u (cid:4) =−∇(cid:4) p (cid:4)+∇(cid:4)2u (cid:4), Re= s s (10.15)
∂t(cid:4) μ
Analternativeistouseadifferentstandardfortime,
x ρx2 ρu x
t = s, giving s = s s = Re (10.16)
s u μt μ
s s
inwhichcasethenondimensionalNavier–Stokesequationis
∂u(cid:4)
Re + Reu (cid:4)·∇(cid:4) u (cid:4) =−∇(cid:4) p (cid:4)+∇(cid:4)2u (cid:4) (10.17)
∂t(cid:4)
Ifyouwantthepressureinpascals,takethenondimensionalpressure(fromthecomputer)
andmultiplyitbythepressurestandard:
μu
p = p p (cid:4) = s p (cid:4) (10.18)
s
x
s
OptionTwo:High-SpeedFlows
ThisoptionismostapplicableforahighReynoldsnumber.MultiplyEq.(10.12)byx /ρu2
s s
togive
x ∂u(cid:4) p μ
s +u (cid:4)·∇(cid:4) u (cid:4) =− s ∇(cid:4) p (cid:4)(cid:4)+ ∇(cid:4)2u (cid:4) (10.19)
t u ∂t(cid:4) ρu2 ρu x
s s s s s
The symbol p(cid:4)(cid:4) is used now for Option Two. Choose the pressure standard so that the
coefficient of the pressure gradient term is 1.0 and make a similar choice for the time
standard:
x x p
s =1, t = s or s =1, or p =ρu2 (10.20)
t u s u ρu2 s s
s s s s
ThenthenondimensionalNavier–Stokesequationis
∂u(cid:4) 1
+u (cid:4)·∇(cid:4) u (cid:4) =−∇(cid:4) p (cid:4)(cid:4)+ ∇(cid:4)2u (cid:4) (10.21)
∂t(cid:4) Re
Ifyouwantthepressureinpascals,takethenondimensionalpressure(fromthecomputer)
andmultiplyitbythepressurestandard:
p = p p (cid:4)(cid:4) =ρu2p (cid:4)(cid:4) (10.22)
s s
```

---

## Стр. 233

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:ENTRYFLOWINAPIPE 221
By comparing Eq. (10.17) with Eq. (10.21) you see that the two different dimensionless
pressuresarerelatedby
p (cid:4) = Rep (cid:4)(cid:4) (10.23)
Itiseasytoshowthatthepressureinpascalsisthesameinbothoptions.Thedimensional
pressuredropinOptionOneisgivenbyEq.(10.18).Thisisalso
μu ρu2 ρu2 μu
(cid:6)p = p (cid:6)p (cid:4) = s(cid:6)p (cid:4) = s(cid:6)p (cid:4), since s = s (10.24)
s
x Re Re x
s s
ThedimensionalpressuredropinOptionTwoisgivenbyEq.(10.22).ByusingEq.(10.23)
youget
ρu2
(cid:6)p =ρu2(cid:6)p (cid:4)(cid:4) = s(cid:6)p (cid:4) (10.25)
s Re
whichisthesameasEq.(10.24).
Thereasonforhavingbothofthemisthatforslowflowsthedimensionlessresultoften
does not depend upon the Reynolds number and for high-speed flows the convergence
is better in the form of Eq. (10.21). In this book, we mainly use Option One, but some-
times convert the results to Option Two for comparison with the literature. In Comsol
Multiphysics, to use the nondimensional version we must change the units to “none” in
Preferences. Once you have solved a nondimensional equation, to get the results in units
foraspecificcase,youmustidentifyforyourcasethestandardsusedtomaketheequation
dimension, such as distance (e.g., a radius and length), and a velocity (average velocity
somewhere,where?).
EXAMPLE:ENTRYFLOWINAPIPE
Next, consider entry flow into a pipe as illustrated in Figure 10.1. The flow is taken as
uniform in radius at the entrance (taking the value 1.0 at each radial position), and the
velocityhastodevelopintoitsfullydevelopedprofile.Thepiperadiusistakenas0.5.How
fardownstreamdoyouhavetogotogetafullydevelopedsolution?(Anotherwaytopose
thisquestionishowmucherrordoyoumakeifyouassumefullydevelopedflowwhenit
isnot?)AsdiscussedintheintroductiontoChapter9,themajorstepsforapplyingComsol
Multiphysicsaretoopenit,choosetheproblemwewishtosolve,setourpreferences,create
a geometry, identify parameter values, choose and set the boundary conditions, create a
mesh,solvetheproblem,andthenexaminethesolution.Thesestepsaredescribedcarefully
inthisfirstexample,butbesuretoreviewtheiconsinFigures9.2–9.4.
Step 1 (Open and Set Preferences) Open Comsol Multiphysics and choose 2D
axisymmetric in the Model Wizard and click the next arrow. Then open “Fluid Flow”
and “Single Phase Flow” and choose “Laminar Flow,” click the next arrow. The Settings
windowwillhavealistofPresetoptions;selectStationaryandthenclicktheFinishflag.
ThenodesattheleftofthescreenarecalledtheModelBuilderandtheyprovideaguideto
thenecessarysteps.
```

---

## Стр. 234

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
222 FLUIDFLOWINTWOANDTHREEDIMENSIONS
z, v
r = 0 r, u
FIGURE 10.1 Entryflowintoapipe.
WewillinturnusetheModel1,Study1,andResultsnodes.Notetheiconsatthetop,
right. The second one from the left is to “show” additional things, and we choose “Dis-
cretization”and“EquationView.”Intherootnodewecanchooseasystemofdimensions
inthesettingswindow;fortheUnitSystemchoose“none.”
Step 2 (Define the Geometry) Open the Model 1 node by clicking on the arrow to the
lefttoexpandthisnode.ThenrightclickontheGeometrynodeandchooseRectangle.Set
thewidthto0.5andtheheightto2.Thenclickthe“build”iconatthetopofthesettings
window.
Step3(DefinetheProblem) WiththeModel1nodeopen,clickonthe“LaminarFlow’
nodeandchangetheCompressibilityoptiontoIncompressibleflowinthesettingswindow.
Openthe“LaminarFlow”nodeandselect“FluidProperties.”Clickonthedomain,the+
toaddthedomaintotheSelectionBoxifitisnotselected.Changethedensityandviscosity
toUserdefined,withρ =10,μ=1.
Step4(SettheBoundaryConditions) RightclickLaminarFlowandchooseInlet.Select
theboundary2and+toaddittotheSelectionbox;setthenormalvelocityto1.0.Right
clickLaminarFlowandchooseOutlet.Selecttheboundary2,then+toaddittothebox;
andchangetheboundaryconditionfromPressure,noviscousstress(sinceweknowthere
is viscous stress in fully developed flow) to Pressure, p = 0. The centerline boundary
0
conditionisautomaticinaxisymmetricgeometry(symmetryaboutr=0),andallowsslip,
and the default boundary condition is velocity zero, which is appropriate for the wall at
r = 0.5. A neutral boundary is one through which flow occurs but without our placing
specificconditionsonit(likeaholeintoanotherdomain).
Step5(CreateaMesh) Choose“Mesh1”andtheSettingswindowforElementSizewill
appear. Accept “Normal” and then click the Build icon. A mesh will be created in your
```

---

## Стр. 235

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:ENTRYFLOWINAPIPE 223
(a) (b) (c)
FIGURE 10.2 (a)Mesh,(b)arrowplot,and(c)streamlinesforentryflowintoapipe.
domain (see Figure 10.2a). If you forget this step, it will be performed automatically for
youwhenyousolvetheproblem.
Step6(SolvetheProblem) Choose“Study1”andrightclick=.Afteramoment,acolor
plotofthevelocitymagnitudewillappearintheGraphicsWindow.Whatisplottedisthe
valueofU=sqrt(u2+w2).
Step7(ExaminetheSolution) Toobtainmorespecificinformation,rightclickResults,
choose“2DPlotGroup,”rightclick“2DPlotGroup2”andchooseArrowSurface.Click
theploticontoseethearrowplot(Figure10.2b).Also,rightclickagain“2DPlotGroup
2”andchoosestreamline;choosea“StreamlinePositioning”andclicktheploticontoget
thestreamlineplot(seeFigure10.2c).
```

---

## Стр. 236

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
224 FLUIDFLOWINTWOANDTHREEDIMENSIONS
2
1.5
1
0.5
0
0 0.1 0.2 0.3 0.4 0.5
r
yticoleV
Outlet
Inlet
FIGURE 10.3 Velocityatinletandoutlet.
Step8(MakeMorePlots) TheinletvelocityisfoundbyrightclickingResults,choosing
“1DPlotGroup.”Rightclickthatandchoose“LineGraph.”Thenselectboundary2,change
the “X-Axis Data Expression” to r, and click the plot icon. The result is a step function.
Changethetitleandaxislabelsto“InletVelocity,”randw(seeFigure10.3).Thevelocity
isnotexactly1.0forallradiiattheinlet,becausethereisadiscontinuityintheboundary
conditions.Theboundaryconditionsusev=1ononeboundaryandv=0onanadjoining
boundary,andtheprogramhastochoosewhichonetouseatthecorner.Comsoldoesagood
jobofsatisfyingtheseconflictingconditions.(Itisnotpossibletoachievethoseboundary
conditionsphysically.)Repeatthisprocedureunderthesame“PlotGroup”butchoosethe
outlet boundary (see Figure 10.3). To see the approach to fully developed flow, plot the
axialvelocityalongthecenterline.RightclickResults,choose“1DPlotGroup.”Rightclick
“1DPlotGroup”andselect“LineGraph,”thenselectboundary1,thecenterline,thenthe
+toaddittotheSelectionbox.Changethe“X-AxisDataParameter”to“Expression,”z.
ChangethetitlesandaxislabelsandclicktheploticontogetFigure10.4.
Step 9 (Improve the Solution) There is a small increase in the centerline velocity near
theexit;thisisnotavalidsolution.Thereasonisthatthefiniteelementfunctionsarelinear
functions.Forlaminarflows,quadraticfunctionsusuallygivebetterresults.ClicktheShow
button (see Figure 9.2) and click Discretization. Then go back to Laminar Flow; there is
nowanoptionforDiscretizationoffluids.Thedefaultvalueis“P1+P1,”whichmeansthat
boththevelocityandthepressureareapproximated withlinearelements.Change thatto
“P2+P1”;thenthevelocityisapproximatedwithquadraticelements.RightclickStudy=
togetthenewsolution.Selectthe“LineGraph”thathasthecenterlinevelocityplottedand
youseethattheuptickattheendhasdisappeared.Figures10.3and10.4aremadewiththis
solution.
Step 10 (Calculate Average Properties) To calculate average quantities, right click on
DerivedValues(underResults)andselect“Integration/LineIntegration.”Clickontheinlet
boundary 2, then + to add it to the Selection box and choose to integrate velocity. Click
```

---

## Стр. 237

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:ENTRYFLOWINAPIPE 225
2
1.8
1.6
1.4
1.2
1
0 0.5 1 1.5 2
z
yticolev
enilretneC
FIGURE 10.4 Centerlinevelocityinpipeflow.
thebox“IncludeSurfaceIntegral”in“IntegrationSettings”andthen=(atthetop)toget
thevalue.ItislistedinResultsas0.7846.Ifyouwonderwhethertheintegrationhasbeen
doneusingrdr orjustdr,changetheexpressionto1andclickthe=sign.Thevaluethat
appearsis0.7846,whichistheareaofacirclewithradius0.5:
(cid:10)R
π
2π rdr =πR2 = =0.7854 (10.26)
4
0
Thus, the 2πrdr is included automatically and the average velocity is 0.7846/0.7854 =
0.9990.Thisisnotquite1.0duetothediscontinuityoftheinletvelocityatthewall.
100
10−1
10−2
10−2 100 102 104
)s
aP(
ytisocsiV
Shear rate (s−1)
FIGURE 10.5 Viscosityofashear-thinningfluid.
```

---

## Стр. 238

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
226 FLUIDFLOWINTWOANDTHREEDIMENSIONS
Step11(Report) Todocumentyourwork,saveapictureofthedomainandmesh;dothis
byclickingthecamera,thenBrowse,giveaname,thenSave,thenOK.Besuretogivethe
dimensions,identifytheboundaryconditions,givevaluesofparametersyouused,listhow
manyelementsanddegreesoffreedomwereused,andindicatehowsolutionswithdifferent
numberofelementscompare.Thengivetheresultsandindicatewhytheyarereasonable.
Next,changetheproblemslightlyandtaketheinletvelocityasthefullydevelopedvelocity
profile:
(cid:11) (cid:2) (cid:3)(cid:12)
r2
v(r,0)=2 1− (10.27)
0.5
Step 12 (Solve Again) Use a fully developed inlet velocity. This is inserted in Laminar
Flow,asthevvelocity:
2∗(1−(r/0.5) ∧ 2) (10.28)
Thestreamlinesarenowstraight.
EXAMPLE:ENTRYFLOWOFANON-NEWTONIANFLUID
Next, consider the entry flow of a non-Newtonian fluid, essentially the same problem as
before,exceptwithadifferentfluid.Theonlythingyouneedtochangeistheexpression
for viscosity, which is no longer constant. The shear viscosity is modeled as a Carreau
function,whichisaslightextensionofEq.(9.14):
η−η (cid:8) (cid:9)
∞ = 1+(λγ˙)2 (n−1)/2 (10.29)
η −η
0 ∞
Theη ∞,η
0
,λ,andnareallparametersthatareusedtofitdata,takenhereasη
∞
=0.05,η
0
=
0.492,λ=0.1,andn=0.4.AplotoftheviscosityversusshearrateisgiveninFigure10.5.
For small shear rates, the viscosity is essentially constant, as it is for a Newtonian fluid.
For extremely large shear rates, the same thing is true. For moderate shear rates, though,
theviscositychangeswithshearrate.Inpipeflow,orchannelflow,theshearrateiszeroat
thecenterlineandreachesamaximumatthewall.Thus,theviscosityvariesgreatlyfromthe
centerlinetothewall.ThiscomplicationiseasilyhandledinComsolMultiphysics.Once
you know how to solve the problem for a Newtonian fluid (as in Figure 10.3), there are
twomajorchangesyoumustmakeforanon-Newtonianfluid.Oneofthoseistorepresent
theviscosity,Eq.(10.29),inComsolMultiphysics.Theotheristobesmartabouthowyou
obtainaconvergedsolution.
Step1(OpenandSetPreferences) OpenthesolutionforentryflowofaNewtonianfluid
andsaveitwithanewname.
Step2(DefinetheProblem) Openthe“LaminarFlow”nodeandselect“FluidProperties.”
Changetheviscositytoeta.Wenextneedtodefine“eta.”Thatinturnrequiresdefinition
of the “shearrate.” Right click on the “Global Definitions” and click Parameters. Enter
```

---

## Стр. 239

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:FLOWINMICROFLUIDICDEVICES 227
thefollownamesandvalues:“etainf,”0.05;“eta0,”0.492;“lambda,”0.1;“n,”0.4.Goto
the “Model node 1” and right click Definitions and open Variables. Enter the following
formulas.
eta = etainf+(eta0-etainf)*(1+(lambda*gammadot)ˆ2)ˆ((n-1)/2)
gammadot2 = 2*(urˆ2+(u/r)ˆ2+wzˆ2)+(uz+wr)ˆ2
gammadot = sqrt(gammadot2).
Alternatively, use the variable mod1.spf.sr for the shear rate in place of gammadot since
ComsolMultiphysicscalculatesitautomatically.
Step 3 (Solve the Problem) In this case, change click the “Initial Value” node under
“LaminarFlow”andputinanaxialvelocityof2∗(1−(r/0.5)∧2).Thisgivestheprogram
something to work with. If one starts with an initial velocity of v = 0 (the default), the
programmayreturnamessagesayingitcannotconvergeorthatittriedtodividebyzero.
Thus, you should always obtain a solution for a Newtonian fluid first, before invoking
the non-Newtonian viscosity: simply replace the word “eta” with 1.0 or some number
appropriate to your case, solve the problem, put back the “eta,” and use the resolve op-
tion. This time the computer has a guess of a solution to work from, and a solution
isfound.
Step 4 (Check Reynolds Number) Next, check the Reynolds number, which is 390,
ensuring that the flow is laminar. The peak average velocity is 0.078 m/s, and in laminar
flowthepeakvelocityshouldbetwicethat,or0.156m/s,whichitis.
EXAMPLE:FLOWINMICROFLUIDICDEVICES
Next, consider flow in what is called a T-sensor. Two flows come together, join, and
traversedownonechannel,asillustratedinFigure10.6.Thisdeviceisusedinmicrofluidic
medicaldevices,whicharediscussedfurtherinChapter11.Here,youwillconsideronly
the flow (which has no special utility until the convective diffusion equation is added in
Chapter11).
FIGURE 10.6 FlowinaT-sensor.
```

---

## Стр. 240

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
228 FLUIDFLOWINTWOANDTHREEDIMENSIONS
Step1(OpenandSetPreferences) OpenComsolMultiphysicsandchoosetwodimen-
sions;next,LaminarFlow;next,Stationary,finish.
Step2(DefinetheGeometry) In“Model1”rightclickGeometryandchooseRectangle;
makeoneofwidth2,height0.5,basecorneratx=−0.5,y=−0.25;clickBuildAll.Do
thisagainwiththerectangleofwidth0.5,height1.5,basecorneratx=−1,y=−0.75.
Youcaneitherretaininternalboundariesornot;iftheyarethere,themeshwillbeaffected
nearthem,soiftheinternalboundarieshavenopurposeitisbestnottoretainthem.
Step3(DefinetheProblem) Openthe“LaminarFlow”node,thenthe“FluidProperties”
node.Under“FluidProperties,”changethedensitytoUserDefined,setthevalueto1.0.Do
thesamefortheviscosity.ThiscorrespondstoanondimensionalequationwithaReynolds
numberof1.
Step4(SettheBoundaryConditions) Rightclickthe“LaminarFlow”nodeandchoose
Inlet.Selectthetopboundary,+,toaddittothe“BoundarySelection”box.SettheNormal
inflow velocity to U = 1. Do this again and select the bottom boundary; set its Normal
0
inflowvelocitytoU =1.Againrightclickthe“LaminarFlow”nodeandchooseOutlet.
0
Selecttheright-mostboundary,+,toaddittothe“BoundarySelection”box.Changethe
boundaryconditionfrom“Pressure,noviscousstress”to“Pressure,withp =0”.Weknow
0
thereareviscousstresseswhenthereisflowbetweentwowalls.
Step 5 (Create a Mesh) Click the Mesh node and Build All to get the mesh (see
Figure10.7).
Step6(SolvetheProblem) ThenrightclickStudy=togetthesolution.
Step7(ExaminetheSolution) Toseethestreamlines,rightclickresultsandchoose2D
PlotGroup.ThenrightclickitandchooseStreamlines;youmayhavetomakeachoicein
“StreamlinePositioning”(seeFigure10.8).
3
7
1 5 9
6
4
2
FIGURE 10.7 MeshforflowinaT-sensor.
```

---

## Стр. 241

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:FLOWINMICROFLUIDICDEVICES 229
FIGURE 10.8 StreamlinesforflowinaT-sensor.
Step8(ValidatetheSolution) Tovalidatepartofthesolution,theoverallmassbalanceis
calculated.Rightclick“DerivedValues”underResults,choose“LineIntegration.”Then,in
turn,integratethevelocityoverboundaries2,3(input)and9(output).Dothisbyselecting
a boundary, + to put it in the Selection box, then = (at the top). Taking into account the
directionofflow(oneoftheintegralsisnegative),thesumofflowratesis0.9914inand
0.9726out.Thisisaccuratetowithin1.8%.
Step 9(Improve theSolution) There are afew ways toimprove the accuracy. The first
oneistochangethetrialfunctionsforvelocity;thedefaultchoiceislinearfunctions,butwe
canchangethemtoquadraticfunctions,whichroughlydoublesthenumberofunknowns.
DothatbyfirstselectingtheShowiconandclickingDiscretization(ifyouhavenotalready
setitinPreferences).Thenchoosethe“LaminarFlow”node,andthentheDiscretization
option(nearthebottom).Ifitisnotshowing,usethearrowatthetopoftheModelBuilder
to say Show More Options. Change from “P1 + P1” to “P2 + P1”. The flow rate in is
0.9972versus0.9971out,foranerrorof0.01%.Thesesolutionswereobtainedusing1213
elements;forP1+P1therewere2260degreesoffreedomwhereasforP1+P2therewere
8150degreesoffreedom.Thisisagoodlesson:forlaminarflowatlowReynoldsnumbers,
usingquadraticfunctionsforvelocityismuchbetterthanthedefaultfunctions(linear).
Step10(SolveforFullyDevelopedFlowIn) Ifwewantedfullydevelopedflowintothe
device,wewoulduseEq.(10.30)fortheinletprofileratherthan1.0(withtheappropriate
signatthetopandbottom):
(cid:13) (cid:14)
v =−24(x +1) x + 1 (10.30)
2
Todothat,changethetwoinletstoVelocityfieldandinserttheformulaforthey-velocity.
RightclickStudy=;nowthestreamlinescominginarestraight(seeFigure10.9).Theflow
ratesinsumto1.000andthatistheflowrateout,too,sothisisveryaccurate.
```

---

## Стр. 242

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
230 FLUIDFLOWINTWOANDTHREEDIMENSIONS
FIGURE 10.9 StreamlinesinaT-sensorwhentheinletvelocityisparabolic.
EXAMPLE:TURBULENTFLOWINAPIPE
Next,considerflowinapipeataflowratehighenoughforturbulencetooccur.Generally,
thisoccurswhenevertheReynoldsnumberisgreaterthan2200,wheretheReynoldsnumber
isdefinedintermsoftheaveragevelocityandthepipediameter:
ρ <v > D <v > D
Re= = (10.31)
μ ν
Youcansolvetheproblemwithaninletvelocitythatisflat;thus,youfindtheentrylength
it takes to achieve fully developed turbulent flow, and the velocity profile downstream is
the fully developed one. When you solve for a kinematic viscosity of 10−6 m2/s (water),
diameterof0.05m(about2inches),andavelocityof2m/s(acommonoptimalvelocity),
youwillgetaReynoldsnumberof105.
TheturbulencemodelinComsolMultiphysicsisindimensional(SI)units.Itiscontained
intheCFDmodule,whichmaynotbeavailableinyoursystem.Ifitis,turbulenceismodeled
using the k-ε model. In this model, the turbulent kinetic energy is represented by k, and
the rate of dissipation of turbulent kinetic energy is represented by ε. Furthermore, the
viscosityisaugmentedbyaturbulenteddyviscosity,whichisafunctionofkandε.Special
equationshavebeendevelopedforbothvariables,andthesemustbesolvedalongwiththe
momentumequationwhichhastheturbulenteddyviscosityinitaswell.Alltheseequations
areincludedinComsolMultiphysics.
(u·∇)u=−∇p/p+∇·[(v+v )∇u]
T
(u·∇)k =τ ∂x −ε+∇·[(v+v /σ )∇k]
ij j T k (10.32)
ε ε2
(u·∇)ε =Cε1 τ
ij
∂u
i
/∂x
j
−Cε2 +∇·[(v+v
T
/σ ε)∇ε]
k k
AlthoughCε1 andCε2 aredimensionless,theturbulentviscosity,v
T
,iscalculatedintheSI
system.Thus,alldimensionsmustbeinmeters,meterpersecond,andsoon.
```

---

## Стр. 243

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:TURBULENTFLOWINAPIPE 231
The main caution is that these equations are only an approximation of reality, and the
formulasandequationshavebeenchosentomodelexperimentaldata.Thismeansthatthey
are only as good as the data they were derived from, and the data are usually found in
relativelysimpleflows.Theexperimentsaredefinitelynoteasytocarryout,buttheyare
foridealizedsituations,suchasfullydevelopedflowinapipeorpastaflatplateorinajet.
Thus, the equations should be used with caution. Other methods in turbulence are much
moretimeconsumingandmayrequirebanksofcomputersrunningforhours.Thatworks
forresearch,butisnotsuitableforday-to-dayengineeringwork.
Step1(OpenandSetPreferences) OpenComsolMultiphysicsandchoose2D,axisym-
metric.ThenchooseFluidFlow/TurbulentFlow/TurbulentFlow,k-ε,Finish.
Step2(DefinetheGeometry) In“Model1,”rightclickGeometryandselectRectangle;
makeitawidthof0.025andalengthof0.1andclick“BuildAll.”Wearegoingtosolvethe
problemforfullydevelopedflow,sothelengthisnotimportant.Ifitistoolong,though,
lotsofelementswouldberequired,leadingtolongersolutiontimes.
Step 3 (Define the Materials) To define the materials, right click Materials and choose
OpenMaterialBrowser.ThenopenBuild-Inandchoosewaterand+toaddthematerial.
Ratherthanusingthathere,wewilluseadensityof1000kg/m3 andaviscosityof0.001
Pas,setin“TurbulentFlow,Userdefineddensityandviscosity.”
Step4(DefinetheProblem) Click“TurbulentFlow”andchangetheCompressibilityto
“IncompressibleFlow.”
Step 5 (Set the Boundary Conditions) Right click “Turbulent Flow” and choose Wall;
clickthewallboundary,+toaddittotheSelectionwindow.Rightclick“TurbulentFlow
andchoose“PeriodicFlowCondition.”Setthe“PressureDifference”to60Pa.Rightclick
“Turbulent Flow” and choose “Pressure Point Constraint.” Click one node at the exit, +,
to add it to the Selection box, and set it to zero. Since periodic boundary conditions are
being used, no velocity boundary conditions are needed except for zero velocity along
thewall.
Step 6 (Create a Mesh) Click the Mesh node and “Build All.” A mapped mesh will
requirethefewestnumberofelements.
Step7(SolvetheProblem) Thenrightclick“Study1,”=.Thesolutionmaytakeawhile
(dependingonthemeshyouhavechosen).Thestreamlinesarestraightindicatingtheflow
isfullydevelopedthroughout.
Step8(ExaminetheSolution) Theexitvelocityprofileandcenterlinevelocityareshown
inFigure10.10.Thepeakvelocityisabout2.06m/s.Thecenterlinevelocityfluctuatesa
bitaboutthevalue2.06(notethescale).TheprofilesofkandεareshowninFigure10.11.
ThepressurealongthecenterlineisshowninFigure10.12.
Step9(ExaminetheSolutionAgain) Themostimportantcheck,though,istocompare
with experimental data. To get the average velocity, right click “Derived Values” under
```

---

## Стр. 244

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
232 FLUIDFLOWINTWOANDTHREEDIMENSIONS
2.2
2
1.8
1.6
1.4
1.2
1
0.8
0 0.005 0.01 0.015 0.02 0.025
)s/m(
yticolev
laixA
Radius (m)
FIGURE 10.10 Velocityprofileforfullydevelopedturbulententryflowinapipe.
9
8
7
6
5
4
3
2
1
0
0 0.005 0.01 0.015 0.02 0.025
)3s/2m(
etar
noitapissid
tnelubruT
0.025
0.02
0.015
0.01
0.005
0
0 0.005 0.01 0.015 0.02 0.025
(a)
Radius (m)
(b)
)2s/2m(
ygrene
citenik
tnelubruT
Radius (m)
FIGURE 10.11 Turbulentkineticenergy(a)andrateofdissipation(b)forfullydevelopedturbulent
flowinapipe.
```

---

## Стр. 245

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:START-UPFLOWINAPIPE 233
60
50
40
30
20
10
0
−10
0 0.02 0.04 0.06 0.08 0.1
)aP(
erusserP
Distance (m)
FIGURE 10.12 Pressuredropinturbulentflow.
theResultsnode.Select“LineIntegration1.”Inthe“LineIntegration”panel,open“Inte-
grationSettings”andchoose“Computesurfaceintegral(axialsymmetry).”Justtotestthe
integration, change the Expression to 1.0 and choose =. The value is 0.0019635, which
isappropriateifoneisintegrating2πrdr.Thus,thecross-sectionalareais0.0019635m2.
WiththeExpressionreplacedbyspf.U,onegets0.0034715.Theaveragevelocityisthen
0.0034715/0.0019635=1.768.
Step10(ComparewithExperimentalData) Thepressuredropperlengthis60Pa/0.1
mwitharadiusof0.025m.Thewallstressisτ =7.5Pa.Thefrictionfactoristhen
w
τ w = (cid:6) 2 p L R , f = ρ < 2τ v w >2 = Lρ (cid:6) < p v R >2 =4.8×10 −3 (10.33)
ThisisabithigherthanthevalueforasmoothpipeataReynoldsnumberof8.84×104,
wheref =4.6×10−3 (PerryandGreen,2008,pp.6–10).
EXAMPLE:START-UPFLOWINAPIPE
Aclassicprobleminfluidmechanicsisthetransientdevelopmentofflowinapipe.Inthis
idealized problem, the fluid is initially at rest with no applied pressure gradient. At time
zero,apressuregradientisapplied,andflowbegins.Thevelocityisslowenoughthatthe
flowislaminar.Afteracertainamountoftime,theflowbecomessteady.
Step1(OpenandSetPreferences) OpenComsolMultiphysicsandchoose“2D,axisym-
metric.”Thenchoose“LaminarFlow;”next,“TimeDependent,”finish.
Step2(DefinetheGeometry) In“Model1,”rightclickGeometryandselectRectangle;
makeitawidthof0.0025mandalengthof0.025mandclick“BuildAll.”Wearegoingto
```

---

## Стр. 246

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
234 FLUIDFLOWINTWOANDTHREEDIMENSIONS
solvetheproblemforfullydevelopedflow,sothelengthisnotimportant.Ifitistoolong,
though,lotsofelementswouldberequired,leadingtolongersolutiontimes.
Step 3 (Define the Problem) Click “Laminar Flow,” then choose Discretization and
change to “P2 + P1.” (Use the Show icon if Discretization is not showing.) Click on
“FluidProperties”nodeandsetthedensityandviscositytoUserdefined,1000kg/m3 and
0.001Pas.
Step4(SettheBoundaryConditions) Rightclick“LaminarFlow”andchoose“Periodic
Flow Condition.” Set the pressure difference to 2.5 Pa. Right click on “Laminar Flow”
and choose “Pressure Point Constraint.” Choose apoint at theoutlet and setthepressure
p to0.
0
Step5(CreateaMesh) ChooseMeshand“BuildAll.”
Step6(SolvetheProblem) Under“Study1,”clickon“Step1:TimeDependent”toset
thetimesatwhichthesolutionwillbeplotted.Wewantasolutionfrom0to7,butwanta
finerdiscretizationinitially.Thus,useforTimes:00.10.20.30.40.50.60.70.80.91.02
34567.RightclickStudy=togetthesolution.
Step7(ExaminetheSolution) RightclickResultsandchoose“1DPlotGroup.”Right
click it and choose “Line Graph.” The velocity is chosen automatically. In the Settings
window, open Legends and mark the “Show legends” box. Click on the plot icon to get
Figure10.13.ThefigureshownwasreplottedusingMATLAB.
Step8(PlottheSolutionVersusTime) RightclickonResultsandchoose“PointPlot.”
Selectthepointatr=0,z=0,+,toaddittotheSelectionbox.Clickontheploticonto
obtainFigure10.14.Thisshowsthatsteadystateisachievedbyt=7.
0.16
0.14
0.12
0.1
0.08
0.06
0.04
0.02
0
0 0.5 1 1.5 2 2.5
Radius (m) x 10−3
)s/m(
yticoleV
t = 7
t = 3
t = 2
t = 1.0
t = 0.8
t = 0.6
t = 0.4
t = 0.2
FIGURE 10.13 Transientvelocityprofiles.
```

---

## Стр. 247

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:FLOWTHROUGHANORIFICE 235
0.16
0.14
0.12
0.1
0.08
0.06
0.04
0.02
0
0 1 2 3 4 5 6 7
)s/m(
yticoleV
Time (s)
FIGURE 10.14 Transientlaminarflowinapipe,velocityatr=0,z=0.
Step 9 (Check Reynolds Number) Next, check the Reynolds number, which is 390,
ensuring that the flow is laminar. The peak average velocity is 0.078 m/s, and in laminar
flowthepeakvelocityshouldbetwicethat,or0.156m/s,whichitis.
EXAMPLE:FLOWTHROUGHANORIFICE
Thenextproblemisflowthroughanorifice.Ifthepipeorchannelisverysmall,theflow
maybelaminar.Thisisusuallythecaseinmicrofluidicdevices.Ifthechannelissmall,the
orificewouldnotbeinfinitesimallysmall,andthewidthoftheorificemayhaveaneffect.
You will solve for the flow here, whereas in Chatpter 11 you will extend the problem to
solve for the temperature rise due to viscous dissipation. In this chapter, you assume the
viscosityisconstant.Thisproblemwassolvedbyaseniorchemicalengineering student,
FebeKusmanto,whilestudyingtheeffectoforificeswithafinitethicknesses(Kusmanto
etal.,2004).
Step1(OpenandSetPreferences) OpenComsolMultiphysicsandchoose“2D,axisym-
metric”;next,“LaminarFlow”;next,Stationary,finish.Settheunitsto“none”intheroot
node,andchangethediscretizationfrom“P1+P1”to“P2+P1.”
Step 2 (Define the Geometry) Right click on Geometry and choose Rectangle; make
one of width 3, height 16, base corner at 0,0; click “Build All.” Right click geometry
again and choose a rectangle; set the width to 2.5, height to 0.15, base corner at r = 0,
z = 3.925. This will make the diameter of the orifice hole, D, equal to 1, and thickness
of the orifice plate/diameter of the hole, L, is 0.15. Right click Geometry again, choose
“BooleanOperations”andclickDifference.Thedomainwewantisthefirstoneminusthe
secondone.
Step 3 (Define the Problem) Click on the “Laminar Flow” node, then the “Fluid Prop-
erties” node. Under “Fluid Properties,” change the density to “User defined” and set the
```

---

## Стр. 248

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
236 FLUIDFLOWINTWOANDTHREEDIMENSIONS
valueto1.0.Dothesamefortheviscosityandsettheviscosityto1/Re;thiscorrespondsto
anondimensionalequation.WewillmaketheReynoldsnumberdependonx,sorightclick
Definitions,chooseVariables,anddefineReas10∧x.
Step 4 (Set the Boundary Conditions) Right click on the “Laminar Flow” node and
choose Inlet. Select the bottom boundary, +, to add it to the “Boundary Selection” box.
Enter the z-velocity as (2/36)∗(1−(r/3)∧2). This makes the average velocity through the
orifice1.0.Rightclick“LaminarFlow”andchooseOutlet.Selectthetopboundary,+to
addittotheSelectionbox,andsettheboundaryconditiontop=0(nottheonewithzero
shearstress).
Step5(CreateaMesh) ClickontheMeshnodeand“BuildAll”togetthemeshshown
inFigure10.15.Thishas4556elementsand25,023degreesoffreedom.
(a) (b) (c)
FIGURE 10.15 Flowthroughanorifice:(a)mesh;(b)Re=1;(c)Re=101.5=31.6.
```

---

## Стр. 249

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:FLOWTHROUGHANORIFICE 237
50
40
30
20
10
0
0 5 10 15
erusserp
sselnoisnemiD
Re = 31.6
Re = 10
Re = 0,1
Distance
FIGURE 10.16 PressureprofilesforRefrom0.01to31.6.
Step6(Solve theProblem) Rightclick“Study 1” andchoose “Parametric Sweep.” We
wanttheReynoldsnumberstogofrom1toabout30;maketheReynoldsnumber=10∧x,
withxgoingfrom0to1.5.Thus,settheparameterasxin“GlobalDefinitions/Parameters”
and define the parameter values as range (0,0.1,1.5) (see Chapter 9, Section “Parametric
Solution”).Thenrightclick“Study1”=togetthesolutions.
Step7(ExaminetheSolution) Toseethestreamlines,rightclickResultsandchoose“2D
Plot Group.” Then right click it and choose Streamlines. The solution shown is for Re =
101.5(thelastparameter.ToseethesolutionforsomeotherRe,changetheparametervalue
inthe“2DPlotGrouppanel”;clicktheploticontocreatetheplot.Twosolutionsareshown
inFigure10.15.Figure10.15bandcshowsthestreamlinesattwoReynoldsnumbers.This
figureillustratesthefactthatrecirculationoccurs,andtheregionofrecirculationincreases
astheReynoldsnumberincreases,eventhoughtheflowisstilllaminar.Figure10.16shows
thecorrespondingpressureprofiles.Thepressurechangesoccurveryneartheorifice,and
the pressure drop is almost entirely caused by the orifice with only a small contribution
from fully developed flow in the tube. As the Reynolds number increases, the pressure
reducesaftertheorifice.Then,itgraduallyreturnstoahighervalueintheregionknownas
thevenacontracta.
Figure10.17showsthepressuredropasafunctionofReynoldsnumber.Theseresults
areplottedintwoways,correspondingtothetwodifferentwaystonondimensionalizethe
equations.TheoneinFigure10.17aismostsuitableforslowspeedlaminarflow,because
thepressuretermplottedisconstantwithReynoldsnumberoverquitearange.Theonein
Figure10.17bismostsuitableforhighReynoldsnumbersbecausethatformofthepressure
termisconstantoncetheReynoldsnumbergetshighenough.Figure10.17balsolookslike
atypicalfrictionfactorplot.Bothcurves,however,givethesamevalueofpressuredropin
pascals,andtheplottedcoefficientsarerelatedbyEq.(10.34):
(cid:6)p Re (cid:6)p ρ <v > D (cid:6)pD
= = (10.34)
1ρ <v >2 2 ρ <v >2 μ μ<v >
2
```

---

## Стр. 250

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
238 FLUIDFLOWINTWOANDTHREEDIMENSIONS
104
103
102
101
100
10−2 100 102 104
Reynolds number
>v<
ρ/pΔ2
103
102
101
10−2 100 102 104
Reynolds number
>v<μ/D
pΔ
(a)
(b)
FIGURE 10.17 Dimensionlesspressuredropinorifice:(a)preferredplotforlowReynoldsnum-
ber;(b)preferredplotforhighReynoldsnumber.
ThedottedlineistheanalyticalsolutiontoStokesflowbyDaganetal.(1982):
2(cid:6)p 12π 64 L (cid:6)pD L
= + , or =6π +32 (10.35)
ρ <v >2 Re Re D μ<v > D
AstheReynoldsnumberincreases,youmustdecideifthelengthofthedomainissufficiently
longthatthevelocityprofilesandpressureprofileshavereturnedtotheirfullydeveloped
values. Another way to determine this is to solve the problem on a longer domain and
comparetheanswersfromtheproblemswithdifferentlengths.Becausethepressuredrop
shouldbethesame,aslongasthepressuredropfromthefullydevelopedflowisnegligible
ortakenintoaccount,thisisavalidtest.
```

---

## Стр. 251

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:FLOWINASERPENTINEMIXER 239
FIGURE 10.18 Meshusedtomodeltheserpentinemixer.
EXAMPLE:FLOWINASERPENTINEMIXER
Slowflowinaserpentinemixerisusedtomixtwochemicalsthatcomeinatdifferentsides
oftheporttotheleft.ThegeometryandmeshareshowninFigure10.18;therewere70,008
elementsand170,598degreesoffreedomtosolveforthethreevelocitycomponentsand
pressure using a “P1 + P1” discretization (the default). It was solved using “P2 + P1”
discretizationinanearlierversionofComsolMultiphysicsbyZacheryTyreewhenhewas
aseniorchemicalengineeringstudentattheUniversityofWashington(Neilsetal.,2004).
AfewflowlinesareplottedinFigure10.19,showinghowthemixingofthefluidstreams
occurs as the fluid moves along the channels, turns, and goes up or down a chimney. To
solvethisprobleminComsolMultiphysics,downloadthegeometryfromthebookwebsite.
Thensetthedensityandviscosity,inlet(u·n=−1)andoutlet(p=0)boundaryconditions,
FIGURE 10.19 Flowlinesinserpentinemixer.
```

---

## Стр. 252

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
240 FLUIDFLOWINTWOANDTHREEDIMENSIONS
andsolve.Plotsaremadeasin2Dproblemswiththeminorchangeofchoosing3DPlots
ratherthan2DPlots.Ofcourseyoucancreate2DPlotsfromthe3Dsimulation,too.
MICROFLUIDICS
Thefieldofmicrofluidicsinvolvesflowanddiffusioninsmalldevices,usuallydefinedas
lessthan1mminwidth/height.Therearetwoimportanttechnologiesthatusemicrofluidics:
microreactorsandalab-on-a-chip.Thelab-on-a-chipapplicationsincludebothanalytical
devices for the chemistry laboratory and medical devices that are used in point-of-care
medicaltreatment.Asophisticatedmeasurementcanbemadewhereveryouare,theresults
canbeelectronicallytransmittedtoyourdoctor,whothenhasthefinishedlabresultsand
can act on them immediately. The technologies provide interesting problems for flow in
thelaminarregion.Theyalsoprovideimportantchallengesfordiffusion,sincesometimes
the diffusion layer is very thin and requires a very fine mesh to resolve. Provided here
aresuchproblems,alongwithsimplerversionsthatallowtheengineertodeterminehow
sophisticated the model needs to be in order to design the device. Sometimes your basic
understanding of fluid mechanics, heat transfer, and diffusion will allow you to make
reasonable estimates for the design. References involving microreactors are Koch et al.
(2007)andGokhaleetal.(2005);areferencesdealingwithmicro-andnanoscaletransport
areKirby(2010)andFinlaysonetal.(2007);agoodreferenceaboutbiologicalapplications
isGomez(2008).
Whywouldyouwanttohaveachemicalreactorthatyoucanholdinyourhandorput
onyourdesk?Well,youwouldnotwanttoholditorputitonyourdesk,butmicroreactors
haveseveraladvantageousfeatures.First,youcancontrolthereactiontime,temperature,
and pressure very closely in a way you cannot in a packed bed or large tube. This may
enhance safety since you can control the temperature and reactive material better. Atom
efficiencyisalsoimproved,allowingyoutomakemoreofthematerialyouwantandless
of the by-products that have to be disposed of. The results are often more reproducible,
too.How,then,doyoumakemorethanalaboratorybeakerofmaterial?Youscaleupby
whatiscalled“numberingup”:yousimplymakemanyreplicasandcombinetheoutputs.
Oneadvantageofthisisscaleup:youdonothavetostudyalargerversionofthereactor,
in which new phenomena may be relevant, since the duplicative reactors are the same as
the one you have already studied. This also means that you do not have to build a huge
plant;buildamodestplant,andthenasthemarketgrows,addtoitwithsimilarreactors.Of
courseyoulosethebenefitofthesixth-tenthrule:thecapitalcostgoesupasthesixth-tenth
powerofthecapacity.Thisleadstoverylargeplants.But,inreturn,youmayhavelower
laborcosts(oneestimate50–75%less).Aswithanyreactor,though,youhavetosolvefor
theflowinaspecificgeometry,findthepressuredrop,andthensolveforconcentrationand
temperature.
For medical purposes, microfluidic devices can be used in a variety of ways (Gomez,
2008).Smallfluidstreamswithdifferentchemicalscanbemixedinpreciseways.Some-
timescellsaresortedtoprovidejusttheonesyouwanttoanalyze,thusimprovingthedis-
crimination.Point-of-carediagnosticsisespeciallyusefulindevelopingcountries,because
sometimes the device can be made cheaply, and the chemicals do not require refrigera-
tion.Ratherthancollectingblood,takingittoalaboratory,usingmultiplereagentstodo
biochemicalanalyses,amicrofluidicdevicecantakeadropofblood,addsmallamounts
of the appropriate chemicals and do the analysis “on the spot.” For example, Professor
```

---

## Стр. 253

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
MICROFLUIDICS 241
PaulYager’slaboratoryattheUniversityofWashingtondesignedadevicetodifferentiate
betweensixdifferentdiseaseswhosemainsymptomisafever.Withoutthebloodtest,the
doctor or nurse may not know which disease is causing the fever, and the treatment may
notbefocusedasitshouldbe.Thus,Chapters10and11haveproblemsinvolvingtheflow
anddiffusionofchemicalsinmicrofluidicgeometries.
Whentheflowisslow,asinmicrofluidicdevices,itisconvenienttopresentresultsina
slightlydifferentwaythanforturbulentflow.Considertheflowofanincompressiblefluid
inastraightpipe.Thepressuredropisafunctionofthedensityandviscosityofthefluid,
theaveragevelocityofthefluid,andthediameterandlengthofthepipe.Therelationship
isusuallyexpressedbymeansofafrictionfactordefinedasfollows:
1 D (cid:6)p
f ≡ (10.36)
4 L 1ρ <v >2
2
TheReynoldsnumberis
ρ <v > D
Re≡ (10.37)
η
TheusualcurveoffrictionfactorisgiveninFigure10.20ainalog–logplot.Foranygiven
Reynolds number, one can read the value of friction factor, and then use Eq. (10.36) to
determinethepressuredrop.Intheturbulentregion,forRe>2200,onecorrelationisthe
Blasiusformula:
f
=0.0791/Re0.25
(10.38)
Inthelaminarregion,forRe<2200,thecorrelationis
f =16/Re (10.39)
When the definitions are inserted into Eq. (10.39) for laminar flow, one obtains for the
pressuredrop
L μ<v >
(cid:6)p =32 (10.40)
D D
Thus, in laminar flow in a straight channel, the density of the fluid does not affect the
pressuredrop.Tousethecorrelationforfrictionfactor,orFigure10.20a,onemustknow
thedensity.ThisproblemisavoidedifoneplotstheproductoffrictionfactorandReynolds
numberversusReynoldsnumber,sincefromtheirdefinition
(cid:6)pD2
fRe= (10.41)
2Lμ<v >
ThisisshowninFigure10.20b.NoticethatforRe<1theonlythingneededisthenumerical
constant,here16.Forafullydevelopedpipeflow,thequantityfRedoesnotchangeasthe
Reynoldsnumberincreasesto 2200,butitdoesinmorecomplicatedcases.Thiscoversthe
```

---

## Стр. 254

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
242 FLUIDFLOWINTWOANDTHREEDIMENSIONS
103
102
101
100 105
eR
f
102
101
100
10−1
10−2
10−3
100 105
Reynolds number
f
Reynolds number
(a)
(b)
FIGURE 10.20 Friction losses (pressure decreases) for fully developed pipe flow. (a) Standard
presentationReynoldsnumber.(b)LowReynoldsnumberpresentation.
rangeinwhichmostmicrofluidicdevicesoperate.Topredictthepressuredrop,allthatis
neededisthesinglenumberforthegeometryandflowsituationinquestion.Thewaythese
numbersaredeterminedisbestillustratedbylookingatthemechanicalenergybalancefor
aflowingsystem.
Consider the control volume shown in Figure 10.21, with inlet at point 1 and outlet
at point 2. In the following, (cid:6) variable means the variable at point 2 (outlet) minus the
variableatpoint1(inlet).Themechanicalenergybalanceis(Birdetal.,2002)
(cid:2) (cid:3) (cid:10)2
1<v3 > dp
(cid:6) 2 <v > +g(cid:6)h+ ρ = Wˆ m −Eˆ v (10.42)
1
```

---

## Стр. 255

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
MICROFLUIDICS 243
2
1
FIGURE 10.21 Geometryandnotationformechanicalenergybalance.
For no height change g(cid:6)h = 0; for no pump in the control volume Wˆ =0; for an
m
incompressiblefluidwithconstantdensity:
(cid:10)2
dp 1 1
= (p − p )= (cid:6)p (10.43)
ρ ρ 2 1 ρ
1
Thus,underalltheseassumptionswehave
(cid:2) (cid:3)
1<v3 > 1
(cid:6) 2 <v > + ρ (cid:6)p =−Eˆ v (10.44)
Bycontinuitythemassflowrateisthesame,w =w .Thedefinitionoftheviscouslosses
1 2
is
(cid:10) (cid:10) (cid:10)
Ev =− τ :∇vdV = μ[∇v+(∇v)T]:∇vdV ≥0, Eˆ v = E w v, w =ρ v·ndS
V V
(10.45)
RewriteEq.(10.44)intheform
(cid:2) (cid:3)
1<v3 > 1 p − p
(cid:6) 2 <v > +Eˆ v =− ρ (cid:6)p = 1 ρ 2 (10.46)
MechanicalEnergyBalanceforLaminarFlow
When the flow is slow and laminar, we use the nondimensionalization for the pressure
identifiedasOptionOneearlier.Thenthenondimensionalmechanicalenergybalanceis
(cid:2) (cid:3)
Re(cid:6) 2 1< < v v (cid:4) (cid:4) 3 > > +Eˆ v (cid:4) =(p 1 (cid:4) − p 2 (cid:4) )where Eˆ v (cid:4) = μ ρx v s Eˆ v = μ ρx v s E w v (10.47)
s s
Forturbulentflow,areasonableapproximationisthatthevelocityisconstantwithrespect
toradialpositionintheinletandoutletducts,andthen<v(cid:4)3 >/<v(cid:4) >=<v(cid:4)2 >.This
isnottrueforlaminarflow,though.
```

---

## Стр. 256

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
244 FLUIDFLOWINTWOANDTHREEDIMENSIONS
Forfullydevelopedflowthroughatubewithaconstantdiameter,D,thekineticenergy
doesnotchangefromoneendtotheother.Wealreadyhaveaformulaforthepressuredrop
intermsofthefrictionfactor,sothat
(cid:6)pD L
p (cid:4) − p (cid:4) = =32 (10.48)
1 2 μ<v > D
Thus,theviscousdissipationterminEq.(10.47)forlaminarflowinastraightchannelis
L
Eˆ(cid:4) =32 (10.49)
v
D
Thus, the dimensionless viscous dissipation is proportional to L and does not depend on
theReynoldsnumberaslongastheflowislaminarinastraightpipe.Thereasonforusing
thenondimensionalizationofOptionOneisbecauseofthisresult:itcoversawiderange
offlowratesusingonlyasinglenumber.
NotethatinEq.(10.47)theReynoldsnumbermultipliesthetermrepresentingthechange
of kinetic energy, and the complete term may be small because the Reynolds number is
small.ConsiderthecasewhentheReynoldsnumberisextremelysmall(i.e.,zero).Then
anyflowsituationisgovernedbyStokesequation,thatis,Eq.(10.17)withRe=0:
∇(cid:4)2v (cid:4) =−∇(cid:4)
p
(cid:4)
(10.50)
Thus, the solution to Eq. (10.50) does not depend on the Reynolds number. In this case,
withRe=0,thedimensionlessviscousdissipationterminEq.(10.47)isaconstantandthe
kineticenergytermisnegligible.Tocorrelatethepressuredropinlaminarflow,themain
taskistocalculatetheviscousdissipationterm,Eˆ(cid:4).Thisisusuallythecaseinmicrofluidic
v
devices.
Aconvenientwaytocorrelatedataforexcesspressuredropwhentherearecontractions,
expansions,bendsandturns,andsoon,whentheflowisturbulentistowritethemas
(cid:6)p = K1ρ <v >2 (10.51)
excess 2
Then,tocalculatetheexcesspressuredropforanygivenfluidandflowrate,oneonlyneeds
toknowthevaluesofK,whicharetabulatedinPerryandGreen(2008).
As shown earlier, for slow flow the pressure drop is linear in the velocity rather than
quadratic,andadifferentcorrelationispreferred.Write
μ<v >
(cid:6)p = K (10.52)
excess L
D
ValuesofK fordifferentgeometriesarecalculatedinseveralproblems.Thetwocoefficients
L
canberelatedbyequatingthe(cid:6)p formulas:
excess
K
K = Re (10.53)
L
2
Thus,toestimatethe(cid:6)pinadeviceonemerelyneedstosolveoneflowproblemtogetK .
L
WeseebelowthatthisworkswellforRe<1.
```

---

## Стр. 257

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
MICROFLUIDICS 245
D1/2
D /2
2
CL
FIGURE 10.22 Contractionflowgeometry.
PressureDropforContractionsandExpansions
Consider a large circular tube emptying into a smaller circular tube, as shown in
Figure 10.22. The pressure drop in this device is due to viscous dissipation in the fully
developed regions of the large and small channels, plus the extra viscous dissipation due
tothecontraction,plusthekineticenergychange.FortheflowillustratedinFigure10.22,
wewritetheexcesspressuredropforthecontractionasthetotalpressuredropminusthe
pressuredropforfullydevelopedflowinthelargeandsmallchannels.Thepressuredrop
forfullydevelopedlaminarflowisknownanalytically,ofcourse[Eq.(10.40)]:
(cid:6)p =(cid:6)p −(cid:6)p −(cid:6)p (10.54)
excess total largechannel smallchannel
The excess pressure drop is correlated by using (cid:6)p = K η<v >/D and K can
excess L L
be determined from finite element calculations. Note that one must specify which aver-
agevelocityanddistanceareusedinthiscorrelation,andtheusualchoicesaretheaverage
velocityandthediameterortotalthicknessbetweenparallelplates,allatthenarrowend.
ThevalueofK dependsonthecontractionratio,too,andsomeofthemarecalculatedin
L
theproblems.Typicalvaluesrangefrom8to15.Figure10.23showsthetotalpressuredrop
103
102
101
100
10−1
10−2
10−2 10−1 100 101 102
L−K
Total excess pressure drop
Due to
viscous
dissipation
Due to kinetic energy change
Reynolds number
FIGURE 10.23 Laminar flow excess pressure drop for a 3:1 contraction in a circular channel.
K is the total pressure minus the fully developed pressure drop in the two regions, expressed as
L
K =(cid:6)p D /η<v >.
L excess 2 2
```

---

## Стр. 258

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
246 FLUIDFLOWINTWOANDTHREEDIMENSIONS
and the contributions due to viscous dissipation and kinetic energy changes. The viscous
term predominates at low Reynolds numbers (Re < 1, i.e., in microfluidics) whereas the
kineticenergytermpredominatesathighReynoldsnumber(>100).
WhentheReynoldsnumberisnotvanishinglysmall,K dependsonReynoldsnumber,
L
too,andthedependenceiseasilydeterminedusingCFD.Forexample,fora3:1contraction
in a pipe the results are shown in Figure 10.23. The departure from a constant K is
L
due partially to extra viscous dissipation at higher Reynolds number, but mostly due to
kineticenergychangeforRe>10.Formulasforthekineticenergychangeforavarietyof
axisymmetricorchannelcontractionsorexpansionsaregivenbyFinlaysonetal.(2007).
GENERATIONOFTWO-DIMENSIONALINLETVELOCITYPROFILESFOR
THREE-DIMENSIONALSIMULATIONS
ConsiderflowinthechannelshowninFigure10.24.Inthesquarecorner,thechannelis1
dimensionlessunitsquare,andeachlegis3unitslong.Theinletvelocityisfullydeveloped
flowwithanaverageflowrateof1.0.Theexcesspressuredropiscalculated.Toobtainthe
fully developed flow at the inlet, it is necessary to learn how to use Linear Extrusion in
ComsolMultiphysics.Tofigurethepressuredropinastraightchannelwithasquarecross
section,usefRe=14.2(Finlayson,1972).TheDinEq.(10.36)isthehydraulicdiameter,
D=4A/C.TheareaisW2andthecircumferenceis4W,sothehydraulicdiameterisW.
ComsolMultiphysicsisopenedfora3DsimulationusingLaminar,steadyflow.Inthe
root icon, set the units to “none.” Be sure that discretization is chosen to be displayed.
Inthe“Model1”/“LaminarFlow,”openDiscretizationandchangethediscretizationfrom
FIGURE 10.24 Squarecorner.
```

---

## Стр. 259

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
GENERATIONOFTWO-DIMENSIONALINLETVELOCITYPROFILES 247
P1 + P1 to P2 + P1. In Geometry, choose “Work Plane” and draw the projection on
thesurfacez=0,choose“Booleanoperations/Union”(andpressBuild)toconnectthem
without internal boundaries. Then choose extrude, for a distance of 1. In the “Model
1/Laminar Flow/Fluid Properties” set density to 0.001 and viscosity to 1 (for the low
Reynoldsnumbercase).Forthefirstsimulation,settheinletvelocityto1.Setthepressure
at the outlet to zero (not the one with no shear stress). Under “Model 1/Mesh” choose
“normal” mesh and build; it uses 48,863 elements and 381,536 degrees of freedom. The
average velocity at the inlet is 0.9934. The pressure is zero at the outlet, and the average
pressureattheinletis215.882.UsingtheformulainvolvingfrictionfactorandReynolds
numbergives
W2(cid:6)p ρ <v > W 28.4μ<v >
=14.2, or(cid:6)p = L (10.55)
L4W1ρ <v >2 μ W2
2
Here,W =1,μ=1,<v>=1,L=2×3=6sothat(cid:6)p=28.4L=170.4.Thus,the
excesspressuredropis45.4.Someofthispressuredropisduetotherearrangementofthe
velocityprofileattheinlet.
Next,solvetheproblemwhentheinletvelocityistheproperone,proceedasfollows.
Step1(Definea2DProblem) satisfyingtheNavier–Stokesequationsbyaddingasecond
“Modelfor2D,Poisson’sequation”;thiswillbe“Model2.”Makethedomainbethesquare
from0to1ineachdimension.Setthevalueofu2=0onallfourboundaries,andsolve
forsomevalueoff.Thenadjustthef sothattheaverageis1.0;thef is28.4543.
Step2(IdentifyVertices) Nowgoto“Model2/Definitions”andrightclicktoget“Model
Couplings/LinearExtrusion.”ForSource,usethesolutionforu2onthesquare.ForDes-
tination, choose the solution on Geometry 1. Set the vertices as follows: for the source,
make them appear as in Table 10.1; do this for the destination, too. The fourth one is, of
course,definedbytheotherthree.(Note:Itisconfusingtoonlyspecifythreeverticesfor
the square, but that is the way it is; the program will not work if you specify the fourth
one.)Inthesamesettingswindows,forthegeometricentity,forthe2Dproblemselectthe
entireDomainandforthe3DproblemselectBoundaryandpicktheinletboundary.
Step 3 (Create a Function) Then go to “Model 1/Definitions/Variables” and define a
variableu_fully_devasmod2.linext1(mod2.u2).
Step4(AssignBoundaryConditions) Intheboundaryconditions,settheinletvelocity
tou_fully_dev.
Step 5 (Connect the problems) You also must choose “Step 1:Stationary” and open
“ValuesofVariablesnotsolvedfor.”Besuretoclicktheboxandidentifythesolutionto
beused(Solution2).
TABLE10.1 VertexChoiceforLinear
Extrusion;2DProblem;3DInlet
3 4 1 2
2 – 4 –
```

---

## Стр. 260

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
248 FLUIDFLOWINTWOANDTHREEDIMENSIONS
FIGURE 10.25 SolutionofPoisson’sequationonasquare.
2.0951
2
1.5
1
0.5
0
1
1
0 4
–1 3
2
–2
1 0.5
–3 0
z
y x
0
0
FIGURE 10.26 Velocityprofileinasquareturn.
```

---

## Стр. 261

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 249
Step6(Solvethe3DProblem) For“Study1”(the3Dcase),youcanturnoff“Stationary,
Poisson’sEq.”For“Study2”(the2Dcase),youcanturnoff“Stationary,LaminarFlow.”
Then solve “Study 2,” getting the solution shown in Figure 10.25, with a peak value of
2.0956; then solve “Study 1.” The x-velocity is shown in Figure 10.26. Now the average
pressureontheinletis190.65.Thus,theexcesspressureis190.65–170.4=20.25.When
thedensityischangedto1,theaveragepressureisalmostthesame,190.68,sotheexcess
pressureis20.48.Asexpected,thereisverylittledifferencebetweenthosesolutionsatlow
Reynoldsnumber,providedthenondimensionalformisused.
CHAPTERSUMMARY
ThischapterillustrateshowtouseComsolMultiphysicstosolvetheNavier–Stokesequa-
tionsinavarietyofsituations.Someoftheseproblemsareclassic,suchasentryflowintoa
pipeandtransientstart-upofpipeflow.Mostexamplesareforlaminarflowintwodimen-
sions,butonemodelisturbulentflowintoapipe,andothermodelsareforcomplicated3D
geometries.
PROBLEMS
10.1 SolvefortheentryflowofaNewtonianfluidintoapipeusingtheparametersinthe
1
example.ReproduceFigure10.2throughFigure10.4.
10.2 Solvefortheentryflowofapower–lawfluidintoaregionbetweentwoflatplates.
1
Theviscosityisgivenby
η=0.2γ˙ −0.6 (10.56)
Theplatesareadistanceof0.005mapart,andtheappliedpressuregradientis60
Painalengthof0.3m.Thedensityofthefluidisthatofwater.(Hint:followthe
steps in the example of entry flow in a pipe, except use a power–law formula for
viscosityandusetwoflatplatesratherthanapipe.)
10.3 1 SolveProblem10.2exceptusetheCarreaufunction,Eq.(10.29)withη ∞ =0.05,
η =0.492,λ=0.1,andn=0.4.(Hint:followthestepsintheexampleofentry
0
flowinapipe,exceptusetheCarreaufunctionforviscosityandusetwoflatplates
ratherthanapipe.)
10.4 Compare the Carreau viscosity as a function of shear rate (Figure 10.5 and
1
Problem10.3)withthatofthepower-lawfluidinProblem10.2.
10.5 Solve for the start-up flow of the power-law fluid and problem described in
1
Problem10.2.Howlongdoesittaketoreachsteadystate?
10.6 Solve for the start-up flow of the Carreau fluid and problem described in
1
Problem10.3.Howlongdoesittaketoreachsteadystate?
10.7 Solvefortheflowthroughanorifice.ReproduceFigure10.15forReynoldsnumbers
1
of 31.6 using the parametric sweep from 1 to 31.6. Plot the pressure coefficient
versusReynoldsnumber,asinFigure10.16.
```

---

## Стр. 262

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
250 FLUIDFLOWINTWOANDTHREEDIMENSIONS
10.8 Solve the example of a microfluidic T-sensor, except have the average velocity
1
cominginthebottomtwiceashighasintheexample.Comparetheflowratesin
bothstreamsandouttoensurethatthetotalflowinequalsthetotalflowout.
10.9 Considerlaminarflowpastaflatplate.Createageometryasalongrectangle,1m
2
long and 0.1 m high. Use density of 1000 kg/m3 and viscosity of 0.001 Pa s. Set
the velocity to zero on the plate, and set it to 0.1 m/s on the left. Use an open
boundarywithzeronormalstressatthetopandanoutletwithp=0attheright.
Youmayhavetorefinethemeshconsiderablytoseetheboundarylayer.Compare
yoursolutionwiththeBlasiussolutioninyourtextbook.
10.10 Solveforthedragonasphereinaflowingstreamwithauniformvelocityprofile
2
upstream.SolveforzeroReynoldsnumber(Stokesflow).Comparethesolutionwith
an analytical solution in your textbook. (Hint: set the density to a small number
to simulate Stokes flow. The drag is obtained by integrating the stress over the
boundaryofthesphere.UsetheExpressionbutton.)
10.11 Solveforthedragonasphereinaflowingstreamwithauniformvelocityprofile
1
upstream.SolveforReynoldsnumberfrom1to100.Putthesphereinacylindrical
tube,butuseanopenboundarywithzeronormalstressonthetube(thiswillmimic
aninfinitedomain).Howdoesthequalitativebehaviorofthesolutionchangewith
Reynoldsnumber?
10.12 Solveforthedragonasphereinaflowingstreamwithauniformvelocityprofile
2
upstream.SolveforReynoldsnumberfrom1to100.Putthesphereinacylindrical
tube with a diameter of 5. For this problem, use zero velocity on the cylindrical
tube,whichmimicstheeffectofthewall.
10.13 Project.UsetheproblemsetupinProblem10.12anddeducethewalleffectwhen
measuring the terminal velocity by dropping a sphere into a fluid. Compare with
PerryandGreen(2008).
10.14 Solveforthedragonacylinderinaflowingstreamwithauniformvelocityprofile
2
upstream.SolveforReynoldsnumber=1,5,10,20,40.Usethenondimensional
form with radius = 0.5, upstream velocity = 1, ρ = Re, and η = 1. [The other
methodofnondimensionalization(ρ=1andη=1/Re)worksbestastheReynolds
number gets high. But use the one with ρ = Re and η = 1 when calculating the
drag force.] Far from the cylinder use an open boundary with zero normal stress
(thiswillmimicaninfinitedomain.)
(a) How does the qualitative behavior of the solution change with Reynolds
number? Prepare graphs that display interesting features of the solution for
Re=10.
(b) Plot the dimensionless drag (what you get by integrating the total force on
thecylinder)versusReynoldsnumber.Thedragcoefficientcanbedetermined
fromyourforcesusingtheformulaC =2F(cid:4)/Re.TheforceF(cid:4)canbecalculated
D
by integrating the total force on the surface of the cylinder. Then multiply it
by 2 (to account for the other side, assuming you solve the problem using
symmetry).
(c) Compute the drag coefficient at Re = 1 and 10 and compare with Perry and
Green(2008).
```

---

## Стр. 263

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 251
10.15 Solveforturbulentflowinapipeusingtheparametersintheexample(ifyouhave
2
accesstotheCFDmodule).Usevelocitiesof(a)0.2;(b)0.6;(c)1.4m/s.Compare
resultswithFigures10.10and10.11.
10.16 DothemicrofluidicprobleminFigure10.7butinthreedimensionsforthefollowing
2
parameters. The size of the channels are 100 μm in cross section, the inlet ports
and the exit ports are 100 × 100 μm. The section after the inlet is 500 μm long.
The inlet velocities are fully developed with an average velocity of 0.1 mm/s.
The density and viscosity are those of water (density of 1000 kg/m3, viscosity =
0.001Pas).WhatistheReynoldsnumberineachinlet;inthesectionbetweenthe
inletandoutlet?Showthestreamlines.Whatisthepressuredropinthedevice?
10.17 (AllpartsasaProjectoronepartasaproblem.)Solveforthe2Dflowinchannels
1
ofvariousshapesasshowninFigure10.27.
(a) Inthesharpbend,thechannelis1dimensionlessunitwide,andeachlegis3
unitslong.
(b) Inthesmoothbend,theradiusalongthecenterlineisonegapwidth.
(c) Inthesmoothbend,longradius,theradiusis1.5timesthegapsize.
(d) IntheT,eachlegis3unitslong.Forallcasesuseafullydevelopedflowprofile
forachannelattheinletwithadimensionlessaverageflowrateof1.0.
UseComsolMultiphysicsinanondimensionalformwithadensityof0.001(to
getbasicallylowReynoldsnumber)todeterminethepressuredrop;thencalculate
itforflowinastraightchannelthatisaslongasthecenterlinedistanceofthedevice.
Subtractthestraightchannelresultfromthetotaltoobtaintheexcesspressuredrop.
Comment. What is K ? For one of the cases recalculate the pressure drop with a
L
dimensionaldensityof1(Re=1).
FIGURE 10.27 Geometriesforpressuredropcalculations.
10.18 Solveforthe3Dflowina90degreeturnofaroundpipewithr/d=1(Figure10.28).
2
Useanaverageinletvelocityof1.0andsolveforReynoldsnumbersfrom0.01to
100. Plot K and K versus Reynolds number from 0.01 to 100 for laminar flow
L
andfrom104 to2×105 forturbulentflow.Forturbulentflow,usecorrelationsin
Perry and Green (2008, Eq. 6-97, pp. 6-18–6-19) to get K = 0.18 at a Reynolds
number of 106, and Re > 2 × 105. For Reynolds numbers between 104 and 2 ×
105,multiplythisnumberbythecorrectionfactorgiventhere:
1−2.2
C =2.2+ (log Re−log (104))
Re log (2×105)−log (104) 10 10
10 10 (10.57)
1−2.2
C =2.2+ (log Re−4)
Re 5.3−4 10
```

---

## Стр. 264

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
252 FLUIDFLOWINTWOANDTHREEDIMENSIONS
0.5
0
–0.5
0
1
0
–2
–1
–2
FIGURE 10.28 Pipecorner.
10.19 Project.Thepressuredropforacontractionisrepresentedasthedifferencebetween
1
thetotalpressuredropminusthetheoreticalpressuredropforfullydevelopedflows
inthelargeandsmallsection.DeterminetheK forslowflowanda2:1;3:1;and
L
4:1 contraction for both channel flow and pipe flow. For the 3:1 pipe flow case
(Figure10.22),solveforReynoldsnumbersfrom0.01to100.Basethedefinition
ofK onthevelocityanddiameter/thicknessofthesmallerregion,sincethepressure
L
dropthereisthelargest.
10.20 Compute the excess pressure drop in a 3:1 contraction of a square channel
2
(Figure 10.29). The excess pressure drop is the total pressure drop minus theo-
retical pressure drop for fully developed flow along the centerline. Express the
resultintermsofK .
L
10.21 Computetheexcesspressuredropinthe2DT-sensorandH-sensoratRe=1.The
1
excesspressuredropisthetotalpressuredropminusthetheoreticalpressuredrop
forfullydevelopedflowalongthecenterline.ExpresstheresultintermsofK .
L
10.22 Solveforflowinaregularporousmedia,asshowninFigure10.30.Thedomainis
1
a square from −1 to +1 and each circle has a radius of 0.5. The top and bottom
boundariesaresymmetryboundaries,theleftboundariesareinletboundaries,and
the right boundaries are outlet boundaries. There is no slip on the surfaces of the
cylinders. Solve for slow flow in dimensionless terms when the normal stress on
therightsideis0andontheleftsideis1.
```

---

## Стр. 265

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 253
1.5
6
1
0.5 4
0
1.5
2
1
0.5
0 0
FIGURE 10.29 3:1contractionusingsymmetryonthey−xplane(z=0)andthez−xplane
(y=0).
10.23 ConsiderflowinacrossasshowninFigure10.31,firstforchannelflowandthen
2
for3Dflowwhenthecrosssectionisasquare.Thelengthofthelegsis7andthe
channelwidthis1,indimensionlessterms.Oftentimesamicrofluidicdevicewill
have a flow segment like this, but with much longer channels. In those channels
the flow is fully developed and we know what it is. However, at the cross, the
flowisdisturbed.Whatdistancedoesittake(inchannelwidths)toreturntofully
developedflow?DothisforsmallReynoldsnumber.
FIGURE 10.30 Periodicflowbetweencylinders.
```

---

## Стр. 266

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
254 FLUIDFLOWINTWOANDTHREEDIMENSIONS
(a)
0.5
0
–0.5
2
2
0
0
–2
–2
(b)
FIGURE 10.31 Flowinacross:(a)channelflow;(b)3Dflow.
```

---

## Стр. 267

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 255
FIGURE 10.32 Flowinabend.
10.24 Solvefortheflowinabend,firstintwodimensionsandtheninthreedimensionsas
2
showninFigure10.32.Thelengthofthestraightchannelsis3,withwidth1.The
circularregionshaveradii1,1.5,and2.Forthe3Dproblem,extrudethegeometry
toaheightof1.0.
10.25 Solve for the flow in an H-sensor in three dimensions. Extrude the H-sensor in
2
Problem 10.21 to one unit height. You will have to use two linear extrusion cou-
plings, one for each inlet branch, but you only need to solve Poisson’s equation
once.Determinetheexcesspressuredrop.
10.26 Project.ComputethepressuredropfortheserpentinemixeratRe=1.Byusingthe
cut-planeoption,determinethepressuredropfor1,2,3,and4segments:straight
channels,chimneys.Thencorrelateyourresultsintermsofthenumberofstraight
channels and chimneys in order to provide an analytical formula for a serpentine
ofanynumberofstraightchannelsandchimneys.
10.27 Project. A microfluidic device was designed by Micronics (Redmond, WA) and
adapted for metabolic fingerprinting applications by Drs. Colin Mansfield and R.
Anthony Shaw at the NRC Institute for Biodiagnostics in Canada. The purpose
was to take a sample of serum (comprising both metabolites and proteins) and
use diffusion across a serum/water interface to partly extract metabolites for di-
agnostic or analytical characterization. The efficacy of this process was assessed
and optimized by specifically targeting the extraction of serum creatinine (a rep-
resentativemetabolite)attheexpenseofserumalbumin(arepresentativeprotein).
With that accomplished, infrared spectroscopy could be used to characterize the
metabolite-rich aqueous stream with minimal interference from serum proteins.
TheconvectionanddiffusionproblemisspecifiedinChapter11(Problem11.28);
```

---

## Стр. 268

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
256 FLUIDFLOWINTWOANDTHREEDIMENSIONS
FIGURE 10.33 Geometryforalaminarfluiddiffusioninterfacedevice.
here,considerjusttheflowproblem.Firstconsiderflowintothedeviceshownin
Figure 10.33. The height is 330 mm and the two inlet portions each are 110 mm
high.Thedepthis4.5mm,butsolvetheproblemintwodimensions.Theflowrates
are2μL/sforthereceiver(water;topstream)and1μL/sforthesample.Forthe
flowprobleminthischapter,taketheviscosityas1.6mPasforbothfluids;thisis
changedinProblem11.28.
(a) Solveforthestreamlinesattheinletinthegeometryshownbelow.
(b) Compare that with a geometry that has a knife edge at a height of 165 mm.
Further details about the device can be obtained from the Comsol website
(FinlaysonandShaw,2010),thebookwebsite,andSchattkaetal.(2011).
10.28 When fluid is flowing between two flat plates and there is a hole or slit in the
1
bottom plate, there is also a difference between the pressure at the bottom of
the hole/slit and the top plate. This is called the hole pressure and the effect can
be used to measure the first normal stress coefficient of polymers (a measure of
elasticity).HereconsideraNewtonianfluidandsolvetheholepressureproblemin
twodimensions(i.e.,foraslit)whenW =H =LforRe=1(seeFigure10.34).
Plotthepressureonthebottomoftheholeandthetopjustacrossit.1
H
L
W
FIGURE 10.34 Two-dimensionalholepressuregeometry.
1ThisproblemwasthefirstproblemsolvedbytheGalerkinfiniteelementmethodbytheauthorandhisstudents
(JacksonandFinlayson,1982a,b).Atthetime,wewroteourownfiniteelementcode,computersweremuch
slower and very much smaller, so only 12, 29, and 110 elements were used for a 2D problem. Despite that
limitation,comparisonwithexperimentwasquitereasonableforNewtonianfluids.
```

---

## Стр. 269

```text
P1:OTA/XYZ P2:ABC
JWBS084-c10 JWBS084-Finlayson May31,2012 10:10 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 257
10.29 Project. Expand Problem 10.28 to three dimensions. For the 3D case, make the
entrancebe1×8,makethelengthbe4,andputthecylinderofdiameter1centered
atadistanceof1.5fromtheinlet.Thenthegeometryfromthesideisthesameasthe
2Dcase.Thecylinderismadetoextendthroughtothetopsurfacesothatintegrals
canbecomputedonthecircleonthetopsurfacetocomparewiththesameintegrals
onthebottomofthecylinder.Theproblemwassolvedinnondimensionalform,with
ρ=1,μ=1.Besuretochangefromcompressibleflowtoincompressibleflow(in
themodel),usenodimensions,andchangetoquadraticvelocity(Discretization).As
anapproximation,taketheinletvelocityasu =6∗z(1−z)∗y1/7∗(8−y)1/7/1.328.
Comparetheresultsforthreedimensionswiththoseobtainedintwodimensions.
Rationalizeanydifferences.
```

---

## Стр. 270

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
11
HEAT AND MASS TRANSFER IN
TWO AND THREE DIMENSIONS
Chemicalreactionandmasstransferaretwouniquephenomenathathelpdefinechemical
engineering.Chapter8describesproblemsinvolvingchemicalreactionandmasstransfer
inaporouscatalyst,andhowtomodelchemicalreactorswhentheflowiswelldefined,as
in a plug-flow reactor. Those models, however, did not account for the complicated flow
situations sometimes seen in practice, where flow equations must be solved along with
the transport equation. Microfluidics is the chemical analog to microelectromechanical
(MEMS)systems,whicharesmalldeviceswithtinygears,valves,andpumps.Thegenerally
accepteddefinitionofmicrofluidicsisflowinchannelsofsizeonemillimeterorless,and
itisessentialtoincludebothdistributedflowandmasstransferinsuchdevices.
Microfluidicdevicesoftenaresmallerthanapenny,soanewnamehasbeeninvented
for them: lab-on-a-chip. The pharmaceutical industry uses these devices for drug design,
delivery,anddetection,andthebiomedicalindustryusesthemforsensorsanddrugdelivery.
Industrial applications include the study of new reaction mechanisms and pathways that
leadtoimprovedselectivitywithfewerpollutants.Becauseofthesmallsizeofmicrofluidic
devices,aprecisecontroloftemperatureispossible,whichimproveskineticinformation,
especiallywithcatalysts.Someelementsofafuelcellaresmallenoughtobemicrofluidic
devices,too.Iflarge-scaleproductionisrequired,engineersuse“numberup”ratherthan
“scale up” to achieve high throughput. The techniques of the electronic industry can be
usedtoproducemanysmalldevicescheaply,andengineerssimplyadd“clones”toincrease
theproductionrateofchemicals.
This chapter uses Comsol Multiphysics to solve problems involving two-dimensional
(2D) or three-dimensional (3D) flow and diffusion of mass and/or heat. Convection and
diffusion of mass and heat is often governed by the convective diffusion equation. The
flowproblemsaretreatedinChapter10,butsometimestheparameters,suchasviscosity
and density, depend upon the concentration and temperature. In that case, you have to
IntroductiontoChemicalEngineeringComputing,SecondEdition.BruceA.Finlayson.
©2012JohnWiley&Sons,Inc.Published2012byJohnWiley&Sons,Inc.
259
```

---

## Стр. 271

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
260 HEATANDMASSTRANSFERINTWOANDTHREEDIMENSIONS
solve all the partial differential equations together. This chapter illustrates how to use
Comsol Multiphysics to solve problems in the geometries discussed in Chapter 10: the
T-sensor, an orifice, and the serpentine mixer. You will learn how to solve the equations
either sequentially, one after the other, or simultaneously; make the transport properties
suchasviscosityfunctionsoftemperatureorconcentration;andlearntoassesstherelative
importanceofconvectionanddiffusion,whichisessentialforinterpretingnumericalresults.
InstructionalObjectives: Afterworkingthroughthischapter,youwillbeableto
1. Modeldiffusionandheatconductionin2Dand3Dsituations,withandwithoutflow.
2. Solvetheflowandconvectivediffusionproblemssequentiallytosavetime.
3. Applyvariousboundaryconditions,includingperiodicboundaryconditions.
4. Handlevariableviscositydependingonconcentrationandwallreactions.
5. UnderstandtheimportanceofthePecletnumberandusethatinformationadroitly.
6. Calculate properties of the solution (mixing cup average concentrations and vari-
ances).
7. Checkyoursolutionforcontinuityofmass.
Inaddition,youwillbeintroducedtomasstransferproblemsinthefieldofmicrofluidics.
CONVECTIVEDIFFUSIONEQUATION
Theequationgoverningmasstransferwithflowis
∂c
+u·∇c=∇·(D∇c) (11.1)
∂t
Whenthediffusivityisconstantitis
∂c
+u·∇c= D∇2c. (11.2)
∂t
In2Drectangularcoordinates,Eqs.(11.1)and(11.2)become
(cid:2) (cid:3) (cid:2) (cid:3)
∂c ∂c ∂c ∂ ∂c ∂ ∂c
+u +v = D + D
∂t ∂x ∂y ∂x ∂x ∂y ∂y
(cid:2) (cid:3) (11.3)
∂2c ∂2c
= D + when Disconstant.
∂x2 ∂y2
Heattransferissimilar,butwithdifferentparameters.Thevectorrepresentationis
(cid:2) (cid:3)
∂T
ρC +u·∇T =∇·(k∇T)
p ∂t
(11.4)
=k∇2T whenk isconstant.
```

---

## Стр. 272

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
NONDIMENSIONALEQUATIONS 261
In2Drectangularcoordinates,theequationis
(cid:2) (cid:3) (cid:2) (cid:3) (cid:2) (cid:3)
∂T ∂T ∂T ∂ ∂T ∂ ∂T
ρC +u +v = k + k
p ∂t ∂x ∂y ∂x ∂x ∂y ∂y
(cid:2) (cid:3) (11.5)
∂2T ∂2T
=k + whenk isconstant.
∂x2 ∂y2
The velocity in the equation comes from the solution to the Navier–Stokes equation
describedinChapter10(oranotherflowequation).
NONDIMENSIONALEQUATIONS
Diffusion in liquids can be slow, and this makes the problems hard to solve, as shown
below.Thebestwaytolearnhowimportantdiffusionisforanyproblemistocalculatethe
Pecletnumber.Equation(11.3)ismadenondimensionalusingthetechniquesillustratedin
Eq.(10.13).Letc(cid:3)(x(cid:3),y(cid:3),t(cid:3))bethenondimensionalconcentration,andc=c c(cid:3)(x(cid:3),y(cid:3),t(cid:3)).
s
Eq.(11.3)foraconstantdiffusivitybecomes
(cid:2) (cid:3) (cid:2) (cid:3)
c ∂c(cid:3) u c ∂c(cid:3) ∂c(cid:3) Dc ∂2c(cid:3) ∂2c(cid:3)
s + s s u (cid:3) +v(cid:3) = s + (11.6)
t ∂t(cid:3) x ∂x(cid:3) ∂y(cid:3) x2 ∂x(cid:3)2 ∂y(cid:3)2
s s s
Multiplyingbyx2/Dc gives
s s
(cid:2) (cid:3) (cid:2) (cid:3)
x2 ∂c(cid:3) u x ∂c(cid:3) ∂c(cid:3) ∂2c(cid:3) ∂2c(cid:3)
s + s s u (cid:3) +v(cid:3) = + (11.7)
t D ∂t(cid:3) D ∂x(cid:3) ∂y(cid:3) ∂x(cid:3)2 ∂y(cid:3)2
s
You may already have picked the time standard in the flow problem. If you choose t =
s
x /u , the coefficients of the first and second terms are the same, and the coefficient is
s s
calledthePecletnumber:
u x
Pe= s s (11.8)
D
Theequationisthen
(cid:2) (cid:3) (cid:2) (cid:3)
∂c(cid:3) ∂c(cid:3) ∂c(cid:3) ∂2c(cid:3) ∂2c(cid:3)
Pe + Pe u (cid:3) +v(cid:3) = +
∂t(cid:3) ∂x(cid:3) ∂y(cid:3) ∂x(cid:3)2 ∂y(cid:3)2
(cid:2) (cid:3)
∂c(cid:3) ∂c(cid:3) ∂c(cid:3) 1 ∂2c(cid:3) ∂2c(cid:3)
or +u (cid:3) +v(cid:3) = + (11.9)
∂t(cid:3) ∂x(cid:3) ∂y(cid:3) Pe ∂x(cid:3)2 ∂y(cid:3)2
Typical boundary conditions include setting the concentration (temperature) to a spe-
cificvalue,havingnofluxthroughaboundary,andsometimeshavingthefluxthroughthe
```

---

## Стр. 273

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
262 HEATANDMASSTRANSFERINTWOANDTHREEDIMENSIONS
boundary,tobeproportionaltothedifferencebetweenaninterfaceconcentration(temper-
ature)andanexternalvalue.Atanoutflowboundary,chooseconvectiveflux.
EXAMPLE:HEATTRANSFERINTWODIMENSIONS
Thefirstproblemconsideredisheatconductioninasquare,whichisaclassicalproblem:
∂2T ∂2T
+ =0 in 0≤ x ≤1,0≤ y ≤1 (11.10)
∂x2 ∂y2
T =1on x =0
T =1on y =0
T =0on y =1 (11.11)
∂T
n·∇T ≡ =0on x =1
∂n
Step1(OpenandSetPreferences) OpenComsolMultiphysicsandchoosetwodimensions
andclickthenextarrow.ThenselectHeatTransfer/HeatTransferinSolidsandnext;Finally,
clickStationaryandthefinishflag.(SeetheiconsdisplayedinFigures9.2–9.4.)Clickthe
rootnodeandchangeunitsto“none”atthebottomofthesettingswindow.
Step2(DefinetheGeometry) RightclickGeometryandchooseasquare.Makeit1by1
withbasepointat(0,0);click“BuildAll.”
Step 3 (Define the Problem) Right click “Heat Transfer” and select “Heat Transfer in
Solids” if it is not already there. Open “Heat Transfer in Solids” and change the thermal
conductivityto“Userdefined,”value1.
Step4(SettheBoundaryConditions) Rightclick“HeatTransfer”andchooseTempera-
ture. Select boundaries 1 and 2 (the lowest one and the left most one), + to add it to the
Selectionbox,andsetthevalueto1.Dothisagainandselectboundary3(topone)andset
thetemperatureto0.Theright-handboundaryisinsulated,ascanbeseenbyclickingon
“ThermalInsulation”;theotherboundariesareshownasoverridden.
Step5(CreateaMesh) ClickonMeshand“BuildAll”;themeshisshowninFigure11.1.
Step6(SolvetheProblem) Rightclickon“Study1”and=togetthesolution.
Step 7 (Examine the Solution) The solution will be plotted in a color plot. Contours
of temperature are also made automatically. If they are not, they can be made by right
clicking Results, choosing “2D Plot Group,” and then right clicking on “2D Plot Group”
andchoosingContour.Clickontheploticontoseetheplot,Figure11.2.Saveitbyclicking
thecamera.
```

---

## Стр. 274

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:HEATTRANSFERINTWODIMENSIONS 263
3
1 4
2
FIGURE 11.1 Finiteelementmeshforheattransferproblem.
FIGURE 11.2 Solutiontoheattransferproblem.
```

---

## Стр. 275

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
264 HEATANDMASSTRANSFERINTWOANDTHREEDIMENSIONS
EXAMPLE:HEATCONDUCTIONWITHAHOLE
Next,introduceaholeinthemiddleofthesamediagram.Theboundaryconditionsonthe
sidesoftheholearethermalinsulation.
Step1(OpenandSetPreferences) Opentheprevioussolution.
Step2(DefinetheGeometry) RightclickonGeometryandchooseSquare.Makethesides
ofthesquare0.4,andputthebasepositionat(0.3,0.3);click“BuildAll.”Rightclickon
Geometry;choose“BooleanOperations,”andchooseDifference.Addthefirstsquareand
subtractthesecondone.Thenchoose“BuildAll.”
Step3(SettheBoundaryConditions) Tocheckthattheinsideboundariesareinsulated,
clickonHeatTransfer/ThermalInsulation.Thenewboundariesarelisted,sotherewillbe
noheatfluxacrossthem.
Step 4 (Create a Mesh) Click on Mesh, “Build All” to get the mesh, which has 572
elements.
Step5(SolvetheProblem) Rightclick“Study1”andchoose=togetthesolution.
Step 6 (Examine the Solution) The contour plot is shown in Figure 11.3; the settings
are the same as in the first case. Notice that the contours of constant temperature are
perpendiculartothethermallyinsulatedboundaries,whichisappropriatebecausethereis
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
FIGURE 11.3 Solutiontoheattransferproblemwithaholeinthecenter.
```

---

## Стр. 276

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:CONVECTIVEDIFFUSIONINMICROFLUIDICDEVICES 265
nogradientnormaltotheboundary.Tofindtheheatfluxontheuppersurfaceofthehole,
rightclicktheResults/DerivedValues’nodeandchoose“LineIntegration.”Thenchange
theexpressionto−Ty,whichistheverticalheatflux.Thevalueis0.046.Itshouldbezero.
Toseetheeffectofmeshrefinement,choosetwofinerdiscretizations,fineandfiner.The
valuesofthisintegralarethen0.0414forfine,798elements;0.0325forfiner.Choosingtwo
finermeshesgives0.0213forextrafine,1598elements;5434elements;andforextremely
fine,0.0133,43644elements.Clearlytheintegratedheatfluxisconvergingtozeroasthe
meshisrefined.
Ifwewantedtosolvethisproblemwithphysicalpropertiesinsteadofinanondimen-
sional form, we would need to open “Model 1” and “Open Materials Browser.” Choose
“Built-in”andselectAluminumandrightclick“AddMaterial”toputitinthesimulation.
Be sure that the domain number, 1, appears in the box. Then go back to “Heat Transfer
in Solids” and change the thermal conductivity from “User defined” to “From material.”
Changethetemperaturesto296and273andsolveagain.
EXAMPLE:CONVECTIVEDIFFUSIONINMICROFLUIDICDEVICES
TheT-sensorisdescribedinChapter10,butitskeyuseistotransferachemicalfromone
flowingstreamtotheother.Thus,theconvectivediffusionequationmustbesolved,too.A
fluid(suchaswater)comesinthetopandbottom,butthetopstreamcontainsadissolved
chemicalthatneedsistobetransferred.Thebottomstreammaycontainadifferentchemical
thatwillreactandfluoresce,thuspermittingavisualdetection.Yourgoalistopredicthow
fastthetransfertakesplace.TheT-sensorwasdevelopedbyWieglandYager(1999)and
Hatchetal.(2001).
Step1(OpenandSetPreferences) OpentheComsolMultiphysicsfileforthefluidflow
problem in Chapter 10. First, we add physics by right clicking “Model, 1” choosing
“TransportofDilutedSpecies,”next;Stationary,finish.
Step2(SettheVariables) RightclickDefinitionsandchooseVariables,andsetPeto1.
Step3(DefinetheProblem) Clickonthe“TransportofDilutedSpecies”nodeandchoose
Discretization.ChangefromLineartoQuadratic.IfDiscretizationdoesnotappear,goto
theShowbutton(seeFigure9.2)andchooseDiscretization.Rightclickon“Transportof
Diluted Species” and choose “Convection and Diffusion.” Select the total domain, +, to
addittotheSelectionbox.Changethevelocitytouandv.Thediffusivityisastand-infor
1/Pe,sochangeitto1/Pe.
Step 4 (Set the Boundary Conditions) To set the boundary conditions, right click
on“TransportofDilutedSpecies”andchooseInlet.Choosethetopboundary,+,toaddit
totheSelectionbox.Keepthevalueas0.Dothesamethingforthebottomboundary,but
settheConcentrationto1.0.Rightclickon“TransportofDilutedSpecies,”chooseOutlet;
selecttheoutletboundary,+,toaddittotheSelectionbox.
Step5(SolvetheProblem) Tosolvetheproblem,rightclickon“Study2”andchoose=.
```

---

## Стр. 277

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
266 HEATANDMASSTRANSFERINTWOANDTHREEDIMENSIONS
FIGURE 11.4 SolutiontoT-sensordiffusion/convectionproblemwithD=1.
Step6(ExaminetheSolution) Thevelocityshowsfirstinthegraphicswindow.Toseethe
concentration,rightclickonResultsandchoose“2DPlotGroup.”Rightclickon“2DPlot
Group”andchooseSurface.Thedefaultexpressionisspf.U.Changeittoc.Alsochangethe
Datasetto“Solution2.”Clicktheploticontoseetheplotofconcentration.InFigure11.4
wedothesamethingbutchooseContourratherthanSurface.Tocheckthemassbalance,
right click on the Derived Values under Results and choose “Line Integration.” Integrate
v∗c over the top and bottom boundary (0.0 and 0.5000000). Integrate u∗c over the outlet
(0.4999998).Thus,themassbalanceisquitegood.
Step8(ChangethePecletNumber) ChangethePecletnumberto50andrepeat.Clickthe
VariablesnodeunderDefinitionsandchange1to50.Rightclick“Study2”andchoose=.
Change to the plot of concentration, Figure 11.5. Now there is good mixing, but not as
good as when the Peclet number is smaller. The flow rates in and out are 0.499959 and
0.5000000,whichgivesaquiteaccuratemassbalance.ChangethePecletnumberto500
FIGURE 11.5 SolutiontoT-sensordiffusion/convectionproblemwithD=1/50.
```

---

## Стр. 278

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:CONVECTIVEDIFFUSIONINMICROFLUIDICDEVICES 267
FIGURE 11.6 SolutiontoT-sensordiffusion/convectionproblemwithD=1/500.
and repeat, giving Figure 11.6. Now the mixing is not nearly as good. The mass balance
numbersarethesameasbefore,givingagoodoverallmassbalance.Note,however,that
theconcentration(inthescale)goesfrom−0.019to1.0212.Thisindicatesthatthereare
oscillationsinthesolution,buttheyareontheorderof2%.Thiserrorcanbedecreasedif
desiredbyrefiningthemesh.
Step 9 (Plot Two Solutions) To plot outlet concentration profiles for Pe = 50 and 500,
rightclickGlobalDefinitions,chooseParameters,andusePe(youcansetavalue).Now
rightclickon“Study2”andchoose“ParametricSweep.”Whenyouclickonthe+,thePe
willappearinthewindow;selectitandAdd,thenOK.Clickontheparametericonandset
therangefrom50to500withastepof450.Rightclick“Study2”andchoose=.Right
clickonResults,choose“1DPlotGroup”;rightclickitandchoose“LineGraph.”Thetwo
concentrationprofilesareplottedononegraph,Figure11.7.
1
0.8
0.6
0.4
0.2
0
0 0.1 0.2 0.3 0.4 0.5
noitartnecnoC
Pe = 500
Pe = 50
y
FIGURE 11.7 ExitconcentrationsforPe=50and500(D=1/50and1/500).
```

---

## Стр. 279

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
268 HEATANDMASSTRANSFERINTWOANDTHREEDIMENSIONS
EXAMPLE:CONCENTRATION-DEPENDENTVISCOSITY
Theviscosityofamixturedependsuponitsconcentration,althoughoftenthatdependenceis
small.Toresolvethepreviousproblemandallowtheviscositytodependuponconcentration
usethefollowing(arbitrary)formula
μ=1+c (11.12)
Then the viscosity of the material coming into the top of the T-sensor is 2, whereas the
viscositycomingintothebottomis1.Tomodifythemodel,performthefollowingsteps.
Step1(SettheVariables) Wewanttochangetheviscosityfrom1to1+alpha∗c,starting
with the previous solution. The alpha is used so that it can be a parameter, either 0 or 1.
ClickontheParametersnodeunderGlobalDefinitions.Defineaparameteralphaandsetit
to0.BesurethePeis500.(ThealphacanalsobesetinVariablesin“Model1”.)
Step2(DefinetheProblem) Clickonthenode“FluidProperties”under“LaminarFlow”
andchangetheviscosityfrom1to1+alpha∗c.
Step3(SolvetheProblem) Rightclick“Study1”andchooseanotherParametricSweep;
usealphaastheparameter:clickontheparametericon,selectalpha,Add,thenOK,then
set the value to range (0,1). Also right click on the “Parametric Sweep” and delete the
oneusingPecletnumber.Clickon“Study1”andnoticethattherearetwoequationslisted
there,theflowequationandtheconcentrationequation.Makesurethatbothareselected
tobesolved(greencheckmark),sincetheviscositydependsontheconcentration,which
dependsontheflow,whichdependsontheviscosity.Rightclick“Study1,”choose=.
Step 4 (Examine the Solution) Click on the “Line Graph” node under “1D Plot Group”
toseetheconcentrationprofileattheoutletforthetwosolutions:bothwithPe=500but
one with viscosity = 1 the other 1 + alpha∗c. Clearly there is not much difference; see
Figure11.8.
1
0.8
0.6
0.4
0.2
0
0 0.1 0.2 0.3 0.4
noitartnecnoC
μ = 1+c μ = 1
y
FIGURE 11.8 T-sensordiffusion/convectionproblemwithD=1/500andμ=1,μ=1+c.
```

---

## Стр. 280

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:VISCOUSDISSIPATION 269
EXAMPLE:VISCOUSDISSIPATION
Sofartheexampleshaveassumedthatviscousdissipationdoesnotcauseanappreciable
temperaturerise.Viscousdissipation,ofcourse,alwaysincreasesthetemperature,butoften
the increase is negligible. However, it is important to know the magnitude or provide an
upperbound.Toseetheeffectofviscousdissipation,aheatgenerationtermisaddedtothe
energyequation.In2Dproblemsthisheatgenerationtermis
(cid:4) (cid:5)(cid:2) (cid:3) (cid:2) (cid:3) (cid:6) (cid:7) (cid:8) (cid:9)
∂u 2 ∂v 2 ∂v ∂u 2
(cid:4) v =μ 2 ∂x + ∂y + ∂x + ∂y , Cartesiangeometry (11.13)
and
(cid:10)(cid:2) (cid:3) (cid:2) (cid:3) (cid:11) (cid:12) (cid:13) (cid:7) (cid:8)
∂u 2 ∂v 2 v 2 ∂u ∂v 2
(cid:4) v =2μ ∂z + ∂r + r +μ ∂r + ∂z , cylindricalgeometry
(11.14)
TheeffectofviscousdissipationisillustratedherefortheorificeproblemsolvedinChapter
10.Thenotationusesuastheradialvelocityandwastheaxialvelocity:
Q =2 ∗ Br ∗ (wz ∧ 2+ur ∧ 2+(u/r) ∧ 2)+Br ∗ (wr +uz) ∧ 2 (11.15)
TheBrinkmannumberis
u2 C μ
Br =Pr s , Pr= p (11.16)
C T k
p s
Theparametersusedinthisexampleare
ρ =1,η=1/Re,Pr=7,Re=31.62,C =Pr ∗ Re=221.3,Br =0.141 (11.17)
p
There are two options for the temperature boundary conditions. In the first option, the
system can be adiabatic where all walls use the boundary condition of no flux. In the
secondoption,thewallscanbemadeofmetal,withplentyofcoolantoutside,andthenthe
boundaryconditionwoulduseaconstanttemperature.Here,adiabaticboundaryconditions
are used. Thus, the temperature out of the device (minus the inlet temperature) gives the
temperatureriseduetoviscousdissipation.
Step 1 (Open and Set Preferences) Open the Comsol Multiphysics file for the orifice
problem solved in Chapter 10. Right click “Model 1” and choose “Add Physics.” Select
“HeatTransfer/HeatTransferinFluids”;next,Stationary,finish.
Step2(SettheVariables) ClickonVariablesandaddthefollowing:Re=31.62,Pr=7,
Cp=Pr∗Re,Br=0.141.
Step 3 (Define the Problem) Click on the node “Heat Transfer in Fluids” under “Heat
Transfer.”ChangetheVelocityto“Velocityfield(spf/fp1).”Setthephysicalpropertiesto
k=1,density=1,Cp=Cp,gamma=1.Theflowproblemneedstobechangedtousea
```

---

## Стр. 281

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
270 HEATANDMASSTRANSFERINTWOANDTHREEDIMENSIONS
viscosityof1/31.62.UnderStudy1,deletethe“ParametricSweep.”Under“Study1,”click
on “Step 1: Stationary” and make sure the Physics interface selected is “Laminar flow.”
Rightclickon“Study1”andchoose=.Thissolvestheflowproblem.Tocreatethesource,
right click “Heat Transfer” and choose “Heat Source.” Select the domain, +, to add it to
theSelectionbox.TheQisdefinedas2∗Br∗(wz∧2+ur∧2+(u/r)∧2)+Br∗(wr+uz)∧2
toagreewithEq.(11.15).ForHeatTransfer,chooseDiscretizationandchooseQuadratic
ifitisnotalreadyQuadratic.
Step 4 (Set the Boundary Conditions) The thermal problem is solved with adiabatic
boundaries. The default conditions are axial symmetry on the centerline and adiabatic
boundaries everywhere else. Right click on -Heat Transfer-, choose Inlet, select the inlet
boundary, +, and set the Temperature to 1. Then Right click on -Heat Transfer-, choose
Outlet,selecttheoutletboundary,+.
Step5(SolvetheProblem) Clickon“Step1:Stationary”under“Study2”andmakesure
theheattransferoptionisselected.Rightclickon“Study2”andchoose=.
Step6(ExaminetheSolution) ThenrightclickonResults,choose“2DPlotGroup.”Right
clickonitandchooseContour.ChangetheexpressiontoT2andclicktheploticon,giving
Figure11.9.TheeffectofviscousdissipationisshowninFigure11.9whentheflowfieldis
thatshowninFigure10.15c.Thepeaktemperatureisonly1.045◦C,whichisonly0.045◦C
higher than the input temperature. It is also possible to make the viscosity depend upon
temperature. Before doing that, you can solve the problem with a constant viscosity to
determinethemaximumtemperaturerise.Ifthetemperatureriseissmall,youhaveverified
thattheassumptionthattheviscosityisconstant.Ifthetemperatureriseislarge,thenthe
problemcanbesolvedallowingtheviscositytodependupontemperature.Lettheviscosity
dependupontemperature,asinEq.(11.18):
μ=μ exp(E/RT) (11.18)
0
Equation (11.18) is inserted for the viscosity for the Physics/Subdomain Settings for the
Navier–Stokesequation:
μ=mu0 ∗ exp(E/(R ∗ T)) (11.19)
Naturally,youmustusethecorrectunits.YoucanalsousetheMaterialsBrowsertogetthe
viscosityvariationwithtemperatureifdesired.
EXAMPLE:CHEMICALREACTION
It is easy to model the microfluidic device as a chemical reactor. You prepare the flow
problemasillustratedinChapter10,addtheconvectivediffusionequation,andenterthe
reactionrate.Supposetherateofreactionis
Rate=kc2, whererateisinmolepervolumepertime (11.20)
```

---

## Стр. 282

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:CHEMICALREACTION 271
FIGURE 11.9 Temperaturerise(K),Re=101.5=31.6,20contourlevelsfrom1to1.048.
Step1(OpenandSetPreferences) Openthemicrofluidicsimulationwithbothflowand
diffusion.
Step 2 (Define the Problem) To add a reaction rate, right click “Transport of Diluted
Species”andchooseReactions.Thenselectthedomain,+,togetitintotheSelectionbox.
SetR torate.RightclicktheDefinitionsnodeunder“Model1”andchooseVariables.De-
C
finerate=−k∗c∗c.Rightclick“GlobalDefinitions”andchooseParametersandsetk=0.1.
Step3(SolvetheProblem) Rightclickon“Study1”andchoose=togetthesolution.The
materialreactsveryquickly.
```

---

## Стр. 283

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
272 HEATANDMASSTRANSFERINTWOANDTHREEDIMENSIONS
EXAMPLE:WALLREACTIONS
Awallreactioncanbeincludedaswell.Supposerateofreactiononthewallis
Rate=−k c2, whererateisinmoleperareapertime (11.21)
b
Thefluxboundaryconditionis
−n·N= N , N=−D∇c+uc (11.22)
0
Next,youneedtoaugmentthefluxequationonthewall.Thenormalvelocityonthewall
issettozerofortheflowproblem.Thus,thediffusivefluxequalstherateofreaction.Enter
intothewindowforN thefollowingexpression:
0
N =−kb ∗ c ∗ c (11.23)
0
Step 1 (Define the Problem) For a surface reaction, right click on “Transport of Diluted
Species” and choose Flux. Choose a boundary, +, to add it to the Selection box. Check
theSpeciescboxandsetN =−kb∗c∗c.ChoosetheParameterssubnodeunder“Global
0,c
Definitions”andsetkb=0.1.
Step2(SolvetheProblem) Rightclick“Study1,”andchoose=.
Step3(ExaminetheSolution) Chooseacontourplotofc;nowthereactioninterfaceis
nearthedividingstreamlineandnearthewall,too.
EXAMPLE:MIXINGINASERPENTINEMIXER
To illustrate what is possible in three dimensions, consider the serpentine mixer that is
modeledinChapter10.Theideaisthatattheinlettherearetwostreamsentering,andone
ofthemcontainsadifferentchemical.Theobjectiveistomixthechemicalsinasshorta
distanceaspossible.Becausemixingbydiffusionisslow,chimneysandturnsareinserted
toenhancethemixingandmakeitoccurinashorterdistance(Neilsetal.,2004).
Step1(OpenandSetPreferences) OpentheComsolMultiphysicsfilefortheserpentine
fluid flow problem in Chapter 10. First, we add physics by right clicking “Model 1,”
choosing“TransportofDilutedSpecies,”next;Stationary,finish.
Step2(DefinetheProblem) Clickonthe“TransportofDilutedSpecies”nodeandchoose
Discretization. Change from Linear to Quadratic. Right click on Transport and choose
“Convection and Diffusion.” Select the total domain, +, to add it to the Selection box.
Changethevelocityto“Velocityfield(spf/fp1).”Thediffusivityisastand-infor1/Pe,so
changeitto1/Pe.GobacktoDefinitions,rightclickVariables,andsetPeto1000.
Step 3 (Set the Boundary Conditions) To set the boundary conditions, right click
on“Transport of Diluted Species” and choose Inlet. Choose the left inlet boundary, +,
```

---

## Стр. 284

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:MIXINGINASERPENTINEMIXER 273
to add it to the Selection box. Set the value to 1. To get this boundary you may have to
change the orientation of the model. Do the same thing for the right inlet boundary, but
leave the Concentration as 0. Right click on Transport, choose Outlet; select the outlet
boundary,+,toaddittotheSelectionbox.
Step4(SolvetheProblem) Tosolvetheproblem,rightclickon“Study2”andchoose=.
Step 5 (Examine the Solution) The velocity shows first in the graphics window. To see
theconcentration,rightclickonResultsandchoose“2DPlotGroup.”Rightclickon“2D
Plot Group” and choose Surface. The default expression is spf.U. Change it to c. Also
changethe“Dataset”to“Solution2.”Clicktheploticontoseetheplotofconcentration,
Figure11.10.
Step 6 (Make More Plots) A plot of the concentration profile inside the domain (Figure
11.11) is obtained by opening “Data sets” under Results, and right clicking to get “Cut
Plane.” In the settings window you can determine where the plane will be, and choose
the plot icon to see the plot. Notice that there are some small errors, since the maximum
concentrationis1.081andtheminimumvalueis−0.0219,butthesearesmallenoughtobe
ignored.Theregionwheretheyoccurcanbefoundbyplottingonlyvaluesofconcentration
greaterthan1.0;nextplotonlyvaluesofconcentrationlessthan0.0.
1.0806
1
0.8
0.6
10
0
–0.2 0.4
5
3
2
1
0 0 0.2
z
y x 0
–0.0219
FIGURE 11.10 Concentrationdistributiononthewallofaserpentinemixer.
```

---

## Стр. 285

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
274 HEATANDMASSTRANSFERINTWOANDTHREEDIMENSIONS
Contour: c
0.65 0.754
0.754
0.6
0.7275
0.55
0.7011
0.5 0.6746
0.45 0.6482
0.6217
0.4
0.5953
0.35
0.5688
0.3 0.5424
0.25 0.516
0.4895
0.2
0.4631
0.15
0.4366
0.1 0.4102
0.05 0.3837
0.3573
0
0.3308
–0.05
0.3044
–0.1 0.2779
–0.15 0.2515
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 0.2515
FIGURE 11.11 Concentrationdistributionintheyz-planeatx=8.
MICROFLUIDICS
Many microfluidic devices involve diffusionofmassaswellasfluidflow.The following
articles give details of these applications: Jensen (1999), Stone and Kim (2001), Chow
(2002),Freemantle(2005),Henry(2005),andausefulwebsiteiswww.Lab-on-a-Chip.com.
Thevelocitycrossingaplanenormaltotheflowisseldomuniform,sothediffusionmust
beexaminedinthemidstofnonuniformvelocityprofiles.Thesimplestillustrationofthis
effectiswithTaylordispersion.
Forsimplicity,considerflowbetweentwoflatplatesasshowninFigure11.12.Theflow
islaminarandthevelocityprofileisquadratic.Nowsupposetheenteringfluidhasasecond
chemicalwiththeconcentrationshown,1.0inthetophalfand0inthebottomhalf.Asthis
fluidmovesdownstream(totheright),thevelocityishighestinthecenter,sothesecond
chemicalmovesfastthere.However,itcanalsodiffusesideways,andthefluidelementthat
doesfirstdiffusesidewaysthenmovesslowerdowntheflowchannel.Atapointnotonthe
c = 1
FIGURE 11.12 Diffusioninafullydevelopedplanarflow.
```

---

## Стр. 286

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
MICROFLUIDICS 275
(a)
(b)
FIGURE 11.13 Fully developed velocity profile in (a) 1 × 8 rectangular channel; (b) 1 × 8
rectangularchannelwithsliponthesidewalls.
centerline,theconcentrationisdeterminedbythisslowervelocityintheflowdirectionand
diffusion sideways because the concentration on the centerline is always higher than the
concentrationinadjacentfluidpaths.ThisiscalledTaylordispersion(Deen,1998).Taylor
(1953) and Aris (1956) showed how to model the average concentration as a function of
length using a simpler equation (dispersion in the flow direction only) and an effective
dispersioncoefficientgivenby(whereD isthehydraulicdiameter)
h
<v >2 D2 K <v >2 D2 Pe2
K = D+ h or =1+ h =1+ (11.24)
192D D 192D2 192
Next,considerfullydevelopedflowinanarrowchannel,whichistypicalofamicrofluidic
device. The normal view is shown in Figure 11.13 with flow going into the paper. The
velocityvariesinxandyaccordingtotheequation
(cid:2) (cid:3)
∂2v ∂2v (cid:6)p
η + =− (11.25)
∂x2 ∂y2 L
AtypicalsolutionisshowninFigure11.13a.Ifoneusesamodelignoringtheedgeeffects,
oneisessentiallyusingthevelocityprofileshowninFigure11.13b.
When diffusion is added into the problem, these two flow situations (a and b) are
different.Takethe3DflowsituationshowninFigure11.14,withthevelocityprofilebeing
thesameforallx.Letthematerialononesidehaveadiluteconcentrationofsomespecies
z
x
y
FIGURE 11.14 Three-dimensionalrectangularchannel.
```

---

## Стр. 287

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
276 HEATANDMASSTRANSFERINTWOANDTHREEDIMENSIONS
(taken = 1), and on the other side there is no concentration of that species (c = 0). As
the material flows down the channel, diffusion perpendicular to flow occurs, so we must
characterizethemixing.
CharacterizationofMixing
Toevaluatemixing,itisnecessarytohaveaquantitativemeasure.Thevariancefromthe
mean is appropriate, but in a flowing system some fluid elements have a higher velocity
than others. The concept in chemical engineering that is used to account for this is the
mixingcupconcentration.Thisistheconcentrationoffluidiftheflowemptiedintoacup
thatwaswellstirred.Inmathematicalterms,themixingcupconcentrationis
(cid:14)
c(x,y,z)v(x,y)dxdy
c = A (cid:14) (11.26)
mixingcup
v(x,y)dxdy
A
Notethattheaveragevelocitytimesthemixingcupconcentrationgivesthetotalmole/mass
fluxthroughanareaatpositionz.Thenitisnaturaltodefinethevarianceoftheconcentration
fromthemixingcupconcentration:
(cid:14)
[c(x,y,z)−c ]2v(x,y)dxdy
mixingcup
c = A (cid:14) (11.27)
variance
v(x,y)dxdy
A
AverageConcentrationalonganOpticalPath
Opticalmeasurementsarefrequentlymadethroughthethinlayerofamicrofluidicdevice.
Theaverageconcentrationisthendeterminedbytheintegralalongthepath,suchas
(cid:14)L (cid:14)L
c = c(x.y,z)dy/ dy (11.28)
optical
0 0
When the velocity is variable in the y-direction some regions of the fluid are moving
faster than others. Thus, the optical measurement, or integration along the optical path,
may not be comparable to the mixing cup concentration along the same path. Indeed, it
isentirelypossiblethatseveraldifferentflowandconcentrationdistributionscangivethe
sameaveragealonganopticalpath.Inthatcase,computationalfluiddynamicscanbeused
tointerprettheopticalmeasurements.
PecletNumber
The dimensionless convective diffusion equation is Eq. (11.9), where the Peclet number
is a ratio of the time for diffusion, x2/D, to the time for convection, x /v . Typically, Pe
s s s
```

---

## Стр. 288

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
MICROFLUIDICS 277
isverylarge,andthispresentsnumericalproblems.ThesecondformofEq.(11.9)shows
thatthecoefficientoftheterminthedifferentialequationwithhighestderivativegoesto
zero;thismakestheproblemsingular.ForlargebutfinitePetheproblemisstilldifficultto
solve.Forasimpleone-dimensional(1D)problemitcanbeshown(Finlayson,1992)that
thesolutionwilloscillatefromnodetonodeunrealisticallyunless
Pe(cid:6)x(cid:3) v x (cid:6)x
≤1, or s s ≤1 (11.29)
2 2D x
s
ThismeansthatasPeincreases,themeshsizemustdecrease.Sincethemeshsizedecreases,
ittakesmoreelementsorgridpointstosolvetheproblem,andtheproblemmaybecometoo
big.Onewaytoavoidthisistointroducesomenumericaldiffusion,whichessentiallylowers
thePecletnumber.Ifthisextradiffusionisintroducedintheflowdirectiononly,thesolution
maystillbeacceptable.Varioustechniquesincludeupstreamweighting(finitedifference;
PeyretandTaylor,1983)andPetrov–Galerkinfiniteelement;HughesandBrooks,1979).
Comsol Multiphysics includes a variety of such techniques, called stabilization, and you
cantweaktheparameters.Basically,ifanumericalsolutionshowsunphysicaloscillations,
eitherthemeshmustberefined,orsomeextradiffusionmustbeadded.Sinceitistherelative
convectionanddiffusionthatmatter,thePecletnumbershouldalwaysbecalculatedevenif
theproblemissolvedindimensionalunits.ThevalueofPewillalertthechemist,chemical
engineer,orbioengineerwhetherthisdifficultywouldariseornot.Typically,v isanaverage
s
velocity,x isadiameterorheight,andtheexactchoicemustbeidentifiedforeachcase.
s
Sometimes an approximation is used to neglect axial diffusion since it is so small
comparedwithaxialconvection.Iftheflowisfullydevelopedinachannelthenonesolves
(forsteadyproblems)
(cid:2) (cid:3)
∂c ∂2c ∂2c
w(x,y) = D + (11.30)
∂z ∂x2 ∂y2
ThisisamuchsimplerproblemsincetheDcanbeabsorbedintothelength,z,
(cid:2) (cid:3)
∂c ∂2c ∂2c
w(x,y) = + (11.31)
∂(zD) ∂x2 ∂y2
Innondimensionaltermstheequationis
(cid:2) (cid:3)
∂c(cid:3) ∂2c(cid:3) ∂2c(cid:3)
w(cid:3) (x (cid:3),y (cid:3) ) = + (11.32)
∂(z(cid:3)/Pe) ∂x(cid:3)2 ∂y(cid:3)2
Then all results should depend upon z(cid:3)/Pe not z(cid:3) and Pe individually. The velocity is not
a constant; it depends upon x and y. Thus, the problem is different from the following
formulation:
(cid:2) (cid:3) (cid:2) (cid:3)
∂c(cid:3) ∂2c(cid:3) ∂2c(cid:3) ∂c(cid:3) ∂2c(cid:3) ∂2c(cid:3) z(cid:3)
<w(cid:3)> = + or = + , wheret (cid:3) =
∂(z(cid:3)/Pe) ∂x(cid:3)2 ∂y(cid:3)2 ∂t ∂x(cid:3)2 ∂y(cid:3)2 <w(cid:3)>Pe
(11.33)
(cid:15) (cid:15)
where<w(cid:3) >= w(cid:3)(x(cid:3),y(cid:3))dx(cid:3)dy(cid:3)/ dx(cid:3)dy(cid:3).
A A
```

---

## Стр. 289

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
278 HEATANDMASSTRANSFERINTWOANDTHREEDIMENSIONS
These phenomena are explored in the problems. Figures 11.4–11.6 illustrate the con-
centrationprofilesthatcanoccur.
EXAMPLE:CONVECTIONANDDIFFUSIONINA
THREE-DIMENSIONALT-SENSOR
Next,weinvestigatea3DT-sensor.
Step 1 (Open and Set Preferences) Prepare a problem for flow in a 3D T-sensor that is
extrudedfromthe2Dversionby0.5intheverticaldirection.
Step2(DefinetheProblem) Rightclickon“Model1”andchoose“AddPhysics.”Select
“Transport in Diluted Species” and then Stationary, and finish. In that model, set the
diffusion coefficient to 1/Pe and insert the velocity components u, v, and w. Change the
DiscretizationtoQuadratic.
Step3(SettheBoundaryConditions) Forthetwoinletboundaries,makeonehavecon-
centrationzeroandtheotherone.Selecttheoutflowboundary.
Step 4 (Solve the Problem) A “Study 3” will be generated, and deselect the flow and
Poisson’sequationsothatonlytheconvectivediffusionequationissolved.165,692degrees
offreedomareused.
Step5(ExaminetheSolution) ForPe=50,theintegralofcis0.5006,theintegraluis
1.937,theintegralofc∗uis0.9686,themixingcupconcentration,integralofc∗u/1.937,is
0.50008,andthevarianceis0.02008.Thelimitsontheplotofconcentrationare0–1,sothe
solutionhasnovisibleoscillations;isoconcentrationsurfacesareshowninFigure11.15.
Step6(ExamineAnotherSolution) ForPe=500,theintegralofcis0.5012,theintegral
uis1.937,theintegralofc∗uis0.9684,themixingcupconcentration,integralofc∗u/1.937,
is 0.500004, and the variance is 0.1594, indicating that mixing is minimal. The limits
on the plot of concentration are −0.013 to 1.0025, so the solution has small oscillations;
isoconcentrationsurfacesareshowninFigure11.16.
Step7(ExaminetheSolutiononaCut-Plane) UnderResults/DataSets,rightclickand
choose2DCutPlane.Definetheplaneastheyz-planeatx=0.51.Thevalue0.51wasused
sothatitwasjustinsidetheturn;thisavoidsinvolvingallthesideboundariesoftheinlet
ducts.ThesimilarnumbersforPe=500were:theintegralofcis0.500004,theintegralu
is1.943,theintegralofc∗uis0.9716,themixingcupconcentration,integralofc∗u/1.943,
is0.5002,andthevarianceis0.2207.Ina2Dproblem,themaximumvarianceis0.25,so
thisindicatesthatlittlemixinghasoccurreduptothatpoint.
Step8(ExaminetheSolutiononaLineProbe) Sometimesitisconvenienttomeasurethe
concentrationbyshiningalightofaspecificwavelengththroughthedeviceanddetermining
theabsorption.Theanalogofthisisusingalinethroughthedevice.ChooseResults,right
click on “Cut Line 3D” and identify the coordinates of the line. For example, for the
solutionsshowninFigures11.15and11.16,atthepointx=2.5(theend)andy=−0.075
```

---

## Стр. 290

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
EXAMPLE:CONVECTIONANDDIFFUSIONINATHREE-DIMENSIONALT-SENSOR 279
1
1
0.8
0.4 0.6
0.2
0
2 0.4
0.5
0 1
0.2
–0.5
0
z
y x
0
0
FIGURE 11.15 ConcentrationforPe=50.
1.0025
1
0.8
0.4 0.6
0.2
0
2 0.4
0.5
0 1
0.2
–0.5
0
z
y x
0
–0.0129
FIGURE 11.16 ConcentrationforPe=500.
```

---

## Стр. 291

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
280 HEATANDMASSTRANSFERINTWOANDTHREEDIMENSIONS
theintegrationofcfromz=0to0.5was0.1948forPe=50butonly0.0571for500.This
indicatesthatlittleofthematerialfromthetophalfgotthroughtothelowerhalfwhenPe
was500.
CHAPTERSUMMARY
ThischapterillustratedtheuseofComsolMultiphysicsforproblemsofheatconduction,
heat conduction and convection, and mass diffusion and convection. These problems are
complicated,buttheydofollowconditionsinreal-lifethatengineersmusttackle.Knowing
howtodothiswillallowyoutoworkinavarietyofmodernindustries.
PROBLEMS
Steady,Two-DimensionalProblems
11.1 HeattransfertakesplaceinthegeometryshowninFigure11.17.BoundariesAare
1
insulated;alongboundaryBthetemperatureis1.0;theboundaryconditionatCis
∂T
−k =hT (11.34)
∂n
Usek=1,h=3andsolveforthetemperatureprofile.(b)Usek=0.01,h=3and
solveforthetemperatureprofile;comparetheresults.
1
0.2 A B B A
A A 1
C
3
FIGURE 11.17 Heattransferinamicrochemicalreactor.
11.2 A slotted-electrode electrochemical cell is shown in Figures 11.18–11.19 (see
1
OrazemandNewman,1984).Thegoverningequationforpotentialis
∂2φ ∂2φ
∇2φ =0, or + =0 (11.35)
∂x2 ∂y2
```

---

## Стр. 292

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 281
hν hν hν
Glass
Counterelectrode
Semiconductor
FIGURE 11.18 Slotted-electrodeelectrochemicalcell.
L G
h
φ=1
A B
t
E φ=0 F
FIGURE 11.19 Solutiondomain.
Determinethecurrentdistribution(∂φ/∂n)alongthefacesABandEF.Thevari-
ablesaret=0.25,h=1,L=2.5,andG=1.
11.3 Project.SolveLaplace’sequation[Eq.(11.33)]intheregionshowninFigure11.20
1
withthefollowingboundaryconditions:
(cid:2) (cid:3)
∂u ∂u πθ
u =0 alongθ =0, = =0 along θ =α, u =sin alongr =1
∂n ∂θ 2α
(11.36)
```

---

## Стр. 293

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
282 HEATANDMASSTRANSFERINTWOANDTHREEDIMENSIONS
u = f(θ)
∂u/∂ θ = 0
u=u0 = 0
FIGURE 11.20 Solutiondomain.
(a)α =π/4;(b)α =3π/4;(c)α =π;(d)α =3π/2.Commentonthesingularity
thatoccursatthecorner,despitethesmoothboundaryconditionsforu.Theexact
solutionis
(cid:2) (cid:3)
πθ
u =r π/2α−1sin (11.37)
2α
InComsol,youneedtoconvertthe(x,y)valuesofapointontheboundaryinto
θ values,usingthearccosfunction(acos).
11.4 SolveProblem9.2inacylindricalpelletwhoselengthequalsitsdiameter.Compare
1
theaveragereactionrateinthecylindricalpelletwiththatinasphericalpellet.
11.5 SolveProblem9.6inacylindricalpelletwhoselengthequalsitsdiameter.Compare
1
theaveragereactionrateinthecylindricalpelletwiththatinasphericalpellet.
11.6 It is desired to measure the thermal conductivity of a ferrofluid, a suspension
2
of magnetic particles in an oil-based solvent (Rosensweig, 1985). The fluid is
contained in a thin layer between two thick copper plates, with insulation at the
edges,asshowninFigure11.21.Thedimensionsareradiusofinnercircleis0.02m;
Copper
Ferrofluid
Copper
C
L
ssalgixelP
Insulation
FIGURE 11.21 Thermalconductivitymeasurementdevice.
```

---

## Стр. 294

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 283
thicknessofplexiglassis0.005m;thicknessofinsulationlayeris0.01m.Theheight
ofthecoppercylindersis0.01m,andthethicknessoftheinternallayercontaining
theferrofluidis0.002m.SolvefortheheattransferprobleminComsolusingthe
materialpropertiesintheMaterialBrowser.Usenylonfortheplexiglass(ithasthe
samethermalconductivity).Createanewmaterialnamed“Insulation”andusek=
0.09W/mK,whichisavalueforasbestos.Theestimateofthethermalconductivity
isk=0.25W/mK.Intheexperiment,anelectricheaterwillsupplyheattothetop
copperlayerandthetemperaturewouldbemeasured.Here,takethetopofthetop
copperat30◦Candthebottomofthebottomcoppercylinder25◦Canddetermine
theheatflux.Useaninsulatingboundaryonthetopandbottomoftheplexiglassand
insulation,andatemperatureontheoutsideoftheinsulationof25◦C.Determine
the accuracy of the measurement: use the heat flux and temperature drop across
the ferrofluid from Comsol and the thickness to determine the measured thermal
conductivity.Whatistheerror?Howcanthemeasurementbeimproved?
HeatTransferwithFlow
11.1 Solve for the heat transfer from a sphere maintained at temperature 1 when a
1
Newtonianfluidisflowingpastitwithatemperatureofzero.Useconstantviscosity
andintegratethefluxoverthesurfacetofindtherateofheattransfer.(a)Re=0
(Stokessolution)andPe=1,10,and100.(b)repeatpart(a)withRe=10.
11.2 SolvethefollowingGraetzproblemusingtheconvectionandconductionmodule
1
in Comsol Multiphysics. When there is no axial conduction, you can absorb the
Peclet number into the distance, z, and solve the problem once for all Pe. Solve
witharadiusof1.0andalengthofz/Pe=1;use“Outlet”astheoutletboundary
condition:
(cid:2) (cid:3) (cid:16)
2(1−r2)Pe ∂T =2(1−r2) ∂T = 1 ∂ r ∂T , ∂T (cid:16) (cid:16) (cid:16) =0,
∂z ∂(z/Pe) r ∂r ∂r ∂r
r=0
T(1,z)=1, T(r,0)=0 (11.38)
ComputetheNusseltnumber,whichisgivenby
(cid:16)
−
∂T (cid:16)
(cid:16)
(cid:16)
∂r u R
Nu = r=1 , <T >=averagetemperature, Pe= avg (11.39)
<T >−1 D
11.3 Solve the same Graetz problem as in Problem 11.8, but add in axial conduction.
1
SolvetheequationsintheformofEq.(11.40)witharadiusof1.0,alengthof6,
andPe=20:
(cid:7) (cid:2) (cid:3) (cid:8) (cid:16) (cid:16)
2(1−r2) ∂T = 1 1 ∂ r ∂T + ∂2T , ∂T (cid:16) (cid:16) (cid:16) =0, ∂T (cid:16) (cid:16) (cid:16) =0,
∂z Pe r ∂r ∂r ∂z2 ∂r ∂z
r=0 z=L
T(1,z)=1, T(r,z =0)=0 (11.40)
```

---

## Стр. 295

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
284 HEATANDMASSTRANSFERINTWOANDTHREEDIMENSIONS
11.4 TheboundaryconditionsinProblem11.9arenotreallyappropriatesincetherecan
1
beconductionupstreamintotheunheatedregion.Solvetheproblemfromz=−2
to6,includingtheupstreamregion.UsePe=20.Theequationsare
(cid:7) (cid:2) (cid:3) (cid:8) (cid:16) (cid:16)
2(1−r2) ∂T = 1 1 ∂ r ∂T + ∂2T , ∂T (cid:16) (cid:16) (cid:16) =0, ∂T (cid:16) (cid:16) (cid:16) =0,
∂z Pe r ∂r ∂r ∂z2 ∂r ∂z
r=0 z=L
T(r,z =−2)=0 (11.41)
T(1,z)=0, z ≥0, T(1,z)=1, z <0 (11.42)
ComparetheanswerwiththeanswerinProblem11.9.
11.5 SolvetheGraetzProblem11.9butuseaboundaryconditionofT =1attheoutlet.
1
SolvewithPe=30onashortdomain,L=6;solveonalongdomain,L=30.This
problemillustratestheimportanceofhavingthecorrectboundaryconditions(see
ChangandFinlayson,1980).
ReactionwithKnownFlow
11.12 Convection, diffusion, and reaction in a packed bed reactor are governed by the
2
followingequationsinacylindricaldomainwithlength2andradius0.1:
(cid:2) (cid:3)
∂c ∂c D ∂ ∂c
+u = r −kc
∂t ∂z r ∂t ∂r
(cid:16) (cid:16)
c(r,z,0)=c 0 , c(r,0,t)=c 1 , ∂ ∂ r c (cid:16) (cid:16) (cid:16) =0, −D ∂ ∂ r c (cid:16) (cid:16) (cid:16) =k m (c| r=R −c 2 )
r=0 r=R
(11.43)
Solvewiththefollowingparameters.Youshouldintegratetoabout0.2:
c =0, c =1, c =0, u =0, w =10, D =0.1, D =0, k =10, k =1
0 1 2 rr zz m
(11.44)
11.13 Equation (11.45) shows the dimensionless equations for a nonisothermal packed
2
bedreactorinacylindricaldomain:
(cid:2) (cid:3) (cid:2) (cid:3)
∂c 1 ∂ ∂c ∂T 1 ∂ ∂T
=α r +βR(c,T), =α(cid:3) r +β(cid:3) R(c,T)
∂z r ∂r ∂r ∂z r ∂r ∂r
(cid:16) (cid:16) (cid:16) (cid:16)
∂
∂
r
c (cid:16) (cid:16)
(cid:16)
= ∂
∂
T
r
(cid:16) (cid:16)
(cid:16)
=0,
∂
∂
r
c (cid:16) (cid:16)
(cid:16)
=0, − ∂
∂
T
r
(cid:16) (cid:16)
(cid:16)
= Biw[T(1,z)−Tw]
r=0 r=0 r=1 r=1
c(r,0)=0, T(r,0)=1
(11.45)
```

---

## Стр. 296

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 285
Here, c represents the conversion, not the concentration. Solve this problem
usinga1DAxisymmetricoptionwithTimeDependent.Thinkofzastime,t,and
integratetot=3:
R(c,T)=(1−c)ey−y/T, α =α(cid:3) =1, β =0.3, β(cid:3) =0.2, γ =20, Tw =0.92
(11.46)
and(a)Biw=1;(b)Biw=20.Thedimensionlessvariablesaredefinedas
Ld Ld Gd C
α = p , α(cid:3) = p , Pe = p, Pe = p
R2Pe R2Pe m ρD h Gd k
m h e p e
(11.47)
β =
k
0
Lρ
, β(cid:3) =
(−(cid:6)H
rxn
)k
0
c
0
L
, Biw =
hwR
G C GT k
p 0 e
whered istheparticlediameter,Gisthemassflux,D istheeffectivediffusivity,
p e
k istheeffectivethermalconductivity,andh istheheattransfercoefficientatthe
e w
cylindricalwall.Commentontheradialdistributionoftemperatureandconcentra-
tioninthetwocases.Basedonthislimitedexperience,giveyourrecommendations
aboutwhenthetemperatureandconcentrationwillvarysignificantlyintheradial
direction.
ReactionwithNoFlow
11.14 Equation (11.48) governs the transient reaction and diffusion with a
1
Michaelis–Menten reaction in a porous media. Integrate the equations to steady
stateusingtheparametersφ2 =10, v =2,Bi =20:
m
(cid:2) (cid:3)
∂c 1 ∂ ∂c c
= r2 −φ2R(c), R(c)=
∂t r2∂r ∂r v+c
(cid:16) (cid:16) (11.48)
∂ ∂ r c (cid:16) (cid:16) (cid:16) =0, − ∂ ∂ r c (cid:16) (cid:16) (cid:16) = Bi m [c(1,t)−1], c(r,0)=0
r=0 r=1
11.15 Project.Equation(11.49)governsthereactionofcarbonmonoxideinathinporous
materialwithplatinumasthecatalyst:
(cid:2) (cid:3) (cid:2) (cid:3)
∂c 1 ∂ ∂c ∂T 1 ∂ ∂T
= r2 −φ2R(c,T), = r2 +βφ2R(c,T)
∂t r2∂r ∂r ∂t r2∂r ∂r
(cid:16) (cid:16) (cid:16)
∂ ∂ r c (cid:16) (cid:16) (cid:16) = ∂ ∂ T r (cid:16) (cid:16) (cid:16) =0, − ∂ ∂ r c (cid:16) (cid:16) (cid:16) = Bi m [c(1,t)−cw],
(cid:16)r=0 r=0 r=1
− ∂ ∂ T r (cid:16) (cid:16) (cid:16) = Bi h [T(1,t)−Tw],c(r,0)=0, T(r,0)=1,
r=1
(cid:7) (cid:2) (cid:3)(cid:8)
c 1
R(c,T)= exp γ 1−
(1+Kc)2 T
(11.49)
```

---

## Стр. 297

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
286 HEATANDMASSTRANSFERINTWOANDTHREEDIMENSIONS
Theparametersare
φ2 =625, β =0.02, K =20, γ =30, Bi
m
=200, Bi
h
=5, cw =1, Tw =1
(11.50)
What is the maximum temperature rise in the catalyst? (Note: If the standard
temperatureis600◦K,usedinthedefinitionofthedimensionlessactivationenergy,
then the actual temperature is 600 times the dimensionless temperature.) Where
doesthemaximumreactionrateoccur?
SolveforConcentrationandFlow
11.16 SolvetheflowanddiffusionproblemfortheT-sensorasillustratedintheexample.
1
Thenconsiderasimilarflowproblemwithwatercominginbothinlets.However,
oneinletcontainsonechemical,identifiedasA,andtheotherinletcontainsanother
chemical,identifiedasB.Thetworeactwiththereactionrate
A+B→C, rate=−kc c (11.51)
A B
To solve this problem, you need to use the Navier–Stokes equation and two con-
vectionanddiffusionequations.Usethesameparametersasintheexample,plus
k=3,c in=1,c in=1.ComparesolutionswithPe=1,10,and100.
A B
11.17 Solveforthediffusionina2DH-sensor.TaketheT-sensorgeometryandaddona
2
sectionthatmimicstheinputsection.Determinethefractionofmaterialgoingout
thetopoutletwhenitallcomesinthetopinlet;alsocomputethevarianceforPe=
50,100,200,500,1000.
11.18 Reproduce Figures 11.4–11.6. Also compute the variance of the concentration
1
comingoutforPe=50and100.
11.19 SolvetheprobleminExample:Viscousdissipation.
1
11.20 Consider flow into a 3D channel that is one unit high, eight units across, and ten
2
units long for a Reynolds number of 1.0. Solve for the flow coming in the 1 × 8
crosssection.Use“P1+P1”discretizationforflow.First,useauniformvelocity
in,tocheckforanyerrorsinyourrepresentation.Next,applylinearcoupling(see
Chapter 10) to have a fully developed flow coming in. Then solve the convective
diffusionequationwiththeconcentration=1ontheright-handsideoftheinletand
zeroontheleft-handsideoftheinlet.Uselineardiscretizationforconcentration.
Compute the variance at the outlet for Pe = 100, 200, 500, 1000. Discuss the
accuracyofyourcalculationsandindicatestepsthatcouldbetakentoimprovethe
accuracy.Alsosolvetheproblemwhenthevelocityprofileisthefullydeveloped
velocityinachannel,whichisequivalenttohavingsliponthesidewalls.Toachieve
this, just take the velocity in the x direction as 6∗z∗(1−z). Although the problem
withslipcouldbesolvedintwodimensions,solveitinthe3Dgeometrywiththe
samemeshusedwithno-slip.
11.21 Solvethesameproblemasin11.20excepthavetheconcentration=1inthelower
1
halfoftheinletand0inthetophalf.
```

---

## Стр. 298

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 287
0
–10
–20 2
0
0.5
0
–0.5 –2
FIGURE 11.22 PipeT-sensor.
11.22 Project. Solve for flow and diffusion in a pipe-T consisting of two pipes coming
together and branching off into one (Figure 11.22). The diameter of the pipes is
1.0,theinletlengthsare2.0longandthelengthofthesinglepipeis20.0.Compute
the variance for a Peclet number of 500 and use the cut-plane option tocalculate
variancesatseveralvaluesofz(cid:3).
11.23 Project.Solvefortheflowanddiffusionina3DH-sensorwherethechannelhasa
squarecrosssection.TaketheT-sensorgeometryandaddonasectionthatmimics
theinputsection.Determinethefractionofmaterialgoingoutthetop(orleft)outlet
whenitallcomesinthetop(orleft)inlet.SolveforRe=1(basedontheinletto
oneport),Pe=100,200,500,1000.
11.24 SolvefordiffusionintheserpentinemixerforPe=100,300,and1000.Determine
2
thevarianceatdifferentlengthsusingcut-planes.Plottheresultsononegraphasa
functionofz(cid:3)/Pe.
```

---

## Стр. 299

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
288 HEATANDMASSTRANSFERINTWOANDTHREEDIMENSIONS
11.25 For the geometry of the T-sensor and conditions of Problem 10.16, solve the
2
concentration problem in a 3D T-sensor when the diffusivity is 10−10 m2/s and
10−11 m2/s.
11.26 Solveforconvectionanddiffusionfortheproblem10.24intwodimensions.Usea
2
Pecletnumberof1000.Constructthemeshinstripssothatyoucanuseboundary
elementsalongthecenterlinetoimprovetheaccuracy.
11.27 Suppose one has done experiments with water flowing in straight channels mea-
2
suring300×120mm.Theaverageflowrateis0.01m/s.Theinletconcentration
takesthevalue1.0inthebottomhalfand0.0inthetophalfandthediffusivityis
10−8 m2/s. It is desired to scale up to 2.5 × 1 mm, that is, a scale-up by a factor
of 8.5, keeping the average velocity at 0.01 m/s. What are the Reynolds number
and Peclet number in both devices? Do you expect the solutions to be the same?
Calculatethevarianceoutofeachdevice.
11.28 Project.ThelaminarfluiddiffusioninterfacedeviceintroducedinProblem10.27is
tobeusedwhenbothametabolite(takenhereascreatinine)andprotein(takenhere
asalbumin)enterinthesample.UsingthesamespecificationsfromProblem10.27,
butextendingthedimensionlesslengthby10,solvefortheconcentrationprofiles
ofbothcreatinineandalbuminwhenbothenterwithadimensionalconcentration
of1.0.Nowtheviscositydependsuponthealbuminconcentration:η=1+0.6cA
mPas(cA=1isthemaximumalbuminconcentration).Sincetheviscositydepends
upon thealbuminconcentration, even infullydeveloped flow thevelocity profile
willnotbequadratic(Birdetal.,2002,pp.56–68),andtheanalyticalsolutionthere
(whentheinterfaceishalfwaybetweenthetwosides)isextendedtomoregeneral
casesin“PoiseuilleFlowofTwoImmiscibleFluidsBetweenFlatPlateswithAp-
plicationstoMicrofluidics”onthebookwebsite.Thediffusivitiesofcreatinineand
albumininbothserumandwateraretakenas9.1910−10 m2/sand6.710−11 m2/s,
respectively. Determine the enhancement factor if the stream in the upper half at
theoutletiscollected.
11.29 Oneuseofserpentinemixersistocreateagradientinconcentrationacrossthedevice
2
by careful arrangement of successive mixers. Gomez (2008) describes devices
developed by Chung etal.(2005) togenerate gradients for studying proliferation
anddifferentiationofhumanneuralstemcells.Theycanalsobeusedtodifferentiate
stemcells(Gomez,2008).ConsiderthedeviceshowninFigure11.23;thegeometry
is available on the book website. Model it for flow and concentration in two
dimensionswhenRe=1.ThebottominletcontainswaterandBSA(bovineserum
FIGURE 11.23 Devicetogenerateconcentrationgradients.
```

---

## Стр. 300

```text
P1:OTA/XYZ P2:ABC
JWBS084-c11 JWBS084-Finlayson May26,2012 14:22 PrinterName:YettoCome Trim:7in×10in
PROBLEMS 289
albumin)withadimensionlessconcentrationof1;thetoponecontainswaterand
Laminin, with dimensionless concentration of 1.0. Although both of these have
similardiffusivities(6×10−11m2/s),useaPecletnumberof1000fortheLaminin
inthetopinletand100fortheBSAinthebottominlettodemonstratetheeffect
ofthePecletnumber.Asthetwostreamsenterthecross-flowchannel,thecenter
outflow has a concentration of both BSA and Laminin. This is repeated further
downstream.Determinetheconcentrationgradientafterthestreamshavedivided
intothree,thenfour,thenfivestreamsandrecombined.Thelongsegmentsare10
units long and the width of the channel is always 1 unit long. The mesh can be
obtainedfromthebookwebsite.
NumericalProblems
11.30 SolvetheproblemofheattransfershowninFigure11.2usingthefinitedifference
1
methodinExcel.Use(cid:6)x=(cid:6)y=0.1withQ=0inEq.(E.53).Thepointsgofrom
1ton+1inxandfrom1tom+1iny.Fortheboundaryconditionsontemperature,
makethecellvaluebetheboundarycondition.Fortheboundaryconditionofzero
flux,intheydirection,set
T n+2,j =T n,j (11.52)
Thentheequationforapointonthatboundaryis
(cid:17) (cid:18)
T n+1,j = 1
4
T n+1,j+1 +T n+1,j−1 +2T n,j (11.53)
Plotthetemperature,too.
11.31 SolvetheproblemofheattransfershowninFigure11.3usingthefinitedifference
2
methodinExcel.Use(cid:6)x=(cid:6)y=0.1withQ=0inEq.(E.53).Inotherwords,add
thehole.Forthepointsalongtheinternalboundary,x=0.3,theequationwillbe
D5=0.25∗(D4+D6+2∗C5)forpoints5–7inthey-direction
H5=0.25∗(H4+H6+2∗I5)forpoints5–7inthey-direction
E4=0.25∗(D4+F24+2∗E3)forpoints5–7inthex-direction
E8=0.25∗(D8+F28+2∗E9)forpoints5–7inthex-direction
D4=0.25∗(D3+C4+D5+E4),similarlyforeachofthecorners
Theseequationsarederivedbynotingthatforzeroflux,thepointsoneithersideof
theboundaryhavethesamevalue(withafalseboundary).Plotthetemperature,too.
11.32 Project. Solve for flow between flat plates with an inlet concentration of 1.0 in
onehalfand0.0intheotherhalf.Usethefinitedifferencemethodforbothaflat
velocity profile and a quadratic velocity profile. Plot the variances versus z(cid:3)/Pe;
comparewiththeapproximationsolution(seebookwebsite)
(cid:4) (cid:17) √ (cid:18)
0.25 1−1.476 2z(cid:3)/Pe , z(cid:3)/Pe≤0.05
σ2 = (11.54)
0.220exp(−10z(cid:3)/Pe), z(cid:3)/Pe>0.05
```

---

## Стр. 301

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp1 JWBS084-Finlayson May31,2012 10:8 PrinterName:YettoCome Trim:7in×10in
A
APPENDIX
®
HINTS WHEN USING EXCEL
ThisappendixprovideshintswhenusingMicrosoftExcel.1 AppendixAincludesgeneral
featuresthatareusefulinalltheapplicationssolvedwithExcelinthisbook.Otherfeatures
areillustratedinthecontextofspecificexamples,andalistoftheseisprovidedattheendof
thisappendixforhandyreference.Thisappendixassumesyouhavesomeexperiencewith
Excel;specialfeaturesusefulforcalculationaredescribed.Foramoredetaileddescription
ofExcel,consultotherbooksdevotedtoExcelorthebookwebsite.
INTRODUCTION
WhenExcelopens,thereareseveraltabsacrossthetop,aslistedinTableA.1.Itiseasyto
find out what each one does: simply put your cursor above one of the commands and an
explanationappears,alongwithalinktomoreinformation.Youcanalsousethequestion
markintheupper-rightcorner.NoticeparticularlytheFile/Optionsnearthebottom.Clickon
itandthenclickonAdd-Ins.YouwanttobesurethatthefollowingapplicationsareActive
Applications: Analysis Toolpak, Aspen Plus V7.3 Excel Calculator, Aspen Simulation
WorkbookV7.3,andSolverAdd-In.Iftheyarenotactive,selectthemandchooseGo.If
theydonotappear,useyouroriginalDVD
Each tab has a number of groups. The home tab has the following groups: clipboard,
font, alignment, number, and so on. To copy cells down, click on a cell and choose Fill
down.Thecontentsofthecellabovearecopieddown.Ifthecellabovehasaformula,the
formulaisalsocopieddown,incrementingtherownumberbyone.Youcanalsoselectthe
lowerrightcornerofacellandcopydown,too.SupposetheoriginalformulausedB2.If
1ExcelisaregisteredtrademarkofMicrosoftCorporation,Inc.
IntroductiontoChemicalEngineeringComputing,SecondEdition.BruceA.Finlayson.
©2012JohnWiley&Sons,Inc.Published2012byJohnWiley&Sons,Inc.
291
```

---

## Стр. 302

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp1 JWBS084-Finlayson May31,2012 10:8 PrinterName:YettoCome Trim:7in×10in
292 APPENDIXA:HINTSWHENUSINGEXCEL
TABLEA.1 TabsinExcel
File Home Insert PageLayout Formulas DataReview View Aspen
theformulaisdraggedtotheright,B2ischangedtoC2.Iftheformulaisdraggeddown,
theB2ischangedtoB3.Ifyoudonotwantthattohappen,thatis,youwanttheformula
inallcolumnstouseB2,thenuseabsoluteaddresses.Intheformula,changeB2to$B$2.
Optionssuchas$B2andB$2arealsopossible.Ifyouselectacelltagintheequationand
press F4, it turns into an absolute address. On the Macintosh, selecting the cell tag and
pressing command-T (apple-T) does the same thing; if you continue to press it, the tag
cyclesbetweenB2,$B$2,B$2,$B2,B2.Toinsertanewrow,selectarowontheleft-hand
side and choose Insert/Row. A new row is placed above the one you have selected. The
cellsarerenumbered,andalltheformulasarechanged,too,toreflectthenewnumbering
system.Usethissamemethodtoinsertacolumn;thenewcolumnwillappeartotheleftof
theoneyouhaveselected.
CALCULATION
Whendoingcalculations,itisconvenienttonamethecellssothattheycanbereferredto
inawaythatmeanssomethingtoyou,forexample,TratherthanB2.Tonameacell,select
thecellandenterthenameofthevariableintheupperleft-handcornerofthespreadsheet
andthenpressReturnorEnter.ThenyoucanuseT inyourformulasratherthanB2.
IntheFormulasTab,inFunctionLibraryGroup,youcanfindanumberoffunctionsin
Math&Trig. These include cos, cosh, acosh, ln, log10, and so on. “More Functions” has
engineeringfunctionssuchasBesselfunctions.“ShowFunctions”(totherightof“Trace
Precedents”) display all formulas rather than the calculated results. Calculation Options
allow you to choose Automatic (the spreadsheet recalculates every time you change one
cell) or Manual (the spreadsheet will wait till you choose Calculate Now (for the whole
workbook)orCalculateSheet(foronlythesheetshowing).Thisissometimesusefulwhen
solvingaprobleminwhichtheformulasareintertwinedandtheformulainonecelldepends
ontheanswerinanothercell,whichdependsonthevalueinthefirstcell.Inthesecases,it
isconvenienttoturnoffiterationwhilepreparingtheformulasinthespreadsheet,andthen
turnitononcetheentirespreadsheetiscomplete.
YoucanuseGoalSeektofindthevalueofavariabletomakeanequationzero(orsome
othernumber.Forexample,supposewewishtosolvef(x)=x∗x−2∗x=0.Theformula
willbeputinonecell,andanothercellwillbeidentifiedasxandsonamed.OpenWhat-If
AnalysisintheDataToolsGroup,GoalSeekandsettheformulacelltozerobychanging
thexcell.Theanswermaynotbeasgoodasyoulike,butPreferencescanbeusedtoreduce
theerrorcriterion.
If Solver has been supplied as an Add-In (see above), the word Solver is seen in the
Analysis Group. This program is a sophisticated program to solve nonlinear equations.
ThisoperatesinthesamewayasGoalSeekbutitismuchmorerobustandgivessmaller
errors. You have a choice of methods; usually GRG Nonlinear will work, but sometimes
itisusefultouseEvolutionaryfirst.Iftheanswerisnotaccurateenough,youcanchange
theConstraintPrecisiontoavalueyouthinkisreasonableforyourproblem.(Thedefault
parametersaresetforbusinessapplications,wheretenthsofacentdonotmatter.)When
```

---

## Стр. 303

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp1 JWBS084-Finlayson May31,2012 10:8 PrinterName:YettoCome Trim:7in×10in
APPENDIXA:HINTSWHENUSINGEXCEL 293
TABLEA.2 MatrixMultiplicationinExcel
A B C
1 10 5 2
2 1 11 4
3 3 7 12
4
5
6 0.105263 -0.046559 -0.002024
7 0.000000 0.115385 -0.038462
8 -0.026316 -0.055668 0.106275
9
10
11 1 0 0
12 -1.38E-17 1 0
13 0 0 1
thesolverwindowisopen,chooseOptions,andclickAllMethods.Youcanalsolimitthe
numberofiterations.ExamplesaregiveninChapters2–5.
Ifthespreadsheetiteratestomeaninglessnumbers,youcanresetitbyusingCTRL-Zor
usingtheundotypingkey.
YoucansolvemultipleequationsbyusingSolver,too.Forexample,ifthevariables x
andyareplacedincellsA1andA2,respectively,youcanputequationsintocellsB1and
B2 that use x and y. Then choose Solver and set B1 to zero by varying A1 through A2,
subjecttotheconstraintthatB2=0.Convergencemaybedifficultandthismightnotwork.
ItispossibletouseExcelwithAspen.TheAspenTabisanadd-in(seeFile/Options/Add-
Ins);usingitallowsyoutouseExceltocalculatecertainthingsinyourAspenmodel.This
procedureisbeyondthescopeofthisbook,butmoreinformationisavailableinChapter5
oftheAspenPlusUserModel.
TwoofthefunctionsunderMath&TrigareMINVERSEandMMULT.Thesefunctions
have the obvious use. The inverse function, of course, must act on a square matrix, and
creates a square matrix. Consider a 3 × 3 matrix. Create the matrix, say in cells A1:C3
(seeTableA.2).ThenincellA6type=MINVERSE(A1:C3).YoucanalsoinserttheA1:C3
cellbyselectingthecells.ClickoncellA6,presstheshiftkey,andselecttheothercorner
of the matrix, C8. Press Function Key F2, then CTRL-Shift-Enter (CTRL-Shift-Return
on the Macintosh). The inverse appears in A6:C8 cell. You can check by multiplying
thesetwomatricestogether;theresultshouldbetheidentitymatrix.ClickoncellA11,type
=MMULT(A1:C3,A6:C8).ClickoncellA11,presstheshiftkey,andselecttheothercorner
ofthematrix,C13.PressF2,theCTRL-Shift-Enter.Thematrixmultiplicationappearsin
A11:C13.Indeed,itistheidentitymatrix.
PLOTTING
PlottinginExceliseasy.Choosethecellsyouwishtoplot,suchasthefirsttwocolumns.
ThenchoosetheInsertTab,chooseXY Scatter,andclickonthegraphstyleyouwant.To
labeltheaxes,selectthefigure,chooseLayout,AxisTitles.Clickonthetitleyouwishto
changeandtypethenewvalues.Toputmultiplelinesonthegraph,selectmorecolumns.
```

---

## Стр. 304

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp1 JWBS084-Finlayson May31,2012 10:8 PrinterName:YettoCome Trim:7in×10in
294 APPENDIXA:HINTSWHENUSINGEXCEL
IMPORTANDEXPORT
Thereareseveralwaystodothis.Thefirstmethodworkswhenyouhaveasinglecolumn
totransfer.ToexportcolumnsfromExcel,selectthecolumnofcells,choosetheHomeTab
andthenCopy,openanapplicationthatacceptstextfiles,andchoosePaste.Togetasingle
columnofnumbersintoExcel,copythecolumninanotherapplication(onewithTabs),in
Excelselectonecell,andchoosePaste.Togetseveralcolumns(withtabsorspaces)into
Excel,usetheImportfunction.
Youcanexportthecontentsofthespreadsheettoatextfilethatcanbeusedastheinput
toanotherprogram.Thisisanicewaytohaveauserinterfaceforaprogramthatrequires
significant computing capability (beyond what Excel offers). You could put the physical
parametersforthecaseyouarestudyingintotheExcelspreadsheet,allowingthemtobe
changedeasily.Youthenexporttheinformationandhavetheothercomputerprogramread
the text file to get the data. To export the information (the contents of the cells, not the
figures from the spreadsheet), choose Save As, change the format to a text formats, such
asText(Tabdelimited),andsaveit.Ifyouopenthisfileinawordprocessorortexteditor,
you will see the information displayed in exactly the same format as in the spreadsheet.
It is not trivial to get these numbers into other programs, which have to read the spaces
appropriately, and some knowledge of the C computer language may be necessary, but
it does make a nice interface for a program that you will use many times. For example
(cid:3)
MATLABR canreadsuchfiles.
PRESENTATION
The insert tab allows you to put figures and charts into your spreadsheet. One important
optionisTextBoxintheTextGroup.Youcandrawaboxonyourspreadsheet(andresize
it) and type into it whatever you want. It can be anywhere on the spreadsheet, covering
multiplecells.Inthistab,intheSheetOptionsGroup,youcanchoosetoshowthegridlines
(ornot)andtheheadings(1,2,3,...,A,B,C,...)(ornot).
IntheReviewTabyouhaveachancetocheckyourspelling,translatetoanewlanguage,
andsoon.Youcanprotectyoursheetorworkbooksothatotherscannotopenitwithouta
password,andyoucansharetheworkbookwithothersonanetworksothatseveralpeople
canuseit.TheNewCommentcommandallowsyoutofillatextboxwithsomeinformation
that will be hidden until you click on it. A small red arrow is created in the upper right
locationofthecelltoindicatethereisacommentthere.Putyourcursorabovethearrow
andthecommentisdisplayed.
IntheViewTab,theWorkbookViewsGroupprovidesavarietyofwaysthatthesheetcan
bedisplayed.IntheShowGroup,GridlinesworksthesameasinthePageLayoutTab:ifit
ischecked,linesareshowndividingthecells,andtheyarenotdisplayedifitisunchecked.
IntheZoomGroup,Zoomallowsyoutozoominorout;ZoomtoSelectionallowsyouto
chooseasectionofthesheetandexpandittotheentirescreen.Choose100%toreturnto
theoriginalview.
In the Window Group, there are provisions for breaking the sheet into separate parts.
You may wish to display one column while you scroll through other columns. Put that
column(e.g.,columnA)attheleftmostcolumnshown,andchooseFreezePanes.Thenas
you scroll to see columns B → Z → AA → AX, and so on, column A continues to be
displayed.Thisishelpfulforacaseinwhichthecolumnrepresentsthechemicalnamesand
```

---

## Стр. 305

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp1 JWBS084-Finlayson May31,2012 10:8 PrinterName:YettoCome Trim:7in×10in
APPENDIXA:HINTSWHENUSINGEXCEL 295
propertiesandeachoftheothercolumnsreferstoonestream.Theremightbehundredsof
streamsandyouwouldlikethefirstcolumnidentifyingrowstoremainvisibleatalltimes.
To make a professional-looking spreadsheet, it is important to provide documentation
forthereader.Youcanestablishdifferentsections,surroundedbyboxes(seeFigures2.1).
Title,yournameanddate
DataInput—thesearevaluesthattheusermaychange
ParameterValues—thesearevaluesthattheuserwillnotchange,butareneeded
Formulasused—thisdefinestheproblem
Results
To make the boxes, select the cells to be enclosed, in the Home Tab, Number Group,
choose the arrow at the bottom right, choose Border, and then Outline (or some other
format.
The Split command allows you to divide the Sheet into two vertical panels or two
horizontalpanels,orfour,2×2.Simplyputyourcursorintheupperleft-handcellofthe
lowerright-handpanelandchooseSplit.Toundothis,chooseSplitagain.
Youcaninsertpictures,equations,andhyperlinks(towebsites),too.Besuretotrythe
hyperlinkwhileconnectedtotheinternettoensurethatitworks.
Sometimesyouwanttoreproducepartofyourspreadsheetinanotherspreadsheetorin
anotherareaofyourexistingone.Youcanselecttheareaofthespreadsheet,chooseCopy,
movetotheupper,left-mostcellofthenewareaandchoosePaste.Becarefulbecausethis
willcopyallformulas,too.Ifyouwantonlythevaluesfromaspreadsheet,copythepart
youwantandchoosePasteSpecial;thenchoosethedesiredoption(suchasValue).Youcan
alsopasteintoWord.IfyousimplyusePaste,youcanmanipulatethespreadsheetinside
Word(resizeit,changethefont,etc.).IfyouusePasteSpecial,oneoptionistopastethe
spreadsheetasapicture.InthatcasethewholeimageisfrozenbeforeitisputintoWord.
```

---

## Стр. 306

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
B
APPENDIX
®
HINTS WHEN USING MATLAB
This appendix provides hints and tips when using MATLAB®.1 It assumes that you are
a beginner in using MATLAB, but not an absolute beginner in computer programming.
Most likely, you remember concepts from a computer programming class taken earlier.
IncludedinAppendix Baregeneralfeaturesthatareusefulinalltheapplications solved
withMATLAB.Otherfeaturesareillustratedinthecontextofspecificexamples;alistof
examples is provided at the end of the appendix for handy reference. You will probably
wanttoskimthisappendixfirst,thenstartworkingsomeoftheproblemsthatuseMATLAB
togatherexperience,andfinallycomebackandreviewthisappendixinmoredetail.That
way you will not be burdened with details that do not make sense to you before you see
whereandhowyouneedthem.AbookwithmoredetailisbyGilat(2010),andMATLAB
itselfhasexcellenthelpmenusthatarereferredtointhisAppendix.
OutlineofAppendixB:
1. Generalfeatures
2. Programmingoptions:input/output,loops,conditionalstatements,timing,matrices
3. Findingandfixingerrors
4. Eigenvaluesofamatrix
5. Evaluationofanintegral
6. Interpolation:splinesandpolynomials
7. Solvealgebraicequations
8. Integrateordinarydifferentialequationsthatareinitialvalueproblems
9. Plotting
1MATLABisaregisteredtrademarkofTheMathWorks,Inc.TheversiondiscussedhereisR2012a.
IntroductiontoChemicalEngineeringComputing,SecondEdition.BruceA.Finlayson.
©2012JohnWiley&Sons,Inc.Published2012byJohnWiley&Sons,Inc.
297
```

---

## Стр. 307

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
298 APPENDIXB:HINTSWHENUSINGMATLAB
10. Otherapplications
11. Import/exportdata
12. Programminggraphicaluserinterfaces(GUIs)
13. MATLABhelp
14. ApplicationsofMATLAB
GENERALFEATURES
ScreenFormat
Tostart,openMATLAB.ThescreenwillappearasinFigureB.1.Ontheupperline,note
thequestionmarkthatleadstoexcellenthelpinformation.Totherightofthatisthelocal
folder that MATLAB is pointing to. If the picture were larger, it would have the words
“CurrentFolder”infrontofit.WhenyouaskMATLABtofindafile,itlooksinthatfolder
first.Tomovetooneofyourfolders,clickonthe...andbrowsetothedesiredfolder.The
largeareasonthescreenareasfollows.Ontheleftisalistofthefilesthatareinyourcurrent
folder, and below it would be information about a file you selected from the list. In the
middleistheCommandWindow,whichiswhereyouwillissuecommandsinteractively.
To the right is the Workspace that lists variables you have defined and their values, and
below it is the Command History, which records your commands in sequence. Many of
these items you can drag from the Workspace or Command History into the Command
Windowtoentertheirvaluesintothecommandworkspaceortoexecuteacommandagain.
For a quick illustration of using MATLAB, look at the “Getting Started with MATLAB”
video.Clickonthe“NewtoMATLAB?,WatchthisVideo”linkatthetopofthecommand
window.Alternatively,choosethequestionmark,thenopenMATLAB,anddoubleclickon
FIGURE B.1 MATLABscreen.
```

---

## Стр. 308

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXB:HINTSWHENUSINGMATLAB 299
Demo.Thevideoisthefirstone,anditiseitheronyourcomputer(iftheentireMATLAB
wasloadedoriginally)orontheinternet.
LookundertheDesktopmenu;youcanchoosewhichwindowsyouwantopen.Ifyou
madeamistake,chooseDesktopLayout/defaulttogetbacktoFigureB.1.
Sometimes you have files in more than one folder, and you need to access them even
if that is not your “current folder.” Use the path command to point to an area where you
store your programs and data. First enter path in the command window to see the list of
MATLABfoldersthatwillbesearched.Thenenterthecommand(modifiedtoidentifythe
newfolder,perhapswithaC:\:
path(path,’/Users/yourname/foldername’).
When MATLAB looks for an m-file (a program you write), it will look in all these
directories,fromtoptobottomuntilitfindsonewiththesamename.Then,itwillusethat
m-file.
Stop/ClosingtheProgram
Whenyoustopwork,saveyourm-filesinafolder,soyoucanusethemnexttime.Youcan
alsosavetheworkspace,whichwillsaveallthenumericalvaluesthathavebeencalculated.
Thisisconvenientifyouhavetointerruptyourworkforashorttimeanddonotwanttostart
over.Ofcourse,mostofyourworkiscontainedinyourm-files,whichyoualwayswantto
save.Ifasimulationcontinuesforalongtimeandyouwanttohaltit,pressControl+Break
orControl+ConthePCorControl+ContheMacintosh.Thiswillstoptheprogramasa
forcedquit.
m-filesandScripts
In MATLAB you write computer programs that are called MATLAB function files (or
m-files) as well as scripts, which run in the command window. The m-files are saved on
your computer and can be used by simply typing their name in the command line. In
additiononem-filecancallanotherm-file.Scriptsarealistofcommandsthatcanalsobe
saved;iftheyarepastedintothecommandwindowtheywillbeexecuted.Youwillwantto
includecommentsinyourm-filesandscriptsthatexplainwhatthefiledoes.Thisisdone
byinsertinga%;everythingafter%onalineisconsideredacomment.Thesecomments
remindyouofdetailswhenyoucomebacktotheprogramatalatertime.Youcanexecute
an m-file that is listed in your current folder by double clicking it; then edit it if desired,
saveit,andfinallyrunitbypressingthegreenarrow.MATLABhasmanyfunctionsofits
own;youcanseealistofthembypressingthefunctionbutton(fx).Thenyoucansearch
either by category or by key words. To see how to use one of them, issue the command:
help functionname. When you write your own m-files, the line may extend too far. By
putting...attheend,thecommandcontinuesinthenextline.SimpleMATLABprograms
are illustrated in Chapters 2–9. As you become more experienced using MATLAB you
should look at the Videos “Working in the Development Environment” and “Writing a
MATLABProgram.”AccesstheseviatheHelpquestionmark,MATLAB,Demos
```

---

## Стр. 309

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
300 APPENDIXB:HINTSWHENUSINGMATLAB
WorkspacesandTransferofInformation
When you use MATLAB, your results will only be as good as the programs you write.
Thus,itisimportanttounderstandthestructureofworkspacesandm-files,aswellashow
todisplayintermediateresults,transferparametersfromonem-filetoanother,anddebug
your code. Most of the problems encountered by beginning users involve errors in these
areas,andonlycarefulcheckingwillhelpyoufindthem.
Thecommandworkspaceisanareaofcomputermemorythatisreservedforparameters
youdefinefromthecommandlineinMATLAB.Eachm-filehasitsownuniqueworkspace,
andthisworkspacedoesnotcommunicatewiththecommandworkspaceunlessyoumake
it happen. It is sort of like Facebook: you and your friends have to agree to be friends
to see what the others are doing (transfer information). There are two ways to set up the
communication:usingtheglobalcommandorcallingargumentsofthem-files.
“Global”Command
Figure B.2 shows a command window and two m-files. The global commands in each
one determine which variables are available in the m-files. Assume you have typed the
command.
global a b c
inthecommandline.Thengiveavaluetoa,b,andc.
a =2
b=3
c=4
Thequestionisthen:howcanyougetthesevaluesofa,b,andcintoanm-file?Youdo
this by putting a global command in the m-file; the command lists the variables that you
wanttobeavailable.InFigureB.2,theparametersa=2andb=3areavailablein“m-file
one”anda=2andc=4areavailablein“m-filetwo.”Ifaischangedin“m-fileone,”it
Command workspace m-file one m-file two
Global a b c Global a b Global a c
a b c a b a c
Global workspace: a b c
FIGURE B.2 Globalandlocalvariables.
```

---

## Стр. 310

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXB:HINTSWHENUSINGMATLAB 301
ischangedforalltheprograms.Inotherwords,thechangeismadeinthecentral,global
locationandthus,theexchangegoestwoways.Ifthevariablecisusedin“m-fileone,”it
mustbedefinedtheresinceitisalocalvariablein“m-fileone.”Whateveritsvalue,itdoes
notchangetheglobalvalueofcbecausecisnotlistedintheglobalcommandof“m-fileone.”
The second way to pass parameters is to use “list the parameters” in the function
statementofthem-file.Forexample,them-file
function y=name(x,parameters)
expectsvaluesofxandparameterstobesuppliedwhenthem-fileiscalled.Thevariable
parameterscanbeavector,thatis,containingseveralelements.
DisplayTools
Whenyouarecheckingyourprogramming,youwillwanttoexaminethevalueofvarious
parameters.The“;”repressesthedisplayoftheresultofthecalculation.Removethe“;”,
and you will see the result of each line of your code in the Command Window as it is
executed.Itisessentialthatyoulookatthistoverifyyourcode.
Youcanalsocauseavariabletobedisplayedusingoneofthefollowingthreecommands:
disp(x)gives: x=2.34
xgives: x=2.34
disp(“nowisthetime”)gives: nowisthetime
You can issue these commands from the command window to see the value of any
variableinthecommandworkspace.Ifyouwanttoknowthevalueofalocalvariableinan
m-fileyoumustputoneofthesecommandsinthem-fileandexecutethem-file.Alsolook
attheWorkspace.Thevariablesarelistedtherealongwiththeirvalues.Thisisanotherway
tocheckyourresults.
Ifyouneedmoresignificantdigits,try
format long: 1.234567890e + 02
format long e: 1.234567890e + 02
format short: 123.4568
format short e: 1.2346e+02
Toeliminateallvariables
clear all
Thisishelpfulwhendebuggingbecauseiteliminatesvariablesthatmayhavebeenset
incorrectlyinpreviouscalculations.MATLABthenstartsfromscratch.MATLABmaybe
savinganumberthatyoudonotrealize,whichmakesithardtofindyourmistake.
ClassesofData
Mostofyourworkwillinvolvenumbers,butsometimesyouwillwanttousetextorwords.
A number is usually a double precision number, using 64 bits. Its class is double, which
```

---

## Стр. 311

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
302 APPENDIXB:HINTSWHENUSINGMATLAB
canbeseenbyissuingthecommand:whos.Acharacterstringisofclasschar.Anumber
canbeconvertedtoacharacterusingthenum2strcommand:
»a=1.234
»b=num2str(a)
»whos
Name Bytes Class
a 8 double
b 10 char
The reverse command is str2num(b). There are other classes as well; see the help
commandandsearchonclass.
PROGRAMMINGOPTIONS:INPUT/OUTPUT,LOOPS,
CONDITIONALSTATEMENTS,TIMING,ANDMATRICES
Input/Output
Youcanasktheuserforinputwiththefollowingcommand.
viscosity = input(‘What is the viscosity (Pa s)?’)
Whenyousee“Whatistheviscosity(Pas)?,”typethevalueandpressreturn.Youcan
displayinaspecifiedformat.
fprintf(‘%5.3f %10.5f\n’,x,y)
2.345 234.56789
TheseareC-commands,andthenotationmeans
f - floating point
\n is a carriage return
e - exponential format
5.3 means five characters, three after the decimal point.
To write a text file, you must open it, write it, and close it. The following command
writes a text file that has two columns, x and y, with as many entries as defined by the
vectorsxandy(whichhavethesamelength).
fid = fopen(‘ChEData’,’w’) % w for write
fprintf(fid,’%5.3f %10.5f\n’,[x,y])
fclose(fid)
Toreadatextfile,youmustopenit,readit,andcloseit.
fid = fopen(‘ChEData’,’r’) % r for read
[x y] = fscanf (fid,’%5.3f %10.5f’)
fclose(fid)
```

---

## Стр. 312

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXB:HINTSWHENUSINGMATLAB 303
Loops
It is sometimes useful to execute a command over and over, putting each result in one
elementofavector.Theformatis
for i=1:10
y(i) = ...
end
Ifyouwanttostopbeforetheend
for i=1:10
y(i) = ...
if y(i) > 25 break,end
end
ConditionalStatements
Sometimestheprogramneedstoexecutedifferentinstructionsdependingonacalculated
result.Herearesomeexamples.
if (condition1) % examples of condition1: i==3, i<3
% (note double equal sign)
...
else
...
end
Anotheroption:
if (condition1)
...
elseif (condition2)
...
else
...
end
Stillanotheroption:
switch lower(num)
case {1} % execute when num = 1
y = ...
case {2, 3} % execute when num = 2 or 3
y = ...
otherwise % execute when num is neither 1, 2 or 3
y = ...
display (‘there is an error’) % this is optional if num
should be 1, 2, or 3
end
```

---

## Стр. 313

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
304 APPENDIXB:HINTSWHENUSINGMATLAB
TimingInformation
Turn on clock at one place in the program—tic. Turn off clock at another place in the
program—toc—andtheelapsedtimeisdisplayed—elapsed_time=2.34.
Matrices
Vectorsarerow(1×3)
x =[2 3 4]
orcolumn(3×1)
x = [ 2
3
4]
Thetransposeofxisx(cid:2).
Setmatrixvaluesindifferentways:
A = [ 1 2 3 4 carriage return
5 6 7 8]
A = [ 1 2 3 4; 5 6 7 8]
size(A)givesdimensionsofA
size(A) = 2 4
Operateonallelementsatonce.IfT(:)isavectorofT (K)youmightwantitin◦C:
t =T −273
MATLABwilldothisforallelements inT(:)andmakeanewvectort(:).Operateon
oneelementofamatrix
t(i)=T(i)−273%Note:MATLABiscasesensitivesothatt(i)andT(i)aredifferent.
Obtainrowsfrommatrix
a =A(1,:) or a =[1234]
YoucanuseaorA(1,:)incalculationsorplotting.
MatrixMultiplication
⎢ ⎥ ⎢ ⎥
⎢ ⎥ ⎢ ⎥
⎢ 2 4 6 ⎥ ⎢2⎥
TakethematrixA=⎣
8 10 12
⎦
andthevector x
(cid:2)⎣
3
⎦.
14 16 18 4
```

---

## Стр. 314

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXB:HINTSWHENUSINGMATLAB 305
The3×3matrixAisformedby
A=[246; 81012; 141618]
Matrixmultiplicationisachievedwiththeasterisk.
⎢ ⎥⎢ ⎥ ⎢ ⎥
⎢ ⎥⎢ ⎥ ⎢ ⎥
⎢2 4 6⎥⎢2⎥ ⎢ 40 ⎥
⎣
8 10 12
⎦⎣
3
⎦=⎣
94
⎦
(B.1)
14 16 18 4 148
A ∗ x’
ans = [40
94
148]
is[3×3][3×1]=[3×1]matrix.Notetheapostropheonx;isacolumnvector,whichis
neededformatrixmultiplication.IfyouhadusedA∗x,MATLABwouldhavetoldyouthat
theinnermatrixelementshavetoagree.Multiplytermselementbyelement:
u(i)=[x(i)]2 (B.2)
u=x.∗x=[4916]
(cid:6)
Notetheperiodbeforetheasterisk.Themultiplication 3 [x(i)]2ismadeby
i=1
x ∗ x (cid:2) =29
Thisisasinglenumberbecausethematrixmultiplicationis[1×3][3×1]=[1×1]
x’ ∗ x = [ 4 6 8
6 9 12
8 12 16]
is[3×1][1×3]=[3×3].
x∗xismeaningless.
[1×3][1×3]=?
ElementbyElementCalculations
Ifyouwanttocalculatesomethingforeveryelementinthevector,youneedtoprecedethe
+,-,∗,/,ˆ,andsoon,commandwithaperiod.Forexample,ifyouhaveaseriesofxandy
values:
x =0:0.1:1; y =1:0.1:2
thecommand
z = x./y
computesz(i)= x(i)/y(i)foreachi.
```

---

## Стр. 315

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
306 APPENDIXB:HINTSWHENUSINGMATLAB
MoreInformation
Tolearnmoreaboutmatrices,viewtheVideo“WorkingwithArrays”(underhelp,MAT-
LAB,Demos).AlsolookatMathematics(underhelp,MATLAB,UsersGuide).
FINDINGANDFIXINGERRORS
AnimportantlessonyoucanlearnaboutusingMATLABishowtofinderrors.Onecommon
errormessagefromMATLABis
???Undefined function or variable ‘q’.
This means that q is either an undefined function or an undefined variable. If q is a
function or m-file, then MATLAB cannot find it. Check the working directory or use set
pathandmakesurethatthepathissettothefolderwhereyoustoredthem-fileandthatyou
haveaddedthatpathtothelist.Donotforgettosaveyourpathlistsothatitistherethenext
timeyouuseMATLAB.Ifqisavariable,ithasnotbeensetorwasnottransferredcorrectly.
One source of confusion is when you think you have defined a variable, but have not
really.Usedisp(x)toseethecurrentvalueofxinthecommandworkspace.Ifthevariable
issupposedtobeinanm-file,runthem-filewithacommandaddedtodisplaythevariable,
andthatwillgiveyouthevalueofxinthem-fileworkspace.Thatshouldgiveyouahint
aboutpossiblesourcesoftheerror.Themostcommoncauseofthismistake(andonethat
ishardtofindunlessyoucheckthecodesystematically)isforgettingtopassaparameter
tothem-fileeitherusing“global”orasaparameter.Thereasonitisdifficulttofindthese
mistakes is that in your mind you have set the value of the parameter in the program
somewherebutfailedtotransferittotheappropriatem-file.
Anothertypicalerrormessageis
??? Index exceeds matrix dimensions
This message means that a matrix like A(i,j) was called with either i or j too big (i.e.,
beyondthedefinitionofA),orafunctionusesamatrixthathasnotbeendefinedyet.
Theprogramsillustratedinthisbookarefairlysimple,andtheyareeasytodebug.All
programmersmakemistakes;goodprogrammerslearntofindthem!Findingthemiseasyif
youtakethetime.Firstconsideralineinacodeinthecommandwindow.Setalltheparam-
etersusedinthelineandexecutetheline.Comparetheanswerwithacalculationdonewith
acalculatororoneyoudidbyhand.Besurethatalltheparametersyouusearedifferent,and
donotusezeroorone,becausesomemistakeswillnotbepickedupifthevariableiszeroor
one.Theparametersyouusefortestingcanbesingle-digitnumbersthatareeasytocalcu-
lateinyourhead,andtheycanbecompletelyunrelatedtotheproblemyouaresolving.You
canalsocopyalinefromanm-fileandpasteitintothecommandwindowtocheckit,too.
Ifthecodeyouwishtocheckisinanm-file,thefirstcheckistoseethatalltheparameters
arepassedcorrectlyandhavebeensetintheworkspaceavailabletothem-file.Theeasiest
waytodothisistorequestthatthem-fileprintallthevariablesyouexpecttobetransferred
tothem-file,atthestartofthem-file,andcheckthattheyarecorrect.Ifavariablehasnot
beenset,MATLABwillgiveyouanerrormessagewithoutrunningthecode.Ittellsyou
the line and column where the undefined variable is. The problem is probably improper
passingofparametersorincorrectuseoftheglobalcommandor,sometimes,atypingerror.
```

---

## Стр. 316

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXB:HINTSWHENUSINGMATLAB 307
MATLABprovidesseveralcommandstohelpyoudebugtheprogram.Checkthevalue
ofavariablebylookingintheworkspace.Thecommand“whos”willlistthevariablesand
their type, as well as whether they are local or global variables. This is also a command
thatisusefulinsideanm-file(whenchecking),sinceitlistsallthevariablesthatthem-file
canaccess,andiftheoneneededisnotthereyoucanthensearchforthereason.
You can make the program stop at a certain point and return to the keyboard mode.
Then you can access values of the parameters. To stop the program, issue the command
“dbstopatlinenumberinfilename.”“Filename”isthenameofthem-file,and“linenumber”
is the line number in the m-file where you wish to stop. Alternatively, put the command
“keyboard”intothem-filewhereyouwishtostop.ThecommandcursorchangestoK»and
youcanissuecommands.Forexample,typingthenameofavariablewillcauseitsvalue
tobeprinted.Thisisaconvenientwaytoaccessthevalueofvariablesinanm-file.Ifyou
thenwanttoaccessvariablesintheprogramthatcalledthem-file,saydbup.Tocontinue
computing,type“return”andpressthereturnkey.Tostopthecalculationaltogether,type
“dbquit.”
EIGENVALUESOFAMATRIX
EigenvaluesarethepolynomialrootstoEq.(B.3).
|A −λδ |=0 (B.3)
ij ij
TheyareeasytocalculateinMATLABusingthe“eig”command.
» lambda=eig(A)
lambda = 32.2337
-2.2337
-0.0000
EVALUATEANINTEGRAL
Toevaluatetheintegral,Eq.(B.4),defineasetofpointsintheintervaltobeintegrated,as
the vector x (need not be uniformly spaced). Then evaluate the function at each of these
points.Calculatetheintegralusingthetrapezoidrule.
(cid:7)2
area= x2dx (B.4)
0
x =[0:0.1:2]
y = x.∗x
area=trapz(x,y)
SPLINEINTERPOLATION
Make a cubic B-spline pass through all the data points: [x(i), y(i), i = 1,...,m]. A cubic
spline is a cubic function of position, defined on small regions between data points. It is
```

---

## Стр. 317

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
308 APPENDIXB:HINTSWHENUSINGMATLAB
1
0.5
0
−0.5
−1
−1.5
0 2 4 6 8 10
FIGURE B.3 Splinefitofasetofdatapoints.
constructed so the function and its first and second derivatives are continuous from one
regiontoanother.Itusuallymakesanicesmoothcurvethroughthepoints.Thefollowing
commandscreateFigureB.3.
x = 0:1:10; y = cos(x); % evaluate cos at a set of x values
xx = 0:.25:10; % set up a finer mesh for plotting
yy = spline (x,y,xx); % evaluate the spline function at the
points xx
plot(x,y,’*’,xx,yy) % plot the original points with*
and the spline curve
% x(i),z(i),i = 1, ... ,m
InterpolateData,EvaluatethePolynomial,andPlottheResult
For data points x(i),z(i),i =1,...,m fit a polynomial of degree n in the least squares
sense.
y = p 1 xn + p 2 xn−1+···+ p n x + p n+1 (B.5)
p = polyfit(x,z,n)
Thecommand“v=polyval(p,w)”evaluatesthepolynomialpatthewpoints(wcanbe
avector).Plotthedatapoints(y)andthepolynomial(v)
w = [0:.1:10]
v = polyval(p,w)
plot(x,y,’ro’,w,v,’b−’)
```

---

## Стр. 318

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXB:HINTSWHENUSINGMATLAB 309
SOLVEALGEBRAICEQUATIONS
Using“fsolve”
Solve f ({y })=0,i =1,...,nforthevector{y }.Therearethreesteps.
i j j
Step1 Settheinitialguessofthesolution.
y0=[0 0]
Step2 Nameandconstructthem-file“prob2.m,”whichevaluatesthefunction.
Step3 Call“fsolve,”whichisintheoptimizationtoolboxinMATLAB,whichallversions
donothave.
z = fsolve(@prob2,y0)
z = − 1.4456 − 2.4122
You need to make several checks. The number of unknowns is set by the number of
elementsintheinitialguess,y0.Them-file“prob2”calculates f , i =1,...,n,andthere
i
havetobeasmanyelementsinf asthereareiny.Them-fileneedstobechecked,ofcourse.
TheonlywayyoucanmakeMATLABfindthesolutiontoyourproblemistomakesure
them-filegivesthecorrectsetoffswhengivenasetofys.Ifthe“fsolve”doesnotwork
well,trymakinganinitialvalueproblemandsolvingitusingimplicitmethods,integrating
toalongertime.
dy
i = f ({y }), y(0)=initialguess (B.6)
i j i
dt
SolveAlgebraicEquationsUsing“fzero”or“fminsearch”
(BothinStandardMATLAB)
Ifyouhaveasinglefunctionofonevariable,youcanusethe“fzero”functioninplaceof
“fsolve,” and it is called in a similar way. If you have several fs that you want to make
zero,youcanmakethenormofthevectorf zero.Thenormcanbethesquarerootofthe
sumofthesquaresoftheelements,orthemaximumoftheabsolutevalueofallelements.
Then“fminsearch”usesoptimizationmethodstofindthevectorythatmakesthenorma
minimum.Thismayworkforsimpleproblems,especiallyoneswithconstraints,butitis
lesssuccessfulonlargeproblems.
INTEGRATEORDINARYDIFFERENTIALEQUATIONSTHATARE
INITIALVALUEPROBLEMS
Tosolveasingleordinarydifferentialequation
dy
= f(t,y), y(0)= y (B.7)
0
dt
weusethe“ode”setoffunctionsinMATLAB.Therearefoursteps.
```

---

## Стр. 319

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
310 APPENDIXB:HINTSWHENUSINGMATLAB
Step1 Settheinitialcondition,y0.
y0=3
Step2 Setthetimespanfortheintegration.
tspan=[0 10]
Step3 Nameandconstructthem-filerhs.m,whichevaluatesthefunctionf(t,y).
Step4 Callode45.
[t, y] = ode45(@rhs, tspan, y0) or [t, y] = ode45(@rhs, [0 10], 3)
Them-fileis
function ydot=rhs(t,y)
ydot = ...
Since MATLAB will integrate whatever equation you give it, and the m-file “rhs” is
goingtobeusedmanytimes,youmustinsurethatitiscorrect:giventandy,itcomputes
thecorrectf(t,y)andputsthevalueintothevariableydot,whichisthenusedbyMATLAB
toconstructthesolution.Onceyouhavecheckedtheprogramandrunit,itiseasytoplot
thesolution.
plot(t,y)
Ifyouwantdataoutputatspecifictimes,use
tspan = [0:1:10] for data at t = 0, 1, 2, ..., 10.
Iftheintegrationistakinganinterminableamountoftime,itispossiblethatyouhave
defined a stiff system of equations (see Appendix E). In that case, change to an implicit
method(forstiffequations,hencethes-designation).
[t , y] = ode15s(@rhs, tspan, y0) or ode23s(@rhs, tspan, y0)
Ifyouwantthesolutiontobeplottedasitiscomputed,leaveoffthe[t,y].
ode45(@rhs, tspan, y0)
Tosolveasetofordinarydifferentialequations
dy
i = f ({y }), y(0)= y (B.8)
i j i i0
dt
wedothesamestepsexceptthattheinitialconditionisnowavectorwithNelements,the
m-file“rhs”mustcomputeNfunctionsusingthevectorywithNelements,andwehaveto
returntheresultasacolumnvector.
y0 = [0 1 3]
tspan = [0 10]
[t , y] = ode45(@rhs, tspan, y0)
```

---

## Стр. 320

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXB:HINTSWHENUSINGMATLAB 311
Them-fileis
function ydot=rhs(t,y)
% now there are y(1), y(2) and y(3) and t, which can be used
% to evaluate fi.
ydot(1) = ... term1 = ...
ydot(2) = ... or term2 = ...
ydot(3) = ... term3 = ...
ydot =ydot(cid:2) ydot = [term1;term2;term3]
Nowtheoutputfrom“ode45”isavector,t,andamatrix,y.Thevectoryhasasmany
columns as there are unknowns (here called N), and it has as many rows as there are
elements in the vector t. The output has to be a column vector, hence the (cid:2). Once the
solutionisfound,allcomponentsofitcanbeplotted.
plot(t,y)
Ifyouwishtosolvetheproblemmoreaccuratelythanisdonewiththedefaultparameters,
youcanchangethem.Thefollowingcommandsshowhowtochangetherelativetolerance
and absolute tolerance from the default values of 10−3 to 10−9. You can place different
accuracylimitsondifferentvariables,too.Toseealltheoptions,sayhelpodeset.
OPTIONS=odeset(‘RelTol’,1e-9,’AbsTol’,1e-9)
[t , y] = ode45(@rhs, tspan, y0,OPTIONS)
Differential–AlgebraicEquations
Some problems may have ordinary differential equations and algebraic equations, too.
These are not always easy to solve, but MATLAB has methods for them. Open the help
MATLAB/User’sGuide/Mathematics/Calculus/OrdinaryDifferentialEquationsandmove
down to Differential–Algebraic Equations. Examples are given there, but they require
careful adjustment of the error tolerances, which depend on the type of problem being
solved.
ChecklistforUsing“ode45”andOtherIntegrationPackages
Whenusing“ode45,”yourm-filefortheright-handsidemustmeettheseconditions:
(cid:2)
Thenameinthecallingcommandmustbethesameasthefilename;andnameinthe
functionisimmaterial.If“ode45”identifies@rhs,thenthefilenameofthem-filehas
tobe“rhs.m.”Thefirstlineofthem-filecanbefunctionydot=nothing(t,y).
(cid:2)
Thevariabletspan(orwhateveritiscalled)musthaveatleasttwovalues.
(cid:2)
Thenumberofentriesinthevectorfortheinitialconditionsmustbethesameasthe
numberofright-handsidescalculatedinthem-file.
(cid:2)
Whetheryoucalltheoutputfromthem-file“ydot”orsomethingelseisyourchoice,
butiftheoutputiscalled“ydot,”them-filemustcomputerallelementsofthevector
ydot.
(cid:2)
Theoutputofthem-filemustbeacolumnvector.
```

---

## Стр. 321

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
312 APPENDIXB:HINTSWHENUSINGMATLAB
(cid:2)
Variablescanbeusedinthem-fileprovidedtheyare(a)globalvariables,(b)passed
asparametersinthecallingargument,or(c)setinthem-file.Checktheirvalueinside
them-filebyrunningthem-file.
(cid:2)
The m-file will be called many times by the “ode45” function. However, you only
have to check the calculation once. Check the m-file by giving it t and all the y(i);
computewhatyouexpecttheright-handsidestobeandseethatthecomputergives
thosevalues.ThisistheonlywaytoensurethatMATLABissolvingtheproblemyou
wantsolved.
PLOTTING
SimplePlots
Foravectorxwithnentries,andavectorywithnentries,plottheminoneoffourways:
1.plot(x,y) 2.loglog(x,y) 3.semilogx(x,y) 4.semilogy(x,y)
Toplotmorethanonevariable:
plot(x, y1, x, y2) % if the y1 and y2 are known at the same
values of x
plot(x1,y1,x2,y2) % if y1 is known at x1 and y2 is known at x2
Addtitles:
title(‘This is the title’)
xlabel(‘x’)
ylabel(‘y’)
Addalegend:legend(‘‘first curve,’’ ‘‘second curve’’).
Plotonlyonecolumnofamatrix,herethesecondcolumn:plot(t,y(:,2)).
AddDatatoanExistingPlot
Issuethecommand:holdonandcontinueplotting.Furtherlines,symbols,andsoonwill
beaddedtotheexistingfigure.Whendone,type:holdoff.
DressUpYourPlot
Plotindifferentcolorsusing: plot(x, y, ‘r’, x, y2, ‘b’).
Usedifferentmarkers: plot(x, y, ‘or’, x, y2, ‘∗b’).
Usedifferentlineoptions: plot(x, y, ‘-r’, x, y2, ‘: b’).
To get both the symbols and the lines, use both line styles and markers: plot(x,
y, ‘-or’, x, y2, ‘:∗b’).
Limit the plot to x ≤ x ≤ x , y ≤ y ≤ y , regardless of the data: axis(
min max min max
[xmin xmax ymin ymax] ).
```

---

## Стр. 322

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXB:HINTSWHENUSINGMATLAB 313
FIGURE B.4 Multipleplots.
Limittheplottox ≤x≤x ,regardlessofthedata:xlim( [xmin xmax] ).
min max
Limittheplottoy ≤y≤y ,regardlessofthedata:ylim( [ymin ymax] ).
min max
Getmoreinformation:help axis.
Tochangethewidthofthelinesadd“LineWidth”,2totheplotcallingargument.
MultiplePlots
Togetmultipleplotsonthesamescreenusethecommandsubplot.FigureB.4showssix
plotsononescreen.
Thecommand:subplot(2,3,1)makesa2×3arrayofplotsinonefigureandthe
plottingcommandsfollowingthiscommandapplytothefirstplot(upperleft-handcorner).
Forthesecondfigure,saysubplot(2,3,2)andthenextplotwillbeinthemiddleof
thetoprowofthreefigures.Thefinalnumberistheplotsequence,numberedfromleftto
rightandthentoptobottom.
Sometimesyouwanttoprepareseveralplots,examinetheminturn,anddecidewhether
tosavethemorprintthem.Onewaytodothisistoinsertthefollowingcommandafterthe
plot command: pause. This causes the program to stop at that point in the code, and you
canexportthefigureorprintit.Thenpressanykeytocontinue.
3DPlots
Toplotafunctionz(x,y),createanx−ygrid(rectangular),evaluatethefunctionateach
gridpoint,andplot.
Createthexgrid:x = 0:0.05:1.
Createtheygrid:y = 1:0.2:3.
Createthecombinedmesh: [X,Y] = meshgrid(x,y).
Evaluatethefunction:Z=fn(x,y)wherefnisanexpressionorfunction;forz = x2+y2:
Z = X.*X + Y.*Y
Plotthe3Dplot:mesh(X,Y,Z)
Colorinthesurface:surf(X,Y,Z)
Createcontoursin2D:contour(X,Y,Z,20)
Createcontoursin3D:contour3(X,Y,Z,20)
```

---

## Стр. 323

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
314 APPENDIXB:HINTSWHENUSINGMATLAB
MoreComplicatedPlots
Possiblesymbolsare
+ plus ˆ triangle (up)
o circle v triangle (down)
∗ star > triangle (right)
. point < triangle (left)
x cross p pentagram
s square h hexagram
d diamond none no marker (default)
Thecolorsareinthedefaultorderformultipleplots,butwhiteisnotused.
b blue Line types
g green - solid
r red -- dashed
c cyan : dotted
m magenta _. dashdot
y yellow
k black
w white
UseGreekLettersandSymbolsintheText
TheseareTEXcommands.
α \ alpha (cid:5) \ Gamma ∞ \ infty
β \ beta (cid:7) \ Delta ≥ \ geq
γ \ gamma (cid:9) \ Theta ≤ \ leq
. . . . ∂ \ partial
. . . . ± \ pm
ω \ omega (cid:12) \ Omega (cid:8) \ Re
(cid:9) \ Im
Bold,Italics,andSubscripts
Tomakethetitle,xlabel,orylabelappearinboldfacetype,withafontsizeof12,use
ylabel(‘specific volume’, ‘fontsize’,12,’fontweight’,’b’)
Tomakethelabelappearinitalics,use
ylabel(‘specific volume’,’fontangle’,’italic’)
Toaddasubscript,useQ_1tomakeQ .ToaddasuperscriptuseQ∧1tomakeQ .To
1 1
increasethesizeofthetext,whichmayberequiredforpublication,use
set(gca,’LineWidth’,2,’FontSize’,18)
Forotheroptions,ofwhichtherearehundreds,usethehelpmenu.Toincreasethesize
ofthelegendusetheregularlegendcommandand
hx=legend; set(hx,’FontSize’,18)
```

---

## Стр. 324

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXB:HINTSWHENUSINGMATLAB 315
Itispossibletocreateplotsbyissuingcommands(asshownlater)andbycreatingthem
interactively. The Videos “Using Basic Plotting Functions” and “Creating a Basic Plot
Interactively”provideadditionaldetails(findin“help/MATLAB/Demos”section).Touse
theinteractivefeature,plotsomethingandthenusethemenusinthefiguretoperformsome
ofthesameactionsasdonewithcommands.
OTHERAPPLICATIONS
Examplessolvingtwo-pointboundaryvalueproblemsareshowninChapter9,andexamples
solving time-dependent problems in one spatial dimension are shown there, too. In these
problemsyouwanttoknowthesolutionateachx-positionasafunctionoftime.Itissimple
toplotthesolutionversustime,butitismoreinstructivetoplotthesolutionforallpositions
atseveraldifferenttimes.Thisisdoneasfollows.
PlottingResultsfromIntegrationofPartialDifferentialEquations
UsingMethodofLines
tspan = [0 10], y0 = [...]
[t , y] = ode45(@rhs,tspan,y0)
plot(t,y)
Thisgivesaplotofeachvariabley(t,i)versustime.Here,y(t,i)isthesolutionatpoint
x(i)andtimet.Toplotthesolutionversusx(i),atvarioustimes,specifythatyouwantthe
solutionataselectnumberoftimes.
tspan = [0:1:10] % 11 different times
y0 = [...]
[t , y] = ode45(@rhs,tspan,y0) % compute the solution
% y(j,i) is a matrix: the column number is i,
% and the row number j
% identifies the time, t(j)
x = [...] % specify the x-positions of the i-th variable
% there are the same number of entries for x as for y0
hold on
for i=1:11
plot(x(:),y(i,:))
end
hold off
IMPORT/EXPORTDATA
There are a variety of methods for importing and exporting data. Discussed here are
methodsforexchangingnumbersbetweentextfilesandvariablesinMATLABaswellas
betweenExcelandMATLAB.AnillustrationisalsogiveninwhichanExcelapplication
is programmed with text, text blocks, and data, which can be read by Excel. Additional
applicationsaredescribedinthevideo“ImportingDatafromFiles,”availablefromthehelp
menu,MATLAB,Demos.
Suppose you have a text file with two columns of numbers and five rows. This could
havebeenwritteninNotepadonthePCorTextEditontheMacintosh.Theeasiestwayto
```

---

## Стр. 325

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
316 APPENDIXB:HINTSWHENUSINGMATLAB
FIGURE B.5 Importwizard.
readthedataistousetheImportWizard.SelectFile>ImportData.Thenselectthetext
fileyouwishtoimportfrom.TheImportWizardwilldisplaythetextfileontheleft-hand
sideand the data inMATLAB on theright-hand side.You can choose toimportthe data
as an array, or as vectors in columns or rows. Choose next and the data is in MATLAB
as an array. See Figure B.5 by choosing File/Import Data. In this case the text file had
the numbers 1–10 in two columns, five rows, and that is how the array “test” appears in
MATLAB,too.Toexportthedata,usethecommand
save newfilename arrayname -ascii
SupposeyouhaveanExcelfilewithonlynumbers.Youcaneasilyimportitusingthe
command:
[num] = xlsread(‘filename.xlsx’).
ThearraynumnowcontainsthenumbersfromtheExcelfilefilename.xlsx.Toexport
anarray“A”fromMATLAB,usethecommand:
[num] = xlswrite(‘filename’,A).
The data goes into the Excel file. It is also possible to specify where it goes in (sheet
andrange).Seethehelpmenuforfunctions,DataImportandExport,Spreadsheets.
Itismorecomplicatedtodotheimportandexportwhenbothtextandnumericalvalues
are involved. Illustrated here is just one way of doing that, but it allows you to easily
create what is equivalent to a GUI in Excel, import the information into MATLAB, and
performcalculations.TheproblemposedisthesameasshowninFigure2.1,buttheExcel
spreadsheet will be used to enter the data, it will be transferred to MATLAB, and the
program “specvol” will calculate the specific volume. The Excel spreadsheet is prepared
as shown in Figure B.6a. The darkened blocks need to be filled in by the user. Then one
savesthespreadsheetinaTabdelimitedformat,aspvt_data.txt,givingtheresultshownin
```

---

## Стр. 326

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXB:HINTSWHENUSINGMATLAB 317
pvt calculation
chemical name
n-butane
Tc(K) pc(atm) omega
425.2 37.5 0.193
conditions
T(K) p(atm)
393.3 16.6
method
1
1-RK
2-RKS
3-PR
(a) (b)
FIGURE B.6 ExcelspreadsheettoprovidedatatoMATLAB:(a)spreadsheet;(b)tabdelimited
result.
FigureB.6b.Theprogramtoreadthedataandperformthecalculationsisshownlater.The
answers,ofcourse,arethesameasbefore.
% pvt calculation with input from Excel
global T p Tc pc R aRK bRK icode
inputfile = strcat(‘pvt_data.txt’)
fid = fopen(inputfile,’r’);
% read chemical data
for i=1:4;tline = fgets(fid);end % this line skips the first
% two lines from Excel
chemicalname = sscanf(tline,’%s’)
for i=1:1;tline = fgets(fid);end
Tc = fscanf(fid,’%g%’)
pc = fscanf(fid,’%g%’)
omega = fscanf(fid,’%g%’)
% read conditions
for i=1:4;tline = fgets(fid);end
input1 = fscanf(fid,’%g’,2);
T = input1(1)
p = input1(2)
% pick an equation of state
for i=1:3;tline = fgets(fid);end
icode = fscanf(fid,’%g’,1)
% icode for EOS
% = 1 Redlich-Kwong
% = 2 Redlich-Kwong-Soave
% = 3 Peng-Robinson
```

---

## Стр. 327

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
318 APPENDIXB:HINTSWHENUSINGMATLAB
fclose(fid); % close the file pvt_data.txt
% set up the problem
R=0.08206
if icode==1
aRK=0.42748∗(R∗Tc)ˆ2/pc
bRK=0.08664∗R∗Tc/pc
alpha = (Tc/T)ˆ0.5;
elseif icode==2
aRK=0.42748∗(R∗Tc)ˆ2/pc;
bRK=0.08664∗R∗Tc/pc;
m=0.48+1.574∗omega-0.176∗omega∗omega;
alpha = (1+m∗(1-(T/Tc)ˆ0.5))ˆ2;
else
aRK=0.45724∗(R∗Tc)ˆ2/pc;
bRK=0.07780∗R∗Tc/pc;
m=0.37464+1.54226∗omega-0.26992∗omega∗omega;
alpha = (1+m∗(1-(T/Tc)ˆ0.5))ˆ2;
end
aRK=aRK∗alpha
% solve the problem
vol=fzero(‘specvol’,2)
Z=p∗vol/(R∗T)
Import/ExportwithComsolMultiphysics
See Appendix D for ways to transfer data between Comsol Multiphysics and MATLAB.
YouneedalicenseforLiveLinkwithMATLAB.
PROGRAMMINGGRAPHICALUSERINTERFACES
You can also make GUIs in MATLAB. This may be convenient if you are preparing a
programthatcanbeusedbysomeonenotfamiliarwithMATLAB.Datacanbeenteredand
theprogramtoldtorun,withappropriateoutput.Tolearnaboutthis,gotothehelpmenu,
UsersGuide,CreatingGUIs.
MATLABHELP
Whenyouarereallystuck,issuethecommand
help commandname
Thismayleadyoutothesolutionyouarelookingfor.Issuingthecommand
help
gives you a table of contents; look at “help funfun,” for example, to see all the methods
andoptionsforintegratingdifferentialequations.Alternatively,clickonthearrowandlook
underMATLAB;thereareseveralfolders(seeFigureB.7)thatleadyoutoinstructionsto
performspecifictasks.
```

---

## Стр. 328

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp2 JWBS084-Finlayson May30,2012 8:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXB:HINTSWHENUSINGMATLAB 319
FIGURE B.7 Help/searchwindow.
APPLICATIONSOFMATLAB
There are many chemical engineering examples in the book that use MATLAB; see the
TableofContents.Listedhereareexamplesapplyingspecialtechniques.
(cid:2)
Solving a single nonlinear equation, Chapter 2, p. 15, Chapter 3, p. 34, Chapter 4.,
p.53,Chapter8,p.164
(cid:2)
Plotting,Chapter2,p.18
(cid:2)
Multipleequations,fewunknowns,Chapter4,p.56
(cid:2)
Integrateordinarydifferentialequation,Chapter8,pp.141,144,146,156,166
(cid:2)
Fitstraightlinetodata,bookwebsiteonparameterestimation
(cid:2)
Polynomialregression,bookwebsiteonparameterestimation
(cid:2)
Nonlinearregression,bookwebsiteonparameterestimation
```

---

## Стр. 329

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp3 JWBS084-Finlayson May18,2012 13:11 PrinterName:YettoCome Trim:7in×10in
C
APPENDIX
®
HINTS WHEN USING ASPEN PLUS
ThisappendixgivesafewhintsandtipsonusingAspenPlus.1 Itassumesthatyouarea
beginner,soitshowsthemainstepsyougothroughtouseAspenPlus,withscreenshotsto
illustratewhatyoushouldseeonthescreen.Youshouldworkthroughthisappendixusing
Aspen Plus to reproduce the examples shown here and review the examples again when
you use Aspen Plus in other chapters. Keep in mind that this is a complex program with
manyoptionsdevelopedoverdecadesbyengineersworkingforAspenTechnologyaswell
as the companies using the program. Some engineers’ whole job is doing simulations to
modelchemicalprocess,anditisunrealistictoexpectabeginnertodothesame.However,
youcanuseAspenPlustodomany powerfulthings,anditisimportanttoknowthefull
capabilitiesavailabletoyou.
INTRODUCTION
Begin by opening Aspen Plus. For a new problem, it is useful to choose a template
that is similar to your problem; you can also open previous problems. You have several
choicesbeforeproceeding:choosingatemplatefromRefineryorSimulations,andchoosing
Flowsheet,DataRegression,oroneofthePhysicalPropertyoptions.IfyoupickFlowsheet,
thescreenthatappearsisshowninFigureC.1.
SeveralmenusinFigureC.1areusedoverandover,soitisworthwhiletoidentifythem,
proceedingfromlefttoright.Followalongonthecomputerasthemenusarelisted.TheFile
menuhastheusualitems:New,Open,Save,andsoon.OnemenuitemisExport,which
allowsyoutoexportareport,asummary,theinput,andanymessagesprovidedduringthe
1AspenPlusisaregisteredtrademarkofAspenTechnology,Inc.Thisbookusesversion7.3.
IntroductiontoChemicalEngineeringComputing,SecondEdition.BruceA.Finlayson.
©2012JohnWiley&Sons,Inc.Published2012byJohnWiley&Sons,Inc.
321
```

---

## Стр. 330

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp3 JWBS084-Finlayson May18,2012 13:11 PrinterName:YettoCome Trim:7in×10in
322 APPENDIXC:HINTSWHENUSINGASPENPLUS
FIGURE C.1 Openingscreen.
run.Thereport,inparticular,ishandytohavewhendoneasaprintedsummary.TheView
menuhasoptionstosettheToolbar(choosetheiconsyouwantalongthetop),showthe
ModelLibrary,orshowtheControlPanel(whichsummarizestheconvergenceofthelast
calculation. If the model has many units in it, Zoom enlarges the flowsheet, but an even
betteroptionistouseFlowsheetSections(seelater).View/CurrentSelectiononlyiswhere
you limit the flowsheet to one section or several. The options Input Summary, History,
andReportallgiveinformationthatisusefulinyourreport.TheDatamenuactslikethe
DataBrowser(seelater).TheToolsmenuhasoptionsforAnalysis(toplotthermodynamic
propertiesofpurecomponentsorbinarymixtures;NISTThermoDataEngine(lookforthe
blueandredTDEicon)(tofindandreportthermodynamicpropertiesofpurecomponents),
andMolecularDrawing(torepresentchemicalsnotalreadyinthedatabase).Theseoptions
aredescribedinmoredetailbelow.TheTools/PropertyMethodSelectionprovidesanaid
for choosing the method to calculate thermodynamic properties. Tools/Options provides
manychoices:forexample,doyouwantthenamesoftheblocksorstreamstoappearon
thespreadsheet?
FLOWSHEET
ModelLibrary
Thepossiblemodelsareshowninthemenubaratthebottom(seeFigureC.2.)Ifthisdoes
notappear,choosetheView/ModelLibrarymenu.Themodelsareorganizedbyfunction,
FIGURE C.2 Modellibrary.
```

---

## Стр. 331

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp3 JWBS084-Finlayson May18,2012 13:11 PrinterName:YettoCome Trim:7in×10in
APPENDIXC:HINTSWHENUSINGASPENPLUS 323
FIGURE C.3 Flowsheetofadistillationcolumn.
such as Mixers/Splitters, Separators, Heat Exchangers, Columns, or Reactors, and so on.
Clickonthetabtoseethedifferentpossibilities:anewmenuliststhedifferenttypeswithin
that class. Click on Columns, for example, and you see choices such as DSTWU, Distl,
RadFrac, and so on. A brief description about the unit is displayed beneath the model
library,butthatmaynotshowupunlessyouhavemaximizedthescreen.
PlaceUnitsonFlowsheet
To place a model or unit operation (now called a block), on your flowsheet click on the
desiredmodelandthenclickinthescreenwhereyouwanttheblocktoappear.FigureC.3
showsaDSTWUblock. Continueinthisfashionuntilyouhave theblocks youwant.To
delete a block, click on it and either choose Edit/Delete or right click and scroll down to
delete.Inthedatabrowser,selectFlowsheetandcheckthateachunithasthecorrectstreams
inandout(seeFigure7.3).ByusingtheTools/OptionsoptionandtheFlowsheetTabyou
cancausetheblock(andstream)namestoappear ontheflowsheet(ornot),andyoucan
have them assigned numbers with a specified prefix (or not). If not, you will be asked to
supplyanameforeveryblock(andstream)asyouenterthem.
ConnecttheUnitswithStreams
Clickonthe“MaterialStreams”iconinthelower,leftcornerofthescreen(seeFigureC.1,
whereitappearsinthelowerleft-handcorner,orFigureC.2whereitappearsontheleft).
Thenclickintheflowsheetwhereyouwantthestreamtooriginateanddragthecursorto
whereyouwantittoend.Continueinthiswayuntilyouhaveplacedallthestreamsinyour
flowsheet.Whenyouaredone,clickthearrowtotheupperleftofthe“MaterialStreams”
box(FiguresC.1andC.2)todisconnectthedrawingoption.Ifyouaddedstreamsyoudo
notwant,selectthemandchooseEdit/Deleteorrightclickandscrolldowntodelete.You
canalsorenameunitsandstreamsbyusingrightclickandscrollingdowntorename.Ifyou
selectTools/OptionsandtheFlowsheetTab,youcanhavethestreamsandblocksnamed
automatically,oryoucansetitsothatyouhavetosupplyaname.
Data
Find the pair of eye glasses in the top row. This icon opens the Data Browser, which
providesalistofwindowstobecompleted(seeFigureC.4):Setup,Components,Properties,
Flowsheet,Streams,Blocks,Utilities.Thesearediscussedinturn.
```

---

## Стр. 332

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp3 JWBS084-Finlayson May18,2012 13:11 PrinterName:YettoCome Trim:7in×10in
324 APPENDIXC:HINTSWHENUSINGASPENPLUS
FIGURE C.4 Setup/ReportOptionsforstreams.
Setup
Youcanspecifyatitleforyourproblem,choosetheunitsyouwant(thesecanbeoverridden
ineachstreamandblock),andcreatereportoptions.Todothis,clickontheglasses(Data
Browser)anddouble-clickthefolderSetup.IntheSetup/ReportOptionswindowyouput
checksintheboxesforthepropertiesyouwishtoincludeinyourreport,asillustratedin
FigureC.4.
DataEntry
Aspen Plus has a menu that walks you through the procedure to specify a process. Find
thepairofeyeglassesinthetoprow.ThisiconopenstheDataBrowser,whichprovidesa
listofwindowstobecompleted(seeFigureC.4).Alternatively,youcanchooseDataand
thenchooseSetup,Components,Properties,andsoon.Anotherwayistochoosetheicons
showninFigureC.5.
Bypressingthe icon,fillingoutthewindowthatappears,andpressingitagain,you
canproceedthroughthedataentryphaseofaproblemeasily.The (showninFigureC.4)
FIGURE C.5 IconsinAspenPlus:Setup,Components,Properties,Streams,Blocks,DataBrowser,
andNextStep;Run,Step,Reinitialize;MolecularDraw,TDE,ModelSummary.
```

---

## Стр. 333

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp3 JWBS084-Finlayson May18,2012 13:11 PrinterName:YettoCome Trim:7in×10in
APPENDIXC:HINTSWHENUSINGASPENPLUS 325
FIGURE C.6 Componentidentification.
can be used to step from window to window, but it includes all the windows, even if
theyarecomplete.Themenuitemsontheleftthatareinredarenotcomplete,andmust
be completed. Double-click them in turn, starting from the top. Then click on the red
submenus. A new window will appear, asking you to fill in the needed information. To
closeupthemenu,clickonafolder,andthesubfoldersbeneathitwillbehiddenagain.A
thirdalternativeistochangethe“All”showninFigureC.6to“Input”andclickonthe .
Thistakesyouthrougheachwindowonebyone.
Asyouaddinformationitmightbeconvenienttogobackandforthbetweentheflowsheet
and the window you are filling in. Under Window choose Workbook rather than Normal
andaTabwillbeplacedatthebottomthatpermitsyoutomovebackandfortheasily.
SpecifyComponents
Type the name of the component in the left-hand column of the window. If you type in
a name and the third column is not automatically filled in (as in Figure C.6 for C5H12),
double-click on the blank box in the third column. Type the name into the window that
appears, choose Find Now, and search for your chemical in the list provided. Close the
windowafterspecifyingallthechemicalsappearinginyourprocess.
SpecifyProperties
You use Property Method to tell Aspen Plus what thermodynamic model you want to
use. Initially all models are available. You can limit the choices by selecting an industry
orapplication,andthenonlythepertinentchoicesareavailable.Chapter 6discussesthis
choiceinmoredetail,butthisisonedecisionthatmustbevalidatedbycomparisonwith
experimental data. In a design situation this is essential. You have the choice of a num-
berofdatabases,butforintroductoryuse,choosethelatestanddefaultdatabase.Whena
programhasbeeninuseinindustryformanyyears,eachuserwantstheirdatabasetobe
retained, so that databases tend to get added on and little housekeeping takes place. The
Tools/PropertyMethodSelectionAssistantprovidesguidanceforthechoiceofthermody-
namicpropertycalculation.TheNISTThermoDataEngineprovidestheparametersused
inthethermodynamicmodels.
```

---

## Стр. 334

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp3 JWBS084-Finlayson May18,2012 13:11 PrinterName:YettoCome Trim:7in×10in
326 APPENDIXC:HINTSWHENUSINGASPENPLUS
FIGURE C.7 Streaminformation.
SpecifyInputStreams
Whenyouopenupthestreamfolder(ontheleft),thestreamsthatareinputstreamstothe
processwillbeshowninred.Clicktheminturn,fillinginthepropertiesofthatstream.You
mustspecifytheflowrateofeachspecies(althoughnotnecessarilythosethatarezero),the
temperature,andthepressure,asshowninFigureC.7.Youcanspecifymolefractionsand
thetotalflowrateifyouprefer.Youdonotneedtospecifyconditionsininternaloroutput
steams; the computer will calculate those. Sometimes it is helpful to specify an internal
streamtospeedconvergence,butyouneedtoknowwhichonetouse(seeChapter7).
SpecifyBlockParameters
Click each block in turn and fill in block parameters (see Figure C.8). Sometimes the
window has multiple options, which you need to complete if they are red. If you want
FIGURE C.8 Blockparameters.
```

---

## Стр. 335

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp3 JWBS084-Finlayson May18,2012 13:11 PrinterName:YettoCome Trim:7in×10in
APPENDIXC:HINTSWHENUSINGASPENPLUS 327
some of the results (like temperature and pressure) to appear on the flowsheet, choose
Tools/Options/andtheResultsTabandselecttheitemstodisplay.
RUNTHEPROBLEM
To run the problem, choose the blue in the new window and click OK or click on the
closed triangle (see Figure C.5). The open triangle allows you to calculate one unit at a
time. (If some data is not yet specified, the program will tell you.) By choosing the
button,yougetthemostinformationbackfromthecomputer,includinginformationabout
convergence,asshowninFigure7.7a.
Ifyouruntheproblem,makeachangeinaparameter,andruntheproblemagain,Aspen
Pluswillusethefirstsolutionasthestartingguessforthesecondproblem.Ifyoudonot
wantthistohappen,chooseRun/Reinitializeorthereinitializebutton(seeFigureC.5),and
the starting values are put back to the default values (flow rates of internal streams and
output streams are usually zero). You can also do the iterative calculations one unit at a
timebychoosingtheRun/StepmenuorCRTL+F5ortheopentriangle.
ScrutinizetheStreamTable
In the left-hand window, click Results/Summary and Stream to get the mass and energy
balances,thevaluesofflowrateandenthalpyofeachstream,asillustratedinFigureC.9.
When the stream information is displayed on the screen, click Stream Table to get the
FIGURE C.9 Streamtable.
```

---

## Стр. 336

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp3 JWBS084-Finlayson May18,2012 13:11 PrinterName:YettoCome Trim:7in×10in
328 APPENDIXC:HINTSWHENUSINGASPENPLUS
informationontheflowsheet.Ifyouclickontheupperleftblankboxofthestreamtable,
thetablewillbecopiedtoaformatthatcanbepastedintoaspreadsheetlikeExcel.
CheckingYourResults
TakethestreamsintheStreamTableandfollowthemthroughtheprocess.Didthecomputer
dowhatyouintended?Aretheresultsreasonable?ByusingtheDataBrowser,youcanlook
attheresultsforeachblock,oryoucanchoosetheModelSummaryicon(seeFigureC.5)
andobtaintheresultsforeachcollectionoflikemodels(i.e.,alltheheatexchangers).
You expect Aspen Plus to be correct, but there are two possible problems: lack of
convergence and poor choices of thermodynamic correlations. By using the button to
run your problem you will get printed information about the convergence or lack of it.
Read the output! You get this information from the View/Control Panel menu, too. The
properchoiceofthermodynamic correlationcanonlybedeterminedbycomparisonwith
experimentaldataorwithexperience.(Thisisonereasonwhychemicalengineersarepaid
a lot—for their experience.) Naturally, at this point in your career, few of you have that
experience.However,youcanstilllookatyourmassandenergybalancesandseeifthey
makesense.Everynumberneedstobeexamined.
There are three important sources of summary information, all listed under the View
menu:InputSummary,History,andReport.Youshouldlookatthese—youmaydetectan
errorbyviewingthesummariesprovidedthere.
ChangeConditions
Toruntheproblemwithdifferentconditions,lookfortheword“All”inawhitebox(see
itinFigureC.4).TheoptionsareAll,Input,Results;scrolldowntoInput,andmakeyour
changes using the menu on the left. Click the button to rerun the problem. To rerun
the problem you must change something. If you just want to run 30 more iterations, for
example,addaspaceinthetitleandclick .
REPORT
TransfertheFlowsheetandMassandEnergyBalance
toaWordProcessingProgram
Selecttheflowsheetbydraggingthemousefromtheupper,leftcornertothelower,right
corner. Copy the flowsheet and paste it into the application. You can also use the Print
Screenkeyandthengotoyourwordprocessingprogramandpasteit.UsethePicture/Crop
function to select the portion of the diagram that you want displayed. The best way to
capture the Stream Table is toselectthe entiretable and pasteitintoExcel. This isdone
fromtheResults/Summary/Streamoption.
Ifyouwouldlikethetemperatureandpressuretoappearontheflowsheet,ensurethat
GlobalDataischeckedintheViewmenu,chooseTools/Options/ResultsViewandclickthe
boxesfortemperatureandpressure.FigureC.10showstheresultingchangeintheflowsheet.
PrepareYourReport
DetailedinformationcanbeobtainedusingtheView/Reportmenu.Thisgivesdetailsabout
individual blocks. The View/History menu gives information about the convergence and
whatcalculationshavebeendone.TheView/InputSummaryliststheparametersyouhave
```

---

## Стр. 337

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp3 JWBS084-Finlayson May18,2012 13:11 PrinterName:YettoCome Trim:7in×10in
APPENDIXC:HINTSWHENUSINGASPENPLUS 329
Temperature (K) 299
Pressure (atm) 9
297
9
OVERHEAD
365
INPUT DIST
9
BOTTOM
FIGURE C.10 Addingtemperatureandpressuretotheflowsheet.
set.Everyreportshouldhaveaflowsheetwithblocksandstreamslabeled,massandenergy
balances referenced to the flow sheet, and a text description of the process. You should
outlinetheproblem,describethechoicesyouhavemade,andlistallthewaysyouexamined
yourresultsforvalidity.Whenyouarereallydone,youcanchooseFileandExport.Inthe
“Saveastype”window,scrolldowntoreportFiles(∗.rep).Browsetothefolderwhereyou
wanttosaveitandclickSave.Atextversionofthewholesimulationissaved,givingall
thedetailyousuppliedandalltheresults.Itisveryusefultodocumentyourwork(perhaps
as an Appendix in a report), and the report gives the detail needed to write a descriptive
report.Itdoesusepaper,though,ifyouprintit.Forexample,thereportforthefour-column
gas plant problem in Chapter 7 was 10 pages long. You can choose the Model Summary
iconandobtaintheresultsforeachcollectionoflikemodels(i.e.,alltheheatexchangers).
SaveYourResults
Saveyourprogramandresultsinthecomputermemory.Agoodstrategyistocreateafolder
foreachnewproblemandsaveyourprogramandresultsinthefolder.Thereasonisthat
whenyouchooseFile/Save,fivefilesarecreated.TostartfromtheyellowAspenfilemany
ofthesefilesareneeded.Itisalsousefultosaveyourfileperiodicallywhenworking,just
incasesomethinggoeswrongandyouneedtorestart.Youcanrestartfromthebackupfile
(.bkp)alone,andthisissufficienttoredotheproblemwithouthavingtosetanyconditions,
althoughyoumayhavetoresolveit;thisfile.bkpisalsousefulwhendifferentversionsof
Aspenareused.
GettingHelp
Click andthentheboxonsomething(e.g.theDataBrowserwindoworsomewhereon
theflowsheet).TheHelpmenuprovidesdetailedhelpinallareas,andyoucansearchby
contents,index,orkeywords.
ADVANCEDFEATURES
FlowsheetSections
If your process has already been divided into flowsheet sections, you can access each
sectionbyitself.Todoso,chooseeither(1)flowsheet/flowsheetsectionsfromthemenuat
```

---

## Стр. 338

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp3 JWBS084-Finlayson May18,2012 13:11 PrinterName:YettoCome Trim:7in×10in
330 APPENDIXC:HINTSWHENUSINGASPENPLUS
FIGURE C.11 Flowsheetsections.
the top; (2) Alt+F11; or (3) choose (glasses)/flowsheet/sections. In all cases the sections
willbelistedontheleftandalsoinawindowtotherightasshowninFigureC.11.Donot
click on any section on the left panel. Choose one section from the list on the right, and
thenclickMakeCurrentSection(lowerright-handcorner).Thenclickthe×toclosethe
window.GotoViewandselectCurrentSelectiononly.Thentheonlyflowsheetshownwill
bethatsection.
Another alternative is to zoom the flowsheet. Using CTRL up arrow or down arrow
zoomsinorout,respectively.
Whenmakingyourflowsheet,youcanmakeselectionsasfollows.Selecttheflowsheet
sectionsasmentionedearlier.Globalwillbeshown.Changeitsnametoasectionnameof
yourchoice.Thenpreparetheflowsheetforthatsection.Gobacktoflowsheet/sectionsand
rightclickonSections,chooseNewandprovideanewname.Thenmakethenewsection
current. All process units you enter after that will be in that new section. To connect the
sections,unclickView/CurrentSelectionOnlyandtheentireprocesswillbeshown.Then
youcanchooseastreamandchangeitssourceordestinationsothatoneisinonesection
andtheotherisintheothersection.Ifyouwishtomoveaprocessunitfromonesectionto
another,selecttheunitandrightclick.Choose:changesection.
MassBalanceOnlySimulationsandInclusionofSolids
Sometimesitisdesirabletosimulateaprocessusingmassbalancesonly,withoutenergy
balances. To do that in Aspen Plus, click on the Browser, choose Simulation/Simulation
options,anduncheckthebox“PerformHeatBalanceCalculations.”Thentheparameters
forenergybalanceswillnotberequired.UnitslikeFSplit,Sep,Sep2willbeusable;units
likeDSTWU,Flash2,RStoic,andsoon,canbeusedifyoudonotuseheatduties.Afull
list can be seen by choosing the Help button in Aspen and entering “mass balance only
simulations”intotheindex.
In Aspen, the liquid/vapor stream is generally called “Mixed.” In versions 7.2 and
earlier,solidssuspendedintheliquid(orevenbythemselves)arecontainedinasubstream
called“CISOLID.”AspenTechsuppliesapdffile“GettingStartedModelingProcesseswith
Solids.” Solids are generally given a molecular weight of 1 so that in chemical reactions
the stoichiometric coefficient is an integer multiplying the molecular weight. Aspen Plus
```

---

## Стр. 339

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp3 JWBS084-Finlayson May18,2012 13:11 PrinterName:YettoCome Trim:7in×10in
APPENDIXC:HINTSWHENUSINGASPENPLUS 331
checksthisandtellsyouifthemassisnotbalancedinareactor.Inversion7.3simplesolids
canbecontainedinthe“Mixed”stream;inthistext,theyhavebeenleftin“CISOLID.”
TransferbetweenExcelandAspen
ItispossibletotransferinformationbetweenExcelandAspen.GoingfromAspentoExcel
issimple:thestreamsummarycanbecopiedtotheclipboardbyclickingtheblanksquare
in the upper left corner; then open Excel and paste it. It is also possible to transfer from
Excel toAspen. One operation istoimportTxydata setfromExcel toAspen Properties.
Thenyoucanestimateorregressthepropertyparameters.Todothis,seetheinstructions
underhelp,searchonExcel.ItisalsopossibletohaveablockthatisdefinedinExceland
linkedtoAspen.NotealsothatExcelhasanAspenTab,andyoucanopen(enable)Aspen
Simulation Workbook from Excel. Both of these operations are beyond the scope of this
bookthough.
BlockSummary
After doing the calculation, the results for each block should be examined. This is done
mosteasilybychoosingResultsSummary/ModelSummaryfromeithertheDatamenuor
the Data Browser. All the blocks are listed there, with like blocks grouped together, and
canbeaccessedwiththetabsatthebottom.
CalculatorBlocks
Calculator blocks are blocks that the user defines to do a specific calculation that is not
available in Aspen Plus. The programs can be from Excel, or they can be written using
FORTRAN.Simplecalculationscanbedoneusingthein-lineFORTRANthatcomeswith
Aspen.Anexampleisgivenbelow.Morecomplicatedcalculationscanbedonebywriting
aFORTRANsubroutineexternaltoAspenandcompilingit.Itcanbelinkeddynamically
toAspen.
Todemonstratethecalculatorblock,considertheflowsheetshowninFigureC.12.Stream
1isdefinedas100lb/hofwater.Wewouldlikestream2tobehalftheflowrateofstream1.
Obviouslywecouldsetit,butthisblockmightbeinthemiddleofaprocessforwhichwe
donotknowtheflowrateofstream1apriori.WechooseFlowsheetingOptions/Calculator
MIXER
2
1 3
FLORATIO
CALCULATOR
FIGURE C.12 Calculatorblock.
```

---

## Стр. 340

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp3 JWBS084-Finlayson May18,2012 13:11 PrinterName:YettoCome Trim:7in×10in
332 APPENDIXC:HINTSWHENUSINGASPENPLUS
FIGURE C.13 Sequenceforcalculatorblock
intheDataBrowser.ThecalculatorblockisnamedFLORATIO.Variablesarenamedand
setasfollows:SECONDisthewaterflowrateinstream2.FEEDisthewaterflowratein
stream1.Theformulais
SECOND=0.5 ∗ FEED
To write this in the box for Calculate Tabs, put the cursor in the empty box and right
click,choosevariablelist.PickSECONDandrightclickandpaste.Thentype=0.5∗anddo
thesamethingforFEED.SincethisisaFORTRANcommand,makesurethatthefirstsix
columnsareblankandtheSbeginsintheseventhcolumn.ThenclickontheSequencetab.
WewantthecalculationtohappenbeforetheMIXERblockiscalculated;seeFigureC.13.
TheMIXERisaunitoperation,andwechoosetheBlockname:MIXER.Wemustidentify
theinformationgoingintoandoutoftheblockcalculation.ChoosethevariableFEEDas
the input variable and SECOND as the export variable; do this by placing the cursor in
theboxandclickingit.Nowwhenthecalculationsequencebegins,thefirstthingthatwill
becalculatedwillbeFLORATIO;itwilltakeFEEDandcalculateSECOND.Thenwhen
MIXERiscalculateditwilladdthemtogether.Inthissimpleexample,itwasnecessaryto
specifythetemperatureandpressureofstream2,andasmallamountofwater,sinceitis
aninputstream(used0.001).
AspenExamples
Aspen comes with a number of examples that are on your local disk, Program Files
(×86)/AspenTech/AspenPlusV7.3/GUI/App/.Examplesandsomeoftheunitsthatarein
eachexamplearelistedinTableC.1.SimpleunitslikeMixer,HeatExchangers,RStoic,and
soonarenotlistedthere.IfyouarehavingtroublewithoneoftheblockslistedinTableC.1
youshouldlookattheappropriateexampletoseeaworkingversionofthatblock.Inaddi-
tion,PhysicalSolventshasanexampleofequilibriumabsorptionusingRADFRAC,Amines
hasanexampleofrate-basedabsorptionusingRADFRAC,andAmmoniahasanexample
ofFlash2usedasanabsorber.Inaddition,thereareexampleswithpolymersandscaling.
MOLECULEDRAW
Aspen Plus also has the capability to estimate physical properties from the structure.
You can click on the Molecule Draw icon (see Figure C.5) and draw the molecule with
```

---

## Стр. 341

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp3 JWBS084-Finlayson May18,2012 13:11 PrinterName:YettoCome Trim:7in×10in
selpmaxEnepsAniskcolBfoselpmaxE
1.CELBAT
roXtaeH
neercS
rehsurC
retnaceD
retliF
lanoitnevnocnoN
sdiloS
XtaeHM
liuqER
gulpR
RTSCR
rotcartxE
CARFDAR
tilpsS
elpmaxE
X
ainommA
X
X
X
leseidoiB
X
X
X
nrocmorflonahteoiB
X
X
X
nrocmorflonahteiB
revots
X
noitarenegoC
X
X
X
laocwofldeniartnE
refiisag
X
X
X
X
X
X
X
X
CCGI
X
X
X
laocdebgnivoM
refiisag
X
gnitroterelahsliO
X
stnevloslacisyhP
X
X
X
X
sagenilepiP
X
X
X
dicacirufluS
X
aerU
X
reuaB
X
X
esahP-3
333
```

---

## Стр. 342

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp3 JWBS084-Finlayson May18,2012 13:11 PrinterName:YettoCome Trim:7in×10in
334 APPENDIXC:HINTSWHENUSINGASPENPLUS
differentatoms,differentbonds,anddifferentconfigurations.Toseehowtodothis,search
on “molecular draw.” The connectivity of molecules is used in estimation of physical
propertiesbytheAspenPhysicalPropertySystemorbytheNISTThermoDataEngine.
APPLICATIONSOFASPENPLUS
Manychemicalengineeringapplicationsaredescribedinthetextandcanbefoundusing
theTableofContents.Specializedtechniquesaredescribedin
(cid:2)
TestofThermodynamics,Chapter3,p.39;Chapter6,p.97
(cid:2)
NISTThermoDataEngine,Chapter3,p.41
(cid:2)
Sensitivity,Chapter6,p.102
(cid:2)
DesignSpecs,Chapter6,p.102
(cid:2)
Convergence,Chapter7,p.120
(cid:2)
UtilityCost,Chapter7,p.118
(cid:2)
GreenhouseGasEmissions,Chapter7,p.120
(cid:2)
Optimization,Chapter7,p.122
(cid:2)
ChemicalReactor,PlugFlow,Chapter8,p.159
```

---

## Стр. 343

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp4 JWBS084-Finlayson May18,2012 8:11 PrinterName:YettoCome Trim:7in×10in
D
APPENDIX
HINTS WHEN USING
®
COMSOL MULTIPHYSICS
This appendix gives an introduction to the use of Comsol Multiphysics. The program
Comsol Multiphysics,1 uses the finite element method to solve fluid flow, heat transfer,
andmasstransferproblems,aswellasmanyotherequations.Inthepastdecade,computer
software has become very powerful, and this allows chemical engineers to solve very
complicatedproblems.Thisposesaproblemthough:youmaybetemptedtoposeaproblem
thatiswaymorecomplicatedthanyouneed.Instead,heedEinstein,“makeitassimpleas
possible,andnosimpler.”Anotherproblemisthatmanydetailsofthecomputerprogram
arehiddenfromyou,oratleastnotreadilyaccessible.Byclickingbuttons,orforgettingto
makeaparticularchoice,youmayinadvertentlysolvethewrongproblem.
Ontheotherhand,engineersusedtoreduceallproblemstoonesthatcouldbesolved
analytically,becausethentheycouldsolvethem.Theassumptionsusedinthesimplification
might or might not be justified, but the analytical form of the answer aided their under-
standingoftheproblem.Moderncomputerprogramscansolvethosesimpleproblems,and
thesolutionprovidesatestofthecomputerprogramandyouruseofit:Doesthecomputer
solutionagreewiththeanalyticalsolutionwhenitshould?Buttheprogramscanalsosolve
realisticproblemsthatareimpossibletosolveanalytically.Whatyouhavetodois(a)pose
arealisticformoftheproblem,and(b)verifyyouhavesolveditaccuratelyenough.
Thefiniteelementmethodreplacesadifferentialequationwithalargesetofalgebraic
equations.Thedetailstomakethisswitcharecomplicated,butfortunately,ComsolMulti-
physicshasdonethatforyou.Youstillneedtoknowhowtousetheprogram,because,after
all,itisuptoyoutodecideifyouhavesolvedtherightproblem,determinedtheaccuracy,
andderivedusefulpropertiesfromthesolution.
The examples are made with the Chemical Reaction Engineering Module addition to
ComsolMultiphysics,version4.2a.However,mostofthemcan besolvedwiththebasic
1ComsolMultiphysicsisaregisteredtrademarkofComsol,Inc.ThisbookusesVersion4.2a.
IntroductiontoChemicalEngineeringComputing,SecondEdition.BruceA.Finlayson.
©2012JohnWiley&Sons,Inc.Published2012byJohnWiley&Sons,Inc.
335
```

---

## Стр. 344

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp4 JWBS084-Finlayson May18,2012 8:11 PrinterName:YettoCome Trim:7in×10in
336 APPENDIXD:HINTSWHENUSINGCOMSOLMULTIPHYSICS
ComsolMultiphysics,althoughthenthestoichiometryofareactionwillbeuptoyou.Ifyou
wouldliketoknowwhatmodulesareincludedinyourversion,gotoOptions/Licensesorthe
bookwebsite.AppendixEdescribesthefiniteelementmethodinoneandtwodimensions
soyouhavesomeconceptoftheapproximation:goingfromasingledifferentialequation
toasetofalgebraicequations.Thisappendixpresentsanoverviewofmanyofthechoices
provided by Comsol Multiphysics. Illustrations of how Comsol Multiphysics is used to
solveproblemsaregiveninChapters9–11.Thus,youmaywishtoskimthisappendixona
firstreading,andthencomebacktoitasyouusetheprogramtosolvetheexamples.More
comprehensive accounts of Comsol Multiphysics are available for version 3.5a (Wilkes,
2006;Zimmerman,2008;DattaandRakesh,2010).
BASICCOMSOLMULTIPHYSICSTECHNIQUES
ThefirststepafteryouhaveinstalledComsolMultiphysicsistoopenit,thenchoosethepull-
downmenuOptions/Preferences.Clicktoshow“EquationView”andDiscretization,since
theseareusedfrequentlytoverifywhatequationyouaresolvingandwhatapproximation
youareusingforthedependentvariables.Ifyoudothis,theywillbeavailableeverytime
youopenComsolMultiphysics.
OpeningScreens
Figure D.1 shows the top, left of the opening screen of Comsol Multiphysics. Look at
the options across the top. The Model Builder is where you will define your problem; at
the start it has the title “Untitled,” but this will be replaced with the name you give the
problemwhenyousaveit.TotherightoftheModelBuilderistheModelWizard.Thisis
whereyoupickthedimensionsoftheproblem,fromnodimensions(ordinarydifferential
equations),to1D,2D,or3D,includingaxisymmetricproblems.Moreinformationabout
thesechoices isgiven below andintheexamples. Thesmall,rectangular boxand square
box in the Model Wizard part of the screen act in the same way as the same icons in the
ModelBuilder,namelytocontractorexpandthewindow.
TotherightoftheModelWizardistheGraphicswindow.Onitsright,orperhapsbelow
it,arethreeiconsthatrepresentMessages,Log,andResults(tables):seeFigureD.2.The
Logtabdisplaysinformationaboutthecalculationsastheyproceed;clickingontheResults
tabshowstablesthatyouhavecreated(seelater),andMessagestabgiveserrormessages,
FIGURE D.1 ComsolMultiphysicsopeningscreen,left.
```

---

## Стр. 345

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp4 JWBS084-Finlayson May18,2012 8:11 PrinterName:YettoCome Trim:7in×10in
APPENDIXD:HINTSWHENUSINGCOMSOLMULTIPHYSICS 337
FIGURE D.2 ComsolMultiphysicsopeningscreen,tabs.
forexample,whensomethingisamiss.IfyouwanttoexpandtheModelBuilder,Settings,
or Graphics windows to cover the screen, double-click on the tabs. Double-click the tab
againtoreversetheprocess.
As you use the various tabs, the screen may end up in a form you do not want. One
waytogetbacktheoriginalscreenistochooseOptions/DesktopLayout/andtheneither
“Widescreen Layout” (the three areas are across the screen from left to right), “Regular
ScreenLayout”(thefirsttwoareasareoneabovetheotherontheleftwhereastheGraphics
windowgoesfromtoptobottom),or“ResetDesktop.”
Equations
Tosolveaproblem,onebeginswiththeModelWizard.Choosethedimensions:0D,1D,1D
Axisymmetric,2D,2DAxisymmetric,or3D.ThenclickontherightarrowintheModel
Wizard. The next screen lists the options for models (see Figure D.3a). The main ones
are “Chemical Species Transport,” “Fluid Flow,” and “Heat Transfer.” Each of these has
additionaloptions,someofwhichareshowninFigureD.3b.Theavailableoptionsdepend
onyourlicense,buttheonesshowninFigureD.3barethosethatcomewiththeComsol
MultiphysicsandChemicalReactionEngineeringModule.Themorelimitedchoiceswith
only the basic Comsol Multiphysics are displayed in Figure D.3c. Find the equation you
want, click on the right arrow at the top of the Model Wizard, and choose Stationary or
“TimeDependent.”Thenclickonthefinishflag:youhavefinishedpickingthedifferential
equation!
TheModelLibrary(seethetabinFigureD.1)containsmodelsthathavealreadybeen
solved.YoucanopenthemandseebothcapabilitiesofComsolMultiphysicsandexamine
how the problem is set up. Examples setting up a problem are given in Chapters 8–11,
butheretheyaresummarizedwithafewmoreoptionsdisplayed.Basically,wearegoing
to work down the Model Builder window, opening options (called nodes) and acting on
them: “Model 1,” “Study 1,” Results. A heat transfer problem in two dimensions is used
asanexample.AfterchoosingintheModelWizard:2D,“HeatTransfer/HeatTransferin
Solids/Stationary”andthefinishflag,onehasthemenushowninFigureD.4(althoughthe
Model1willbeclosed;clickonthenodearrowtoopenit.)Notetheiconsatthetop,right
of the Model Builder panel. The second one from the left is to “show” additional things,
and we choose “Discretization” and “Equation View.” In the root node we can choose a
systemofdimensionsinthesettingswindow;forthe“UnitSystem”choose“none.”
SPECIFYTHEPROBLEMANDPARAMETERS
Westepthrough“Model1”inturn:Definitions,“Geometry1,”Materials,“HeatTransfer
(ht),”“Mesh1.”Ifweclickonheat_example,theninthesettingswindow,nearthebottom,
isaplacewecanchoosetheunitsfordatainput.ThedefaultunitsareSI.
```

---

## Стр. 346

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp4 JWBS084-Finlayson May18,2012 8:11 PrinterName:YettoCome Trim:7in×10in
338 APPENDIXD:HINTSWHENUSINGCOMSOLMULTIPHYSICS
FIGURE D.3 EquationoptionsfortheComsolMultiphysicswiththeChemicalReactionEngi-
neeringModule:(a)subjectareas,(b)chemicalspecies,fluidflow,heattransfer,(c)optionswithonly
ComsolMultiphysics.
```

---

## Стр. 347

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp4 JWBS084-Finlayson May18,2012 8:11 PrinterName:YettoCome Trim:7in×10in
APPENDIXD:HINTSWHENUSINGCOMSOLMULTIPHYSICS 339
FIGURE D.4 Modelchoicesforheattransferexample.
Physics
If you right click on Model 1, the following options are available: Add Physics, Mesh,
Delete,Rename,Properties,andDynamicHelp.Thefirstoneallowsyoutoaddasecond
equationtothemodel(notdoneinthisexample);thesecondoneallowsyoutoaddasecond
mesh so that you can solve the problem on two different meshes. The Properties option
allowsyoutoaddcommentsthatwillbesavedalongwiththemodel.Theotheroptionsare
self-explanatory.
Definitions
RightclickonDefinitionstoseetheoptionsthere;considertheVariables.Clickonitand
a table appears; you can define variables here, assign a number to them or define them
in terms of an equation you write. A variety of functions are supplied, but you can write
yourownusingthesameformatusedinExcelandMATLAB:+,–,∗,/,∧,andsoon.For
example, choose function step. In the settings window the default function step is a step
changelocatedatx=0goingfrom0to1withatransitionwidthof0.1.Theseparameters
canbechanged.Thenanywhereyouwanttousesuchafunction,youcanjustuseitsname
intheexpression.Theprobesareusefulforobtainingspecificresults,saythevalueofthe
solutionatapointinsidethedomainoralonganinternalline(seelater).Anumberofuseful
iconsareidentifiedinFigureD.5.
Geometry
RightclickonGeometry.Ifyouclickononeoftheshapes(rectangle,square,circle,etc.)
ascreenappearsthatallowsyoutodefinetheshapeandplaceitpreciselyinthegeometry.
Ifyouhavedefinedtwoshapes,anotheroptionappears:BooleanOperations.Thisoption
allowsyoutoaddorsubtracttheshapestocreateamorecomplicatedshape.Herearectangle
0.2×0.1misconstructed;thenchoosebuild.Next,defineacircleinsidewitharadiusof
0.01m,andbuild.NowifyourightclickonGeometrynewoptionsappear.TheBoolean
Operation“Difference,”withobjectstoaddR1and+,andobjectstosubtractC1and+,
andthenbuild,resultsinarectanglewithaholeinthemiddle.Inthisexample,thisisnot
donebecausewewanttohaveheatgenerationinthecircle,C1;seeFigureD.6.
```

---

## Стр. 348

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp4 JWBS084-Finlayson May18,2012 8:11 PrinterName:YettoCome Trim:7in×10in
340 APPENDIXD:HINTSWHENUSINGCOMSOLMULTIPHYSICS
FIGURE D.5 Icons: Show, Collapse, Expand Minimize, Maximize; Build, Plot, Expressions,
Export.
Materials
The Materials option allows you to import physical parameters of many compounds as
well as define some yourself. Right click on Materials and open the Materials Browser.
Listed there will be “Built-In” and “Liquids and Gases.” Most of the Build-In materi-
als are solids. If your simulation uses any of these materials, you can simply select it
(e.g., “Built-In/Aluminum,” “Liquids and Gases/Gases/Ethanol vapor,” and “Liquids and
Gases/Liquids/Ethanol”).Pickamaterialandrightclickitto“AddMaterialtoModel.”The
Settings will list the properties that are included, along with typical units. You may have
toaddsomeproperties,too.Thepropertiescanbefunctionsoftemperature(forliquids)or
temperatureandpressure(forgases).Besuretousetheunitsconsistentlythroughoutyour
model.Ifyouaresolvingaflowproblem,under“LaminarFlow”willbe“FluidProperties.”
Thesettingswindowindicates“frommaterial”;leavethatchoice.Youcanpickthetemper-
atureatwhichthepropertiesareevaluatedforanisothermalproblem.Toseethevalueofa
property,youcanrightclickonResults/DerivedValuesandchoosePointEvaluation;then
pickapointinyourdomainandadditintheSettingswindow,usetheExpressionsiconin
thesettingswindowtofindthepropertyyouwant,andclick=.Theanswerappearsinthe
table. You can also change to “user-defined” and specify the value yourself. You specify
unitsinbracketsandtheprogramconvertsthemtoaconsistentsetofunitsthatagreeswith
FIGURE D.6 Geometryforexample.
```

---

## Стр. 349

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp4 JWBS084-Finlayson May18,2012 8:11 PrinterName:YettoCome Trim:7in×10in
APPENDIXD:HINTSWHENUSINGCOMSOLMULTIPHYSICS 341
the Unit System you have chosen in the root node. For example, if you are using the SI
systembutdefineamaterialdensityas1[g/cm∧3];lookatthedensityatapointanditwill
belistedas1000(kg/m∧3).
Discretization
Clickon“HeatTransferinSolids.”Thegeometryisshownalongwithnumbersidentifying
differentpartsofit.Thosenumbersareusuallyinthebox,butiftheyarenotclickonan
objectandchoosethe+.Therearetwoothertabsthatareveryimportant.TheDiscretiza-
tion tab allows you to select the finite element approximation: linear, quadratic, or cubic
functionsdefinedontheelement.Usuallyweusequadraticfunctions.Thesearethedefault
values for temperature. For concentration, though, the default values are linear, and best
resultsareachievedinlaminarflowwithquadraticelements.Forflowintwo-dimensional
cases, use “P2 + P1,” which means the velocity is quadratic and the pressure is linear.
For flow in three dimensions, keep “P1 + P1,” the default. The Dependent Variables tab
identifiesthesymbolusedinthecomputertorepresentquantities,inthiscasethevalueis
T.YouwillnotseetheDiscretizationtabunlessyouhavechosenitundertheShowicon.
BoundaryConditions
OpentheHeatTransferoption:itshows“HeatTransferinSolids,”“ThermalInsulation,”and
“InitialValues.”Thefirstoneistheequationwechoseoriginally;theboundaryconditions
areautomaticallysettothermalinsulationuntilwechangethem.The“InitialValues”option
is provided in case the problem cannot be defined if a variable is zero, for example. In a
reactionrate,ifthetemperatureappearsas1/T,thenTobviouslycannotbezero.Inthatcase
onewouldputanothervalueheretobegintheiterations.Clickon“HeatTransferinSolids.”
MakesurethegeometricobjectswewantareintheSelectionbox;ifnotaddthem.Click
ontheEquationstab.Thentheequationwillbedisplayed;youneedthisforcheckingthe
signsofthingslikeheatsources,andsoon.Youmustalsospecifythethermalconductivity,
eitherbyhavingpickedamaterialintheMaterialsoptionorbychoosing“user-defined”and
insertingthevalue;hereitistakenas1W/mK.Sincethe“HeatTransferinSolids”equation
hastheoptionsofatranslationalvelocity,u ,itisnecessarytochoose“user-defined”for
trans
thedensityandheatcapacitybutthesecanbeleftaszeroforthisexample.
Gobackandrightclickon“HeatTransfer.”Shownareanumberofchoicesforboundary
conditions.Herewechooseinsulatedboundariesattheright-handsideandbottomandset
thetemperaturetozeroontheothertwoboundaries.Thus,choose“Temperature”;selectthe
left-handandtopboundaries,andchoose“+.”Setthevaluetozero.Ifyougobackandlook
at Thermal Insulation you will see that two boundaries have been marked “overridden”;
thosearetheoneswejustset.Wewanttohaveaheatsourceinthecircle.Rightclickon
“HeatTransfer,”choose“HeatSource.”Thenselectthecircle,“+”toaddittothebox.Set
thevalueto1000W/m3;thedimensionsaresetforaninfinitelylongcylinder.Itisuseful
toclicktheEquationtab,too,tocheckthesign.AlthoughSourceisprettydescriptivefor
heattransfer,Reactioninthemasstransferoptioncanbepositive(forproducts)ornegative
(forreagents).
Whenspecifyingboundaryconditions,therearesomebuilt-infunctionsthatareuseful.
Under“GlobalDefinitions”chooseFunctionstoseeavarietyofthem:step,ramp,rectangle,
andtrianglefunctionsaswellasMATLABfunctions.Thestepfunction,forexample,gives
youoptionsfordefiningaregionoverwhichthefunctionwillchange(narroworbroad),
```

---

## Стр. 350

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp4 JWBS084-Finlayson May18,2012 8:11 PrinterName:YettoCome Trim:7in×10in
342 APPENDIXD:HINTSWHENUSINGCOMSOLMULTIPHYSICS
FIGURE D.7 Meshforheattransferexample.
sincethevariablesarerepresentedbycontinuousfunctions.Asimplealternativeistouse
an expression such as 1∗(x < 0.5) + 0.5∗(x > 0.5) to have the function be 1.0 over the
regionx=0to0.5and0.5forlargerx.Butthestepfunctiongivesyoumorecontrolover
thespecification.
Mesh
Clickon“Mesh.”Thedefaultmeshisalways“normal.”Ifyouclickonthe“build”icon,a
meshisgeneratedautomatically.ThemeshisshowninFigureD.7.Keepinmindthatthe
meshessentiallydeterminestheaccuracyofthecalculations.Itisnecessaryforyoutogain
experience,andtodothatitisusefultosolvetheproblemonfinerandfinermeshestosee
ifthesolutionchanges.Itispossibletogobackto“Model1”andaddamesh.Thisisdone
andthe“finer”meshischosen,followedbybuild.
SOLVEANDEXAMINETHESOLUTION
Solve
The problem is solved next. Right click on “Study 1” and choose “= Compute.” If for
somereasonthereisanerror,itwillbelistedunder“Study1”(severallayersdown).Open
“Error”toseethecauseoftheerror.
Plot
The solution is shown in Figure D.8 using contour lines. Here the temperature contours
are all plotted in black, but they can be plotted in color with a scale showing, too. The
temperature can also be plotted with different colors representing different temperatures;
thetemperaturescaleisshownattheright.Thisiscalledasurfaceplot.Tomakechangesin
theplot,rightclickon“2DPlotGroup.”Youcangobackanddefineasecondmesh.Then
under“Study/Stationary,”select“Mesh2”andrightclick“Study1”,=.Thisprovidestwo
solutionswithdifferentdegreesofrefinement.
Suppose we want to find the total heat flux out of the circle. Choose “Results/Line
Integration,”rightclick“LineIntegration,”andselectthepiecesofthecircle:5,6,7,and
8; click “+” to add them to the box. To find the heat flux, click on “Expression +” and
choose heat transfer. There are about 30 variables listed, but some of them are not valid
```

---

## Стр. 351

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp4 JWBS084-Finlayson May18,2012 8:11 PrinterName:YettoCome Trim:7in×10in
APPENDIXD:HINTSWHENUSINGCOMSOLMULTIPHYSICS 343
FIGURE D.8 Solutiontoheattransferexample.
forthisproblem;choosetemperaturegradientmagnitude.Inthecomputerprogramthisis
calledht.gradTmag.Clickonthe“=”andlookattheresultstable.Thevalueis0.314574.
Dothisagain,butchooselines1and3(theleftandtop).Nowthevalueis0.313233.For
aperfectmassbalancetheseshouldbethesame,butthedifferenceis0.001341.Ifyougo
backandchoosea“finer”mesh,thediscrepancyis0.000864,andwith“extremelyfine”it
is0.000374.Thus,asthemeshisrefinedtheanswersgetbetterandbetter.Thereisalways
atrade-offbetweenhighaccuracyandthesolutiontime,butyouneedtobesurethemesh
you use provides sufficient accuracy for your purposes. You can see other variables that
canbeplotted.Thenclickon“replaceexpressions”(thetwogreenandorangearrows).A
longlistofvariablescanbefoundundertheheadings:definitions,heattransfer,geometry,
andmesh.
Ifyouwanttoplotthesolutionoranexpressionalongaboundary,chooseResults,right
click “1D Plot Group,” right click “Line Graph.” Then select the boundary, choose “+”
to add it to the box, define the expression and click the plot icon. The temperature along
the bottom is shown in Figure D.9. When you have more than one solution, you need to
identifyintheSettingswindowwhichsolutionyouwantplotted.Ifyouwanttoplotseveral
variablesonthesameplot,rightclick“1DPlotGroup,”thenrightclick“LineGraph”or
“PointGraph”foreachvariableyouwanttoplot.Ifyouwanttoplotavariablealongaline
ofa2Ddomain,definethe“CutLine2D”inResults/DataSet;thenchoosethatDataSet
inaLineGraph.
PublicationQualityFigures
Theplotscanbesavedinthreeformats:jpeg,bmp(bit-mapped),andpng(portablenetwork
graphics).Noneofthesearepublicationquality.Thus,thelineplotsinthisbookweremade
by exporting the data to a text file, which is imported into MATLAB. In MATLAB you
havetotalcontroloverthewaytheaxesandlegendsarelabeled(fontsize,boldornot,etc.)
Results
Whenyouevaluateanintegral,forexample,thenumericalresultwillappearintheResults
section the Graphics window. Be careful, though, because the size of the column may
be too small to include the exponent unless you expand it by dragging the border to the
right.Unfortunately,manysignificantdigitsaredisplayedunderthedefault“FullPrecision”
```

---

## Стр. 352

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp4 JWBS084-Finlayson May18,2012 8:11 PrinterName:YettoCome Trim:7in×10in
344 APPENDIXD:HINTSWHENUSINGCOMSOLMULTIPHYSICS
0.08
0.07
0.06
0.05
0.04
0.03
0.02
0.01
0
0 0.05 0.1 0.15 0.2
x
erutarepmeT
FIGURE D.9 Temperaturealongbottomboundaryinheattransferexample.
option,manymorethantheaccuracyofthefiniteelementmethodjustifies,andtheexponent
ismoreimportantthantheeighthorninthsignificantdigit.Toavoidthisproblem,clickon
thenumbericonwhenResultsisshowingandonlyfoursignificantdigitswillbedisplayed.
Probes
Ifonewantstoknowthevalueoftemperatureoranyexpressionataspecificpoint,right
click on Definitions, choose Probes and Domain Point Probes. Then indicate the x and y
locations you wish to use. After the solution is found, choose Results and right click on
“Derived Values.” Choose “Point Evaluation.” Then in the Settings window, change the
“DataSet”to“DomainPointProbe.”Choosethe“=”togetthevalueinthetable.Forx=
0.04andy=0.02,thevalueofT was0.0758.Alternatively,definethepointin“CutPoint
2D”inResults/DataSetandchooethatCutPoint2Din“DerivedValues/PointExpression.”
DataSets
If one wants to plot along a line that is not on the boundary, choose “Results/Data Set”
andrightclicktochoose“CutLine2D.”Inthesettingswindow,definethexandypoints
of the beginning and end of the line. Then choose Results, right click to get “Plot 1D
Group.”Openit,andrightclickandchoose“LineGraph.”Inthe“DataSet”use“CutLine
2D.” Click the plot icon to get the plot. If you want to integrate something along a line,
define “Cut Line 2D” the same way. Then use “Results/Derived Values” and right click
“LineIntegration.”Inthedatasetatthetopofthesettingswindow,choose“CutLine2D”
andthen“=.”TheanswerisintheResultsTable.Similarapproachesworkin1Dand3D
problems.In3Dyoucandefineadatasettobeaplaneandplotanexpressioninthatplane.
To define the plane, you can use “Quick” to select a plane perpendicular to a coordinate
axis or “General” to define a plane using three points with x, y, z values specified. In all
thesecasesyouneedtoselectthesolutionyouwanttoplotintheSettingswindow.
Thereareavarietyofoptionsforplotting.Iftheproblemisinthreedimensions,youcan
plot various expressions on surfaces, or in slices, and you can define 2D and 1D plots of
partofthesolution;usuallythisinvolvescreatingaDataSetfirst.Theexpressionsarrows
```

---

## Стр. 353

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp4 JWBS084-Finlayson May18,2012 8:11 PrinterName:YettoCome Trim:7in×10in
APPENDIXD:HINTSWHENUSINGCOMSOLMULTIPHYSICS 345
FIGURE D.10 Icons for graphics: zoom in, out, box, fill screen, view, take picture, minimize,
maximize.
(greenandorangearrows)allowyoutochoosevariousexpressionsthatarepredefinedin
ComsolMultiphysics.Forexample,inaheattransferproblem,theconductiveheatflux,x-
component,iscalledht.dfluxx,ht.dfluxy,ht.dfluxz.Thetemperaturegradientisht.gradTx,
ht.gradTy,ht.gradTz.Therearemanysuchentriesthatcanbeaccessedoncetheexpressions
arrowsareclicked.
Thereareanumberofoptionstochangehowtheplotislabeled.Oncetheplotappears,
lookatthetopGraphicswindow.Theiconsthere(showninFigureD.10)allowyoutomake
theplotbigger,smaller,usethecursortodragacrossthepartyouwouldliketoexpand,and
filltheGraphicsWindow.Clickthecamera,browse,selectthefolderyouwant,providea
name,save,andbackinthecamerawindowclickOK.Youcanrotateathree-dimensional
object,andtogetbacktothestandardview,clicktheiconthatlookslikeanaxis.Thisicon
hassubicons,too,thatviewtheobjectinxy,xz,yzviews.
ADVANCEDFEATURES
Mesh
Theaccuracyofthesolutionmaydependonthemesh,soitisworthwhiletounderstandsome
options when preparing the mesh. Consider first two-dimensional problems. If one right
clicks on the mesh node, several options are available: free triangular, free quadrilateral,
mapped,boundarylayer,andstatistics.Thefirsttwocoverthedomainwitheithertriangles
orquadrilaterals.Themappedmeshcausesthequadrilateralelementstofollowthegeometry
more. Choose the method you want, click build, and the mesh is created. If you want to
refineit,rightclickonrefine;thiswilldivideeachandeveryelement.Ifyouwanttorefine
themeshlocally,itispossibletodothatbyeitherrefiningtheedgesorcreatingadomain
that overlaps the solution domain. In the first case, before creating a domain, right click
meshandchooserefineedge.Pickanedgeoredgesandsetthemaximumelementsizeto
a small number. The edge will be divided, and that refinement will influence the domain
arounditwhenthewholedomainismeshed.Inthesecondcase,createadomainontopof
thegeometryandrefinejustthatdomain.StillanotheroptionistorightclickonMeshand
choose “Boundary Layers.” Under “Boundary Layer Properties” (open the arrow) select
theboundarieswhereyouwantboundarylayermeshestoappear,addthemtotheboxusing
the“+,”andbuild.
As an illustration of one of these methods, consider the microfluidic device shown
in Figure 11.4. If the Peclet number is large (here 2000 is used for illustration), only a
smallamountofmaterialwilldiffusesideways.Ifthemeshisregular(seeFigureD.11a),
the answer may look ragged and irregular, as seen in Figure D.11b. This is because the
elementsarenotsmallenough.IfonekeepsPe(cid:2)x≤2theoscillationswoulddisappear,
butthisisimpracticalforlargePecletnumber.However,inthisproblem,thesharpchange
in concentration is focused on a narrow band in the middle of the device. Thus, create a
domain that is 0.1 × 2.5 along the centerline. Then right click Mesh and choose “Free
triangular mesh” and build. Then choose “More operations/refine.” Choose the narrow
band, set the number of refinements to 2, and click build. The revised mesh is shown
```

---

## Стр. 354

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp4 JWBS084-Finlayson May18,2012 8:11 PrinterName:YettoCome Trim:7in×10in
346 APPENDIXD:HINTSWHENUSINGCOMSOLMULTIPHYSICS
(a)
(b)
FIGURE D.11 Regularmesh(a)andsolution(b),Pe=2000.
in Figure D.12a and the concentration contours are shown in Figure D.12b. Clearly, the
irregularities in Figure D.11b have gone away. The concentration profiles at the exit are
shown in Figure D.13 for the two cases. They are close to each other at the exit, but the
variancesareslightlydifferent(0.1979formesh11aand0.2043formesh11b).Remember
thatthehighestvarianceindicatingnomixingwhateveris0.25.Thistwo-dimensionalcase
is relatively easy, since you can use lots of elements, but in three-dimensional problems
thatmaynotbepractical.
TransfertoExcel
The solution and mesh can be written to a text file that can be entered into an Excel
spreadsheet or a word processor. Under “Results/Export” right click to get “Data 1” and
putinanexpression.Fortheoutput,Browseandputinafilenameandmovetothedesired
folder,thenchooseOK.BackintheDatawindow,clicktheexporticon(boxwitharight-
facingarrowatthetop)andatextfileismade.Thiscanbereadinanyprogramthatreads
```

---

## Стр. 355

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp4 JWBS084-Finlayson May18,2012 8:11 PrinterName:YettoCome Trim:7in×10in
APPENDIXD:HINTSWHENUSINGCOMSOLMULTIPHYSICS 347
(a)
(b)
FIGURE D.12 Refinedmesh(a)andsolution(b),Pe=2000.
text files, but it can also be opened, copied, and pasted into an Excel spreadsheet. If you
wanttodothiswiththemesh,rightclickon“Results/Export”andchooseMesh.Namethe
fileinasimilarmanner,butthistimeyouhaveachoiceofatextfileorabinaryfile(which
canbereadfasterifyouarereadingitinanothercomputationalprogram).Thisfilegives
the locations of the mesh points and element information (which mesh points are in an
element).OpenExcelandchooseImport.Thefilesaredelimitedwithspacesandcolumns
in the text file will go into columns in Excel. You can also do this using MATLAB. For
example,A=[thenpastethefile];youcanthencreatethecolumnsasa=A(:,1),b=A(:,2).
YoucandothesamethingwiththesolutionbychoosingResults/DataSetandchoosinga
Solution.Then“addtoExport”andpickthefiletype(.txt,.csv,.dat);saveitbyBrowsing
tosettheareaandthenusetheexporticon.
LiveLinkwithMATLAB
Ifyouhavealicensefor“ComsolLiveLinkTMforMATLAB”(partoftheComsolofferings)
and MATLAB, you can use MATLAB functions inside Comsol Multiphysics. To do so,
```

---

## Стр. 356

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp4 JWBS084-Finlayson May18,2012 8:11 PrinterName:YettoCome Trim:7in×10in
348 APPENDIXD:HINTSWHENUSINGCOMSOLMULTIPHYSICS
1
0.8
0.6
0.4
0.2
0
0.15 0.2 0.25 0.3 0.35
y
noitartnecnoC
meshd.12
meshd.11
FIGURE D.13 Outletconcentrationwithregularmeshandrefinedmesh.
firstopen“ComsolwithMATLAB.”Thefirsttimeyoudothisyouwillbeaskedtosupplya
usernameandpassword.Youcancreatethem-fileinMATLABorcreateitinatextfileand
save it as filename.m. Create your Comsol model, or open a previous model. Right click
“Global Definitions” and go to “Functions/MATLAB.” One window asks you to define
thefunctionbygivingitaname(e.g.,testfn)andidentifyingthearguments(e.g.,T).The
argumentscanbevariablesintheComsolmodel,andthefunctionnamecanthenbeused
elsewhereinthemodel.Also,youcangivethederivativebyspecifyingthesamefunction
name,thesamevariablename,andthederivativeofthefunctionwithrespecttothevariable.
Inthisexample,theMATLABfunctionis
%saved as testfn.m
function y=f(T)
y=T.*T
Theninthemodelyoucancallthefunctiontestfn(T)andtheMATLABproblemwill
be executed. Note that T (in a one-dimensional problem) is a vector of values at nodes,
sothenotationT∗Twouldnotwork;T.∗Tisneeded.Beforerunningthecode,besurethe
MATLABm-fileandtheComsolfileareinthesamedirectory;otherwisetheprogramwill
respondthatitcannotfindthefunction.
Infuturecalculations,youcanopenjustComsolMultiphysics;thelinkwithMATLAB
willbeestablishedwhenitseesthatthereisaMATLABfunctiondefined.Informationabout
LiveLinkwithMATLABisavailablein“ComsolLiveLinkTMforMATLAB”andExternal
MATLABfunctions.Thisconnectionismuchmorepowerfulthaninthissimpleexample.
You can build models, create geometries and meshes, and do a variety of operations,
includingloops,ifitismoreconvenienttodosoinMATLAB.
Variables
You can define these in either “Global Definitions” or Definitions under a model. But,
if you want to parameterize the solution, the parameters need to be identified in “Global
Definitions.”Thex-derivativeofthevariable“vary”isd(vary,x).
```

---

## Стр. 357

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp4 JWBS084-Finlayson May18,2012 8:11 PrinterName:YettoCome Trim:7in×10in
APPENDIXD:HINTSWHENUSINGCOMSOLMULTIPHYSICS 349
Animation
Tomakeamovie,choose“Results/Report”andrightclicktogetAnimation.Youcansaveit
asafileoropenitinyourbrowser.Usuallythisisdonewherethesolutionisplottedversus
time,andyoucanselectwhichtimevaluesyouwanttoincludeinthemovie.Nearthetop
of the Settings window is Subject with possible choices, such as “2D Plot Group.” Here
youpicktheoneyouwant,whichwassetbeforehandusingResultsandrightclickingon
oneofthe“PlotGroups.”Thus,whatyouplotisdeterminedinthe“PlotGroup,”whichyou
chooseintheAnimationsettings.Youhaveachoiceforoutputofthemovie:gif,flash,or
avi.TheaviformatonlycanbechosenifyouareusingWindows.Thenchoosetheexport
icon. The movie will appear in the graphics window, and a file will be saved, too. If you
select“OpeninBrowser,”yourbrowserwillbeopenedandtheplotwilloccurthereover
anover.Bothgifandflashformatwillruninyourbrowser(onaMacintosh,too),andgif
willruninQuickTimePlayeronaMacintosh.
Studies
When you right click on the name of your problem (root) one option is to “Add Study.”
Suppose you want to compare the solution obtained by using two different meshes (or
eventwodifferentmodels).Tocomparethesolutionbyusingtwodifferentmeshes,inthe
Model, right click and add a mesh; now there is a “Mesh 1” and “Mesh 2.” In the first
Study,whenyouopenStationary,forexample,inSettings,“Mesh1”ischosenbydefault.
Now you could solve the problem on this mesh (“Study 1,” right click =), get the figure
orresults,savethem,thengobackandchangeto“Mesh2”andsolvetheproblemagain.
This time the second mesh would be used. But if you want to quickly go back and forth
betweenthesolutions,andtheirplots,gotothe“Study2”andchoose“Mesh2”forit.Then
solve the problem (“Study 2,” right click =). Then in Results, create two “Plot Groups,”
define the plot, but in one of them choose the data set: “Solution 1” and in the other one
choosethedataset:“Solution2”(orsimilarones).Clickontheploticontoseetheplotof
each.Ifyouclickonnodesinthe“ModelBuilder/Results,”youcanseefirstoneandthen
the other. You can do the same thing with “Derived Results.” For a transient problem, to
plotthevalueofthesolutionatapointforalltime,definethepointasaboveandchoose
“CutPoint2D”in1DPlotGroup.Foratransientproblemthetimevariablewillalreadybe
chosen. To plot the solution along a line for several time values, define the line as above
andchoose“CutLine2D”inthe1DPlotGroup.Toevaluateanintegralofanexpression,
chooseResults/DerivedValue/AverageorIntegration.Clickingtheequalsigncausesatable
ofvaluestobedisplayedunderResults,andthisTablecanbeplottedina1DPlotGroup
by choosing Table Graph. This can also be done by choosing Definitions/Domain Probe
andchoosingtheintegralofanexpression,calleddom1.TheninResults/1DPlotGroup,
chooseGlobalandtheexpressiondom1.
HelpwithConvergence
Ifanon-linearproblemdoesnotconverge,tryputtingagoodguessin“Initialconditions.”
Alsoclickonthequestionmark,type“convergence,”andlookat“AchievingConvergence
whenSolvingNonlinearEquations.”
```

---

## Стр. 358

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp4 JWBS084-Finlayson May18,2012 8:11 PrinterName:YettoCome Trim:7in×10in
350 APPENDIXD:HINTSWHENUSINGCOMSOLMULTIPHYSICS
HelpwithTime-DependentProblems
Implicitmethodsareusedtosolvetime-dependentproblems.Thisgenerallyinvolvessolve
alinearalgebraproblem,Ax=b,ateachiteration.Inanonlinearproblem,theproblemis
linearized about the current iterative solution, which requires evaluating the derivative of
theequationswithrespecttoeachvariable.TheresultiscalledtheJacobian.Itispossible
to speed things up by evaluating the Jacobian only every few iterations, since this takes
considerable time, but when doing so the iterations may not converge. Thus, you have
the option to control some of the time integration methods. To do so, click on “Study
1/SolverConfigurations/Solver1/Time-DependentSolver1.”ThenyoucanchooseDirect,
Advanced,FullyCoupled,andDirect.Clickononeofthemandthedynamichelpicon(looks
likealaptop)toseetheoptions.Generallyforanonlinearproblem,thetimeintegrationis
morerobustwhenchoosing“FullyCoupled,”“JacobianUpdate”everyiteration,allowing
severaliterations,andpossiblyincreasingthetolerancefactor.Ofcourse,itissometimes
best todecrease the tolerance factor tomake surethe solutionis good, since once itgets
off,itmaybehavebadly.Thereareotheroptionsassociatedwithsolvingthelinearalgebra
problem, and these involve how the problem is solved, how it incorporates the sparsity
of the matrix (zeros), and perhaps it will be solved iteratively even for a linear problem
tokeepthememoryrequirementssmall.Consequently,youmayneedtoexperimentwith
thesetoolstogetthebestperformanceforyourproblem.
JumpDiscontinuity
To illustrate how to program a jump discontinuity in Comsol Multiphysics, consider the
followingproblem:
d2c d2n
=0, 0< x <1; =−10n, 1< x <2
dx2 dx2
(cid:2) (cid:2) (cid:2) (D.1)
(cid:2) (cid:2) (cid:2)
c(0)=1,
dc(cid:2)
(cid:2)
=
dn(cid:2)
(cid:2)
, n(1)=
c(1)
,
dn(cid:2)
(cid:2)
=0
dx dx 1+10∗c(1) dx
x=1 x=1 x=2
Thereisdiffusionintheleftregionanddiffusionandreactionintherightregion.Setthe
diffusivityto1.0forbothproblems.Besuretounclickconvectionifitisclickedatthestart.
Attheinterfacethefluxiscontinuousbutthevalueofnatx=1isanonlinearfunctionof
thevalueofcatthesamepoint.OpenComsolMultiphysicsandcreatethetwoproblems
usingTransportmoduleasModel1andModel2.Toconnectthemodels,inModel2,open
Linear Extrusion and set the left point in Model 2 to be identified with the right point in
Model1(identifiedbytheGeometry1and2).TheninModel1,createavariableflux=
mod2.linext1(mod2.c2x).InModel1,fortheright-handboundary,setthevalueoftheflux
tothisvariableflux.InModel1,openLinearExtrusionandsettherightpointinModel1
tobeidentifiedwiththeleftpointinModel2(againidentifiedbytheGeometry1and2).In
Model 2 define the variable cb=mod1.linext2(mod1.c). Also define nofc=cb/(1+10∗cb).
TheninModel2,settheconcentrationontheleftpointtonofc.EliminateStudy2andonly
useStudy1solvingModel1and2.ThesolutionsareshowninFigureD.14.Thevaluesof
candnobeytheequilibriumconstraintattheinnerboundaryandthefluxesarecontinuous
acrossthatboundary.Thefluxescanbeplotted,too,togettheirvalues.
```

---

## Стр. 359

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp4 JWBS084-Finlayson May18,2012 8:11 PrinterName:YettoCome Trim:7in×10in
APPENDIXD:HINTSWHENUSINGCOMSOLMULTIPHYSICS 351
1
0.8
0.6
0.4
0.2
0
0 0.5 1 1.5 2
x
noitartnecnoC
c
n
FIGURE D.14 Solutionwithajumpdiscontinuity.
TABLED.1 SelectedModelLibraryProblemsandTechniquesinComsolMultiphysics
ChemicalEngineering
Surfacediffusionandsurfacereaction
Tubularreactor;weakformandboundaryinterface
FluidDynamics
Time-dependentsolutionofafallingsandparticle
Micromixer
Sloshing_tank;movingmesh,freesurfaceflow
Multiphysics
Free_convection
Marangoni_convection;heatedfromside;howtoincludesurfacetensioninBC
Help
When you are stuck figuring out a command, or node, click on it and then click the
questionmark.Awindowwillappearwithinformationaboutthatspecificcommand.The
informationmaybetoogeneral,tellingyouwhatitdoes,butnothowtouseit,butthatat
leastisastart.
Another source of help is the collection of problems in the Model Library. This is
accessedbychangingfromSettingstoModelLibraryinthemiddlewindow.TableD.1lists
somekeyproblemsandtechniques.
APPLICATIONSOFCOMSOLMULTIPHYSICS
ThisComsolMultiphysicsoptionsdescribedinthisAppendixmerelytouchthesurfaceof
possibilities.Additionalexamplesandapplicationsareprovidedthroughoutthebook,and
specialtechniquesarelistedhere:
```

---

## Стр. 360

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp4 JWBS084-Finlayson May18,2012 8:11 PrinterName:YettoCome Trim:7in×10in
352 APPENDIXD:HINTSWHENUSINGCOMSOLMULTIPHYSICS
(cid:2)
Solving ordinary differential equations that are initial value problems, Chapter 8,
p.149
(cid:2)
Solvingordinarydifferentialequationsthatareboundaryvalueproblems,Chapter9.
(cid:2)
IconsinComsolMultiphysics,Chapter9,p.183–184
(cid:2)
Parametricsolutions,Chapter9,p.188
(cid:2)
Useofdefinedvariables,Chapter9,p.193,203,Chapter10,p.228
(cid:2)
EffectofP1andP2elements,Figure9.13
(cid:2)
Problemswithstrongconvection,Chapter9,p.201,Chapter11,p.267,278,280
(cid:2)
Integrationincylindricalgeometry,Chapter9,p.192
(cid:2)
Viscousdissipation,Chapter11,p.271
(cid:2)
Wallreactions,Chapter11,p.274
(cid:2)
Modelcouplings,Chapter10,p.248
```

---

## Стр. 361

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
E
APPENDIX
MATHEMATICAL METHODS
ThesoftwarepackagesExcel®,MATLAB®,AspenPlus®,andComsolMultiphysics®use
mathematicalmethodsthatarepreprogrammed.Engineerscansolvechemicalengineering
problems without knowing the details of those mathematical methods, but some of you
may be interested in the methods themselves. A brief overview is given here. There are
numerous books that describe the methods in greater detail, including Finlayson (1980,
1992),ConstantinidesandMostoufi(1999),andCutlipandShacham(1999),aswellasthe
Mathematics Section of Perry’s Chemical Engineers’ Handbook (Finlayson and Biegler,
2008) and Ullmann’s Encyclopedia of Industrial Chemistry (Finlayson, 2006). The sub-
jectsinclude
(cid:2)
Nonlinearalgebraicequations.
(cid:2)
Ordinarydifferentialequationsasinitialvalueproblems.
(cid:2)
Ordinarydifferentialequationsasboundaryvalueproblems.
(cid:2)
Partialdifferentialequationsintimeandonespacedimension.
(cid:2)
Partial differential equations in two or more spatial dimensions (and possibly time,
too).
In the case of differential equations, we are always replacing the differential equa-
tion with a finite approximation, with a finite number of grid points or elements, and it
is always necessary to assess the accuracy by solving the problem with more than one
mesh,oratleastcomparingintegralbalances,likeflowinversusflowout.Theseconsid-
erations are emphasized by the discussion in this Appendix as well as several problems
inChapters8–11.
IntroductiontoChemicalEngineeringComputing,SecondEdition.BruceA.Finlayson.
©2012JohnWiley&Sons,Inc.Published2012byJohnWiley&Sons,Inc.
353
```

---

## Стр. 362

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
354 APPENDIXE:MATHEMATICALMETHODS
ALGEBRAICEQUATIONS
Asinglenonlinearalgebraicequationcanbewrittenas
f(x)=0 (E.1)
Iterativemethodsareusedtosolvesuchequations,andthesuccessivesubstitutionand
Newton–Raphsonmethodsaredescribedhere.Letxk bethevalueofxatthekthiteration.
ThegoalistomakexksatisfyEq.(E.1)askincreases.
SuccessiveSubstitution
Inthismethod,theequationismultipliedbyaconstant,β,andaniterativeequationisused:
xk+1 = xk +βf(xk) (E.2)
Undercertainconditions,itcanbeprovedthatthismethodconverges(Finlayson,1980).
The conditions require a bounded derivative df/dx and also a particular sign of β. The
smallerthevalueofβthesloweristheconvergencetothesolution,butalsothenitismore
likelythatasolutioncanbefound.Itissometimeshardtopredictagoodvalueofβ.
Newton–Raphson
Inthismethod,aTaylorseriesiswrittenforEq.(E.1),evaluatedatthexkvalue:
(cid:2) (cid:2)
f(xk+1)= f(xk)+ df (cid:2) (cid:2) (cid:2) (xk+1−xk)+ d2f (cid:2) (cid:2) (cid:2) (xk+1−xk)2 +··· (E.3)
dx dx2 2!
xk xk
The terms higher than linear in xk+1 – xk are discarded, and the left-hand side is set
to zero. You want the left-hand side to be zero, of course, and when you are close to the
solutionthehigherordertermsaresmall.Theiterationsthenproceedasfollows:
f(xk)
xk+1 = xk − (E.4)
df/dx|
xk
Convergenceproofsareavailableundercertainconditions(Finlayson,1980),andonce
the iterate value gets close to the solution, the convergence is very rapid. This method
is generally better than the successive substitution method, except for special cases, but
sometimesagoodinitialguessisrequired.
TheNewton–Raphsonmethodcanbeextendedtosetsofnonlinearequations.Whenthe
equationsare
f ({x })=0,i, j =1,...,n (E.5)
i j
theexpansionis
(cid:2)
f i ({xk+1})= f i ({xk})+ (cid:3)n ∂ ∂ x f i (cid:2) (cid:2) (cid:2) (xk j +1−xk j )+··· (E.6)
j=1 j xk
```

---

## Стр. 363

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXE:MATHEMATICALMETHODS 355
You set the left-hand side to zero, neglect the second order and higher terms, and
rearrangetheequationsas
(cid:2)
(cid:3)n ∂ ∂ x f i (cid:2) (cid:2) (cid:2) (xk j +1−xk j )=−f i ({xk}) (E.7)
j=1 j xk
Thisisalinearproblem,whichcanbewrittenintheform
(cid:2)
(cid:3)n A i k j (xk j +1−xk j )=−f i ({xk}),A i k j = ∂ ∂ x f i (cid:2) (cid:2) (cid:2) (E.8)
j=1 j xk
This problem is now a set of linear equations, which is easily solved. The matrix A
is called the Jacobian. Linear algebra is used to solve this set of equations (Finlayson,
1980,2003):
Ak(xk+1−xk)=−fk,xk+1 =xk −(Ak) −1fk (E.9)
Aftereachstep,theJacobianandfunctionf arereevaluatedandtheprocedureisrepeated.
TheNewton–Raphsonmethodforsetsofequationsalsoconvergesquicklyonceoneisclose
tothesolution,butiterationscaneasilydivergeunlessspecialprecautionsaretaken.The
programsusedinthisbooktakethoseprecautions,whichmakesthemmorereliablethan
programsyoumightwriteyourself.ProblemsthataskyoutoprogramtheNewton–Raphson
methodinclude2.10,2.11,3.16,3.17,4.15,4.16,and8.21.
TheNewton–Raphsonmethodrequiresthatyoudifferentiatethefunctionwithrespect
toallthevariables.Thesecantmethodavoidsthatmathematicalstepandusesanumerical
differencetocalculatethederivative:
(cid:2)
∂f
i
(cid:2)
(cid:2) (cid:2) =
f
i
(xk
j
)− f
i
(xk
j
−1)
(E.10)
∂x
j xk
xk
j
−xk
j
−1
Thevalueofthefunctionsiskeptaftereachiterationinordertomakethiscalculation.The
Wegsteinmethodisessentiallyasecantmethod,withsomeconstraintsontheparameters
asdescribedinChapter7.Itisalsopossibletouseanumericalderivative:
(cid:2)
∂f
i
(cid:2)
(cid:2) (cid:2) =
f
i
(xk
j
+ε)− f
i
(xk
j
)
(E.11)
∂x ε
j xk
OneoftheadvantagesofComsolMultiphysicsisthatitdifferentiatestheequationssym-
bolically,includinganytermsthatyouaddtotheproblem,andthisenhancesconvergence.
The parametric solver in Comsol Multiphysics is possible because the Newton–Raphson
methodisbeingused.ConsiderEq.(E.1)whenitdependsuponaparameter:
f(x(α),α)=0 (E.12)
DifferentiateEq.(E.12)withrespecttoα:
(cid:2) (cid:2)
∂f (cid:2) (cid:2) (cid:2) dx + ∂f (cid:2) (cid:2) (cid:2) =0 (E.13)
∂x dα ∂α
α x
```

---

## Стр. 364

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
356 APPENDIXE:MATHEMATICALMETHODS
OncethesolutiontoEq.(E.12)isknown,itiseasytofindthederivativeofthesolution
withrespecttotheparameter.Becausethematrixinverseisalreadyknown,thiscalculation
isfast.[Actually,anLUdecompositionwouldbedoneratherthananinverse,asitistwice
asfast.SeeFinlayson(1980)andthebookwebsite.]Whenchangingtheparameter,alinear
extrapolationaboutthecurrentsolutionisthenpossible:
dx
x(α+(cid:6)α)= x(α)+ (cid:6)α (E.14)
dα
Thisoftengivesanexcellentguessofthesolutionforthenextvalueofα.Sometimes
eventhesemethodsdonotsolvetheveryhardestproblems.Inthatcase,ahomotopymethod
maybenecessary(Finlayson,etal.2006).
ORDINARYDIFFERENTIALEQUATIONSASINITIALVALUEPROBLEMS
There are excellent methods for solving sets of first-order ordinary differential equations
thatareinitialvalueproblems(ODE-IVP).AnexampleofanODE-IVPis
dy
= f(t,y),y(0)= y (E.15)
0
dt
Notethatalltheconditionsareknownatonetime,t=0.Thusitispossibletocalculate
thefunctionontheright-handsideatt=0togetthederivativethere.Thismakesthesetof
equationsinitialvalueproblems.Theequationsareordinarydifferentialequationsbecause
there is only one independent variable. Any higher-order ordinary differential equation
canbeturnedintoasetoffirst-orderordinarydifferentialequations;theyareinitialvalue
problems if all the conditions are known at the same value of the independent variable
(Finlayson, 1980, 2008, pp. 3 and 48–51; Finlayson, et al. 2006,, vol. B1, pp. 47–59].
Themethodsforinitialvalueproblemsareexplainedhereforasingleequation;extension
tomultipleequationsisstraightforward.Thesemethodsareusedwhensolvingplug-flow
reactors(Chapter8)aswellastime-dependenttransportproblems(Chapters9–11).
Euler’sMethod
InnumericalsolutionsofODE-IVP,thesolutionyatthepointtn isrepresentedbyyn.The
simplest method is Euler’s method, which is obtained by writing a difference expression
forthederivative:
yn+1−yn
= f(tn,yn) (E.16)
(cid:6)t
Thefirst-orderapproximationofthederivativeisnotveryaccurate,sothatthismethod
isnotveryaccurateeither.Itiseasytoprogram,though.RearrangeEq.(E.16)as
yn+1 = yn +(cid:6)tf(tn,yn) (E.17)
Thisequationcanbeappliedrepeatedlytogofromt=0toanytime,t.Thiscanbedone
easilyinMicrosoftExcel.Tosolve
dy
=−y,y(0)=1 (E.18)
dt
```

---

## Стр. 365

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXE:MATHEMATICALMETHODS 357
putthetimestepincellE2;letcolumnAbethetime,columnBthey,andcolumnCthe
firstderivative,dy/dt.Thecellsrepresentingdy/dtarecalculatedusing–yinthesamerow
andputincolumnC:C2=–B2.Thenthevalueofyinthenextrowistakenas
B3:=B2+$E$2 ∗ C2. (E.19)
whichistheequivalentofEq.(E.17).
ThestabilitylimitfortheEulermethodappliedto
dy
=−λy (E.20)
dt
isλ(cid:6)t ≤2(Finlayson,1980).Forotherproblems,dy/dt=f(y,t),itis
(cid:2) (cid:2)
(cid:2) (cid:2)
(cid:2) (cid:2) λ df (cid:2) (cid:2) ≤2 (E.21)
dy
ForsystemstheλistheabsolutevalueofthelargesteigenvalueoftheJacobian,∂f /∂y ,
i j
assumingalleigenvaluesarenegative.
TherearethreemajorproblemsfortheEulermethod.First,theaccuracyispoor,since
the method is based upon Eq. (E.16) in which only a first-order difference expression is
used.Theerrorsinthemethodareproportionalto(cid:6)t.Second,stabilityisdifficulttoachieve
formanyproblems.TheonlywaytohaveastableEulermethodistouseasmallenough
time step-size, but you may not know what value is sufficient. Furthermore, a value that
issufficientatthebeginningmaynotbesufficientlateron,anditmaytakeanexcessively
longtimetofinishthecomputation.Third,tovalidatetheresultsitisnecessarytosolvethe
problematleasttwice,withdifferenttime-steps.Themethodcan,however,beprogrammed
inExcel,andproblems8.19and8.20usethismethod.
Runge–KuttaMethods
TheEulermethodcanbeimprovedbydoingthecalculationintwosteps:
(cid:6)t
y¯ = yn + f(tn,yn)
2
(cid:4) (cid:5) (E.22)
(cid:6)t
yn+1 = yn +(cid:6)tf tn + ,y¯
2
This is a second-order Runge–Kutta method (Finlayson, 1980), sometimes called the
mid-point rule. The first step is an approximation of the solution halfway between the
beginningandendingtime,andthesecondstepevaluatestheright-handsideatthatmid-
point.Theerrorgoesas((cid:6)t)2,whichismuchsmallerthanachievedwiththeEulermethod.
Thesecond-orderRunge–Kuttamethods(thereareseveral)alsohaveastabilitylimitation.
Problem 8.22 requires programming the Runge–Kutta method, and the results can be
compared with those of 8.19 which use the Euler method. The stability limit for this
methodisalsoλ(cid:6)t ≤2.
MATLABandode45andode15s
The method used in MATLAB is a fourth-order Runge–Kutta method with a vari-
able step-size. The (cid:6)t is changed to guarantee the accuracy of the calculation. The
```

---

## Стр. 366

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
358 APPENDIXE:MATHEMATICALMETHODS
accuracy is estimated each step, and the step-size is reduced to meet the specified ac-
curacy. The method still has a stability limitation. The variable step size overcomes two
of the problems—knowing what step size to use and using a small enough step-size to
guaranteeaspecifiedaccuracy.Thismakesthemethodveryrobust,whichiswhyitisthe
workhorse in MATLAB. The method is called ode45 because the fourth-order method is
choseninsuchawaythatitachievesfifth-orderaccuracy.Itisbasedonanolderprogram
called RKF45 that was written by Boeing Computer Services many decades ago. More
detailscanbefoundinFinlaysonetal.(2008,pp.3–49)andFinlaysonetal.(2006,vol.B1,
pp.1–49,60–61)andthebookwebsite.Thestabilitylimitofthismethodisλ(cid:6)t ≤2.8.
Insomeproblems,certainparametersvaryquicklyandothersvarymoreslowly.Forex-
ample,inpacked-bedchemicalreactors,theconcentrationcanchangequicklyintime,but
thetemperaturewillnotchangerapidlybecauseofthelargeheatcapacityofthesolid.Such
problemsarecalled“stiff.”ThemathematicaldefinitionisthattheeigenvaluesoftheJaco-
bianarewidelyseparated,certainlybyfactorsofthousands,perhapsbyfactorsofmillions.
It turns out that the stable step size of an explicit method is limited by the largest eigen-
value(fastestrespondingvariable),butthetimeforsomethingtohappeniscontrolledby
thesmallesteigenvalue(slowestrespondingvariable).Thus,forstiffproblems,manytime
stepswouldneedtobetakenwithasmalltimestep,andthecalculationswouldbeveryslow.
Implicitmethodshavebeendevelopedtoovercomethisproblem.TheBackwardEuler
methodis
yn+1−yn
= f(tn+1,yn+1), or yn+1−(cid:6)tf(tn+1,yn+1)= yn (E.23)
(cid:6)t
Thismethodisstillfirstorder,butitisstableforanystepsize.Theonlyproblemisthat
Eq. (E.23) is a nonlinear algebraic equation for yn+1, and if there are several differential
equations,therewillbeasetofnonlinearalgebraicequationstobesolved.Thisisnotaneasy
task.Somehigherordermethodsarestable,too;thebestareGear’sbackwarddifference
formulas (Gear, 1971; Finlayson et al., 2008, pp. 3–49) and the book website. Methods
suchasthesearealsoincludedinMATLAB,asode15sandode23s.Theseprogramsadjust
thestep-sizetomaintainaspecifiedaccuracy.Theyalsousesophisticatedmethodstosolve
thesetofnonlinearequations.Ifasolutioncannotbefound,thestep-sizeisreduced;then
asolutioniseasiertofind.
Itisalsopossibletohavedifferential–algebraicequations.Therewillbebothdifferential
andalgebraicequations,withallthevariablespossiblyoccurringinalltheequations.This
essentiallymeansthatthevariablesdeterminedfromthealgebraicequationsareactingin-
finitelyfast;thisismerelyasystemofstiffequationstakentoanextreme.Specialmethods
existfortheseproblems,too.Becausesomeofthevariablesaresupposedtochangeimme-
diately,theycannotbeincludedintheerrortestsusedtoselectthetimestep.Informationis
availablebyusingthehelpmenu,MATLAB/User’sGuide/Mathematics/Calculus/Ordinary
DifferentialEquations/InitialValueProblems/Differential–AlgebraicEquations.
ORDINARYDIFFERENTIALEQUATIONSASBOUNDARY
VALUEPROBLEMS
Transportproblemsinvolvesecond-orderdifferentialequations.Althoughasinglesecond-
order differential equation can be reduced to two first-order differential equations, the
problem is not an initial value problem because there are boundary conditions at two
different values of the independent variable. This section describes methods for solving
```

---

## Стр. 367

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXE:MATHEMATICALMETHODS 359
such problems and illustrates them with the finite difference method as well as the finite
elementmethod.
The prototype problem is heat conduction in a slab or reaction and diffusion in a flat
layer, as described in Chapter 9. Here, the methods are demonstrated on a problem with
reactionanddiffusioninaflatlayerwithafirst-orderchemicalreaction:
d2c dc
D =kc,withboundaryconditions (0)=0,c(R)=c (E.24)
dx2 dx 0
FiniteDifferenceMethod
This method is explained first because it is the oldest and the simplest to explain, even
thoughitisnotthemethodembeddedinComsolMultiphysics.Thefirststepistodivide
thespatialregionintosmallerregionsbyplacinggridpointsontheline(seeFigureE.1).
Here, the grid points are evenly spaced; although this is not necessary, it does make the
presentationeasiertograsp.Theunknownfunctiony(x)isexpandedinaTaylorseriesabout
the(unknown)valueatagridpoint:
(cid:2) (cid:2)
y(x)= y(x i )+ d dx y (cid:2) (cid:2) (cid:2) (x −x i )+ d d 2 x y 2 (cid:2) (cid:2) (cid:2) (x − 2! x i )2 +··· (E.25)
i i
Thisequationisevaluatedforpointsoneitherside:
(cid:2) (cid:2)
y(x i+1 )= y(x i )+ d dx y (cid:2) (cid:2) (cid:2) (x i+1 −x i )+ d d 2 x y 2 (cid:2) (cid:2) (cid:2) (x i+1 2 − ! x i )2 +···
(cid:2)i (cid:2)i
(E.26)
y(x i−1 )= y(x i )+ d dx y (cid:2) (cid:2) (cid:2) (x i−1 −x i )+ d d 2 x y 2 (cid:2) (cid:2) (cid:2) (x i−1 2 − ! x i )2 +···
i i
If the last two equations are subtracted and rearranged; you can obtain the following
approximationforthefirstderivativewhenthegridspacingisuniform:
(cid:2)
d dx y (cid:2) (cid:2) (cid:2) = y(x i+1 ) 2(cid:6) − x y(x i−1 ) when(cid:6)x =(x i+1 −x i )=−(x i−1 −x i ) (E.27)
i
This equation is second order, meaning that the errors decrease proportional to (cid:6)x2
once (cid:6)x is small enough. The two equations can also be rearranged by neglecting the
second-orderterms,toobtaintwootherapproximationsforthefirstderivative:
(cid:2)
dy (cid:2) (cid:2) = y(x i+1 )−y(x i )
(cid:2)
dx (cid:6)x
(cid:2)i
(E.28)
dy (cid:2) (cid:2) = y(x i )−y(x i−1 )
(cid:2)
dx (cid:6)x
i
i = 1 2 3 4 n n + 1
y y y y y y
1 2 3 4 n n+1
FIGURE E.1 Finitedifferencegrid.
```

---

## Стр. 368

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
360 APPENDIXE:MATHEMATICALMETHODS
Theseapproximationsareonlyfirstorder,anderrorsareproportionalto(cid:6)xwhenitis
small enough. Another rearrangement gives an approximation for the second derivative.
TakethesumofEq.(E.26)andrearrangeittogive
(cid:2)
d2y (cid:2) (cid:2) (cid:2) = y(x i+1 )−2y(x i )+y(x i−1 ) (E.29)
dx2 (cid:6)x2
i
Thisapproximationcanbeshowntobesecondorderin(cid:6)x.
The idea in the finite difference method is that the differential equation, valid for all
positions x, is replaced by a set of equations representing the equation only at the grid
points, using the equations derived above. Thus, for problem Eq. (E.24), the equation at
gridpointiis
D c i+1 −2c i +c i−1 =kc ,wherec =c(x ) (E.30)
(cid:6)x2 i i i
Such an equation is written for each interior grid point shown in Figure E.1. At the
boundaries,thefinitedifferencemethodusestheboundaryconditions,againwiththefinite
differencerepresentationofderivatives:
(cid:2)
d d x c (cid:2) (cid:2) (cid:2) = c(x 2 ) (cid:6) − x c(x 1 ) ,c n+1 =1 (E.31)
1
It is possible to use a more accurate (second order) derivative, at the cost of extra
programming. Equations (E.30) and (E.31) represent a set of n + 1 algebraic equations
in n + 1 unknowns. The most accurate way to apply the boundary condition at x = 0 in
Eq.(E.24)istointroduceafalseboundarypointatx=–(cid:6)x;callthevaluetherec .The
0
differentialequationatx=0,point1,isthen
c −2c +c
D 2 1 0 =kc (E.32)
(cid:6)x2 1
Butbytheboundaryconditionatx=0,
c −c
2 0 =0, or c =c (E.33)
2(cid:6)x 2 0
Thusthedifferentialequationbecomes
2(c −c )
D 2 1 =kc (E.34)
(cid:6)x2 1
ThismustbeprogrammedseparatelyfromEq.(E.30).
IfyouareusingMATLAB,youcanuselinearalgebratosolvethesetofequations.For
this simple, one-dimensional problem, a special method is used for a tridiagonal matrix.
SeeFinlayson(1980)forcompletedetails.
FiniteDifferenceMethodinExcel
It is possible to program the finite difference method in Excel and use the “Calculation”
featuretohandlethecircularreference.Turnofftheiteration,preparethespreadsheet,and
thenturnthecalculationbackon.Whetherthisconvergesdependsontheinitialguess.
```

---

## Стр. 369

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXE:MATHEMATICALMETHODS 361
TABLEE.1 FiniteDifferenceMethod
inExcelforBoundaryValueProblems
D1 E1 F1
c i−1 c i c i+1
Toseehowthisisdone,rearrangeEq.(E.30)tothefollowingform:
c = c i+1 +c i−1 (E.35)
i 2+k(cid:6)x2/D
Identify the cells in the spreadsheet with the value of concentration at a node, i, as
showninTableE.1.Putthevalueofk(cid:6)x2/D incellA2.TheequationforcellE1would
bedifferent:
=(D1+F1)/(2+$A$2) (E.36)
Next, copy this equation over a series of cells that correspond to the number of grid
points. For the first and last cell (grid point) use a different equation, appropriate to the
boundarycondition.Thenturnontheiterationfeaturetogetthesolution.
Thenextstepistoresolvetheproblemusingmoregridpoints,andasmaller(cid:6)x.This
means you have to program the spreadsheet again, but it does give you an indication if
theanswerchangesmuchasthemeshisrefined,whichiswhatassuresyouthatyouhave
solvedtheproblemaccuratelyenough.Problems9.30(linearandnonlinearproblems)and
9.31,employthismethod.
Afterthelinearalgebraproblemissolved,theresultisanapproximationfory(x)ateach
i
ith grid point. This can be plotted, and the points can be joined by straight lines, giving
an approximation to the solution of the differential equation. More elaborate methods of
interpolationarealsopossible.Thesolutiontothefinitedifferenceequations,though,isan
approximationtothesolutiontothedifferentialequation.Toassessitsaccuracy,youmust
refinethegridandsolveanotherproblem.Bydoublingthenumberofpointsonce,andthen
twice, it is possible to see if the solution changes appreciably. If not, you have found an
adequateapproximation.
FiniteElementMethodinOneSpaceDimension
Thefiniteelementmethodproceedsinaslightlydifferentway.Theunknownsolutiony(x)
isexpandedinaseriesoffunctions,calledtrialfunctions:
(cid:3)n+1
c(x)= c N (x) (E.37)
i i
i=1
Thefunctionsinthefiniteelementmethodareconstant,linear,orquadraticfunctionsof
positioninasmallregion(calledafiniteelement).Theideaisexplainedforinterpolation
ofaknownfunction,Eq.(E.38),whichisplottedinFigureE.2:
11x4+x
z = (E.38)
12
```

---

## Стр. 370

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
362 APPENDIXE:MATHEMATICALMETHODS
1
0.8
0.6
0.4
0.2
0
0 0.2 0.4 0.6 0.8 1
x
noitcnuF
FIGURE E.2 Functionz=(11×4+x)/12
Theregion0≤x≤1isdividedintofiniteelementsusingthesamegridpointsshownin
FigureE.1.Iftheapproximationsaretakenasconstantineachelement,twointerpolations
areshowninFigureE.3.Eventhoughonly8or16elementsareused,thegeneralshapeof
thefunctionisclear.
Next,thesamemeshisused,butwithlineartrialfunctions.Interpolationwith4,8,and16
elementsisshowninFigureE.4.ThisrepresentationismuchbetterthanthatinFigureE.4.
Indeed,with16elements,thecurve—althoughcomposedofstraight-linesegments—looks
like a smooth curve. Whatever the trial function, the approximation is better when more
elementsareused,andmeshrefinementistheeasiestwaytoensurethattheapproximation
isaccurateenough.
Itisbeyondthescopeofthisbooktodescribethemethodusedtoobtainthecoefficientsin
Eq.(E.30),andhowtheboundaryconditionsareincluded,butcompletedetailsareavailable
(Finlayson, 1972, 1980). There are a variety of books available about the finite element
method.AbookbyGreshoandSani(1998)focusesonflowandconvection/diffusionis.In
thefiniteelementmethod,therepresentationofthesecondderivativeisthesameasgiven
bythefinitedifferencemethod,buttherepresentationofthefunctionisdifferent.Thefinite
elementmethodappliedtoEq.(E.24)withlineartrialfunctionsis
D c i+1 − (cid:6) 2c x i 2 +c i−1 = k 6 (c i+1 +4c i +c i−1 ), wherec i =c(x i ) (E.39)
If quadratic functions are used, there are more differences; in fact, the only time the
representations are the same is for first and second derivatives that are second order and
whenusinglineartrialfunctionsinthefiniteelementmethod.
The boundary conditions are applied in the finite element method in a different way
thaninthefinitedifferencemethod,andthenthelinearalgebraproblemissolvedtogive
theapproximationofthesolution.Thesolutionisknownatthegridpoints,whicharethe
pointsbetweenelements,andaformofthesolutionisknowninbetween,eitherlinearor
quadratic in position as described here. (Comsol Multiphysics has available even higher
orderapproximations.)Theresultisstillanapproximationtothesolutionofthedifferential
equation,andthemeshmustberefinedandtheprocedurerepeateduntilnofurtherchanges
```

---

## Стр. 371

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXE:MATHEMATICALMETHODS 363
1
0.8
0.6
0.4
0.2
0
0 0.2 0.4 0.6 0.8 1
x
noitcnuF
1
0.8
0.6
0.4
0.2
0
0 0.2 0.4 0.6 0.8 1
x
noitcnuF
(a)
(b)
FIGURE E.3 Interpolationwith(a)8and(b)16constantfiniteelements.
arenotedintheapproximation.ThefiniteelementcanbeprogrammedinExcel,too,but
thedetailsaremorecomplicatedandbestlefttorealfiniteelementprograms.
InitialValueMethods
Anotheroptionforsolvingboundaryvalueproblemsistotreatthemlikeinitialvalueprob-
lems.Sinceasecond-orderequationcanbereducedtotwofirst-orderequations,twoinitial
conditionsarenecessary.Oneconditionwillbeknownataboundary.Simplyassumeavalue
fortheotherdependentvariableatthatsameboundary,integratetotheotherside,andcheck
if the required boundary condition is satisfied. If not, change the initial value and repeat
theintegration.Thesuccessofthismethoddependsupontheskillwithwhichyouprogram
the iterations from one trial to the next and successive substitution or Newton–Raphson
methodscanbeusedtocontroltheiterations.InthecaseoftheNewton–Raphsonmethods,
```

---

## Стр. 372

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
364 APPENDIXE:MATHEMATICALMETHODS
1
0.8
0.6
0.4
0.2
0
0 0.2 0.4 0.6 0.8 1
x
(a)
noitcnuF
1
0.8
0.6
0.4
0.2
0
0 0.2 0.4 0.6 0.8 1
x
(b)
noitcnuF
1
0.8
0.6
0.4
0.2
0
0 0.2 0.4 0.6 0.8 1
x
(c)
noitcnuF
FIGURE E.4 Interpolation of z = (11 × 4 + x)/12 with (a) 4, (b) 8, and (c) 16 linear finite
elements.
```

---

## Стр. 373

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXE:MATHEMATICALMETHODS 365
onemustdifferentiatethesolutionwithrespecttotheunsatisfiedboundaryconditionand
solveaproblemwithtwiceasmanyunknowns(Finlayson,1980,pp.139–140).
PARTIALDIFFERENTIALEQUATIONSINTIME
ANDONESPACEDIMENSION
Time-dependenttransportproblemsleadtopartialdifferentialequations,buttheseareeasily
solvedbycombiningthemethodsforinitialvalueproblemsandboundaryvalueproblems.
TaketheheatconductionprobleminEq.(9.28):
∂T ∂2T
=α (E.40)
∂t ∂x2
Write the temperature as a function of position, x, and time, t, but consider only the
positions where there is a grid point, x. The function T(x,t) is a function of only one
i i
independent variable, t, and it can be written as T(t). It can be differentiated in time as
i
follows:
∂ dT(t)
[T(x ,t)]= i (E.41)
∂t i dt
Thus,thedifferentialequation(E.40)definedatthex gridpointusingthefinitedifference
i
methodis
dT i =α T i+1 −2T i +T i−1 (E.42)
dt (cid:6)x2
Thisequationiswrittenforeverygridpoint,andyouhaveasetofinitialvalueproblems
forthesetof{T(t)}:
i
dT T −2T +T dT T −2T +T
2 =α 3 2 1, 3 =α 4 3 2
dt (cid:6)x2 dt (cid:6)x2
dT i =α T i+1 −2T i +T i−1, dT n =α T n+1 −2T n +T n−1
dt (cid:6)x2 dt (cid:6)x2
(cid:3)n+1
dT
or i = A T ,i =2,...,n (E.43)
ij j
dt
j=1
The boundary conditions also need to be included, leading to a set of differential–
algebraicequationsasaninitialvalueproblem.Itiseasier,though,ifthealgebraicequations
be separated out. A boundary condition involving the first derivative can be combined
withthedifferentialequationasisdoneaboveforboundaryvalueproblems.Aboundary
condition involving the function can just be applied in whatever equation requires that
specificvalue.Thentheremainingequationsareallordinarydifferentialequations.
Althoughthestandardmethodscanbeapplied,thesetofEqs.(E.43)isstiff,andbecomes
stiffer as the grid resolution becomes smaller. One eigenvalue of the matrix on the right-
handsideofEq.(E.43)approximatestheslowesttimeresponseofthedifferentialequation,
butthelargesteigenvalueissomeconstantdividedbythegrid-spacingsquared.Thus,as
you refine the mesh, the points become closer together, and the eigenvalues get further
apart, making the problem stiffer. Thus, when solving partial differential equations, stiff
methodsareused;inMATLAB,forexample,ode45isreplacedbyode15sorode23s.
```

---

## Стр. 374

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
366 APPENDIXE:MATHEMATICALMETHODS
If you want to solve this problem with Excel using the Euler method, you write the
equationas
α(cid:6)t
Tn+1 =Tn + (Tn −2Tn +Tn ) (E.44)
i i (cid:6)x2 i+1 i i−1
andputTninonerowandTn+1intherowbelow.Inserttheequationsforinteriorpoints
andtheboundaryconditionsandcopydownasmanyrowsasyouwanttimesteps.Youwill
findthatthemethodisstableonlyif
α(cid:6)t 1
≤ (E.45)
(cid:6)x2 2
ThismethodisusedinProblem9.32.
ProblemswithStrongConvection
Anothercomplicationcanbeimportant:inaproblemwithconvection,therateofconvection
may be much faster than the rate of diffusion. The solution may be like a wave moving
alonginspace.Suchproblemsleadtodifficultieswhensolvedonafixedmesh,andthese
difficulties apply to both finite element and finite difference methods. For example, the
convectivediffusionequationrepresentingconvectionwithvelocityvdownapackedbedis
∂c ∂c ∂2c
+u = D (E.46)
∂t ∂x ∂x2
Theboundaryandinitialconditionsare
(cid:2) (cid:2)
−D ∂ ∂ x c +uc (cid:2) (cid:2) (cid:2) =uc 0 , ∂ ∂ x c (cid:2) (cid:2) (cid:2) =0,c(x,0)=c in (x) (E.47)
x=0 x=L
If the inlet condition changes in time, then a wave moves downstream. This equation
canbemadenondimensional,andthisisinstructivehere:
∂c(cid:4) ∂c(cid:4) ∂2c(cid:4)
+ Pe = (E.48)
∂t(cid:4) ∂x(cid:4) ∂x(cid:4)2
ThePecletnumberistherateofconvectiondividedbytherateofdiffusion:
uL
Pe= (E.49)
D
Thefiniteelementmethodappliedtothisequationgivesthefollowingequationateach
gridpoint:
(cid:6) (cid:7)
1 dc i+1 +4 dc i + dc i−1 + Pe c i+1 −c i−1 = c i+1 −2c i +c i−1 (E.50)
6 dt dt dt 2(cid:6)x (cid:6)x2
Itispossibletoshowthatthefiniteelementsolutionwilloscillatewildlyaboveandbelow
theexactsolutionwheneverthereisasharpchangeintheconcentrationandthemeshPeclet
numberistoolarge(Finlayson,1992,p.29andthebookwebsite).Thus,youneed
Pe(cid:6)x ≤2 (E.51)
```

---

## Стр. 375

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXE:MATHEMATICALMETHODS 367
One way to fix this problem is to refine the mesh until Eq. (E.51) is satisfied, but for
largeproblemsthatmayrequiretoomanypoints(especiallyin2Dand3D).Anotherway
istoaddsome“fake”diffusiontotheproblem.Inthiscase,aPetrov–Galerkinmethodis
(cid:6) (cid:7) (cid:6) (cid:7)
1 dc i+1 +4 dc i + dc i−1 + Pe c i+1 −c i−1 = 1+ Pe(cid:6)x c i+1 −2c i +c i−1
6 dt dt dt 2(cid:6)x 2 (cid:6)x2
(E.52)
and this makes the oscillations smaller or eliminates them. The trick is to add enough
“fake” diffusion to dampen the oscillations but not so much as to change the solution.
In Comsol Multiphysics this is called streamline diffusion or stabilization. There are a
numberofothertechniquesfortreatingthisdifficultyassummarizedbyFinlayson(1992).
TheMacCormackflux-correctedmethodisagoodone,andtheprogramtoprepareFigure
9.18b is available from the book website. The finite volume method is what is used with
finitedifferencemethods,andgooddiscussionsofthoseareinLeVeque(1992,2002).
PARTIALDIFFERENTIALEQUATIONSINTWOSPACEDIMENSIONS
You can solve problems in two space dimensions using the same methods as applied in
onedimension,exceptthatthedetailsbecomemorecomplicated.Theproblemsarestiffer,
andimplicitmethodsareusuallyrequired.Theproblemofunwantedoscillationsismore
severebecauseaddeddiffusionmaysmooththesolutionintheflowdirection,asdesired,
butitmayalsodiffuseitinthedirectionperpendiculartoflow,whichisnotdesired.Careful
treatment,though,allowsforstreamlinediffusion,thatis,theextradiffusionisonlyadded
intheflowdirection.ThesedetailshavebeenhandledbyComsolMultiphysics,whichfrees
youtoconcentrateonthephysicsandtheproblemyouwanttosolve;seestabilizationin
thesettingswindowforthephysicsequation.Simpleproblemsinrectangulargeometries
canbesolvedinExcel.
Finite-DifferenceMethodforEllipticEquationsinExcel
The finite-difference method is easy to program in Excel, provided the equation is not
too complicated. Solving the problem in Excel does require solving it more than once,
though, to assess the accuracy. As an example, take the heat conduction equation with a
heatgenerationterm,Eq.(E.53):
(cid:4) (cid:5)
∂2T ∂2T
k + = Q (E.53)
∂x2 ∂y2
Thefinitedifferenceformofthisequationis
T i+1,j −2T i,j +T i−1,j + T i,j+1 −2T i,j +T i,j−1 = Q (E.54)
(cid:6)x2 (cid:6)y2 k
whereT i,j isthetemperatureattheithlocationinthex-directionandthejthlocationinthe
y-direction.Takethecasewhen(cid:6)x =(cid:6)y andrearrangeasshowninEq.(E.55):
T i,j = T i+1,j +T i−1,j +T i,j+1 +T i,j−1 −(cid:6)x2 Q (E.55)
4 k
```

---

## Стр. 376

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
368 APPENDIXE:MATHEMATICALMETHODS
TABLEE.2 FiniteDifferenceMethodin
ExcelforEllipticBoundaryValueProblem
E4-T i,j−1
D5-T i−1,j E5-T i,j F5-T i+1,j
E6-T i,j+1
ThespreadsheetisarrangedasshowninTableE.2.Whenthevalueof(cid:6)x2Q/kisplaced
incellA2theequationforcellE5is
=(D5+F5+E4+E6)/4−$A$2 (E.56)
You copy this equation for every internal grid point, set the boundary equations, and
turnontheiterationfeature togetthesolution.Then youhave todoitagain withafiner
meshtoassesstheaccuracy.Iftheheatgenerationtermdependsontemperature,itiseasy
toincludethatcomplicationjustbyinsertingtheformulainplaceof$A$2.
FiniteElementMethodforTwo-DimensionalProblems
In the finite element method that is used by Comsol Multiphysics, the trial functions are
defined on an element. A square element in two dimensions with bilinear trial functions
hasfourtrialfunctionsperelement.Theelementcovers0≤u≤1,0≤v≤1,andthetrial
functionsare
N =(1−u)(1−v), N =u(1−v)
1 2 (E.57)
N =uv, N =(1−u)v
3 4
The domain is covered with elements to represent a function on the entire domain.
Considerthefunction
z = x2exp(y−0.5) (E.58)
2
1.5
1
0.5
0
1
1
0.5
0.5
0 0
FIGURE E.5 Functionz=x2exp(y–0.5).
```

---

## Стр. 377

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXE:MATHEMATICALMETHODS 369
2
1.5
1
0.5
0
1
1
0.5
0.5
0 0
(a)
2
1.5
1
0.5
0
1
1
0.5
0.5
0 0
(b)
FIGURE E.6 Interpolationofz=x2exp(y–0.5)with16(a)and64(b)bilinearfiniteelements.
which is plotted in Figure E.5. Plots of the finite element interpolation on 4 × 4 = 16
bilinear elements or 8 × 8 = 64 bilinear elements are shown in Figure E.6. Sixty-four
elementsdoaverygoodjobofrepresentingthefunction.Ifquadraticfunctionsareused,
fewerelementsareneededtoapproximateasmoothfunction.Eithervariationalprinciples
ortheGalerkinmethodareusedtodeterminethesetrialfunctionstorepresentthesolution
to differential equations. The method is beyond the scope of this book and is covered by
Finlayson(1972,1980,2003).
The recommendation in this book is to use quadratic elements for concentration or
temperature in 2D and 3D cases, use quadratic elements for flow in 2D cases and linear
elements for flow in 3D cases. For flow the options will be displayed as P1 + P1 and
P2 + P1, where the first order of polynomial refers to the velocity components and the
```

---

## Стр. 378

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
370 APPENDIXE:MATHEMATICALMETHODS
second to the pressure. Other options are also available in Comsol Multiphysics and the
interestedreaderisinvitedtosolveaproblemusingavarietyofchoicesofelements.Areal
questionis“isitbettertoincreasethenumberofelementsorthedegreeofthepolynomial?”
Inbothcasesthedegreeoffreedomincreases,butaccuracy,computermemoryused,and
timetosolutionwillbeaffected.Thetrade-offmaydependontheproblemyouaresolving,
butgenerallypractitionersmakeachoiceofpolynomialandthenrefinethemesh,always
comparingresultsfromdifferentmeshestoassesstheaccuracy.
SUMMARY
Thisappendixgivesabriefoverviewofthemethodsthatarepreprogrammedinthesoftware
packagesExcel,MATLAB,AspenPlus,andComsolMultiphysics.Theinterestedreader
maypursuethereferences,includingthebookwebsite,formorespecificdetails.
PROBLEMS
E.1 VerifythestabilityconditiongivenbyEq.(E.45).Todoso,writetheequationinthe
1
form
Tn+1 = ATn +BTn +CTn (E.59)
i i−1 i i+1
ConsiderthisequationwhenA,B,andCarepositive.Takeabsolutevaluesofboth
sidesandmaketheright-handsidebiggerbyreplacingeachtermbyitsabsolutevalue
(|a+b|≤|a|+|b|). Ontheright-handside,replaceeachTtermbythemaximumover
allvaluesofi.ThenifA+B+C ≤1,themaximumvalueatthen+1timelevel
isnobiggerthanthetimelevelatthentimelevel.Thus,thesolutioncannotbecome
unbounded. The condition that B be positive gives the stability condition (this is a
sufficientcondition).Youcanseewhathappenswhen(cid:6)tistoobigbysolvingoneof
thetransientheattransferproblemswhenB<0.
E.2 ExpandonProblemE.1bywritingthedifferentialequationfortransientheattransfer
1
inacylinderandasphere.UsingtheconditionthatA,B,andCarepositive,howdoes
thestabilityconditionchangefromthatforplanargeometry?Besuretoconsiderthe
differentialequationatr=0.
E.3 ExpandonProblemE.1bywritingthedifferentialequationfortransientheattransfer
1
intwoandthreedimensions.Applyingtheconditionthatallthecoefficientshaveto
bepositive,whatisthestabilitylimitationasyougofrom1to2to3dimensions?
E.4 TodeterminethetruncationerrorinEqs.(E.27)and(E.29),keeptermsupto(x-x)4
1 i
inEq.(E.25).PerformthesamestepsusedtogenerateEqs.(E.25)–(E.29)togetthe
truncationerror.
E.5 SolvetheT-sensorprobleminChapter11withPe=500.Investigatetheaccuracyof
2
the finite element method by calculating the variance at the outlet. To do this, start
withlineardiscretizationandsolvetheproblemonincreasinglydensemeshes.Keepa
recordofthevarianceandthenumberofdegreesoffreedom.Thendothisagainwith
quadraticdiscretization,thenwithcubicdiscretization.Keeptheflowsimulationfixed
```

---

## Стр. 379

```text
P1:OTA/XYZ P2:ABC
JWBS084-bapp5 JWBS084-Finlayson May26,2012 14:49 PrinterName:YettoCome Trim:7in×10in
APPENDIXE:MATHEMATICALMETHODS 371
asyouimprovethediscretizationforconcentration.Plotthevarianceversusnumber
of degrees of freedom. Plot the absolute value of the residual versus the number of
degreesoffreedom.Forthisproblemtheresidualis
Residual=u ∗ cx+v ∗ cy−(cxx+cyy)/Pe (E.60)
When you use linear discretization the second derivatives will not be defined.
Integratetheabsolutevalueoftheresidualovertheentiredomain;theresidualwill
beoscillatingaroundzerosotheabsolutevalueisnecessary.
```

---

## Стр. 380

```text
P1:OTA/XYZ P2:ABC
JWBS084-bind JWBS084-Finlayson May30,2012 8:52 PrinterName:YettoCome Trim:7in×10in
INDEX
Absorber/stripper,99 moleculedraw,332
Absorption,85 NISTthermodynamicsdata,41–43,45–47,98
Acentricfactor,10 plotwizard,39
Activationenergy,286 RadFrac,95–97,106–108,130
Activity,50 report,118
Activitycoefficient,33,94 RGibbs,59,62,130
Activitycoefficientmodels,87,91.Seealso RPLUG,158
Thermodynamicmodel RStoic,73,128–129,133
Adiabaticboundarycondition,269 sensitivityblock,102–103
Adsorbent,solid,199 SEP,73,130,134
Adsorption,85,160 SSplit,134
Airseparationunit,125,129 streamtable,327
AspenPlus.SeealsoConvergence transferbetweenExcelandAspen,331
Aspenexamples,332–333 transfertowordprocessingprogram,328
calculatorblocks,331 utilitycost,118–119
CISOLIDS,131 AspenProperties,20,39
comparisonwithdata,39–43,45–47,98–99 Averagevelocity,225
designspecifications,103–106 Azeotrope,39,87,135–136
DSTWU,106–108,128–129
flash,35–39,83 BackwardEulermethod,358
flowsheet,113 Binaryinteractionparameters,12
flowsheetsections,329 Biologicalweapons,215
history,118 Bird–Carreaufluid,179,190–193,226–227,249
icons,324 Blasiusformula,241
inclusionofsolids,330 Blocks
inputsummary,118 distillation,68
majorblocks,111 mixer,66,73
massbalanceonly,131,330 reactor,67
MCOMP,113 separator,66
MIXED,131 Boilingpoints,94
modellibrary,24,110,322 Boundaryvalueproblems,175–213,358–363
IntroductiontoChemicalEngineeringComputing,SecondEdition.BruceA.Finlayson.
©2012JohnWiley&Sons,Inc.Published2012byJohnWiley&Sons,Inc.
379
```

---

## Стр. 381

```text
P1:OTA/XYZ P2:ABC
JWBS084-bind JWBS084-Finlayson May30,2012 8:52 PrinterName:YettoCome Trim:7in×10in
380 INDEX
Bratu’sequation,205 Convergence,71,85,120–122
Brinkmannumber,269 acceleration,110
Bubblepoint,30,93 inAspenPlus,83,115,121
inComsol,347
Capillarypressure,212 inExcel,13,72,75
Carreauviscosity,226,249 inMATLAB,16,55
Catalyst,137,139,155,205,259 tearstream,122
Al2O3,177 Conversion,67
cylindrical,282 Corrosion,127
platinum,171,285 Cost,7
silver,81 capital,100
Catalyticconverter,173 cooling,100
Cellulosetoethanol,126–128 energy,65
Centrifuge,175 heating,100
Chargedistribution,208 operating,100,109
Chemicalreactionequilibria,49–60,74,76,109, product,65,100
118 rawmaterial,65,100
Chemicalweapons,215 utility,118–119
Chromatography,85,199–203 Coulombforces,86
Coefficientofthermaldiffusion,180 Crossequation,210
Colloids,210 Cycloneseparator,175
Pecletnumber,210 Cylindricalgeometry,178,189,204
viscosity,210
volumefraction,210 Damko¨hlernumber,165
Combustionreaction,205 Darcy’slaw,211
Compressibilityfactor,10,18 Debyeapproximation,208
Compressor,7,113,175 Degreesoffreedom,213
Computationalfluiddynamics(CFD),215 Dewpoint,30
ComsolMultiphysics Diffusion,175.SeealsoConvectivediffusion
chemicalreactionengineeringmodule,337–338 polymer,85
chemicalspeciestransport,337 porouscatalyst,85
convergence,350 Diffusionandreaction,177,204–207,285–286
datasets,344 inasphere,185–188,206
fluidflow,188–193,215–257,337 Diffusioncoefficient,177,211
heattransfer,337 effective,177,203
heattransferinaslab,181–184 inpolymers,207
helpwithtime-dependentproblems,350 thermal,211
icons,181,340 Dipolemoments,33,88
jumpdiscontinuity,350 Dipole–dipoleinteractions,86
linearadsorption,196–199 Directnumericalsimulation(DNS),216
linearextrusion,246 Dispersion
LiveLinkwithMATLAB,347–348 axial,147,204–205
modelbuilder,336 radial,147,204–205
modellibrary,337 Dispersionforces,86
modelwizard,336 Disproportionation,77
parametricsolution,186 Dissipationofturbulentkineticenergy,
probes,344 230–232
reactionanddiffusion,185–188 Distillation85–86,91–97,100–101.Seealso
tabs,337 DSTWU,RadFrac
transfertoExcel,346 numberofstages,92,94–95
Concentration,solid,197 plate-to-plate,95–97
Condenserduty,94–96,100–102 Distillationtower,29
Controlledrelease,85 diameter,7
Controlvolume,242 Drag
Convection,strong,366 oncylinder,250
Convectivediffusion,260,272–280,284–289 onsphere,250
inT-sensor,265–267 Drawdownratio,209
```

---

## Стр. 382

```text
P1:OTA/XYZ P2:ABC
JWBS084-bind JWBS084-Finlayson May30,2012 8:52 PrinterName:YettoCome Trim:7in×10in
INDEX 381
Drug irregularitiesincenterlinevelocity,224
delivery,259 lineartrialfunctions,229
design,259 mesh,223,228,236,240,263
detection,259 quadratictrialfunctions,229
reactiondiffusion,213
Economicviability,65 streamlines,223,229–230,237
Eigenvalues,307 tetrahedron,217
Electricpotential,207 triangle,217
Electrochemicalcell,280 Flash,83
Electrostaticforces,86 Fluidflow,109.SeealsoConvectivediffusion
Endothermicreaction,61 betweenflatplates,249,289
Energybalance,29,109 Carreaufluidinpipe,249
Enthalpy,7 contraction,245,252
Enzyme,126–127,171 entryflowinpipe,221
loading,172 entryflowofnon-Newtonianfluid,226–227
Epoxy,172 expansion,245
Equationofstate,7–8 fullydeveloped,229–230
differentprocesses,90 high-speed,220–221
Grayson,90 holepressure,256–257
idealgas,8–9 inbend,255
Lee–Kesler–Plo¨cker,21 incross,253
Peng-Robinson,9–11,19–20,44,90–92,95,118 inH-sensor,255
Redlich–Kwong,8–11,19,91 inlaminarfluidinterfacedevice,256
Redlich–Kwong–Soave,9–11,19,21,36,45,47, inpipe,249
61–62 inpipe-T,287
vanderWaals,8–9 inporousmedia,252
virial,86 inserpentinemixer,239–240,255
Equilibriumconstant,50–51,147 insquarecorner,246
Equilibriumconversion,62,67,74 inT-sensor,229–230,250
Equipmentsize,109 inturn,251
Euler’smethod,174,356 microfluidicdevice,227–230,251
inExcel,213 Newtonianfluid,178–179,188–190,208
Excel Non-Newtonianfluid,179,190–193,208
add-ins:AnalysisToolpak,291 orifice,through,235–238,249,269–270
add-ins:AspenPlusV7.3ExcelCalculator, pastaflatplate,250
291 power-lawfluidinpipe,249
add-ins:AspenSimulationWorkbookV7.3, slow,219–220
291 start-upinpipe,233–235
add-ins:SolverAdd-In,291 T-sensor,227–230,250
circularreference,76 turbulent,215,230–233
goalseek,12–13,32,52–53,75 Fluorescence,265
matrixcalculations,293 Frictionfactor,241
solver,13,52–53,75 Fuelcell,49,51,259
Excesspressuredrop,245,252 Fugacity,29,33,50
coefficient,33,51
Federaltestcycle,173 Furnace,129
Ferrofluid,282–283
Fertilizer,49 Galerkinmethod,369
Fiberspinning,208–209 Gear’sbackwarddifferencemethod,358
non-Newtonianfluid,209 Gibbs–Duhemequation,41
Finitedifferencemethod,359–361 Gibbsfreeenergy,50
inExcel,213,361–362 Graetzproblem,283
inMATLAB,213 withaxialconduction,283
Finiteelementmethod,217,361–363,368–370 Greenhousegasemissions,120
arrowplot,223 Gridpoint,359
contours,262 refinement,354–363
discontinuityofinletvelocity,224 Growthrate,maximumspecific,170
```

---

## Стр. 383

```text
P1:OTA/XYZ P2:ABC
JWBS084-bind JWBS084-Finlayson May30,2012 8:52 PrinterName:YettoCome Trim:7in×10in
382 INDEX
Hagen–Poiseuillelaw,178 Laplace’sequation,281–282
Heatconduction,109,176,280 Largeeddysimulation(LES),216
2D,withfinitedifferenceinExcel,289 LBBcondition,217
incylinder,207 Lewisnumber,165
inslab,181–185 Lightkey,92,94,100
insquare,262–265 Limitcycle,168–169
tosphere,283 Limitingreagent,67
unsteady Linearadsorption,196–199
incylinder,207 Liquid–liquidextraction,85
inslab,193–196 Lumpedparametermodels,138
Heatexchanger,counter-current,129
Heatflux,182,184 MacCormackmethodwithflux-correction,202–203
Heatofreaction,50,146,177 Massbalance,29,109
Heattransfer,radiation,207 Masstransfer,85,109,259
Heavykey,92,94,100 Masstransfercoefficient,198,203
Homotopymethod,356 MATLAB.SeealsoComsolMultiphysics,LiveLink
H-sensor withMATLAB
2D,286 boundaryvalueproblem,184–185
3D,287 checklistfor“ode45”,311
Humanneuralstemcells,288 conditionalstatements,303
Hydrogen,49,51,53,60,62,72 contours,266–267
Hydrolysis,132,134 display,301
feval,16–17
Immiscibleliquids,85 fminsearch,56–57,309
Implicitmethod,358 fsolve,56,158,164
Incompressiblefluid,222 fzero,16–17,19,34,158,309
Infraredspectroscopy,255 globalcommand,55,142,300
Inhibitionconstant,170 graphicaluserinterfaces,318
Initialvaluemethodsforboundaryvalueproblems, heattransferinaslab,184–185
363 import/exportdata,315–317
Initialvalueproblems,140–163,356–358 initialvalueproblem,140–148,155–157,
Inletvelocityprofile,275 163–165,169–171
Integrals,307 loops,303
IntegratedGasificationCombinedCycle(IGCC), m-files,299
125–126,130 matrixcalculations,304
Intermolecularforces,86 partialdifferentialequation,195–196
Interstitialvelocity,203 passingparameters,143
Ionicsystems,86 plotting,312–314
Isothermalflash,30–39 plottingresultsfrommethodoflines,315
Iterationmethods,65.SeealsoConvergence scripts,299
Broyden,83,121 workspace,300
direct,83,115 Mechanicalenergybalance,242–245
Newton,83,115,121 Medicaldiagnostics,215
Wegstein,83,115,121 Meshrefinement,362,370
Metabolite,288
Jacobian,355 Michaelis–Mentenreaction,171,185–187,285
Microelectromechanicalsystems(MEMS),259
k-εmodel,216 Microfluidics,215,269
K-value,30,33–34,38,44,46 size,215
Microreactor,171
Lab-on-a-chip,259 Minimumnumberofstages,94
Laminarflow,221,229 Minimumrefluxratio,94
Laminarfluiddiffusioninterfacedevice,256,288 Mixing-cupconcentration,276
Langmuir–Hinshelwood–Hougen–Watsonkinetics, Moleculardynamics,86
159 Molecularsieve,135
Langmuirisotherm,200–201,212–213 Monodconstant,170
```

---

## Стр. 384

```text
P1:OTA/XYZ P2:ABC
JWBS084-bind JWBS084-Finlayson May30,2012 8:52 PrinterName:YettoCome Trim:7in×10in
INDEX 383
Monodkinetics,170 Pressuredrop,179
MonteCarlomethods,86 Pressureswingadsorption,203–206,212–213
Multiplesolutions,206 Processcontrol,215
Propertymethodselectionassistant,89,99
NationalInstituteofStandardsandTechnology Protein,255,288
(NIST),seeAspenPlus,comparisonwithdata Pump,7,175
NationalRenewableEnergyLaboratory(NREL), Purgestream,76
127,136 p-xydiagrams,30
Naturalgas,107,119
Navier–Stokesequation,217 Rachford–Riceequation,32,44–45,76
Newtonianfluid,178.SeealsoFluidflow,Newtonian Radialdistributionfunction,86
fluid Raoult’slaw,92
Newton–Raphsonmethod,48,63,174,354 Rateofenergygeneration,176
NISTthermodynamicdataengine(TDE),99,108 Rawmaterials,65,79
Nondimensionalequation,218,261 Reaction,259
Non-Newtonianfluid,179,218,249.Seealso Reactor,7
Colloids,Bird–Carreaufluid,Power-lawfluid adiabatic,162
Nonpolarmolecules,86 batch,139
Nonrandommoleculeinteraction,87 chemical,137
NRTL,seethermodynamicmodel,NRTL continuousstirredtankreactor(CSTR),140,
Numberofstages,94 161–162
“Numberup”,259 withmultiplesolutions,163–164
Nusseltnumber,283 exothermic,137
isothermalplugflow,144,146,150–151,168–169
Oilreservoir,44 masstransfer,137–138,155–159,171–172
Operatingparameters,109 molechanges,171–172
Optimization,122–124 nonisothermalplugslow,146–149,151–152,
OptimizationToolBox,158,164 172–173
Ordinarydifferentialequations,168 plug-flow,259
boundaryvalueproblems,175–213,358–364 transientCSTR,164–165,172–174
implicitmethods,358 variabledensity,153–154
initialvalueproblems,137,309–312 wall,274
inMATLAB,357–358 Reboilerduty,94–96,100–103
solvedwithAspenPlus,158–161 Recyclestream,65,70–76,109
solvedwithComsolMultiphysics,148–152 Refinery,7
solvedwithExcel,162 Refluxratio,92,94
solvedwithMATLAB,140–148,163 minimumrefluxratio,92,94–95
stiff,167 Relativevolatility,91
Oscillationsinsolution,277 Residual,213,371
Reynoldsnumber,230,246
Packedabsorption,97–100,204–205,284–285 RKSWS,seeThermodynamicmodel,RKSWS
Pair-interactionparameters,87 Runge–Kuttamethod,174,357
Partialdifferentialequations,365–370
Partiallysaturatedsoil,211 Saccharification,seeHydrolysis
Pecletnumber,198,210–213,266–267,276–277 Saturation,211–212
Permeability,211–212 Scale-up,288
Phaseseparator,31,37 Scatchard–Hildebrandmodel,87
Poisson–Boltzmannequation,208 Selectivity,259
Poisson’sequation,193,208 Sensitivity,124–125
Polarmolecules,86–87 Sensors,259
Polymericcomposite,172 Sequentialsolutionmethod,70–71
Polymermelt,190,215 Serpentinemixer,272–276,287
Populationbalance,174 Serum,255
Porosity,211 Shearrate,218,225–226
Power-lawfluid,249 Simultaneoussolutionmethod,70–71
Pressure,critical,10 Solubility,118
```

---

## Стр. 385

```text
P1:OTA/XYZ P2:ABC
JWBS084-bind JWBS084-Finlayson May30,2012 8:52 PrinterName:YettoCome Trim:7in×10in
384 INDEX
Solutions.SeealsoThermodynamicmodel Transportprocesses,109
ideal,87 energy,175
non-ideal,39–41 mass,175
Specificvolume,mixture,7 momentum,175
Sphericalgeometry,185,204 Trialfunctions,362,369–370
Splineinterpolation,307 T-sensor,265
Splitfraction,67,69,78 3D,278–280,288.SeealsoFlow,inT-sensor
Stabilitycondition,370 withwallreaction,272
Statisticalmechanics,86–87 withreaction,270–272,286
Steamreformer,61–63 Turbulentflow.Seealsok-εmodel,Largeeddy
Stemcells,289 simulation
Stiffequations,365 eddyviscosity,230
Stoichiometriccoefficient,171 inpipe,230–232,251
Stoichiometry,55,73,136 kineticenergy,230–232
Stokesflow,250 Two-pointboundaryvalueproblem,177–178
Streamlines,182,229–230 T-xydiagrams,39,44,108
Substrateconcentration,170
Successivesubstitution,354 UNIFAC,seeThermodynamicmodel,UNIFAC
Surfacetension,209–210 UNIQUAC,seeThermodynamicmodel,UNIQUAC
Upstreamweighting,277
Tearstream,110
Temperature van’tHoffequation,50
control,217,261 Vapor–liquidequilibria,29–48,109
critical,10 Vaporpressure,29,100
reduced,10 Variance,276
Terminalvelocity,250 Variationalprinciple,369
Thermalconductivity,177,183,282 Velocity
effective,179 average,180–181,192
Thermaldiffusion,coefficientof,180 peak,180–181
Thermalflowfieldfractionation,211 venacontracta,237
Thermalinsulation,262 Viscosity,180
Thermocapillaryflow,209–210 Carreau,179,191
Thermodynamicmodel,29,85,88,92,109.Seealso concentrationdependent,268
Equationofstate shear-thinningfluid,225–226
Boston–Mathias,90 temperaturedependent,270
Chao–Seader,92,94,95,100 Viscousdissipation,271–272,288
electrolyteNRTL,88,90 Voidfraction,197,203
electrolytes,88
Margulesmodel,87 Wastestreams,109
nonrandomtwoliquid(NRTL),87,112 Wastetreatment,65
one-constant,87 Water–gasshiftreaction,49,51–56,60–61,102–106,
regularsolutiontheory,87 130,137,158,172
RKSWS,45 Website,3–4
Schwartzentruber–Renon,90 Wilsonequation,seeThermodynamicmodel,
UNIFAC,33,47,87–88,90–91 Wilson
UNIQUAC,33,46–47,87,90–91 Wong–Sandlerequation,seeThermodynamicmodel,
VanLaarmodel,87 Wong–Sandler
Wilson,33,39,46–47,87,90–91,98
Wong–Sandler,45,90,91 Yield,109
```

---

## Стр. 386

```text
P1:OTA/XYZ P2:ABC
JWBS084-bref JWBS084-Finlayson May26,2012 14:47 PrinterName:YettoCome Trim:7in×10in
REFERENCES
Abramowitz,M.A.,Stegan,I.A.(eds.),HandbookofMathematicalFunctions.NationalBureauof
Standards:Gaithersburg,MD,1964.
Aden,A.,Ruth,R.,Ibsen,K.,Jechura,J.,Neeves,K.,Sheehan,J.,Wallace,B.(NREL);Montague,L.,
Slayton,A.,Luka,J.(HarrisGroup,Seattle),LignocelluosicBiomasstoEthanolProcessDesign
andEconomicsUtilizingCo-CurrentDiluteAcidPrehydrolysisandEnzymaticHydrolysisforCorn
Stover, NREL/TP-510–32438, National Renewable Energy Laboratory, 1617 Cole Boulevard,
Golden,CO80401–3393,ContractNo.DE-AC36–99-GO10337,June,2002.Thedescriptionof
thefullprocessisat:http://www.nrel.gov/docs/fy02osti/32438.pdf.
Aguilo´,A.,Penrod,J.D.,Acetaldehyde.InEncyclopediaofChemicalProcessingandDesign,Vol.
1,McKetta,J.J.(ed.).MarcelDekker:NewYork,1976.
Anonymous,Thepost-alcoholworld.TheEconomistOct.30,2010;84–86.
Aris,R.,Onthedispersionofasoluteinafluidflowingthroughatube.Proc.Roy.Soc.Lond.1956;
A235,67–77.
Aspen,TheAspenModel.2011;http://devafdc.nrel.gov/biogeneral/Aspen_Models./Downloadthe
BKPfile(theAspenbackupfile),theinputfileandthespreadsheet.
Barron,R.F.,CryogenicSystems.OxfordUniversityPress:NewYork,1985.
Beltrami,E.J.,MathematicalModelsforSocietyandBiology.AcademicPress:SanDiego,2002.
Berg,J.C.,AnIntroductiontoInterfacesandColloids:TheBridgetoNanoscience.WorldScientific:
Hackensack,NJ,2010.
Bird, R. B., Armstrong, R. C., Hassager, O., Dynamics of Polymeric Liquids. Wiley-Interscience:
NewYork,1987.
Bird,R.B.,Stewart,W.E.,Lightfoot,E.N.,TransportPhenomena,2nded.Wiley:NewYork,2002.
Broyden,C.G.,Aclassofmethodsforsolvingnonlinearsimultaneousequations.Math.Comput.
1965;19,577–593.
Broyden,C.G.,Theconvergenceofaclassofdouble-rankminimizationalgorithms.J.Inst.Math.
Appl.1970;6,76–90.
IntroductiontoChemicalEngineeringComputing,SecondEdition.BruceA.Finlayson.
©2012JohnWiley&Sons,Inc.Published2012byJohnWiley&Sons,Inc.
373
```

---

## Стр. 387

```text
P1:OTA/XYZ P2:ABC
JWBS084-bref JWBS084-Finlayson May26,2012 14:47 PrinterName:YettoCome Trim:7in×10in
374 REFERENCES
Cavett,R.H.,Applicationofnumericalmethodstotheconvergenceofsimulatedprocessesinvolving
recycleloops.Am.Petrol.Inst.1963;43,57–76.
Chang,M.W.,Finlayson,B.A.,Ontheproperboundaryconditionforthethermalentryproblem.
Int.J.Num.MethodsEng.1980;15,935–942.
Choi,Y.,Stenger,H.G.,Water-gasshiftreactionkineticsandreactormodelingforfuelcellgrade
hydrogen.J.PowerSources2003;124,432–439.
Chow, A. Lab-on-a-chip: opportunities for chemical engineering. AIChE J. 2002; 48, 1590–
1595.
Chu,S.,Carboncaptureandsequestration.Science2009;325,1599.
Chung,B.G.,Flanagan,L.A.,Rhee,S.W.,Schwartz,P.H.,Lee,A.P.,Monuki,E.S.,Jeon,N.L.,
Humanneuralstemcellgrowthanddifferentiationinagradient-generatingmicrofluidicdevice.
Lab.Chip2005;5,401–406.
Constantinides,A.,Mostoufi,N.,NumericalMethodsforChemicalEngineerswithMATLABAppli-
cations.Prentice-Hall:EnglewoodCliffs,NJ,1999.
Cooper,H.W.,Producingelectricityandchemicalssimultaneously.Chem.Eng.Prog.2010;106,
24–32.
Cowfer,J.A.,Gorensek,M.B.,Vinylchloride.InEncyclopediaofChemicalTechnology,Vol.24,
4thed.Kroschwitz,J.I.(Exec.ed.),MaryHowe-Grant(ed.).Wiley:NewYork,1997.
Cutlip,M.B.,Shacham,M.,ProblemSolvinginChemicalandBiochemicalEngineeringwithNu-
mericalMethods.Prentice-Hall:EnglewoodCliffs,NJ,2007.
Dagan,Z.,Weinbaum,S.,Pfeffer,R.,Aninfinite-serriessolutionforthecreepingmotionthroughan
orificeoffinitelength.J.FluidMech.1982;115,505–523.
Datta,A.,Rakesh,V.,AnIntroductiontoModelingofTransportProcesses.CambridgeUniversity
Press:Cambridge,UK,2010.
Deen,W.M.,AnalysisofTransportPhenomena.OxfordUniversityPress:Oxford,UK,1998.
deGroot,S.R.,Mazur,P.,Non-EquilibriumThermodynamics.Dover:NewYork,1954.
DeLeeuw,M.L.,Z.Phys.Chem.1911;77,2841;asreportedbyHirataetal.(1975).
Denbigh, K.,The Principles ofChemical Equilibrium, 3rd ed. CambridgeUniversity Press:Cam-
bridge,UK,1971.
Ellis,S.R.M.,Garbett,R.O,Ind.Eng.Chem.1960;52,385;asreportedbyHirataetal.(1975).
Finlayson,B.A.,TheMethodofWeightedResidualsandVariationalPrinciples.AcademicPress:
London,1972.
Finlayson, B. A., Nonlinear Analysis in Chemical Engineering. McGraw-Hill: New York, 1980;
[reprinted,RavennaPark:Seattle,WA,2003.]
Finlayson,B.A.,NumericalMethodsforProblemswithMovingFronts.RavennaPark:Seattle,WA,
1992.
Finlayson,B.A.,Biegler,L.T.,Grossmann,I.E.Mathematicsinchemicalengineering.InUllmann’s
EncyclopediaofIndustrialChemistry,ElectronicRelease,Vol.B1,Wiley-VCH,Weinheim,2006.
Finlayson,B.A.,Biegler,L.T.,Mathematics.Section3.InPerry’sChemicalEngineers’Handbook,
8thed.Perry,R.H.,Green,D.W.(eds.).McGraw-Hill:NewYork,2008.
Finlayson,B.A.,Shaw,R.A.,ModelingmicrofluidicseparationsusingComsolMultiphysics.Comsol
Conference,Boston,2010;http://www.comsol/papers/8117/.
Finlayson,B.A.,Young,L.C.,Mathematicalmodelsofthemonolithcatalyticconverter:PartIII.
Hysteresisincarbonmonoxidereactor.AIChEJ.1979;25,192–196.
Finlayson,B.A.,Drapala,P.W.,Gebhardt,M.,Harrison,M.D.,Johnson,B.,Lukman,M.,Kunar-
idtipol,S.,Plaisted,T.,Tyree,Z.,VanBuren,J.,Witsara,A.,Microcomponentflowcharacteriza-
tion,Chapter8,Koch,M.V.etal.(eds.),Wiley-VCH,Weinheim2007.
```

---

## Стр. 388

```text
P1:OTA/XYZ P2:ABC
JWBS084-bref JWBS084-Finlayson May26,2012 14:47 PrinterName:YettoCome Trim:7in×10in
REFERENCES 375
Fogler,H.S.,EssentialsofChemicalReactionEngineering,4thed.PrenticeHall:EnglewoodCliffs,
NJ,2010.
Frank-Kamenetskii,D.A.,DiffusionandHeatTransferinChemicalKinetics.PlenumPress:New
York,1969.
Freemantle,M.,Findingthebestconditionsrapidly.C&ENews,February2005;83,11.
Gear, C. W., Numerical Initial Value Problems in Ordinary Differential Equations. Prentice-Hall:
EnglewoodCliffs,NJ,1971.
Gilat,A.,MATLAB:AnIntroductionwithApplications,4thed.Wiley:NewYork,2010.
Gokhale,S.V.,Jayaraman,V.K.,Tayal,R.K.,Kulkarni,B.D.,Microchannelreactors:applications
anduseinprocessdevelopment.Int.J.Chem.ReactorEngr.2005;3,ReviewR2.
Gomez,F.A.,BiologicalApplicationsofMicrofluidics.Wiley-Interscience:Hoboken,NJ,2008.
Gray,J.,Biomolecularmodelinginaprocessdynamicsandcontrolcourse.Chem.Eng.Ed.2006;
40,297–306.
Gresho,P.M.,Sani,R.L.,IncompressibleFlowandtheFiniteElementMethod.Wiley:NewYork,
1998.
Gresho,P.M.,Sani,R.L.,Engleman,M.S.,IncompressibleFlowandtheFiniteElementMethod.
Vol.2:IsothermalLaminarFlow.Wiley:NewYork,1998.
Groenier,W.S.,Thodos,G.,Pressure-volume-temperaturebehaviorofammoniainthegaseousand
liquidstates.J.Chem.Eng.Data1960;5,285–288.
Hatch,A.,Kamholz,A.E.,Hawkins,K.R.,Munson,M.S.,Schilling,E.A.,Weigl,B.H.,Yager,P.,
ArapiddiffusionimmunoassayinaT-sensor.Nat.Biotechnol.2001;19,461–465.
Hellinckx,L.,Grootjans,J.,VandenBoxch,B.,Stabilityanalysisofcatalystparticlethroughorthog-
onalcollocation.Chem.Eng.Sci.1972;27,644–647.
Henry,C.M.,Gowiththeflow.C&ENews,March82,2005;83,57–59.
Hess,G.,Incentivesboostcoalgasification.C&ENews,January16,2006;84,22–24.
Hirata,M.,Ohe,S.,Nagahama,K.,ComputerAidedDataBookofVapor-LiquidEquilibria.Kodansha
Ltd.andElsevier:TokyoandNewYork,1975.
Hlava´c˘ek,V.,Marek,M.,Kub´ıc˘cek,M.,Modellingofchemicalreactors,X:Multiplesolutionsof
enthalpyandmassbalancesforacatalyticreactionwithinaporouscatalystparticle.Chem.Eng.
Sci.1968;23,1083–1097.
Hughes,T.J.R.,Brooks,A.N.,Amulti-dimensionalupwindschemewithnocrosswinddiffusion.
InFiniteElementMethodsforConvectionDominatedFlow,AMDVol.34,Hughes,T.J.R.(ed.).
ASME:NewYork,1979.
Jackson,N.R.,Finlayson,B.A.,Calculationofholepressure:I.Newtonianfluids.J.Non-Newtonian
FluidMech.1982a;10,55–69.
Jackson,N.R.,Finlayson,B.A.,Calculationofholepressure:II.Viscoelasticfluids.J.Non-Newtonian
FluidMech.1982b;10,71–84.
Jensen, K. F., Microchemical systems: status, challenges, and opportunities. AIChE J. 1999; 45,
2051–2054.
Jones,C.A.,Schoenbom,E.M.,Colburn,A.P.,Equilibriumstillformiscibleliquidsdataofethylene
dichloride-toluneandethanol-water.Ind.Eng.Chem.1943;35,666–672.
Kirby,B.J.,Micro-andNanoscaleFluidMechanics.CambridgeUniversityPress:Cambridge,UK,
2010.
Koch,M.V.,VandenBussche,K.M,Chrisman,R.W.,MicroInstrumentation.Wiley-VCH:Weinheim,
2007.
Kolavennu,P.K.,Telotte,J.C.,Palanki,S.,Designofafuelprocessorsystemforgeneratinghydrogen
forautomotiveapplications.Chem.Eng.Ed.2006;40,239–244.
```

---

## Стр. 389

```text
P1:OTA/XYZ P2:ABC
JWBS084-bref JWBS084-Finlayson May26,2012 14:47 PrinterName:YettoCome Trim:7in×10in
376 REFERENCES
Koretsky,M.D.,EngineeringandChemicalThermodynamics.Wiley:NewYork,2004.
Kusmanto,F.,Jacobsen,E.L.,Finlayson,B.A.,Applicabilityofcontinuummechanicstopressure
dropinsmallorifices.Phys.Fluids2004;16,4129–4134.
Ladisch,M.R.,Mosier,N.S.,Kim,Y.M.,Ximenes,E.,Hogsett,D.,Convertingcellulosetobiofuels.
Chem.Eng.Prog.2010;106,56–63.
LeVeque,R.J.,NumericalMethodsforConservationLaws.Birkha¨userVerlag:Boston,1992.
LeVeque, R. J., Finite Volume Methods for Hyperbolic Problems. Cambridge University Press:
Cambridge,UK,2002.
Lin,Y.,Enszer,J.A.,Stadtherr,M.A.,Enclosingallsolutionsoftwo-pointboundaryvalueproblems
forODEs.Comput.Chem.Eng.2008;32,1714–1725.
Liu,K.,Song,C.,Subramani,V.,HydrogenandSyngasProductionandPurificationTechnologies.
Wiley:Hoboken,NJ,2010.
Marsh,H.D.,Severin,M.,Schuster,H.G.,Steamreforming.InEncyclopediaofChemicalProcessing
andDesign,Vol.47,McKetta,J.J.(ed.).MarcelDekker:NewYork,1994.
McKetta,J.J.(ed.),EncyclopediaofChemicalProcessingandDesign.MarcelDekker:NewYork,
1976–1994.
Middleman,S.,FundamentalsofPolymerProcessing.McGraw-Hill:NewYork,1977.
Murti, P. S., Van Winkle, M., Chem. Eng. Data Series 1959; 3, 72, [as reported by Hirata ;et al.
(1975)].
National Academy of Engineering, What you need to know about energy. 2008; http://sites
.nationalacademies.org/Energy/Energy_043338.
NationalEnergyTechnologyLaboratory(www.netl.doe.gov),DOE/NETL-2007/1281,CostandPer-
formanceBaselineforFossilEnergyPlants,Aug.2007.
Neils,C.,Tyree,Z.,Finlayson,B.,Folch,A.,Combinatorialmixingofmicrofluidicstreams.Lab-on-
a-Chip,2004;4,342–350.
Orazem,M.,Newman,J.,Primarycurrentdistributionandresistanceofaslotted-electrodecell.J.
Electrochem.Soc.1984;137,2857–2861.
Otani, S., Matsuoka, S., Sato, M., Tatoray “Tatoray” process—a new transalkylation process of
aromaticsdevelopedbyToray.Jap.Chem.Q.1968;4(4),16–18.
Othmer, D. F., Morley, F. R., Composition of vapors from boiling binary solutions apparatus for
determinationsunderpressure.Ind.Eng.Chem.1946;38,751–757.
Peng,D.-Y.,Robinson,D.B.,Anewtwo-constantequationofstate.Ind.Engr.Chem.Fund.1976;
15,59–64.
Perry,R.H.,Green,D.W.(ed.),Perry’sChemicalEngineers’Handbook,8thed.McGraw-Hill:New
York,2008.
Peyret, R., Taylor, T. D., Computational Methods for Fluid Flow. Springer Verlag: Dusseldorf,
1983.
Pignet,T.,Schmidt,L.D.,KineticsofNH oxidationofPt,Rh,andPd.J.Cat.1975;40,212–225.
3
Platon,A.,Wang,Y.,Water-gasshifttechnologies.Chapter6.InHydrogenandSyngasProduction
andPurificationTechnologies.Lin,etal.(eds.)Wiley:Hoboken,NJ,2010.
Prasad,S.,Gautam,A.,Integratedcoalgasificationcombinedcycleroute.Chem.Engr.World.2004;
39(9),60–61.
Redlich,O.,Kwong,J.N.S.,Onthethermodynamicsofsolutions.5.Anequationofstate—fugacities
ofgaseoussolutions.Chem.Rev.1949;44,233–244.
Regalbuto,J.R.,Cellulosicbiofuels—gotgasoline?Science2009;325,822–824.
Reid,R.C.,Prausnitz,J.M.,Sherwood,T.K.,ThePropertiesofGasesandLiquids,3rded.McGraw-
Hill:NewYork,1977.
```

---

## Стр. 390

```text
P1:OTA/XYZ P2:ABC
JWBS084-bref JWBS084-Finlayson May26,2012 14:47 PrinterName:YettoCome Trim:7in×10in
REFERENCES 377
Rhee,H.K.,Aris,R.,Amundson,N.R.,First-OrderPartialDifferentialEquations,Vol.I,Theory
andApplicationofSingleEquations.Prentice-Hall:EnglewoodCliffs,NJ,1986.
Rosen, E. M., Pauls, A. C., Computer aided chemical process design: the FLOWTRAN system.
Comp.Chem.Engr.1977;1,11–21.
Rosensweig, R. E., Ferrohydrodynamics. Cambridge University Press: Cambridge, MA, 1985;
reprintedbyDoverPublications:NewYork,1997.
Ruthven,D.M.,Farooq,S.,Knaebel,K.S.,PressureSwingAdsorption.VCH:NewYork,1994.
Sage,B.H.,Webster,D.C.,Lacey,W.N.,Phaseequilibriainhydrocarbonsystems:XIX.Thermo-
dynamicpropertiesofn-butane.Ind.Eng.Chem.1937;29,1188–1194.
Sandler,S.I.,Chemical,Biochemical,andEngineeringThermodynamics,4thed.Wiley:NewYork,
2006.
Sandler,S.I.,AnIntroductiontoAppliedStatisticalThermodynamics.Wiley:NewYork,2011.
Schattka,B.,Alexander,M.,Ying,S.L.,Man,A.,Shaw,R.A.,Metabolicfingerprintingofbiofluids
by infrared spectroscopy: modeling and optimization of flow rates for laminar fluid diffusion
interfacesamplepreconditioning.AnalyticalChemistry,2011;83,555–562.
Schmidt,L.D.,TheEngineeringofChemicalReactions.OxfordUniversityPress:NewYork,2005.
Service,R.F.,Anotherbiofuelsdrawback:thedemandforirrigation.Science2009;326,516–517.
Shuler, M. L., Immobilized biocatalysts and reactors. In Chemical Engineering Education in a
Changing Environment. Sandler, S. I., Finlayson, B. A. (eds.). AIChE: New York, 1988, pp.
37–56.
Sircar,S.,Golden,T.C.,Pressureswingadsorptiontechnologyforhydrogenproduction.InHydrogen
andSyngasProductionandPurificationTechnologies,Chapter10,pp.414–450,Liuetal.(ed.).
Wiley,NewYork,2010.
Soave,G.,EquilibriumconstantsfromamodifiedRedlich-Kwongequationofstate.Chem.Eng.Sci.
1972;27,1197–1203.
Stephenson,R.M.,IntroductiontotheChemicalProcessIndustries.Reinhold:NewYork,1966.
Stirling,R.G.,Ethylchloride.InEncyclopediaofChemicalProcessingandDesign,Vol.20,McKetta,
J.J.(ed.).MarcelDekker:NewYork,1984.
Stone,H.A.,Kim,S.,Microfluidics:basicissues,applications,andchallenges.AIChEJ.2001;47,
1250–1254.
Straty,G.C.,Palavra,A.M.F.,Bruno,T.J.,PVTpropertiesofmethanolattemperaturesto300◦C.
Int.J.Thermophys.1986;7,1077–1089.
Taylor,G.,Dispersionofsolublematterinsolventflowingslowlythroughatube.Proc.Roy.Soc.
Lond.,1953;A219,186–203.
TorayIndustries,Inc.,UOPProcessDivision:benzeneandxylenes(TATORAY).Hydro.Proc.1975;
54,115.
Weekman,V.W.Jr.,Gazingintoanenergycrystalball.Chem.Eng.Prog.June,2010;106,23–27.
Wegstein,J.H.,Acceleratingconvergenceofiterativeprocesses.Commun.Assoc.Comput.Mach.,
1958;1(6),9–13.
Weigl,B.H.,Yager,P.,Microfluidicdiffusion-basedseparationanddetection.Science1999;283,
346–347.
Wiebe, R., Tremeame, T. H., Solubility of nitrogen in liquid ammonia at 25◦ from 25 to 1000
atmospheres.J.Am.Chem.Soc.1933;55,975–978.
Wiebe,R.,Tremeame,T.H.,Thesolubilityofhydrogeninliquidammoniaat25,50,75and100C
andatpressuresto1000atmospheres.J.Am.Chem.Soc.1934;56,2357–2360.
Wilkes,J.,FluidMechanicsforChemicalEngineerswithMicrofluidicsandCFD,2nded.Prentice
Hall:EnglewoodCliffs,NJ,2006.
```

---

## Стр. 391

```text
P1:OTA/XYZ P2:ABC
JWBS084-bref JWBS084-Finlayson May26,2012 14:47 PrinterName:YettoCome Trim:7in×10in
378 REFERENCES
Wong,D.S.H.,Sandler,S.I.,Atheoreticallycorrectmixingruleforcubicequationsofstate.AIChE
J.1992;38,671–680.
Young,L.C.,Finlayson,B.A.,Axialdispersioninnon-isothermalpackedbedchemicalreactors.
IECFund.1973;12,412–422.
Young, L. C., Finlayson, B. A., Mathematical models of the monolith catalytic converter: Part I.
Developmentofmodelandapplicationoforthogonalcollocation.AIChEJ.1976a;22,331–343.
Young, L. C., Finlayson, B. A., Mathematical models of the monolith catalytic converter: Part II.
Applicationtoautomobileexhaust.AIChEJ.1976b;22,343–353.
Zimmerman, W. B. J., Multiphysics Modeling with the Finite Element Method. World Scientific:
Singapore,2008.
```
