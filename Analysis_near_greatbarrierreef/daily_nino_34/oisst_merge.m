clc;clear

oisst_nino_dir = "/Users/richard_zhang/Library/CloudStorage/OneDrive-Personal/A_Melbourne-Uni/A_Weather_for_21st_Century_RA_Internship/Local_Remote_Influences_on_Coastal_Rainfall/Analysis_near_greatbarrierreef/daily_nino_34/oisst_nino.nc";

oisst_2020_1231_dir = "/Users/richard_zhang/Library/CloudStorage/OneDrive-Personal/A_Melbourne-Uni/A_Weather_for_21st_Century_RA_Internship/Local_Remote_Influences_on_Coastal_Rainfall/Analysis_near_greatbarrierreef/daily_nino_34/oisst-avhrr-v02r01_2020_1231.nc";

oisst_large = ncread(oisst_nino_dir, 'sst');
lat = ncread(oisst_2020_1231_dir, 'lat');
lon = ncread(oisst_2020_1231_dir, 'lon');


%%
oisst_large = squeeze(oisst_large);

oisst_day = ncread(oisst_2020_1231_dir, 'sst', [761 ,341,1,1],[200,40,1,1]);
lat = ncread(oisst_2020_1231_dir, 'lat', [341],[40]);
lon = ncread(oisst_2020_1231_dir, 'lon', [761],[200]);

%%

time_oisst_large = ncread(oisst_nino_dir, 'time');

oisst_a = oisst_large(:,:,1:8400);

oisst_b = oisst_large(:,:,8401:end);

%%
oisst_98_22 = zeros(200,40,9131);
oisst_98_22(:,:,1:8400) = oisst_a;
oisst_98_22(:,:,8401) = oisst_day;
oisst_98_22(:,:,8402:end) = oisst_b;

%%
time = linspace(1,9131,9131);
filename = "oisst_nino34area_98_22.nc";

nccreate(filename,'sst','Dimensions',{'lon' 200 'lat' 40 'time' 9131});
nccreate(filename,'lat','Dimensions',{'lat' 40});
nccreate(filename,'lon','Dimensions',{'lon' 200});
nccreate(filename,'time','Dimensions',{'time' 9131});
ncwrite(filename,'lat',lat);
ncwrite(filename,'lon',lon);
ncwrite(filename,'sst',oisst_98_22);
ncwrite(filename,'time',time);
ncdisp(filename);
