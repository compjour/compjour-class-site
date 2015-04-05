class ContentArticle
  attr_reader :title, :description, :curriculum_order, :slug, :base_slug, :url, :path

  def initialize(resource)
    @url    = resource.url
    @path   = resource.path
    @slug = ContentArticle.slugify(@path)
    @base_slug = ContentArticle.base_slugify(@path)

    @title  = resource.data.title
    @curriculum_order = resource.data.curriculum_order
    @description = resource.data.description


    _n = resource.data.nav || {}
    @nav_next = _n[:next]
    @nav_prev = _n[:prev]
    @nav_overview = _n[:part_of]
  end

  def nav?
    nav_next? || nav_prev? || nav_overview?
  end

  def nav_next?; @nav_next.present?; end
  def nav_overview?; @nav_overview.present?; end
  def nav_prev?; @nav_prev.present?; end

  def next_nav_article
    @nav_next
  end

  def prev_nav_article
    @nav_prev
  end

  def overview_nav_article
    @nav_overview
  end


  def self.slugify(path)
    path.strip.sub(/\.html$/, '').sub(/^\//, '').sub(/\/$/, '')
  end

  def self.base_slugify(path)
    File.basename(path).strip.sub(/\.html$/, '').sub(/^\//, '').sub(/\/$/, '')
  end

end


def ContentArticle(obj)
  ContentArticle.new(obj)
end
