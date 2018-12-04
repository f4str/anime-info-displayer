const { PythonShell } = require("python-shell");
const items = {
    'rank': 'rank',
    'pic': 'image',
    'name': 'title',
    'type': 'type',
    'ep': 'episodes',
    'date': ['start_date', 'end_date'],
    'score': 'score'
};

function loadHomePage() {
    let options = {
        mode: 'json',
        pythonOptions: ['-u'],
        scriptPath: 'parser'
    };

    PythonShell.run('query.py', options, function (err, results) {
        if (err) {
            throw err;
        }
        generateTable(results);
    });
}

function search(title) {
    let options = {
        mode: 'json',
        pythonOptions: ['-u'],
        scriptPath: 'parser', 
        args: [title]
    };

    PythonShell.run('query.py', options, function (err, results) {
        if (err) {
            throw err;
        }
        generateTable(results);
    });
}

function generateTable(results) {
    let table = document.getElementById('result-table');
    table.innerHTML = table.rows[0].innerHTML;
    
    results.forEach((row) => {
        var tr = document.createElement('tr');
        tr.classList.add('row');
        for (i in items) {
            var td = document.createElement('td');
            td.classList.add(i, 'col');
            if (i == "date") {
                let start = row[items[i][0]] ? row[items[i][0]] : "Present";
                let end = row[items[i][1]] ? row[items[i][1]] : "Present";
                td.innerHTML = start + " -<br /> " + end;
            }
            else if (i == 'pic') {
                td.innerHTML = "<img class='image' src='" + row[items[i]] + "'>";
            }
            else if (i == 'score') {
                td.innerHTML = row[items[i]].toFixed(2) + "/10";
            }
            else {
                td.innerHTML = row[items[i]] ? row[items[i]] : "N/A";
            }
            tr.appendChild(td);
        }
        table.appendChild(tr);
    });
}
