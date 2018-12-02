const PythonShell = require("python-shell");
const sqlite3 = require('sqlite3').verbose();
const items = {
	'rank': 'rank', 
	'pic': 'image',
	'name': 'title',
	'type': 'type',
	'ep': 'episodes',
	'date': ['start_date', 'end_date'],
	'score': 'score'
};

function loadMainPage() {
    let sql = "SELECT * FROM anime ORDER BY rank ASC LIMIT 25";
	createTable(sql);
}

function loadSearch(text) {
    let sql = "SELECT * FROM anime WHERE title LIKE '%" + text + "%' ORDER BY rank ASC LIMIT 25";
    createTable(sql);
}

function createTable(sql) {
    let table = document.getElementById("result-table");
    table.innerHTML = table.rows[0].innerHTML;
    
    let db = new sqlite3.Database('parser/db.sqlite3');
    
    db.all(sql, function (err, rows) {
		if (err) {
			throw err;
		}
		rows.forEach((row) => {
			var tr = document.createElement("tr");
			tr.classList.add("row");
			
			for (let i in items) {
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
	});
	db.close();
}