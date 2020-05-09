function loadWineData(){
  renderGrapeBody()
  wineClicked = d3.select(this).text()
  renderPlot(wineClicked)
  renderWineBlurb(wineClicked)
}
function renderGrapeBody(){
  d3.selectAll(`#featured-grape`).html(
    `  <div class="row">
    <h1><b id="grape-header">Grape</b></h1>
  </div>
    <br>
    <div class="row">
      <div class="column">
        
          <h2>Wine Tasting Metrics</h2>
        
      </div>
      <div class="column">
        
          <h2>Wine Info</h2>
        
      </div>
    </div>
    <div class="row">
      <div class="column">
      
          <div id="wine_plot"></div>
        
      </div>
      <div class="column">
        <div id="wine-info">
          <p id = "wine-blurb">This is the Wine Blurb</p>  
        </div>
      </div>
    </div>`
  )
}
function renderPlot(wine){
    d3.json(`wine_data/${wine}`).then((wine_data) => {
        let data = [{
          type: "scatterpolar",
          r: wine_data.Attribute_Values,
          opacity: .7,
          theta: wine_data.Attribute_Labels,
          line: {
             color: "#000000",
             width: 3
          },
          mode: "markers",
          fill: "toself",
          fillcolor: "#DB3256",
          hoverinfo: "r"
          }];
          
          let layout = {
            polar: {
              radialaxis: {
                visible: true,
                showticklabels: false,
                showline: false
              }
            },
            showlegend: false,
            height: 600,
            width: 600,
            paper_bgcolor: "rgba(0,0,0,0)",
            font:{
              size: 15,
              color: "white"
            }
          };
          Plotly.newPlot('wine_plot', data, layout, {displayModeBar: false});
    })
}
function renderWineBlurb(wine){
  d3.json(`wine_blurb/${wine}`).then((wineBlurb) => {
    d3.select(`#grape-header`).html(wineBlurb.Wine)
    d3.select("#wine-blurb").html(wineBlurb.Blurb)
  }) 
}
d3.selectAll(".dropdown-content").selectAll("a").on("click", loadWineData)
if (wineSelection != "blank"){
  renderGrapeBody()
  renderPlot(wineSelection)
  renderWineBlurb(wineSelection)
  wineSelection = "blank" 
}









