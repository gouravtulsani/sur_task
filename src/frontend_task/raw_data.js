document.addEventListener('DOMContentLoaded', function() {
    var gridDiv = document.querySelector('#myGrid');
    var gridOptions = {
        columnDefs: [
            {
                headerName: 'Age', field: 'age',  resizable: true, filter: "agTextColumnFilter",
            },{
                headerName: 'Work_class', field: 'work_class',  resizable: true, filter: "agTextColumnFilter",
            },{
                headerName : 'Fnl-wgt', field : 'fnlwgt', resizable: true, filter: "agTextColumnFilter",
            },{
                headerName: 'Education', field: 'education',  resizable: true, filter: "agTextColumnFilter",
            },{
                headerName: 'Ed_no', field: 'ed_no',  resizable: true, filter: "agTextColumnFilter",
            },{
                headerName: 'Marital_status', field: 'marital_status', resizable: true, filter: "agTextColumnFilter",
            },{
                headerName: 'Occupation', field: 'occupation',  resizable: true, filter: "agTextColumnFilter",
            },{
                headerName: 'Relation', field: 'relationship',  resizable: true, filter: "agTextColumnFilter",
            },{
                headerName: 'Race', field: 'race',  resizable: true, filter: "agTextColumnFilter",
            },{
                headerName: 'Sex', field: 'sex',  resizable: true, filter: "agTextColumnFilter",
            },{
                headerName: 'Capital_gain', field: 'capital_gain',  resizable: true, filter: "agTextColumnFilter",
            },{
                headerName: 'Capital_loss', field: 'capital_loss',  resizable: true, filter: "agTextColumnFilter",
            },{
                headerName: 'Hours_per_week', field: 'hours_per_week',  resizable: true, filter: "agTextColumnFilter",
            },{
                headerName: 'Native_country', field: 'native_country',  resizable: true, filter: "agTextColumnFilter",
            },{
                headerName: 'Income', field: 'income_range',  resizable: true, filter: "agTextColumnFilter",
            }
        ],
        rowData: []
    };
    new agGrid.Grid(gridDiv, gridOptions);
    fetch('http://localhost:8000/raw_data')
    .then(response => response.json())
    .then(data => {
        var raw_data = data.result
        console.log(data.keys)
        gridOptions.api.setRowData(raw_data)
        gridOptions.api.sizeColumnsToFit()
    })
    .catch(error => console.error(error))
});
