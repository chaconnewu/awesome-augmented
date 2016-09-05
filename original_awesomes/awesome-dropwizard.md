# Awesome Dropwizard [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)][awesome] [![Build Status](https://img.shields.io/travis/stve/awesome-dropwizard.svg)][travis]

[<img src="https://cdn.rawgit.com/stve/awesome-dropwizard/master/dropwizard-hat.png" align="right" width="50">][dropwizard]

[awesome]: https://github.com/sindresorhus/awesome
[travis]: https://travis-ci.org/stve/awesome-dropwizard
[dropwizard]: http://www.dropwizard.io

> Useful resources for creating apps with [Dropwizard](http://www.dropwizard.io)

### Contributing

Please take a quick look at the [contribution guidelines](CONTRIBUTING.md) first.

## Editor Support

*Support for your favorite editors.*

### Eclipse

* [dropwizard-tools](https://github.com/Tasktop/dropwizard-tools) - Eclipse Tools for Dropwizard

## Open Source

* [dropwizard-swagger](https://github.com/federecio/dropwizard-swagger) - Serves Swagger UI static content and loads Swagger endpoints.
* [dropwizard-jaxws](https://github.com/roskart/dropwizard-jaxws) - enables building SOAP web services and clients using JAX-WS API.
* [dropwizard-redirect-bundle](https://github.com/bazaarvoice/dropwizard-redirect-bundle) - allows for HTTP redirects.
* [dropwizard-template-config](https://github.com/tkrille/dropwizard-template-config) - enables you to write your config.yaml as a Freemarker template.
* [dropwizard-caching-bundle](https://github.com/bazaarvoice/dropwizard-caching-bundle) - generate cache-control options for resources and caching responses.
* [dropwizard-xml](https://github.com/yunspace/dropwizard-xml) - Dropwizard bundle for processing and validating XMLs
* [dropwizard-crypto](https://github.com/meltmedia/dropwizard-crypto) - A Crytpographic Bundle for Dropwizard
* [dropwizard-circuitbreaker](https://github.com/mtakaki/dropwizard-circuitbreaker) - A circuit breaker design pattern for dropwizard
* [dropwizard-maxmind-bundle](https://github.com/phaneesh/dropwizard-maxmind-bundle) - MaxMind GeoIP2 support for dropwizard
* [dropwizard-protobuf](https://github.com/dropwizard/dropwizard-protobuf) - Support for reading and writing Google Protocol Buffer objects within Dropwizard
* [dropwizard-configurable-assets-bundle](https://github.com/bazaarvoice/dropwizard-configurable-assets-bundle) - An implementation of an AssetBundle for use in Dropwizard that allows user configuration.
* [dropwizard-activemq-bundle](https://github.com/mbknor/dropwizard-activemq-bundle) - send and receive JSON via ActiveMQ in your Dropwizard application

### Data Stores

* [dropwizard-etcd](https://github.com/meltmedia/dropwizard-etcd) - A Dropwizard Bundle for Etcd
* [dropwizard-mongo](https://github.com/eeb/dropwizard-mongo) - Factories and health checks for connecting to mongoDB.
* [dropwizard-elasticsearch](https://github.com/dropwizard/dropwizard-elasticsearch) - A set of classes for using Elasticsearch in a Dropwizard service
* [dropwizard-service-discovery](https://github.com/santanusinha/dropwizard-service-discovery) - Zookeeper service discovery bundle and client for dropwizard.
* [dropwizard-cassandra](https://github.com/composable-systems/dropwizard-cassandra) - Dropwizard support for Cassandra

### Metrics

* [riemann-bundle](https://github.com/phaneesh/riemann-bundle) - Simplifies dropwizard metrics integration into Riemann
* [metrics](http://metrics.dropwizard.io/3.1.0/manual/third-party/) - Metrics Libraries

### Logging

* [dropwizard-gelf](https://github.com/gini/dropwizard-gelf) - Addon bundle for Dropwizard to support logging to a GELF-enabled servers
* [dropwizard-raven](https://github.com/tradier/dropwizard-raven) - Dropwizard integration for error logging to Sentry
* [dropwizard-logstash-encoder](https://github.com/Wikia/dropwizard-logstash-encoder) - Dropwizard logging addon for sending logs using the logstash-logback-encoder

### Scheduled/Recurrence Jobs

* [dropwizard-quartz](https://github.com/jaredstehler/dropwizard-quartz) - Simple Job Scheduler implementation integrating Guice and Quartz.
* [dropwizard-jobs](https://github.com/spinscale/dropwizard-jobs) - Quartz integration for dropwizard
* [dropwizard-sundial](https://github.com/timmolter/dropwizard-sundial) - Scheduled jobs in Dropwizard using Sundial


### Guice

* [dropwizard-guice](https://github.com/HubSpot/dropwizard-guice) - Adds support for Guice.
* [dropwizard-guicey](https://github.com/xvik/dropwizard-guicey) - Dropwizard guice integration
* [dropwizard-guicier](https://github.com/HubSpot/dropwizard-guicier) - A Dropwizard bundle to handle Guice integration.

## Tutorials

* [Getting Started](http://www.dropwizard.io/0.9.2/docs/getting-started.html)
* [Official docs](http://www.dropwizard.io/0.9.2/docs/manual/index.html)
* [Dropwizard internals](http://www.dropwizard.io/0.9.2/docs/manual/internals.html)
* [Dropwizard Modules Directory](http://modules.dropwizard.io/)

## Guides

* [Serving Static Assets with DropWizard](https://spin.atomicobject.com/2014/10/11/serving-static-assets-with-dropwizard/)
* [Hooking up Custom Jersey Servlets in Dropwizard](https://spin.atomicobject.com/2015/03/30/jersey-servlets-dropwizard/)
* [Using Hibernate DAOs in DropWizard Tasks](https://spin.atomicobject.com/2015/02/03/dropwizard-hibernate-dao/)
* [Hibernate in Dropwizard CLI Commands](http://clearthehaze.com/2015/04/hibernate-in-dropwizard-cli-commands/)
* [Heroku for Highly Available Dropwizard Apps](http://techbytes.anuragkapur.com/2015/05/heroku-for-highly-available-dropwizard.html?m=1)
* [Enabling Newrelic for Dropwizard](http://kyleboon.org/blog/2013/09/23/newrelic-for-dropwizard/)
* [Application Health Checks with DropWizard](http://willhamill.com/2014/12/04/application-health-checks-with-dropwizard)
* [Using Hystrix with Dropwizard](http://christopher-batey.blogspot.com/2014/08/using-hystrix-with-dropwizard.html)
* [Using Dropwizard in combination with Elasticsearch](http://www.gridshore.nl/2014/05/15/using-dropwizard-combination-elasticsearch/)
* [Deploy a Dropwizard Unikernel to AWS](https://boxfuse.com/blog/dropwizard-aws.html)
* [Use Consul's KV store for Dropwizard settings](http://blog.remmelt.com/2015/06/09/use-consuls-kv-store-for-dropwizard-settings/)
* [Effective Health Checks With Dropwizard](https://opsee.com/guides/dropwizard/)

## Community

* [dropwizard-user](https://groups.google.com/forum/#!forum/dropwizard-user)
* [StackOverflow](http://stackoverflow.com/questions/tagged/dropwizard)
* [`@dropwizardio` on twitter](https://twitter.com/dropwizardio)

## Videos

* [Introduction to Dropwizard](https://www.youtube.com/watch?v=2tSWsjtw0ms)
* [Instant-ish Real Service Architecture](https://vimeo.com/37930578)

## Contribute

Contributions welcome! Read the [contribution guidelines](CONTRIBUTING.md) first.

## Awesome!

Check out more [awesome projects](https://github.com/sindresorhus/awesome).

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Steve Agalloco](http://beforeitwasround.com) has waived all copyright and related or neighboring rights to this work.
