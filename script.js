const { PythonShell } = require("python-shell");
const electron = require('electron');
const items = {
	'table-rank': 'rank',
	'table-picture': 'image',
	'table-name': 'title',
	'table-type': 'type',
	'table-episodes': 'episodes',
	'table-date': ['start_date', 'end_date'],
	'table-score': 'score'
};
const months = ['', 'January ', 'February ', 'March ', 'April ', 'May ', 'June ', 'July ', 'August ', 'September ', 'October ', 'December '];

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
		let tr = document.createElement('tr');
		tr.classList.add('row');
		for (i in items) {
			let td = document.createElement('td');
			td.classList.add(i, 'col');
			td.addEventListener('click', function () {
				createAnimePage(row['id']);
			});
			if (i == "table-date") {
				let start = row[items[i][0]] ? row[items[i][0]] : "Present";
				let end = row[items[i][1]] ? row[items[i][1]] : "Present";
				td.innerHTML = start + " -<br /> " + end;
			}
			else if (i == 'table-picture') {
				td.innerHTML = "<img class='table-image' src='" + row[items[i]] + "'>";
			}
			else if (i == 'table-score') {
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

function createAnimePage(id) {
	let newWindow = new electron.remote.BrowserWindow({
		width: 1024, 
		height: 768, 
		title: id.toString()
	});
	newWindow.loadFile('anime.html');
}

function loadAnimePage() {
	id = parseInt(electron.remote.getCurrentWindow().getTitle());
	
	let options = {
	    mode: 'json',
	    pythonOptions: ['-u'],
	    scriptPath: 'parser', 
	    args: [id]
	};

	PythonShell.run('search.py', options, function (err, results) {
	    if (err) {
	        throw err;
		}
		generatePage(results);
	});
}

function generatePage(results) {
	let anime = results[0];
    let tree = results[1];
    
    console.log(anime);
    
    document.getElementById('name').innerHTML = anime['title'];
    document.getElementById('japanese-name').innerHTML = anime['title'];
    document.getElementById('english-name').innerHTML = anime['title_english'];
    document.getElementById('picture').src = anime['image'];
    document.getElementById('score').innerHTML = anime['score'];
    document.getElementById('episodes').innerHTML = anime['episodes'];
    document.getElementById('status').innerHTML = anime['airing'] ? "Airing" : "Finished Airing";
    document.getElementById('rank').innerHTML = anime['rank']; 
    document.getElementById('popularity').innerHTML = anime['popularity'];
    document.getElementById('premiered').innerHTML = anime['premiered'];
    document.getElementById('start-date').innerHTML = months[anime['startdate']['month']] + anime['startdate']['day'] + ", " + anime['startdate']['year'];
    document.getElementById('end-date').innerHTML = months[anime['enddate']['month']] + anime['enddate']['day'] + ", " + anime['enddate']['year'];
    
}
