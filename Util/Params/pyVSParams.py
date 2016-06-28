config_dict = dict(
    ResultsModelWiseResults_OLD=dict(lm=["aic", "bic", "centered_tss", "condition_number", "df_model", "df_resid", "ess",
                                   "f_pvalue", "fvalue", "k_constant", "llf", "mse_model", "mse_resid", "mse_total",
                                   "nobs", "rsquared", "rsquared_adj", "scale", "ssr", "uncentered_tss"]),
    ResultsModelWiseResults=dict(lm=["aic", "df_model", "df_resid", "f_pvalue", "fvalue", "mse_model", "mse_resid", "mse_total",
                                     "rsquared", "rsquared_adj", "ssr"]),
    ResultsModelVariableWiseResults=dict(lm=["bse", "params", "pvalues", "tvalues"]),
    VSVoxelOPS=dict(slice_count="200"),
)