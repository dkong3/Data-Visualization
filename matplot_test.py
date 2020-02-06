from matplotlib import pyplot as plt
import pandas as pd

df1 = pd.read_excel("Post_RIE_P30_SiN_all_6w.xlsx")
lcdu_pr1 = df1.LCDU[0:189]
lcdu_pr2 = df1.LCDU[189:380]
cd_pr1 = df1.CD[0:189]
cd_pr2 = df1.CD[189:380]

cd_w1 =df1.CD[df1.Wafer_ID == '46HXI128SJA7']
print(cd_w1)

plt.plot(cd_pr1, lcdu_pr1, 'o')
plt.plot(cd_pr2, lcdu_pr2, 'o')
plt.xlabel("CD (nm)")
plt.ylabel("LCDU (nm)")
plt.legend(["PR1", "PR2"])
plt.show()



