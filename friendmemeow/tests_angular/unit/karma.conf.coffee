module.exports = (config) ->
  config.set
    basePath: './'
    frameworks: ['jasmine']
    files: [
      './**/*.coffee'
    ]
    exclude: []
    preprocessors: {
      './*.coffee': ['coffee']
    }
    coffeePreProcessor: {
      base: false
      sourceMap: true
    }
    browsers: ['Chrome']
    port: 9876
    autoWath: true
    singleRun: true


