# OrangeADE

Welcome to the OrangeADE!

OrangeADE stands for Orange Autonomous Device Evaluation. It will verify your router/modem remotely against known vulnerabilities.

This project was started in January 2017 by [CeDeROM Tomasz CEDRO](https://www.tomek.cedro.info) for [Orange POLSKA CERT/SOC](https://cert.orange.pl).

USE AT YOUR OWN RISK! =)

## License

OrangeADE is released under the "new" 3-Clause BSD license. See the [LICENSE](LICENSE) file for more details.

## ChangeLog

Stay tuned for more information! =)

20170101
* Project starts. Creative New Year!

## Dependencies

OrangeADE uses / depends on following components:
* [Python 2.7](http://www.python.org) (Routersploit hard dependency)
* [DJango](https://www.djangoproject.org): pysqlite, importlib  
* [RouterSploit](https://github.com/reverse-shell/routersploit): listed in requirements.txt

## Documentation

* [Virtualenv](doc/virtualenv.md): Python Virtual Environment Reference Manual.

## TODO

- [X] Use Virtualenv (DONE 201701).
- [X] Use DJango (DONE 201701).
  - [X] frontend (DONE 201701).
  - [ ] client session (EXPECTED 201703).
  - [ ] job schedule (EXPECTED 201705).
  - [ ] job connector (EXPECTED 201706).
  - [ ] search cache (EXPECTED 201708).
  - [ ] web cache (EXPECTED 201708).
  - [ ] backend (EXPECTED 201709).
  - [ ] result browser (EXPECTED 201709).
  - [ ] statistics (EXPECTED 201710).
- [ ] Select/Implement Task and Queue Manager (EXPECTED 201709).
- [X] Use Bootstrap (DONE 201701).
- [ ] Use Routersploit (EXPECTED 201706).
- [ ] Use other tools (EXPECTED 201710).
- [ ] Internal testing and development (EXPECTED 201710).
- [ ] Public launch (EXPECTED 201801).


## Troubleshooting

* Django test server does not start correctly: Make sure you did install Python Virtualenv and Dependencies correctly. See [Virtualenv Manual](doc/virtualenv.md) for deteils.
  
* Website starts but looks ugly or some functions are missing: Make sure you did correct bootstrap of git submodules (`git submodule init; git submodule update`).

<hr/>
<sup>(C) 2017 [CeDeROM Tomasz CEDRO](http://www.tomek.cedro.info), All rights reserved! :-)</sup>
