function whatIsIt(object) {
    var stringConstructor = "test".constructor;
    var arrayConstructor = [].constructor;
    var objectConstructor = {}.constructor;

    if (object === null) {
        return "null";
    }
    else if (object === undefined) {
        return "undefined";
    }
    else if (object.constructor === stringConstructor) {
        return "String";
    }
    else if (object.constructor === arrayConstructor) {
        return "Array";
    }
    else if (object.constructor === objectConstructor) {
        return "Object";
    }
    else {
        return "don't know";
    }
}

function escapeHTML(unsafeText) {
    let div = document.createElement('div');
    div.innerText = unsafeText;
    return div.innerHTML;
}

(function(Handsontable){
    function customRenderer(hotInstance, td, row, column, prop, value, cellProperties) {
        let text;
        switch(whatIsIt(value)){
        case "Object":
            text = '<pre class="cell">' + JSON.stringify(value, null, 2) + '</pre>';
            break;
        case "Array":
            text = '<pre class="cell">' + JSON.stringify(value) + '</pre>';
            break;
        default:
            text = '<div class="cell">' + escapeHTML(Handsontable.helper.stringify(value)) + '</div>';
        }

        td.innerHTML = text;
        return td;
    }

    Handsontable.renderers.registerRenderer('jsonRenderer', customRenderer);
})(Handsontable);

var container = document.getElementById('hotArea');
var actualConfig = {
data: data,
rowHeaders: true,
colHeaders: true,
columns: columns,
manualColumnResize: true,
manualRowResize: true,
renderAllRows: true,
modifyColWidth: (width, col)=>{
    if(width > maxColWidth) return maxColWidth;
},
afterRenderer: (td, row, column, prop, value, cellProperties)=>{
    td.innerHTML = '<div class="wrapper"><div class="wrapped">' + td.innerHTML + '</div></div>';
}
}
Object.assign(actualConfig, config);
actualConfig.colWidths = undefined;

var hot = new Handsontable(container, actualConfig);

let colWidths = [];
[...Array(hot.countCols()).keys()].map(i => {
    colWidths.push(hot.getColWidth(i));
});

switch(whatIsIt(config.colWidths)){
  case "Array":
    config.colWidths.forEach((item, index)=>{
      colWidths[index] = item;
    });
    break;
  case "Object":
    const colHeaders = hot.getColHeader();
    Object.keys(config.colWidths).forEach((item, index)=>{
      colWidths[colHeaders.indexOf(item)] = config.colWidths[item];
    });
    break;
  default:
}

hot.updateSettings({
    colWidths: colWidths,
    modifyColWidth: ()=>{}
});