(function() {
    d3.csv('static/data/Wine Pairings - Dairy.csv')
        .then(data => {
            console.log(data)
            console.log(data.forEach(entry => entry.wine))            
            const trace1 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.freshsalty),
                name: "Fresh & Salt",
                type: 'bar'
            }
            const trace2 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.delicatenutty),
                name: "Delicate & Nutty",
                type: 'bar'
            }
            const trace3 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.strongfirm),
                name: "Strong & Firm",
                type: 'bar'
            }
            const trace4 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.pungent),
                name: "Pungent",
                type: 'bar'
            }                      
            const layout = {
                title: 'Pairing Ratings by Dairy Groups(Grapes)',
                barmode: 'group',
                xaxis: {
                    title: 'Wine Grapes',
                  },
                  yaxis: {
                    title: 'Pairing Rating',
                  }
            }
            Plotly.newPlot('dairy2', [trace1, trace2, trace3, trace4], layout,{displayModeBar: false})
        })
        .catch(err => console.log(err))       
})()