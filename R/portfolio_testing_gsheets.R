## hypothetical market crash return estimates 
## get portfolio data from google sheet
## reminds of HF "db" haha
## save with encoding "EUC-KR"
## jyk4100
## last modified: 2021-05-08

library(data.table)
library(googlesheets4)
setwd("C:/Users/Kim Jungyoon/Documents/2.study/coding/R")

## read my portfolio data in google sheets (multiple accounts consolidated) ------------------------

## auth through web interface is there more programmatic way??
# url = "https://docs.google.com/spreadsheets/d/1AydUZEV2mmjpgW6vD-ldi7jHSU4BstG0l2o8x9Olhgw/"
sheet_id = "1AydUZEV2mmjpgW6vD-ldi7jHSU4BstG0l2o8x9Olhgw"

# test = read_sheet(ss=sheet_id, sheet=2, range="마이주식!A1:N100") ## range needs to specify sheetname?
port = read_sheet(ss=sheet_id, sheet=2, range="A1:N100") ## range needs to specify sheetname?
setDT(port)

## cleanup
names(port) = c("action","industry","account","name","ticker","Q","P","C","col","proportion","PQ","CQ","pUG","UG")
port[, c("action","col","name", "proportion", "pUG", "UG") := NULL]
port = port[!is.na(port$account), ]
port[, c("account") := factor(port$account, level=c("로빈후드","위불","이트레이드"), labels=c("RH","WB","ET"))]


## 떡락 가정
# crash_pcts = c(0.01, 0.05, 0.10, 0.15, 0.2, 0.25, 0.3)
crash_pcts = seq(from=0.01, to=0.45, by=0.01)
port_sum = get_portsum(port, 0.00)
for(crash_pct in crash_pcts) {
  port_sum = rbind(port_sum, get_portsum(port, crash_pct))
}
setorder(port_sum, "crashpct", "account")
View(port_sum[port_sum$account == "overall", ])

## plot ## eh just line
## 25 프로 떡락 고대로 맞으면 음전 ㅋㅋㅋㅋ
par(mfrow=c(2,2), mar=c(4,4,1,1))
plot(port_sum[port_sum$account == "overall", ]$crashpct, port_sum[port_sum$account == "overall", ]$totalUG,
     xlab="marketdown %", ylab="totalUG_overall")  ; abline(h=0, lty=2, col=2)
plot(port_sum[port_sum$account == "RH", ]$crashpct, port_sum[port_sum$account == "RH", ]$totalUG,
     xlab="marketdown %", ylab="totalUG_RH")  ; abline(h=0, lty=2, col=2)
plot(port_sum[port_sum$account == "WB", ]$crashpct, port_sum[port_sum$account == "WB", ]$totalUG,
     xlab="marketdown %", ylab="totalUG_WB")  ; abline(h=0, lty=2, col=2)
plot(port_sum[port_sum$account == "ET", ]$crashpct, port_sum[port_sum$account == "ET", ]$totalUG,
     xlab="marketdown %", ylab="totalUG_ET")  ; abline(h=0, lty=2, col=2)
par(mfrow=c(2,2), mar=c(4,4,1,1))
plot(port_sum[port_sum$account == "overall", ]$crashpct, port_sum[port_sum$account == "overall", ]$pctUG,ylim=c(-30, 50),type='l',
     xlab="marketdown %", ylab="totalUG_overall")  ; abline(h=0, lty=2, col=2)
plot(port_sum[port_sum$account == "RH", ]$crashpct, port_sum[port_sum$account == "RH", ]$pctUG,ylim=c(-30, 50),type='l',
     xlab="marketdown %", ylab="totalUG_RH")  ; abline(h=0, lty=2, col=2)
plot(port_sum[port_sum$account == "WB", ]$crashpct, port_sum[port_sum$account == "WB", ]$pctUG,ylim=c(-30, 50),type='l',
     xlab="marketdown %", ylab="totalUG_WB")  ; abline(h=0, lty=2, col=2)
plot(port_sum[port_sum$account == "ET", ]$crashpct, port_sum[port_sum$account == "ET", ]$pctUG,ylim=c(0, 120),type='l',
     xlab="marketdown %", ylab="totalUG_ET")  ; abline(h=0, lty=2, col=2)



##
get_portsum = function(df_param, crash_pct) {
  df = copy(df_param)
  df[, c("P2") := df$P * (1 - crash_pct)]
  df[, c("PQ2") := df$P2 * port$Q]
  df[, c("UG2") := df$PQ2 - port$CQ]
  dfsum = df[, j=list("totalUG"=sum(UG2), 
                          "pctUG"=round(sum(UG2)/sum(CQ)*100,2)), by=list(account)]
  dfsum_overall = df[, j=list("totalUG"=sum(UG2), 
                              "pctUG"=round(sum(UG2)/sum(CQ)*100,2))]
  dfsum_overall[, c("account") := "overall"]
  dfsum = rbind(dfsum, dfsum_overall)
  dfsum[, c("crashpct") := crash_pct]
  return(dfsum)
}
