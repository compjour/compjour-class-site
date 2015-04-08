require 'lib/content_article'

class Carm
  attr_reader :curriculum
  def initialize(sitemap)
    @sitemap = sitemap
    @site_resources = sitemap.resources
    @content_articles = formulate_content_articles
    @curriculum = formulate_curriculum
  end



  def get_next_nav_article(c)
    get_content_article(c.next_nav_article)
  end

  def get_prev_nav_article(c)
    get_content_article(c.prev_nav_article)
  end

  def get_overview_nav_article(c)
    get_content_article(c.overview_nav_article)
  end


  def find_content(val)
    get_content_article(val)
  end


  def get_content_article(val)
    case val
    when nil
      raise CantFindContentArticleWithNilSlug
    when ContentArticle
      val
    when Middleman::Sitemap::Resource
      ContentArticle(val)
    else
      # assume it's a base_slug
      get_content_article_by_base_slug(val)
    end
  end

  # ignore scope/collection, just go by slug
  # obviously, if content has the same slug, this
  # is a problem
  def get_content_article_by_base_slug(aslug)
    a = @content_articles.find{|a| a.base_slug == aslug}
    if a.nil?
      raise ContentArticleSlugNotFound, "'#{aslug}' did not match any articles"
    else
      return a
    end
  end



  private
    def formulate_curriculum
      formulate_content_articles.select{|a| a.curriculum_order}.
        sort_by{ |a| a.curriculum_order}
    end

    def formulate_content_articles
       @site_resources.select{|r| r.url =~ /\/(?:tutorials|articles|weeks|homework)\// }.
        reject{|c| c.path =~ /index.html/ }.
        map{|c| ContentArticle(c) }
    end

end



class CarmError < StandardError; end

class ContentArticleSlugNotFound < CarmError; end;
class CantFindContentArticleWithNilSlug < CarmError; end;
