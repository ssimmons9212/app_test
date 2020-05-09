;(function () {
    Plotly.d3.csv("../static/data/world_wine_data.csv", function(err, rows){
        function unpack(rows, key) {
            return rows.map(function(row) { return row[key]; });
        }
        
        let dropDownData = ["Wine Production", "Largest Vineyards", "Exports", "Imports", "Consumption"]
        

        //Default map data
        setChoroplethMap("Wine Production")

        function setChoroplethMap(wineData){

            

            const unitObj = {
                "Wine Production": "Wine Production<br>[MhL]", 
                "Largest Vineyards": "Surface Area in<br>Thousand Hectares<br>[kha]", 
                "Exports": "Log of Exports<br>in Billions [$]", 
                "Imports": "Log of Imports<br>in Billions [$]", 
                "Consumption" : "Million Hectoliters<br>[MhL]"
            }

            const textObj = {
                "Wine Production": unpack(rows, 'Wine Production'), 
                "Largest Vineyards": unpack(rows, 'Largest Vineyards'), 
                "Exports": unpack(rows, 'Exports_Values'), 
                "Imports": unpack(rows, 'Imports_Values'), 
                "Consumption" : unpack(rows, 'Consumption')
            }

            let data = [{
                type: 'choropleth',
                locations: unpack(rows, 'CODES'),
                z: unpack(rows, wineData), //chage on click of Z
                text: textObj[wineData],
                hoverinfo: "text+location",
                colorscale: [
                    [0,'rgb(5, 10, 102)'],[0.35,'rgb(40, 60, 190)'],
                    [0.35,'rgb(40, 60, 190)'], [0.6,'rgb(90, 120, 245)'],
                    [0.6,'rgb(90, 120, 245)'],[1,'rgb(220, 220, 220)']
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
                    title: unitObj[wineData],
                    showticklabels: true

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
                        size: 32
                    }
                },
                autosize: true,

                dragmode: false,
                geo:{
                    showframe: false,
                    showcoastlines: false,
                    projection:{
                        type: 'mercator'
                    }
                }
            }
            
            Plotly.newPlot("map", data, layout, {showLink: false});   
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
    })
})()






