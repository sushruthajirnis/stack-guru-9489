function () {
  var config = {};
  var test_env = karate.properties['TESTENV'];
  var test_suite = karate.properties['SUITE'];

  if(test_env && test_suite){

    karate.log('Running tests for the '+test_env+' with test suite '+test_suite);
    var properties = karate.read('classpath:' + test_env + '-urls.json');
    var data = karate.read('classpath:' + test_env + '-data.json');
    if(properties[test_env]){
      config['base_url']=properties[test_env]['base_url'];
    }
    if(data && data[test_env]){
      config['data']=data[test_env]['data'];
    }
  }

  return config;
}