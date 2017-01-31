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

- [X] Use Virtualenv. 
- [X] Use DJango.
  - [X] frontend.
  - [ ] client session.
  - [ ] job schedule.
  - [ ] job connector.
  - [ ] search cache.
  - [ ] web cache.
  - [ ] backend.
  - [ ] result browser.
  - [ ] statistics.
- [ ] Select/Implement Task and Queue Manager.
- [X] Use Bootstrap.
- [ ] Use Routersploit.

## Troubleshooting

* Django test server does not start correctly: Make sure you did install Python Virtualenv and Dependencies correctly. See [Virtualenv Manual](doc/virtualenv.md) for deteils.
  
* Website starts but looks ugly or some functions are missing: Make sure you did correct bootstrap of git submodules (`git submodule init; git submodule update`).

<hr/>
<sup>(C) 2017 [CeDeROM Tomasz CEDRO](http://www.tomek.cedro.info), All rights reserved! :-)</sup>
