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
	let table = document.getElementById("result-table");

	let db = new sqlite3.Database('database/db.sqlite3');
	db.all("SELECT * FROM anime ORDER BY rank ASC LIMIT 25", function (err, rows) {
		if (err) {
			throw err;
		}
		rows.forEach((row) => {
			console.log(row);

			var tr = document.createElement("tr");
			tr.classList.add("row");

			/*var rank = document.createElement("td");
			rank.classList.add("rank", "col");
			rank.innerHTML = row['rank'];
			tr.appendChild(rank);*/
			
			for (let i in items) {
				var td = document.createElement('td');
				td.classList.add(i, 'col');
				if (i == "date") {
					let start = row[items[i][0]] ? row[items[i][0]] : "Present";
					let end = row[items[i][1]] ? row[items[i][1]] : "Present";
					td.innerHTML = start + " - " + end;
				}
				else if (i == 'pic') {
					td.innerHTML = "<img class='image' src='" + row[items[i]] + "'>";
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