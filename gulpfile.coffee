# include gulp
gulp = require("gulp")

# require things
require('coffee-script/register')
coffee = require("gulp-coffee")
gutil = require('gulp-util')
jshint = require('gulp-jshint')

# do things
gulp.task('default', ["lint"])

gulp.task('lint', [], ->
  gulp.src('friendmemeow/static/js/*.js')
  .pipe(jshint())
  .pipe(jshint.reporter('default'))
  )