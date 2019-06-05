const { PythonShell } = require("python-shell");
const { remote } = require('electron');
const items = {
	'table-rank': 'rank',
	'table-picture': 'image_url',
	'table-name': 'title',
	'table-type': 'type',
	'table-episodes': 'episodes',
	'table-date': ['start_date', 'end_date'],
	'table-score': 'score'
};
const months = ['', 'January ', 'February ', 'March ', 'April ', 'May ', 'June ', 'July ', 'August ', 'September ', 'October ', 'November ', 'December '];

function loadHomePage() {
	let options = {
		mode: 'json',
		pythonOptions: ['-u'],
		scriptPath: 'models'
	};

	PythonShell.run('query.py', options, function (err, results) {
		if (err) {
			throw err;
		}
		generateTable(results);
	});
}

function search(title) {
	if (!title) {
		loadHomePage();
		return;
	}
	
	let options = {
		mode: 'json',
		pythonOptions: ['-u'],
		scriptPath: 'models',
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
		for (let i in items) {
			let td = document.createElement('td');
			td.classList.add(i, 'col');
			td.addEventListener('click', function () {
				createAnimePage(row['mal_id']);
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
				td.innerHTML = row[items[i]] ? row[items[i]].toFixed(2) + "/10" : "N/A";
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
	let newWindow = new remote.BrowserWindow({
		width: 1024, 
		height: 768, 
		title: id.toString()
	});
	newWindow.loadFile('views/anime.html');
}

function loadAnimePage() {
	id = parseInt(remote.getCurrentWindow().getTitle());
	
	let options = {
		mode: 'json',
		pythonOptions: ['-u'],
		scriptPath: 'models', 
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
	
	remote.getCurrentWindow().setTitle(anime['title']);
	
	document.getElementById('name').innerHTML = anime['title'];
	document.getElementById('japanese-name').innerHTML = anime['title'];
	document.getElementById('english-name').innerHTML = anime['title_english'];
	document.getElementById('picture').src = anime['image'];
	document.getElementById('score').innerHTML = anime['score'] ? anime['score'].toFixed(2) : "N/A";
	document.getElementById('episodes').innerHTML = anime['episodes'];
	document.getElementById('status').innerHTML = anime['airing'] ? "Airing" : "Finished Airing";
	document.getElementById('rank').innerHTML = anime['rank']; 
	document.getElementById('popularity').innerHTML = anime['popularity'];
	document.getElementById('premiered').innerHTML = anime['premiered'];
	document.getElementById('start-date').innerHTML = months[anime['startdate']['month']] + anime['startdate']['day'] + ", " + anime['startdate']['year'];
	document.getElementById('end-date').innerHTML = !anime['airing'] ? months[anime['enddate']['month']] + anime['enddate']['day'] + ", " + anime['enddate']['year'] : "N/A";
	document.getElementById('rating').innerHTML = anime['rating'];
	document.getElementById('duration').innerHTML = anime['duration'];
	document.getElementById('source').innerHTML = anime['source'];
	document.getElementById('broadcast').innerHTML = anime['broadcast'];
	document.getElementById('studio').innerHTML = anime['studio'];
	document.getElementById('licensor').innerHTML = anime['licensor'];
	
	let genres = "";
	anime['genres'].forEach((genre) => {
		genres = genres + genre + ', ';
	});
	document.getElementById('genres').innerHTML = genres.substring(0, genres.length - 2);
	
	let ol = document.createElement('ol');
	anime['openings'].forEach((opening) => {
		let li = document.createElement('li');
		li.innerHTML = opening;
		ol.appendChild(li);
	});
	document.getElementById('openings').replaceWith(ol);
	
	ol = document.createElement('ol');
	anime['endings'].forEach((opening) => {
		let li = document.createElement('li');
		li.innerHTML = opening;
		ol.appendChild(li);
	});
	document.getElementById('endings').replaceWith(ol);
	
	document.getElementById('synopsis').innerHTML = anime['synopsis'];
	
	let p = document.createElement('p');
	p.classList.add('small-text');
	for (let i in anime['related']) {
		let span = document.createElement('span');
		span.classList.add('bold');
		span.innerHTML = i + ": <br />";
		let ul = document.createElement('ul');
		for (let j in anime['related'][i]) {
			let li = document.createElement('li');
			li.innerHTML = anime['related'][i][j]['name']; 
			ul.appendChild(li);
		}
		p.appendChild(span);
		p.appendChild(ul);
	}
	document.getElementById('related').replaceWith(p);
	
	document.getElementById('main-container').style.display = 'block';
}
