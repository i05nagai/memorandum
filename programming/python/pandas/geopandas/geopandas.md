---
title: geopandas
---

## geopandas


## Tips

### Convert pandas DF to geopandas DF
* [csv \- Convert a pandas DataFrame to a GeoDataFrame \- Geographic Information Systems Stack Exchange](https://gis.stackexchange.com/questions/174159/convert-a-pandas-dataframe-to-a-geodataframe)


from 

```
import geopandas as gpd
import shapely.wkt

geometry = df['wktcolumn'].map(shapely.wkt.loads)
df = df.drop('wktcolumn', axis=1)
crs = {'init': 'epsg:4326'}
gdf = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)
```

## Reference
kkk
