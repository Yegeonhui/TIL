rm(list=ls())

route=getwd()

strsplit(route,"/")

File_list <- dir(route,pattern=".csv")
File <- File_list[1]

name <- strsplit(File,"_")[[1]][1]
year_Ex<- strsplit(File,"_")[[1]][2]

year_Ex

#문자열길이
year <- 1:(nchar(year_Ex)-4)
year

for (File in File_list){
  File[1]
}

