# Invented labels and predictions; no patient data, packages or API calls.
cases <- data.frame(
  group = rep(c("A", "B"), each = 4),
  reference = c(TRUE, TRUE, FALSE, FALSE, TRUE, TRUE, FALSE, FALSE),
  prediction = c(TRUE, FALSE, FALSE, TRUE, TRUE, TRUE, FALSE, FALSE)
)

score <- function(rows) {
  tp <- sum(rows$reference & rows$prediction)
  fp <- sum(!rows$reference & rows$prediction)
  fn <- sum(rows$reference & !rows$prediction)
  tn <- sum(!rows$reference & !rows$prediction)
  data.frame(n = nrow(rows), tp = tp, fp = fp, fn = fn, tn = tn,
             precision = if (tp + fp == 0) NA_real_ else tp / (tp + fp),
             recall = if (tp + fn == 0) NA_real_ else tp / (tp + fn))
}

print(rbind(overall = score(cases),
            A = score(cases[cases$group == "A", ]),
            B = score(cases[cases$group == "B", ])))
message("Teaching example only: n=4 per group; do not infer population fairness.")
