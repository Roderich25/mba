import pandas as pd

df = pd.read_csv("denue202011.csv", encoding="utf-8", low_memory=False)
df["Key"] = df.cve_ent.apply(lambda x: f"{x:02}") + df.cve_mun.apply(lambda x: f"{x:03}")
# df["Personal"] = df["per_ocu"]

for i in range(2, 7):
    df["Codigo"] = df["codigo_act"].apply(str).apply(lambda x: x[:i])
    # df_temp = df.groupby(["Key", "Codigo", "Personal"]).count()[["id"]].reset_index().rename(columns={"id": "Count"})
    df_temp = df.groupby(["Key", "Codigo"]).count()[["id"]].reset_index().rename(columns={"id": "Count"})
    print(df_temp.shape)
    # df_wide = pd.pivot_table(df_temp, index=["Key"], columns=["Codigo", "Personal"], values="Count").fillna(0).reset_index()
    df_wide = pd.pivot_table(df_temp, index=["Key"], columns=["Codigo"], values="Count").fillna(0).reset_index()
    print(df_wide.shape)
    print(df_wide.head(3))
    print(df_wide.tail(3))
    # df_wide.columns = ['_'.join(str(s).strip() for s in col if s) for col in df_wide.columns]
    print(df_wide.columns)
    df_wide.to_csv(f"summary/202011/denue_wide_{i}.csv", index=False)
