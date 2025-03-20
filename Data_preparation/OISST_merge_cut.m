clc;clear

% Script to merge multiple NetCDF files into yearly files
% For TRMM 3B42 Daily data (3B42_Daily.YYYYMMDD.7.nc4)

% Directory containing all NetCDF files
inputDir = 'C:\Users\lv299\OneDrive\A_Melbourne-Uni\A_Weather_for_21st_Century_RA_Internship\Local_Remote_Influences_on_Coastal_Rainfall\Data_preparation\OISST';  % Update this path

% Directory to save yearly output files
outputDir = 'C:\Users\lv299\OneDrive\A_Melbourne-Uni\A_Weather_for_21st_Century_RA_Internship\Local_Remote_Influences_on_Coastal_Rainfall\Data_preparation';  % Update this path

% Create output directory if it doesn't exist
if ~exist(outputDir, 'dir')
    mkdir(outputDir);
end

% Get list of all NetCDF files
fileList = dir(fullfile(inputDir, 'oisst-avhrr-v02r01_*.nc'));
fprintf('Found %d files to process\n', length(fileList));

%%


lat = ncread("oisst-avhrr-v02r01_1998.nc", "lat");
lon = ncread("oisst-avhrr-v02r01_1998.nc", "lon");

%%
northeast_sst = [];

lat_cut = ncread("C:\Users\lv299\OneDrive\A_Melbourne-Uni\A_Weather_for_21st_Century_RA_Internship\Local_Remote_Influences_on_Coastal_Rainfall\Data_preparation\OISST\oisst-avhrr-v02r01_1998.nc", 'lat', 240, 82);
lon_cut = ncread("C:\Users\lv299\OneDrive\A_Melbourne-Uni\A_Weather_for_21st_Century_RA_Internship\Local_Remote_Influences_on_Coastal_Rainfall\Data_preparation\OISST\oisst-avhrr-v02r01_1998.nc", 'lon', 560, 82);

for i = 1:22
    fileDir = append(fileList(i).folder,"\" ,fileList(i).name)
    northeast_sst = cat(4, northeast_sst, ncread(fileDir, 'sst', [560,240,1,1],[82,82,1,Inf])) ;
    disp(i)
end

%%
northeast_sst = squeeze(northeast_sst);

%%
time = linspace(1,8035,8035);


%%
file_output = "northeast_sst.nc";
nccreate(file_output, 'sst', 'Dimensions',{'lon' 82 'lat' 82 'time' 8035});
nccreate(file_output, 'lat', 'Dimensions', {'lat' 82});
nccreate(file_output, 'lon', 'Dimensions',{'lon', 82});
nccreate(file_output, 'time', 'Dimensions',{'time' 8035});

ncwrite(file_output, 'lat', lat_cut);
ncwrite(file_output, 'lon', lon_cut);
ncwrite(file_output, 'time', time);
ncwrite(file_output, 'sst', northeast_sst);


