rm(list=ls())
setwd("C:/Users/admin/Desktop/iremtech/Geonhui/R_Directory/수과원")
route <- getwd()

File_list <- dir(route,pattern='.csv')

year_Temp <- data.frame(dummy=1:120)


for (excel in File_list){
  #이름가져오기 
  
  year_csv <- strsplit(excel,'_?)[[1]][2]
  
  year <- substr(year_csv,1,4)
  
  data <- read.csv(excel,header=T,stringsAsFactors=F,na.string=c("NA"))
  
  #(name <- paste0("youngduck_2_",year))
  
  youngduck <- subset(data,data$SiteName=="영덕")
  
  youngduck$Temp_S
  year_Temp[,year]?<- youngduck$Temp_S
  
}

year_Temp

