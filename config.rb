require 'lib/carm'

Slim::Engine.disable_option_validator!

set :site_title, 'Computational Journalism'
set :site_deck, 'Stanford COMM 177A/277A'
set :site_author, "Dan Nguyen"
set :class_start_date, '2015-03-30'
set :site_domain, 'http://www.compjour.org'
set :stash_domain, 'http://stash.compjour.org'

set :site_description, "Data-mining, analysis, and visualization for civic purposes"
set :google_analytics_id, 'UA-61452895-1'
set :google_custom_search_id, '012541043402465721355:gangr7fszpw'
activate :directory_indexes
activate :i18n, :mount_at_root => :en
activate :livereload
activate :syntax, :line_numbers => false

######### assets
set :markdown_engine, :kramdown
set :markdown, :toc_levels => 1..3
set :slim, :pretty => true

set :trailing_slash, true
set :css_dir, 'assets/stylesheets'
set :js_dir, 'assets/javascripts'
set :images_dir, 'assets/images'

######### layout stuff
set :layout, 'page'
page "/tutorials/*", :layout => "content_article"
page "/articles/*", :layout => "content_article"
page "/files/code/**/*.html", :directory_index => false

############################# Build-specific configuration
configure :build do

end




activate :s3_sync do |s3_sync|
  s3_sync.bucket                     = 'www.compjour.org' # The name of the S3 bucket you are targetting. This is globally unique.
  s3_sync.region                     = 'us-east-1'     # The AWS region for your bucket.
  s3_sync.delete                     = false # We delete stray files by default.
  s3_sync.after_build                = true # We do not chain after the build step by default.
  s3_sync.prefer_gzip                = false
  s3_sync.path_style                 = true
  s3_sync.reduced_redundancy_storage = false
  s3_sync.acl                        = 'public-read'
  s3_sync.encryption                 = false
  s3_sync.prefix                     = ''
end


