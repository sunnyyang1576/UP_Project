# Created by Cherry at 15.10.2019

import quandl
## this is the script to store all macro-economic values

private_key = "ZKaaB-pEeHGtBu23-5yK"
quandl.ApiConfig.api_key = private_key


# could use the following call to get our data
# details can be found https://www.quandl.com/search?utm_source=google&utm_medium=organic&utm_campaign=&utm_content=api-for-economic-data

# will update later
data = quandl.get("EIA/PET_RWTC_D", returns="numpy")

print(data)