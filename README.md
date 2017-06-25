# Logs Analysis

### Required Items:

*[Vagrant](https://www.vagrantup.com/) Virtual environment*  
*[VirtualBox](https://www.virtualbox.org/)*  
[newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) SQL data for analysis.  
[VM FS Configuration file](https://d17h27t6h515a5.cloudfront.net/topher/2017/June/5948287e_fsnd-virtual-machine/fsnd-virtual-machine.zip) This directory will give you FSND-Virtual-Machine file.  

### Installation

1. Clone the repository and connect to the virtual machine. Make sure newsdata.sql file is in /FSND-Virtual-Machine/vagrant/. 

Clone into the directory: /FSND-Virtual-Machine/vagrant 

```
$ git clone https://github.com/jaafsong/FSND-Project-2-LogAnalysis.git
```

2. Connect to the Virtual Machine from /FSND-Virtual-Machine/vagrant.

```
$ vagrant up
$ vagrant ssh
```

3. Load DB --> Connect to DB. 

```
$ cd /vagrant
$ psql -d news -f newsdata.sql
$ psql -d news
```

4. Create Views:

```
CREATE VIEW countviews_view AS (select title, author, count(*) AS quant FROM articles,log WHERE log.path=CONCAT('/article/',articles.slug) GROUP BY articles.title,articles.author ORDER BY quant DESC);
```


### Results: 

$ python newsdata.py 

```

/vagrant$ python newsdb.py 

 * The Top 3 Most Viewed Articles are:

	Candidate is jerk, alleges rival | --> | 338647 views
	Bears love berries, alleges bear | --> | 253801 views
	Bad things gone, say good people | --> | 170098 views

 * The Most Popular Article Authors are:

	Ursula La Multa | --> | 507594 views
	Rudolf von Treppenwitz | --> | 423457 views
	Anonymous Contributor | --> | 170098 views
	Markoff Chaney | --> | 84557 views

 * Days Greater than 1% with Request Errors:

	2016-07-17 | --> | 2.263 %

```


