(* Medication Dosage Adjustment System - Fuzzy Logic Membership Model
   Jordan Christopher Lyles
   Wolfram Language companion file for computational visualization. *)

ClearAll[x, triMF, lowMF, medMF, highMF];

triMF[x_, {a_, b_, c_}] := Piecewise[{
   {0, x <= a},
   {(x - a)/(b - a), a < x <= b},
   {(c - x)/(c - b), b < x < c},
   {0, x >= c}
}];

lowMF[x_] := triMF[x, {0, 0, 50}];
medMF[x_] := triMF[x, {25, 50, 75}];
highMF[x_] := triMF[x, {50, 100, 100}];

Plot[{lowMF[x], medMF[x], highMF[x]}, {x, 0, 100},
 PlotLegends -> {"Low", "Medium", "High"},
 AxesLabel -> {"Medication desirability score", "Membership"},
 PlotLabel -> "Medication Desirability Membership Functions",
 GridLines -> Automatic,
 ImageSize -> Large]

(* Example weighted pre-screen score before fuzzy inference. *)
medicationScore[pain_, adverse_, cost_, relevance_] :=
  0.35 pain + 0.25 adverse + 0.20 cost + 0.20 relevance;

medicationScore[90, 75, 85, 100]
