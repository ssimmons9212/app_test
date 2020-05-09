;(function () {
    // Plotly.d3.csv("../static/data/world_wine_data.csv", function(err, rows){
    //     function unpack(rows, key) {
    //         return rows.map(function(row) { return row[key]; });
    //     }
        
        let dropDownData = ["Wine Production", "Largest Vineyards", "Exports", "Imports", "Consumption"]
        

        //Default map data
        setChoroplethMap("Wine Production")

        function setChoroplethMap(wineData){

            d3.json("wine_map_data").then((mapData) => {
                let zValue = ""
                if (wineData === "Wine Production"){
                    zValue = mapData.Wine_Production
                } else if (wineData === "Largest Vineyards"){
                    zValue = mapData.Largest_Vineyards
                } else if (wineData === "Exports"){
                    zValue = mapData.Exports
                } else if (wineData === "Imports"){
                    zValue = mapData.Imports
                } else {
                    zValue = mapData.Consumption
                }

                    
                const unitObj = {
                    "Wine Production": "Wine Production<br>[MhL]", 
                    "Largest Vineyards": "Surface Area in<br>Thousand Hectares<br>[kha]", 
                    "Exports": "Log of Exports<br>in Billions [$]", 
                    "Imports": "Log of Imports<br>in Billions [$]", 
                    "Consumption" : "Million Hectoliters<br>[MhL]"
                }
    
                const textObj = {
                    "Wine Production": mapData.Wine_Production, //unpack(rows, 'Wine Production'), 
                    "Largest Vineyards": mapData.Largest_Vineyards,//unpack(rows, 'Largest Vineyards'), 
                    "Exports": mapData.Exports_Values,//unpack(rows, 'Exports_Values'), 
                    "Imports": mapData.Imports_Values,//unpack(rows, 'Imports_Values'), 
                    "Consumption" : mapData.Consumption//unpack(rows, 'Consumption')
                }
    
                let data = [{
                    type: 'choropleth',
                    locations: mapData.CODES,//unpack(rows, 'CODES'),
                    z: zValue, //unpack(rows, wineData), //chage on click of Z
                    text: textObj[wineData],
                    hoverinfo: "text+location",
                    colorscale: [
                        [0,'rgb(152, 26, 68)'],[0.35,'rgb(200, 70, 110)'],
                        [0.35,'rgb(200, 70, 110)'], [0.6,'rgb(225, 121, 156)'],
                        [0.6,'rgb(225, 121, 156)'],[1,'rgb(220, 220, 220)']
                    ],
                    autocolorscale: false,
                    reversescale: true,
                    marker: {
                        line: {
                            color: 'rgb(180,180,180)',
                            width: 0.5
                        }
                    },
                    type: "choropleth",
                    
                    colorbar: {
                        autotic: true,
                        title: {
                            text: unitObj[wineData],
                            font:{
                                color: "white"
                            }
                        },
                        showticklabels: true,
                        tickfont:{
                            color: "white"
                        }

    
                    }
                }]
    
    
                const titleObj = {
                    "Wine Production": "Total Wine Production", 
                    "Largest Vineyards": "World's Largest Vineyards", 
                    "Exports": "Total Dollar Amount in Exports per Country", 
                    "Imports": "Total Dollar Amount in Imports per Country", 
                    "Consumption" : "Wine Consumption per Country"
                }
                
                var layout = {
    
                    title: {
                        text: titleObj[wineData], 
                        font: {
                            family: "Arial",
                            size: 32,
                            color: "white"
                        }
                    },
                    autosize: true,
                    paper_bgcolor: "rgba(0,0,0,0)",
                    dragmode: false,
                    
                    geo:{
                        showframe: false,
                        showcoastlines: false,
                        projection:{
                            type: 'mercator'
                        }
                    }
                }
                
                Plotly.newPlot("map", data, layout, {displayModeBar: false})
              
            }
            );

        
        }
        
        let innerContainer = document.querySelector(".control-row"),
        plotEl = innerContainer.querySelector('.plot'),
        wineSelector = innerContainer.querySelector('.datasets');

        function assignOptions(textArray, selector) {
            for (i = 0; i < textArray.length;  i++) {
                let currentOption = document.createElement('option');
                currentOption.text = textArray[i];
                selector.appendChild(currentOption);
            }
        }

        assignOptions(dropDownData, wineSelector);

        function updateWine(){
            setChoroplethMap(wineSelector.value);
        }

        wineSelector.addEventListener('change', updateWine, false);
    // })
    
})()






