from worst_performers import abstract_worst_performers as awp
import requests
from lxml import html

class yahooWorstPerformers(awp.abstractWorstPerformers):

    def __init__(self):
        super(yahooWorstPerformers, self).__init__()

        self.EXPECTED_ROW_SIZE = 9

    def getStockTicker(self, posible_ticker_row):
        ticker_data = []
        for table_section in posible_ticker_row.xpath('td'):
            section_text = table_section.text_content().replace('\n','').strip()
            if section_text != '':
                ticker_data.append(section_text)

        if len(ticker_data) != self.EXPECTED_ROW_SIZE:
            return ''

        print (('FOUND TICKER' +
               '\n\t Symbol: {} ' +
               '\n\t Company: {} ' +
               '\n\t Price (Intraday): {} ' +
               '\n\t Change: {} ' +
               '\n\t % Change: {} ' +
               '\n\t Volume: {} ' +
               '\n\t Avg Vol (3 month): {} ' +
               '\n\t Market Cap: {} ' +
               '\n\t PE Ratio (TTM): {}'
               ).format(*ticker_data))

        # Just return the ticker name
        return ticker_data[0]

    def getWorstDailyPerformers(self):
        print('Getting CSI Market Worst')

        # page = requests.get('https://finance.yahoo.com/losers', verify=False)
        # tree = html.fromstring(page.content)
        tickers = []
        tree = html.fromstring(self.getPage().encode("ascii", errors="ignore").decode())

        page_tables = tree.xpath('//tbody')
        for page_table in page_tables:
            for table_row in page_table.iterchildren():
                ticker_name = self.getStockTicker(table_row)

                if ticker_name == '':
                    continue

                tickers.append(ticker_name)
        return tickers

    def getPage(self):
        return '''
<!DOCTYPE html>
<html id="atomic" class="NoJs chrome desktop" lang="en-US">
   <head prefix="og: http://ogp.me/ns#">
      <script>window.performance && window.performance.mark && window.performance.mark('PageStart');</script>
      <meta charset="utf-8"/>
      <title>Stock Screener - Yahoo Finance</title>
      <meta name="keywords" content="Stock Screener, industry, index membership, share data, stock price, market cap, beta, sales, profitability, valuation ratios, analyst estimates, large cap value, bargain growth, preset stock screens"/>
      <meta http-equiv="x-dns-prefetch-control" content="on"/>
      <meta property="twitter:dnt" content="on"/>
      <meta property="twitter:site" content="@YahooFinance"/>
      <meta property="fb:app_id" content="90376669494"/>
      <meta name="theme-color" content="#400090"/>
      <meta name="viewport" content="width=device-width, initial-scale=1"/>
      <meta name="description" lang="en-US" content="Stock Screener: Stock Research Center - Use the stock screener to search stocks by industry, index membership, share data such as price, market cap, beta, sales and profitability, valuation ratios, analyst estimates. Create your own screens with over 150 different screening criteria"/>
      <link rel="dns-prefetch" href="//l.yimg.com"/>
      <link rel="dns-prefetch" href="//s.yimg.com"/>
      <link rel="dns-prefetch" href="//csc.beap.bc.yahoo.com"/>
      <link rel="dns-prefetch" href="//geo.query.yahoo.com"/>
      <link rel="dns-prefetch" href="//y.analytics.yahoo.com"/>
      <link rel="dns-prefetch" href="//b.scorecardresearch.com"/>
      <link rel="dns-prefetch" href="//iquery.finance.yahoo.com"/>
      <link rel="dns-prefetch" href="//fc.yahoo.com"/>
      <link rel="dns-prefetch" href="//video-api.yql.yahoo.com"/>
      <link rel="dns-prefetch" href="//yrtas.btrll.com"/>
      <link rel="dns-prefetch" href="//shim.btrll.com"/>
      <link rel="preconnect" href="//l.yimg.com"/>
      <link rel="preconnect" href="//s.yimg.com"/>
      <link rel="preconnect" href="//csc.beap.bc.yahoo.com"/>
      <link rel="preconnect" href="//geo.query.yahoo.com"/>
      <link rel="preconnect" href="//y.analytics.yahoo.com"/>
      <link rel="preconnect" href="//b.scorecardresearch.com"/>
      <link rel="preconnect" href="//iquery.finance.yahoo.com"/>
      <link rel="preconnect" href="//fc.yahoo.com"/>
      <link rel="preconnect" href="//video-api.yql.yahoo.com"/>
      <link rel="preconnect" href="//yrtas.btrll.com"/>
      <link rel="preconnect" href="//shim.btrll.com"/>
      <link rel="icon" href="https://s.yimg.com/os/mit/media/p/common/images/favicon_new-7483e38.svg" sizes="any"/>
      <link rel="alternate icon" href="https://finance.yahoo.com/favicon.ico?bypass=true" type="image/x-icon"/>
      <link rel="canonical" href="https://finance.yahoo.com/losers/"/>
      <meta property="twitter:site" content="@YahooFinance"/>
      <meta property="og:description" content="Stock Screener: Stock Research Center - Use the stock screener to search stocks by industry, index membership, share data such as price, market cap, beta, sales and profitability, valuation ratios, analyst estimates. Create your own screens with over 150 different screening criteria"/>
      <meta property="og:title" content="Stock Screener - Yahoo Finance"/>
      <meta property="twitter:description" content="Stock Screener: Stock Research Center - Use the stock screener to search stocks by industry, index membership, share data such as price, market cap, beta, sales and profitability, valuation ratios, analyst estimates. Create your own screens with over 150 different screening criteria"/>
      <meta property="twitter:title" content="Stock Screener - Yahoo Finance"/>
      <meta property="al:ios:url" content="yfinance://"/>
      <meta property="al:ios:app_store_id" content="328412701"/>
      <meta property="al:ios:app_name" content="Yahoo Finance"/>
      <meta property="al:android:url" content="intent://#Intent;scheme=yfinance;action=android.intent.action.VIEW;package=com.yahoo.mobile.client.android.finance;S.browser_fallback_url=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.yahoo.mobile.client.android.finance;end"/>
      <meta property="al:android:app_name" content="Yahoo Finance"/>
      <meta property="al:android:package" content="com.yahoo.mobile.client.android.finance"/>
      <meta property="apple-itunes-app" content="app-id=328412701, affiliate-data=ct=us.fin.mbl.smart-banner&amp;pt=9029, app-argument=yfinance://"/>
      <meta property="og:image" content="https://s.yimg.com/os/finance/dd-site/img/screener_share.png"/>
      <link rel="stylesheet" href="https://s.yimg.com/zz/combo?os/yc/css/bundle.ce149847.css&amp;os/yc/css/patch.cd698090.css&amp;os/finance/dd-icon/1.0.30/yahoo-finance-icons.css&amp;os/finance/dd-site/css/atomic.1304e1b6.css&amp;os/finance/dd-site/css/app.8e30113a.css"/>
      <script src="https://www.yahoo.com/polyfill.min.js?features=locale-data-en-us%2Cpromise%2Carray.isarray%2Carray.prototype.every%2Carray.prototype.foreach%2Carray.prototype.indexof%2Carray.prototype.map%2Cdate.now%2Cfunction.prototype.bind%2Cobject.keys%2Cstring.prototype.trim%2Cobject.defineproperty%2Cobject.defineproperties%2Cobject.create%2Cobject.freeze%2Carray.prototype.filter%2Carray.prototype.reduce%2Cobject.assign%2Crequestanimationframe%2Cintl&amp;version=2.1.23" defer=""></script><script src="https://s.yimg.com/os/ri/2.4.0/en.js"></script><script src="https://s.yimg.com/zz/combo?ss/rapid-3.42.2.js"></script><script src="https://s.yimg.com/os/finance/dd-site/js/vendor.1645ef5ffe3fb6dd476e.js" defer=""></script><script src="https://s.yimg.com/os/finance/dd-site/js/common.8af13e8bdda0881df55f.js" defer=""></script><script src="https://yep.video.yahoo.com/js/3/videoplayer-min.js?r=nextgen-desktop&amp;lang=en-US&amp;ypv=prod"></script><script src="https://s.yimg.com/rq/darla/3-0-8/js/g-r-min.js"></script><script>(function(html){var c = html.className;c += " JsEnabled";c = c.replace("NoJs","");html.className = c;})(document.documentElement);</script><script>window.Modernizr=function(a,b,c){function d(a){q.cssText=a}function e(a,b){return typeof a===b}function f(a,b){return!!~(""+a).indexOf(b)}function g(a,b){for(var d in a){var e=a[d];if(!f(e,"-")&&q[e]!==c)return"pfx"!=b\n\te}return!1}function h(a,b,d){for(var f in a){var g=b[a[f]];if(g!==c)return!1===d?a[f]:e(g,"function")?g.bind(d\n\tb):g}return!1}function i(a,b,c){var d=a.charAt(0).toUpperCase()+a.slice(1),f=(a+" "+t.join(d+" ")+d).split(" ");return e(b,"string")\n\te(b,"undefined")?g(f,b):(f=(a+" "+u.join(d+" ")+d).split(" "),h(f,b,c))}var j,k,l="2.8.3",m={},n=b.documentElement,o="modernizr",p=b.createElement(o),q=p.style,r=" -webkit- -moz- -o- -ms- ".split(" "),s="Webkit Moz O ms",t=s.split(" "),u=s.toLowerCase().split(" "),v={svg:"http://www.w3.org/2000/svg"},w={},x=[],y=x.slice,z=function(a,c,d,e){var f,g,h,i,j=b.createElement("div"),k=b.body,l=k\n\tb.createElement("body");if(parseInt(d,10))for(;d--;)h=b.createElement("div"),h.id=e?e[d]:o+(d+1),j.appendChild(h);return f=["&#173;",'<style id="s',o,'">',a,"</style>"].join(""),j.id=o,(k?j:l).innerHTML+=f,l.appendChild(j),k\n\t(l.style.background="",l.style.overflow="hidden",i=n.style.overflow,n.style.overflow="hidden",n.appendChild(l)),g=c(j,a),k?j.parentNode.removeChild(j):(l.parentNode.removeChild(l),n.style.overflow=i),!!g},A={}.hasOwnProperty;k=e(A,"undefined")\n\te(A.call,"undefined")?function(a,b){return b in a&&e(a.constructor.prototype[b],"undefined")}:function(a,b){return A.call(a,b)},Function.prototype.bind\n\t(Function.prototype.bind=function(a){var b=this;if("function"!=typeof b)throw new TypeError;var c=y.call(arguments,1),d=function(){if(this instanceof d){var e=function(){};e.prototype=b.prototype;var f=new e,g=b.apply(f,c.concat(y.call(arguments)));return Object(g)===g?g:f}return b.apply(a,c.concat(y.call(arguments)))};return d}),w.canvas=function(){var a=b.createElement("canvas");return!(!a.getContext\n\t!a.getContext("2d"))},w.history=function(){return!(!a.history\n\t!history.pushState)},w.csstransforms3d=function(){var a=!!i("perspective");return a&&"webkitPerspective"in n.style&&z("@media (transform-3d),(-webkit-transform-3d){#modernizr{left:9px;position:absolute;height:3px;}}",function(b,c){a=9===b.offsetLeft&&3===b.offsetHeight}),a},w.csstransitions=function(){return i("transition")},w.video=function(){var a=b.createElement("video"),c=!1;try{(c=!!a.canPlayType)&&(c=new Boolean(c),c.ogg=a.canPlayType('video/ogg; codecs="theora"').replace(/^no$/,""),c.h264=a.canPlayType('video/mp4; codecs="avc1.42E01E"').replace(/^no$/,""),c.webm=a.canPlayType('video/webm; codecs="vp8, vorbis"').replace(/^no$/,""))}catch(d){}return c},w.localstorage=function(){try{return localStorage.setItem(o,o),localStorage.removeItem(o),!0}catch(a){return!1}},w.sessionstorage=function(){try{return sessionStorage.setItem(o,o),sessionStorage.removeItem(o),!0}catch(a){return!1}},w.svg=function(){return!!b.createElementNS&&!!b.createElementNS(v.svg,"svg").createSVGRect},w.inlinesvg=function(){var a=b.createElement("div");return a.innerHTML="<svg/>",(a.firstChild&&a.firstChild.namespaceURI)==v.svg};for(var B in w)k(w,B)&&(j=B.toLowerCase(),m[j]=w[B](),x.push((m[j]?"":"no-")+j));return m.addTest=function(a,b){if("object"==typeof a)for(var d in a)k(a,d)&&m.addTest(d,a[d]);else{if(a=a.toLowerCase(),m[a]!==c)return m;b="function"==typeof b?b():b,"undefined"!=typeof enableClasses&&enableClasses&&(n.className+=" "+(b?"":"no-")+a),m[a]=b}return m},d(""),p=null,m._version=l,m._prefixes=r,m._domPrefixes=u,m._cssomPrefixes=t,m.testProp=function(a){return g([a])},m.testAllProps=i,m.testStyles=z,m.prefixed=function(a,b,c){return b?i(a,b,c):i(a,"pfx")},m}(this,this.document);</script>
      <style>#atomic .render-target-modal #YDC-UH{display:none}#atomic #render-target-modal,#atomic #render-target-viewer{opacity:0}#atomic.modal-postopen #render-target-modal,#atomic.viewer-postopen #render-target-viewer{opacity:1}#atomic.modal-postopen #render-target-mrt,#atomic.modal-postopen .render-target-default,#atomic.viewer-postopen #render-target-mrt,#atomic.viewer-postopen .render-target-default{max-height:100%;overflow:hidden}#render-target-mrt{position:absolute;width:100%}#atomic.default-to-modal-fade .render-target-default,#atomic.default-to-viewer-fade .render-target-default,#atomic.modal-to-default-fade .render-target-modal,#atomic.mrt-to-modal-fade #render-target-mrt,#atomic.mrt-to-viewer-fade #render-target-mrt,#atomic.viewer-to-default-fade .render-target-viewer{position:absolute}#atomic.default-to-modal-fade .render-target-modal{-webkit-animation:fadein .15s ease-out forwards;animation:fadein .15s ease-out forwards}#atomic.modal-to-default-fade .render-target-modal{-webkit-animation:fadeout .15s ease-in forwards;animation:fadeout .15s ease-in forwards}#atomic.default-to-viewer-fade .render-target-viewer,#atomic.modal-to-viewer-fade .render-target-viewer{-webkit-animation:fadein .25s ease-out forwards;animation:fadein .25s ease-out forwards}#atomic.viewer-to-default-fade .render-target-viewer,#atomic.viewer-to-modal-fade .render-target-viewer{-webkit-animation:fadeout .25s ease-in forwards;animation:fadeout .25s ease-in forwards}@-webkit-keyframes fadein{0%{opacity:0}100%{opacity:1}}@-webkit-keyframes fadeout{0%{opacity:1}100%{opacity:0}}@keyframes fadein{0%{opacity:0}100%{opacity:1}}@keyframes fadeout{0%{opacity:1}100%{opacity:0}}</style>
      <style>#atomic .video-lightbox .video-container .yvp-content.yvp-browser-desktop.yvp-state-video.yvp-hide-controls .yvp-html5-video,#atomic .video-lightbox .video-container.playlist-dimmed .yvp-playlist-container{cursor:none}#atomic .video-lightbox .tdv2-applet-canvass .comment-icon,#atomic .video-lightbox .tdv2-applet-canvass .sort-filter-button>svg{fill:#fff!important;stroke:#fff!important}#atomic .video-lightbox .tdv2-applet-canvass .comments-title,#atomic .video-lightbox .tdv2-applet-canvass .message-content>div,#atomic .video-lightbox .tdv2-applet-canvass .see-more-wrapper>div,#atomic .video-lightbox .tdv2-applet-canvass .sort-filter-button>span,#atomic .video-lightbox .tdv2-applet-canvass .username{color:#fff!important}#atomic .video-lightbox .tdv2-applet-canvass a.comment-form{border:none!important}#atomic .video-lightbox .tdv2-applet-canvass .more-button>span{color:#787d82!important}#atomic .video-lightbox .tdv2-applet-canvass .canvass-tumblr-stickers input{width:135px!important}#atomic .video-lightbox .yvp-playlist-container.yvp-playlist-mode-right.yvp-playlist-theme-dark{background:#0c0c0c}#atomic .video-lightbox .video-container .yvp-content{background:0 0}#atomic .video-lightbox .video-container.playlist-dimmed .yvp-playlist-container .yvp-playlist-item{cursor:none;opacity:.2;transition:all .4s ease-in-out;transition-delay:.2s}#atomic .video-lightbox .video-container.playlist-undimmed .yvp-playlist-container .yvp-playlist-item{opacity:1;transition:all .4s ease-in-out;transition-delay:.2s}#atomic .video-lightbox .video-container.playlist-hidden .yvp-playlist-container{opacity:0;transition:all .4s ease-in-out}</style>
      <script>(function () {
         if (!window.YAHOO \n\t !window.YAHOO.i13n \n\t !window.YAHOO.i13n.Rapid) { return; }
         var rapidConfig = {"async_all_clicks":true,"click_timeout":300,"client_only":1,"compr_type":"deflate","keys":{"ver":"ydotcom","navtype":"server","pt":"utility","pct":"screener","pstcat":"equity","pg_name":"predefined","mrkt":"us","site":"finance","lang":"en-US","colo":"gq1","_yrid":"4cc8v0hcupnk2","_rid":"4cc8v0hcupnk2"},"pageview_on_init":true,"test_id":"3.RTgzMTUzMwdmaW4tc3RybS10ZXN0MgZfQ0hHAzAEX3ZlcgM0LjgCRTgzMTk5MwdmbmRtdGVzdAJFODMyNDI5B2ZpbnNzbA--","tracked_mods_viewability":[],"track_right_click":false,"viewability":true,"perf_navigationtime":2,"perf_resourcetime":1,"webworker_file":"/__rapidworker-1.2.js","spaceid":1183335883};
         window.rapidInstance = new window.YAHOO.i13n.Rapid(rapidConfig);
         })();
      </script>
   </head>
   <body>
      <div id="app">
         <div data-reactroot="" data-reactid="1" data-react-checksum="-985647216">
            <div data-reactid="2">
               <div class="render-target-active  render-target-default Pos(a) W(100%) viewer-open_Op(0.999)" id="render-target-default" data-reactid="3">
                  <div class="Bgc($bg-body) Mih(100%) W(100%) US" style="margin-top:175px;" data-reactid="4">
                     <div class="YDC-Header Z(10) End(0) Start(0) T(0) H(0) Panel-open_Translate3d(0,-19px,0) hasScrolled_Translate3d(0,-19px,0) Translate3d(0,0,0) Pos(f) Trsp(a) Trsdu(300ms)" data-reactid="5">
                        <div id="YDC-UH" class="YDC-UH Bgi($uhGrayGradient) Pos(r) Z(1)" data-reactid="6">
                           <div id="YDC-UH-Stack" class="YDC-UH Miw(1007px) Maw(1260px) tablet_Miw(600px)--noRightRail Bxz(bb) Bdstartc(t) Bdstartw(20px) Bdendc(t) Bdends(s) Bdendw(20px) Bdstarts(s) Mx(a) tablet_Bd(n)" data-reactid="7">
                              <div data-reactid="8">
                                 <div data-reactid="9">
                                    <div id="mrt-node-UH-0-UH" data-locator="subtree-root">
                                       <div id="UH-0-UH-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="-1637825331">
                                          <div data-reactid="2">
                                             <div data-reactid="3">
                                                <div id="masterNav" class="C(#fff) Fz(13px) H(22px)" data-reactid="4">
                                                   <ul id="eyebrow" role="navigation" class="H(22px) Lh(1.7) M(0) NavLinks P(0) Whs(nw) Z(11) Bgc(#2d1152) Pos(a) Start(0) End(0)" data-reactid="5">
                                                      <li id="uh-tb-home" class="D(ib) Lh(1.7) Mend(18px) Pstart(10px) Va(t) Zoom" data-reactid="6">
                                                         <a class="C(#fff) Td(n) Pos(r) Z(1) rapidnofollow" href="https://www.yahoo.com/" data-reactid="7">
                                                            <div data-reactid="8">
                                                               <svg class="Cur(p)" width="16" style="cursor:pointer;margin-right:6px;margin-top:1px;vertical-align:top;fill:#fff;stroke:#fff;stroke-width:0;" height="16" viewBox="0 0 32 32" data-icon="home" data-reactid="9">
                                                                  <path d="M16.153 3.224L0 16.962h4.314v11.814h9.87v-8.003h3.934v8.003h9.84V16.962H32" data-reactid="10"></path>
                                                               </svg>
                                                               <b class="Fw(400) Mstart(-1px) Td(u):h" data-reactid="11">Home</b>
                                                            </div>
                                                         </a>
                                                      </li>
                                                      <li id="uh-tb-mail" class="D(ib) Lh(1.7) Mend(18px) Pstart(14px) Va(t) Zoom" data-reactid="12"><a class="C(#fff) Td(n) Td(u):h" href="https://mail.yahoo.com/?.intl=us&amp;.lang=en-US" data-reactid="13">Mail</a></li>
                                                      <li id="uh-tb-flickr" class="D(ib) Lh(1.7) Mend(18px) Pstart(14px) Va(t) Zoom" data-reactid="14"><a class="C(#fff) Td(n) Td(u):h" href="https://www.flickr.com/" data-reactid="15">Flickr</a></li>
                                                      <li id="uh-tb-tumblr" class="D(ib) Lh(1.7) Mend(18px) Pstart(14px) Va(t) Zoom" data-reactid="16"><a class="C(#fff) Td(n) Td(u):h" href="https://www.tumblr.com/" data-reactid="17">Tumblr</a></li>
                                                      <li id="uh-tb-news" class="D(ib) Lh(1.7) Mend(18px) Pstart(14px) Va(t) Zoom" data-reactid="18"><a class="C(#fff) Td(n) Td(u):h" href="https://www.yahoo.com/news/" data-reactid="19">News</a></li>
                                                      <li id="uh-tb-sports" class="D(ib) Lh(1.7) Mend(18px) Pstart(14px) Va(t) Zoom" data-reactid="20"><a class="C(#fff) Td(n) Td(u):h" href="http://sports.yahoo.com/" data-reactid="21">Sports</a></li>
                                                      <li id="uh-tb-finance" class="D(ib) Lh(1.7) Mend(18px) Pstart(14px) Va(t) Zoom" data-reactid="22"><a class="C(#fff) Td(n) Td(u):h" href="http://finance.yahoo.com/" data-reactid="23">Finance</a></li>
                                                      <li id="uh-tb-entertainment" class="D(ib) Lh(1.7) Mend(18px) Pstart(14px) Va(t) Zoom" data-reactid="24"><a class="C(#fff) Td(n) Td(u):h" href="https://www.yahoo.com/entertainment/" data-reactid="25">Entertainment</a></li>
                                                      <li id="uh-tb-lifestyle" class="D(ib) Lh(1.7) Mend(18px) Pstart(14px) Va(t) Zoom" data-reactid="26"><a class="C(#fff) Td(n) Td(u):h" href="https://www.yahoo.com/lifestyle/" data-reactid="27">Lifestyle</a></li>
                                                      <li id="uh-tb-answers" class="D(ib) Lh(1.7) Mend(18px) Pstart(14px) Va(t) Zoom" data-reactid="28"><a class="C(#fff) Td(n) Td(u):h" href="https://answers.yahoo.com/" data-reactid="29">Answers</a></li>
                                                      <li id="uh-tb-groups" class="D(ib) Lh(1.7) Mend(18px) Pstart(14px) Va(t) Zoom" data-reactid="30"><a class="C(#fff) Td(n) Td(u):h" href="https://groups.yahoo.com/" data-reactid="31">Groups</a></li>
                                                      <li id="uh-tb-more" class="D(ib) Lh(1.7) Pend(6px) Pos(r) Pstart(10px) Va(t) Z(4) Zoom" data-reactid="32">
                                                         <a id="uh-tb-more-link" class="C(#fff) Pos(r) Td(n) Z(1) yucs-leavable rapidnofollow" href="https://everything.yahoo.com/" role="button" data-reactid="33">
                                                            <span class="Td(u):h" data-reactid="34">More</span>
                                                            <svg class="Cur(p)" width="8" style="cursor:pointer;margin-left:5px;vertical-align:middle;fill:#fff;stroke:#fff;stroke-width:0;" height="8" viewBox="0 0 512 512" data-icon="CoreArrowDown" data-reactid="35">
                                                               <path d="M500.77 131.432L477.53 108.18c-14.45-14.55-40.11-14.55-54.51 0L255.845 275.363 88.582 108.124c-15.015-14.874-39.363-14.874-54.42.108L10.94 131.486c-14.58 14.44-14.58 40.11-.033 54.442l217.77 217.845c15.004 14.82 39.33 14.874 54.42-.108L500.88 185.82c14.818-14.982 14.87-39.298-.11-54.388z" data-reactid="36"></path>
                                                            </svg>
                                                         </a>
                                                      </li>
                                                      <!-- react-empty: 37 -->
                                                   </ul>
                                                </div>
                                                <div id="UH-0-UH-0-Header" class="Miw(980px) UH Z(10) Py(14px) Pos(r)" data-name="tdv2-applet-uh" data-version="9.0.118" data-reactid="38">
                                                   <div data-reactid="39">
                                                      <div class="Fl(start) Fz(0) M(0) P(0) ie-7_W(190px) Miw(190px) UHMR1D_Py(0)" style="background-color:transparent;" data-reactid="40">
                                                         <div data-reactid="41">
                                                            <style data-reactid="42">#UH-0-UH-0-Header #uh-logo {background-image: url(https://s.yimg.com/rz/d/yahoo_finance_en-US_s_f_pw_351x40_finance.png);} @media  only screen and (-webkit-min-device-pixel-ratio: 2), only screen and ( min--moz-device-pixel-ratio: 2), only screen and ( -o-min-device-pixel-ratio: 2/1), only screen and ( min-device-pixel-ratio: 2), only screen and ( min-resolution: 192dpi), only screen and ( min-resolution: 2dppx) { #UH-0-UH-0-Header #uh-logo {background-image: url(https://s.yimg.com/rz/d/yahoo_finance_en-US_s_f_pw_351x40_finance_2x.png);} }</style>
                                                            <a id="uh-logo" class="Bgpx(0) Bgr(nr) Cur(p) D(b) H(35px) Bgz(702px) Mx(a)! W(92px)" href="https://finance.yahoo.com/" data-reactid="43"><b class="Hidden" data-reactid="44">Yahoo</b></a>
                                                         </div>
                                                      </div>
                                                      <div id="uh-search" class="D(ib) uh-max_Py(50px)" data-reactid="45">
                                                         <form action="/quote/" class="M(0) P(0) Whs(nw)" method="get" name="input" data-reactid="46">
                                                            <label class="Hidden" for="search-assist-input" data-reactid="47">Search</label>
                                                            <table class="Bdsp(0) Bdcl(c) Maw(searchMaxWidth) Miw(searchMinWidth) W(searchWidth) ie-8_W(searchMinWidthLightWeight) ie-7_W(searchMinWidthLightWeight) ie-7_Miw(searchMinWidthLightWeight) ie-8_Miw(searchMinWidthLightWeight)" data-reactid="48">
                                                               <tbody data-reactid="49">
                                                                  <tr data-reactid="50">
                                                                     <td class="W(100%) Va(t) Px(0)" data-reactid="51">
                                                                        <div data-reactid="52">
                                                                           <div class="Z(2) Pos(r)" id="search-assist-input" data-reactid="53">
                                                                              <div class="" data-reactid="54"><input type="text" aria-label="Search" autocomplete="off" autocorrect="off" autocapitalize="off" class="Pos(r) W(100%) M(0) O(0) O(0):f Bgc(#fff) Z(2) Bxsh(n) Bxsh(n):f Fz(15px) Px(15px) Py(8px) Bdrs(0) Pstart(10px) Pend(10px) Va(t)" name="p" placeholder="Search for news, symbols or companies" style="-webkit-appearance:none;" value="" data-reactid="55"/></div>
                                                                              <div class="Pos(a) Ta(start) Start(0) End(0) Bgc(#fff) Z(1) Wob(ba) D(n) Bd Bdc(#aaa) Bdtw(0) Mt(-1px) Whs(n)" data-reactid="56">
                                                                                 <ul class="M(0)" data-reactid="57"></ul>
                                                                              </div>
                                                                           </div>
                                                                        </div>
                                                                     </td>
                                                                     <td class="Va(t) Tren(os) W(10%) Whs(nw) Px(0) Bdcl(s)" data-reactid="58">
                                                                        <div id="search-buttons" data-reactid="59"><button class="Bdrs(4px) Bdtw(0) Bdw(1px) Bgr(rx) Mstart(5px) Bxz(cb) C(#fff) Ff(ss)! Fz(15px) two-btn_Fz(13px) Lh(32px)! Mend(0)! My(0)! Miw(92px) Px(14px) Py(0) Ta(c) Td(n) Va(t) Zoom Bg(searchBtnBg) Bxsh(customShadowSearchButton)" id="search-button" style="filter:chroma(color=#000);" type="submit" data-reactid="60">Search</button></div>
                                                                     </td>
                                                                  </tr>
                                                               </tbody>
                                                            </table>
                                                            <input type="hidden" name="fr" value="uh3_finance_vert" data-reactid="61"/><input type="hidden" name="fr2" value="p:finvsrp,m:sb" data-reactid="62"/>
                                                         </form>
                                                         <ul id="skip-nav" class="Pos(a)" data-reactid="63">
                                                            <li tabindex="3" data-reactid="64"><a class="W(0) D(ib) Whs(nw) Pos(a) Bg(#500095) C(#fff) Op(0) W(a):f Op(1):f P(5px):f" href="#Navigation" data-reactid="65">Skip to Navigation</a></li>
                                                            <li tabindex="3" data-reactid="66"><a class="W(0) D(ib) Whs(nw) Pos(a) Bg(#500095) C(#fff) Op(0) W(a):f Op(1):f P(5px):f" href="#market-summary" data-reactid="67">Skip to Market Summary</a></li>
                                                            <li tabindex="3" data-reactid="68"><a class="W(0) D(ib) Whs(nw) Pos(a) Bg(#500095) C(#fff) Op(0) W(a):f Op(1):f P(5px):f" href="#Main" data-reactid="69">Skip to Main Content</a></li>
                                                            <li tabindex="3" data-reactid="70"><a class="W(0) D(ib) Whs(nw) Pos(a) Bg(#500095) C(#fff) Op(0) W(a):f Op(1):f P(5px):f" href="#Aside" data-reactid="71">Skip to Related Content</a></li>
                                                         </ul>
                                                      </div>
                                                      <ul id="uh-right" class="End(20px) List(n) Pos(a) T(14px)" data-reactid="72">
                                                         <li class="Fl(start) Mx(4px) Mend(9px) V(h)" data-reactid="73">
                                                            <svg class="Cur(p)" width="34" style="fill:#400090;stroke:#400090;stroke-width:0;vertical-align:bottom;" height="34" viewBox="0 0 48 48" data-icon="profile" data-reactid="74">
                                                               <path d="M4.095 33.61c1.092 2.7 2.607 4.937 4.562 6.696 1.94 1.766 4.23 3.072 6.847 3.922 2.632.846 5.472 1.27 8.53 1.27 3.012 0 5.837-.425 8.458-1.27 1.053-.342 2.046-.754 2.986-1.244 1.41-.732 2.705-1.617 3.87-2.678 1.948-1.76 3.472-3.996 4.558-6.697 1.092-2.7 1.636-5.903 1.636-9.614 0-3.702-.544-6.904-1.636-9.61-1.086-2.703-2.608-4.934-4.56-6.694-1.944-1.767-4.23-3.07-6.854-3.922-2.62-.847-5.445-1.27-8.457-1.27-3.06 0-5.9.423-8.53 1.27-.847.277-1.662.607-2.443.98-1.623.777-3.1 1.753-4.404 2.942-1.956 1.76-3.47 3.992-4.562 6.694-1.09 2.706-1.636 5.908-1.636 9.61-.002 3.71.545 6.914 1.635 9.613zM35.838 34.758l-23.674.002v-2.21s.017-1.425 3.123-2.716c1.538-.633 3.35-1.854 6.6-2.24-.997-.705-1.44-2.154-2.29-4.17-.02-.032-.03-.068-.043-.1-.193.032-.393.032-.537-.046-.398-.232-.636-1.48-.642-2.092-.01-.906.48-.824.48-.824s.017 0 .042-.004c-.006-.07-.01-.142-.01-.213 0-.86-.174-2.24.053-2.988.353-1.176.78-2.46 1.72-2.464.874 0 .28-1.006 1.348-1.345 1.102-.348 2.912.262 3.283.262.53 0 1.863.378 2.78 1.284.646.64.572 1.08.93 2.25.23.777.057 2.167.057 3 0 .07-.007.14-.014.213.018.007.03.007.03.007s.487-.082.478.824c-.004.612-.248 1.86-.635 2.092-.146.078-.34.078-.53.052-.01.026-.023.058-.033.09-.85 1.996-1.308 3.457-2.305 4.162 3.283.38 5.107 1.61 6.654 2.25 3.128 1.287 3.14 2.533 3.14 2.533l-.002 2.39z" data-reactid="75"></path>
                                                            </svg>
                                                         </li>
                                                         <li class="D(ib) Mstart(14px) Mt(-1px) ua-ie8_Pb(10px) ua-ie9_Pb(10px)" data-reactid="76">
                                                            <button id="uh-follow" class="Pos(r) Fl(start) D(ib) Bd(0) P(0) Mstart(14px) Mend(13px) Cur(p) ie-7_D(n) ie-8_Pb(10px) ie-9_Pb(10px)" href="#" aria-label="Notifications" data-reactid="77">
                                                               <svg class="Cur(p)" width="28" style="fill:#400090;stroke:#400090;stroke-width:0;vertical-align:bottom;" height="28" viewBox="0 0 512 512" data-icon="nav-bell" data-reactid="78">
                                                                  <path d="M294.2 428.05h-74.4c0 20.543 16.656 37.2 37.2 37.2 20.535 0 37.2-12.47 37.2-37.2zM136.1 195.55c0 62.284-53.51 94.162-55.728 95.452L71 296.352v94.498h372v-94.498l-9.373-5.35c-.562-.318-55.727-32.573-55.727-95.452 0-63.88-12.533-148.8-120.9-148.8-108.368 0-120.9 84.92-120.9 148.8z" data-reactid="79"></path>
                                                               </svg>
                                                               <span id="uh-follow-count" class="Bgc($c-fuji-red-1-a) Bdrs(11px) C(#fff) Start(16px) Fz(11px) Fw(b) Pos(a) Lh(2) Ta(c) T(-11px) W(22px) V(h)" data-reactid="80">0</span>
                                                            </button>
                                                         </li>
                                                         <li class="D(ib) Mstart(14px) Mt(-1px) ua-ie8_Pb(10px) ua-ie9_Pb(10px)" data-reactid="81">
                                                            <a id="uh-mail" class="Pos(r) D(ib) Ta(s) Td(n):h" href="https://mail.yahoo.com/?.intl=us&amp;.lang=en-US&amp;.partner=none&amp;.src=finance" data-reactid="82">
                                                               <svg class="Cur(p)" width="30" style="fill:#400090;stroke:#400090;stroke-width:0;vertical-align:bottom;" height="35" viewBox="0 0 512 512" data-icon="NavMail" data-reactid="83">
                                                                  <path d="M460.586 91.31H51.504c-10.738 0-19.46 8.72-19.46 19.477v40.088l224 104.03 224-104.03v-40.088c0-10.757-8.702-19.478-19.458-19.478M32.046 193.426V402.96c0 10.758 8.72 19.48 19.458 19.48h409.082c10.756 0 19.46-8.722 19.46-19.48V193.428l-224 102.327-224-102.327z" data-reactid="84"></path>
                                                               </svg>
                                                               <b class="Lh(userNavTextLh) D(ib) C($c-fuji-purple-1-c) Fz(14px) Fw(b) Va(t) Mstart(6px)" data-reactid="85"></b>
                                                            </a>
                                                         </li>
                                                      </ul>
                                                   </div>
                                                </div>
                                             </div>
                                          </div>
                                       </div>
                                    </div>
                                    <script>if (window.performance) {window.performance.mark && window.performance.mark('UH-0-UH');window.performance.measure && window.performance.measure('UH-0-UHDone','PageStart','UH-0-UH');}</script>
                                 </div>
                              </div>
                           </div>
                        </div>
                        <div class="HideNavrail_Translate3d(0,-46px,0) Panel-open_Translate3d(0,-46px,0) Translate3d(0,0,0) Trsp(a) Trsdu(300ms)" id="Navigation" role="navigation" tabindex="-1" data-reactid="10">
                           <div id="YDC-Nav" class="YDC-Nav" data-reactid="11">
                              <div class="Bgi($navrailGrayGradient) Pos(r) Pt(3px) Mt(-3px)" data-reactid="12">
                                 <div id="YDC-Nav-Stack" class="YDC-Nav Miw(1007px) Maw(1260px) tablet_Miw(600px)--noRightRail Bxz(bb) Bdstartc(t) Bdstartw(20px) Bdendc(t) Bdends(s) Bdendw(20px) Bdstarts(s) Mx(a) tablet_Bd(n)" data-reactid="13">
                                    <div data-reactid="14">
                                       <div data-reactid="15">
                                          <div id="mrt-node-Nav-0-DesktopNav" data-locator="subtree-root">
                                             <div id="Nav-0-DesktopNav-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="-558680813">
                                                <div id="Nav-0-DesktopNav" class="Pos(r) Z(1)" data-reactid="2">
                                                   <nav class="tdv2-applet-navrail" data-reactid="3">
                                                      <div class="Ff(navFrontFamily)" data-reactid="4">
                                                         <div id="Nav-0-DesktopNav" class="nr-applet-main-nav Pos(r) Start(0) End(0) Z(8) H(navHeight) Lh(navHeight) Fz(13px) Fw(b) Bdw(1px) Miw(980px) Bdc($c-divider) Bdts(s) Bdc(borderColorDark) H(navHeight_uhMagDesign)! Lh(n)! Bdw(0px)! Bdbs(n)! Bdts(n)!" data-reactid="5">
                                                            <div class="Bgc(t) Bgc($bg-header) Pt(2px)" data-reactid="6">
                                                               <div class="nr-applet-title Fl(start) Pend(navPaddings) Bxz(bb) Ov(h) H(navHeight) Pstart(10px) Mstart(-10px)! H(itemHeight_uhMagDesign)! Pend(30px)!" data-reactid="7">
                                                                  <div class="" data-reactid="8">
                                                                     <a class="nr-applet-nav-item Td(n) rapidnofollow Ell Td(n) D(ib) Lh(itemHeight_uhMagDesign) Tt(c)! Bdbc($c-fuji-blue-1-a):h Bdbs(s):h Bdbw(4px):h H(38px) Trstf(l) Trsde(0s) Trsdu(.18s) Trsp(border-bottom-width) C($finNavBlueText) C($finNavBlueText):h" href="/" title="Finance Home" data-reactid="9">
                                                                        <!-- react-text: 10 -->Finance Home<!-- /react-text -->
                                                                     </a>
                                                                  </div>
                                                               </div>
                                                               <div class="nr-applet-main-nav-right Bxz(bb) Fl(end) Px(navPaddings) H(navHeight) W(0px) H(itemHeight_uhMagDesign)!" data-reactid="11"></div>
                                                               <div class="nr-applet-main-nav-left H(navHeight) Mend(80px) Mend(0px)! H(itemHeight_uhMagDesign)!" data-reactid="12">
                                                                  <div class="mainNavInnerWrapper D(tb) H(navHeight) H(itemHeight_uhMagDesign)!" data-reactid="13">
                                                                     <div class="Lh(itemHeight) D(tbc) Lh(itemHeight_uhMagDesign)!" style="width:auto;" data-reactid="14">
                                                                        <ul class="H(navHeight) Ov(h) Pstart(10px) Mstart(-10px) H(itemHeight_uhMagDesign)!" data-reactid="15">
                                                                           <li class="nr-applet-main-nav-item Pend(navPaddings) Whs(nw) Fl(start) H(itemHeight) H(itemHeight_uhMagDesign)! Pend(30px)!" data-subnav-type="networknav_root-1" data-reactid="16">
                                                                              <a class="nr-applet-nav-item Td(n) rapidnofollow nr-list-link Ell Td(n) D(ib) Bdbs(s):h Pos(r) Bdc($fg-header) Lh(cateNavHeight) C($finNavBlueText):h C($finNavBlueText) Tt(n)! Bdbc($c-fuji-blue-1-a)!:h Bdbs(s)!:h Bdbw(4px)!:h H(38px) Trstf(l) Trsde(0s) Trsdu(.18s) Trsp(border-bottom-width) Fw(b)! Lh(itemHeight_uhMagDesign)! Va(m)! Fz(13px) Fl(start) openSubNav" href="/watchlists" title="Explore" data-reactid="17">
                                                                                 <!-- react-text: 18 -->Explore<!-- /react-text -->
                                                                              </a>
                                                                           </li>
                                                                           <li class="nr-applet-main-nav-item Pend(navPaddings) Whs(nw) Fl(start) H(itemHeight) H(itemHeight_uhMagDesign)! Pend(30px)!" data-subnav-type="networknav_root-2" data-reactid="19">
                                                                              <a class="nr-applet-nav-item Td(n) rapidnofollow nr-list-link Ell Td(n) D(ib) Bdbs(s):h Pos(r) Bdc($fg-header) Lh(cateNavHeight) C($finNavBlueText):h C($finNavBlueText) Tt(n)! Bdbc($c-fuji-blue-1-a)!:h Bdbs(s)!:h Bdbw(4px)!:h H(38px) Trstf(l) Trsde(0s) Trsdu(.18s) Trsp(border-bottom-width) Fw(b)! Lh(itemHeight_uhMagDesign)! Va(m)! Fz(13px) Fl(start) openSubNav" href="/portfolios?bypass=true" title="My Portfolio" data-reactid="20">
                                                                                 <!-- react-text: 21 -->My Portfolio<!-- /react-text -->
                                                                              </a>
                                                                           </li>
                                                                           <li class="nr-applet-main-nav-item Pend(navPaddings) Whs(nw) Fl(start) H(itemHeight) H(itemHeight_uhMagDesign)! Pend(30px)!" data-subnav-type="networknav_root-3" data-reactid="22">
                                                                              <a class="nr-applet-nav-item Td(n) rapidnofollow nr-list-link Ell Td(n) D(ib) Bdbs(s):h Pos(r) Bdc($fg-header) Lh(cateNavHeight) C($finNavBlueText):h C($finNavBlueText) Tt(n)! Bdbc($c-fuji-blue-1-a)!:h Bdbs(s)!:h Bdbw(4px)!:h H(38px) Trstf(l) Trsde(0s) Trsdu(.18s) Trsp(border-bottom-width) Fw(b)! Lh(itemHeight_uhMagDesign)! Va(m)! Fz(13px) Fl(start) openSubNav" href="/screener" title="My Screeners" data-reactid="23">
                                                                                 <!-- react-text: 24 -->My Screeners<!-- /react-text -->
                                                                              </a>
                                                                           </li>
                                                                           <li class="nr-applet-main-nav-item Pend(navPaddings) Whs(nw) Fl(start) H(itemHeight) H(itemHeight_uhMagDesign)! Pend(30px)!" data-subnav-type="networknav_root-4" data-reactid="25">
                                                                              <a class="nr-applet-nav-item Td(n) rapidnofollow nr-list-link Ell Td(n) D(ib) Bdbs(s):h Pos(r) Bdc($fg-header) Lh(cateNavHeight) C($finNavBlueText):h C($finNavBlueText)! Bdbw(0px) H(42px) Trstf(l) Trsde(0s) Trsdu(.18s) Trsp(border-bottom-width) C($finNavBlueText) Tt(n)! Bdbs(s) nr-item-selected Fw(b)! Lh(itemHeight_uhMagDesign)! Va(m)! Fz(13px) Fl(start) openSubNav" href="/calendar" aria-selected="true" title="Markets" data-reactid="26">
                                                                                 <!-- react-text: 27 -->Markets<!-- /react-text -->
                                                                                 <p class="Pos(a) B(0) W(100%)" data-reactid="28"><span class="D(b) Bdw(6px) W(0) Fz(0) Lh(0) M(a)" style="border-style:solid;border-color:transparent transparent #fff;" data-reactid="29"></span></p>
                                                                              </a>
                                                                           </li>
                                                                           <li class="nr-applet-main-nav-item Pend(navPaddings) Whs(nw) Fl(start) H(itemHeight) H(itemHeight_uhMagDesign)! Pend(30px)!" data-subnav-type="networknav_root-5" data-reactid="30">
                                                                              <a class="nr-applet-nav-item Td(n) rapidnofollow nr-list-link Ell Td(n) D(ib) Bdbs(s):h Pos(r) Bdc($fg-header) Lh(cateNavHeight) C($finNavBlueText):h C($finNavBlueText) Tt(n)! Bdbc($c-fuji-blue-1-a)!:h Bdbs(s)!:h Bdbw(4px)!:h H(38px) Trstf(l) Trsde(0s) Trsdu(.18s) Trsp(border-bottom-width) Fw(b)! Lh(itemHeight_uhMagDesign)! Va(m)! Fz(13px) Fl(start) openSubNav" href="/industries" title="Industries" data-reactid="31">
                                                                                 <!-- react-text: 32 -->Industries<!-- /react-text -->
                                                                              </a>
                                                                           </li>
                                                                           <li class="nr-applet-main-nav-item Pend(navPaddings) Whs(nw) Fl(start) H(itemHeight) H(itemHeight_uhMagDesign)! Pend(30px)!" data-subnav-type="networknav_root-6" data-reactid="33">
                                                                              <a class="nr-applet-nav-item Td(n) rapidnofollow nr-list-link Ell Td(n) D(ib) Bdbs(s):h Pos(r) Bdc($fg-header) Lh(cateNavHeight) C($finNavBlueText):h C($finNavBlueText) Tt(n)! Bdbc($c-fuji-blue-1-a)!:h Bdbs(s)!:h Bdbw(4px)!:h H(38px) Trstf(l) Trsde(0s) Trsdu(.18s) Trsp(border-bottom-width) Fw(b)! Lh(itemHeight_uhMagDesign)! Va(m)! Fz(13px) Fl(start) openSubNav" href="/topic/yahoo-finance-podcast" title="Originals" data-reactid="34">
                                                                                 <!-- react-text: 35 -->Originals<!-- /react-text -->
                                                                              </a>
                                                                           </li>
                                                                           <li class="nr-applet-main-nav-item Pend(navPaddings) Whs(nw) Fl(start) H(itemHeight) H(itemHeight_uhMagDesign)! Pend(30px)!" data-subnav-type="networknav_root-7" data-reactid="36">
                                                                              <a class="nr-applet-nav-item Td(n) rapidnofollow nr-list-link Ell Td(n) D(ib) Bdbs(s):h Pos(r) Bdc($fg-header) Lh(cateNavHeight) C($finNavBlueText):h C($finNavBlueText) Tt(n)! Bdbc($c-fuji-blue-1-a)!:h Bdbs(s)!:h Bdbw(4px)!:h H(38px) Trstf(l) Trsde(0s) Trsdu(.18s) Trsp(border-bottom-width) Fw(b)! Lh(itemHeight_uhMagDesign)! Va(m)! Fz(13px) Fl(start) openSubNav" href="/live/facebook" title="Events" data-reactid="37">
                                                                                 <!-- react-text: 38 -->Events<!-- /react-text -->
                                                                              </a>
                                                                           </li>
                                                                           <li class="nr-applet-main-nav-item Pend(navPaddings) Whs(nw) Fl(start) H(itemHeight) H(itemHeight_uhMagDesign)! Pend(30px)!" data-subnav-type="networknav_root-8" data-reactid="39">
                                                                              <a class="nr-applet-nav-item Td(n) rapidnofollow nr-list-link Ell Td(n) D(ib) Bdbs(s):h Pos(r) Bdc($fg-header) Lh(cateNavHeight) C($finNavBlueText):h C($finNavBlueText) Tt(n)! Bdbc($c-fuji-blue-1-a)!:h Bdbs(s)!:h Bdbw(4px)!:h H(38px) Trstf(l) Trsde(0s) Trsdu(.18s) Trsp(border-bottom-width) Fw(b)! Lh(itemHeight_uhMagDesign)! Va(m)! Fz(13px) Fl(start) openSubNav" href="/personal-finance" title="Personal Finance" data-reactid="40">
                                                                                 <!-- react-text: 41 -->Personal Finance<!-- /react-text -->
                                                                              </a>
                                                                           </li>
                                                                           <li class="nr-applet-main-nav-item Pend(navPaddings) Whs(nw) Fl(start) H(itemHeight) H(itemHeight_uhMagDesign)! Pend(30px)!" data-subnav-type="networknav_root-9" data-reactid="42">
                                                                              <a class="nr-applet-nav-item Td(n) rapidnofollow nr-list-link Ell Td(n) D(ib) Bdbs(s):h Pos(r) Bdc($fg-header) Lh(cateNavHeight) C($finNavBlueText):h C($finNavBlueText) Tt(n)! Bdbc($c-fuji-blue-1-a)!:h Bdbs(s)!:h Bdbw(4px)!:h H(38px) Trstf(l) Trsde(0s) Trsdu(.18s) Trsp(border-bottom-width) Fw(b)! Lh(itemHeight_uhMagDesign)! Va(m)! Fz(13px) Fl(start) openSubNav" href="/tech" title="Technology" data-reactid="43">
                                                                                 <!-- react-text: 44 -->Technology<!-- /react-text -->
                                                                              </a>
                                                                           </li>
                                                                        </ul>
                                                                     </div>
                                                                     <div class="D(tbc) Va(t) Lh(itemHeight) Lh(itemHeight_uhMagDesign)!" data-reactid="45">
                                                                        <div class="nr-applet-moreNav Fl(start) Pos(r) H(itemHeight) Mstart(-10px) Pstart(10px) V(h) H(itemHeight_uhMagDesign)!" data-subnav-type="more-menu" data-reactid="46">
                                                                           <svg class="Cur(p)" width="16" style="vertical-align:middle;cursor:pointer;margin-top:-1px;color:#696969;fill:#696969;stroke:#696969;stroke-width:0;" height="16" viewBox="0 0 96 96" data-icon="StreamShare" data-reactid="47">
                                                                              <path d="M16 38c-5.516 0-10 4.477-10 10 0 5.525 4.484 10 10 10 5.53 0 10-4.475 10-10 0-5.523-4.47-10-10-10zM48 38c-5.516 0-10 4.477-10 10 0 5.525 4.484 10 10 10 5.53 0 10-4.475 10-10 0-5.523-4.47-10-10-10zM80 38c-5.516 0-10 4.477-10 10 0 5.525 4.484 10 10 10 5.53 0 10-4.475 10-10 0-5.523-4.47-10-10-10z" data-reactid="48"></path>
                                                                           </svg>
                                                                        </div>
                                                                     </div>
                                                                  </div>
                                                               </div>
                                                               <div class="W(100%) H(0)! H(2px) Bgc(borderColorDark_uhMagDesign)" data-reactid="49"></div>
                                                            </div>
                                                         </div>
                                                      </div>
                                                   </nav>
                                                </div>
                                             </div>
                                          </div>
                                          <script>if (window.performance) {window.performance.mark && window.performance.mark('NavLite');window.performance.measure && window.performance.measure('NavLiteDone','PageStart','NavLite');}</script>
                                       </div>
                                    </div>
                                 </div>
                              </div>
                           </div>
                           <div id="YDC-SecondaryNav" class="YDC-SecondaryNav hasScrolled_Bdbw(0px) Bxsh($navrailShadow) hasScrolled_Bxsh(headerShadow) Panel-open_Bxsh(headerShadow) Op(1) Panel-open_Op(0) Trsp(a) Trsdu(300ms)" data-reactid="16">
                              <div id="YDC-SecondaryNav-Stack" class="YDC-SecondaryNav Miw(1007px) Maw(1260px) tablet_Miw(600px)--noRightRail Bxz(bb) Bdstartc(t) Bdstartw(20px) Bdendc(t) Bdends(s) Bdendw(20px) Bdstarts(s) Mx(a) tablet_Bd(n)" data-reactid="17">
                                 <div data-reactid="18">
                                    <div data-reactid="19">
                                       <div id="mrt-node-SecondaryNav-0-SecondaryNav" data-locator="subtree-root">
                                          <div id="SecondaryNav-0-SecondaryNav-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="448043048">
                                             <div class=" Bgc(white) Whs(nw)" data-reactid="2">
                                                <ul data-test="secnav-list" class="D(ib) Bgc(white) M(0) T(0) List(n) Whs(n) Pt(3px) H(37px) Cf Ov(h) Va(m)" data-reactid="3">
                                                   <li class=" D(ib) Bdbw(3px) Bdbs(s) Bdbc(t) Bdbc($c-fuji-blue-1-a):h Cur(p) sec-nav-itm Fw(500) Miw(36px) " style="margin-right:16px;" data-test="secnav-list-itm" data-reactid="4"><a class="D(b) Td(n) Ta(start) C(black) Lh(34px)" href="/calendar" title="Calendars" data-reactid="5">Calendars</a></li>
                                                   <li class=" D(ib) Bdbw(3px) Bdbs(s) Bdbc(t) Bdbc($c-fuji-blue-1-a):h Cur(p) sec-nav-itm Fw(500) Miw(36px) " style="margin-right:16px;" data-test="secnav-list-itm" data-reactid="6"><a class="D(b) Td(n) Ta(start) C(black) Lh(34px)" href="/trending-tickers" title="Trending Tickers" data-reactid="7">Trending Tickers</a></li>
                                                   <li class=" D(ib) Bdbw(3px) Bdbs(s) Bdbc(t) Bdbc($c-fuji-blue-1-a):h Cur(p) sec-nav-itm Fw(500) Miw(36px) " style="margin-right:16px;" data-test="secnav-list-itm" data-reactid="8"><a class="D(b) Td(n) Ta(start) C(black) Lh(34px)" href="/most-active" title="Stocks: Most Actives" data-reactid="9">Stocks: Most Actives</a></li>
                                                   <li class=" D(ib) Bdbw(3px) Bdbs(s) Bdbc(t) Bdbc($c-fuji-blue-1-a):h Cur(p) sec-nav-itm Fw(500) Miw(36px) " style="margin-right:16px;" data-test="secnav-list-itm" data-reactid="10"><a class="D(b) Td(n) Ta(start) C(black) Lh(34px)" href="/gainers" title="Stocks: Gainers" data-reactid="11">Stocks: Gainers</a></li>
                                                   <li class=" D(ib) Bdbw(3px) Bdbs(s) Bdbc(t) Bdbc($c-fuji-blue-1-a):h Cur(p) sec-nav-itm Fw(500) Miw(36px) Bdbc($c-fuji-blue-1-a)!" style="margin-right:16px;" data-test="secnav-list-itm" data-reactid="12"><a class="D(b) Td(n) Ta(start) C(black) Lh(34px)" href="/losers" title="Stocks: Losers" data-reactid="13">Stocks: Losers</a></li>
                                                   <li class=" D(ib) Bdbw(3px) Bdbs(s) Bdbc(t) Bdbc($c-fuji-blue-1-a):h Cur(p) sec-nav-itm Fw(500) Miw(36px) " style="margin-right:16px;" data-test="secnav-list-itm" data-reactid="14"><a class="D(b) Td(n) Ta(start) C(black) Lh(34px)" href="/etfs" title="Top ETFs" data-reactid="15">Top ETFs</a></li>
                                                   <li class=" D(ib) Bdbw(3px) Bdbs(s) Bdbc(t) Bdbc($c-fuji-blue-1-a):h Cur(p) sec-nav-itm Fw(500) Miw(36px) " style="margin-right:16px;" data-test="secnav-list-itm" data-reactid="16"><a class="D(b) Td(n) Ta(start) C(black) Lh(34px)" href="/commodities" title="Commodities" data-reactid="17">Commodities</a></li>
                                                   <li class=" D(ib) Bdbw(3px) Bdbs(s) Bdbc(t) Bdbc($c-fuji-blue-1-a):h Cur(p) sec-nav-itm Fw(500) Miw(36px) " style="margin-right:16px;" data-test="secnav-list-itm" data-reactid="18"><a class="D(b) Td(n) Ta(start) C(black) Lh(34px)" href="/world-indices" title="World Indices" data-reactid="19">World Indices</a></li>
                                                   <li class=" D(ib) Bdbw(3px) Bdbs(s) Bdbc(t) Bdbc($c-fuji-blue-1-a):h Cur(p) sec-nav-itm Fw(500) Miw(36px) " style="margin-right:16px;" data-test="secnav-list-itm" data-reactid="20"><a class="D(b) Td(n) Ta(start) C(black) Lh(34px)" href="/currencies" title="Currencies" data-reactid="21">Currencies</a></li>
                                                   <li class=" D(ib) Bdbw(3px) Bdbs(s) Bdbc(t) Bdbc($c-fuji-blue-1-a):h Cur(p) sec-nav-itm Fw(500) Miw(36px) " style="margin-right:16px;" data-test="secnav-list-itm" data-reactid="22"><a class="D(b) Td(n) Ta(start) C(black) Lh(34px)" href="/mutualfunds" title="Top Mutual Funds" data-reactid="23">Top Mutual Funds</a></li>
                                                   <li class=" D(ib) Bdbw(3px) Bdbs(s) Bdbc(t) Bdbc($c-fuji-blue-1-a):h Cur(p) sec-nav-itm Fw(500) Miw(36px) " style="margin-right:16px;" data-test="secnav-list-itm" data-reactid="24"><a class="D(b) Td(n) Ta(start) C(black) Lh(34px)" href="/options/highest-open-interest" title="Options: Highest Open Interest" data-reactid="25">Options: Highest Open Interest</a></li>
                                                   <li class=" D(ib) Bdbw(3px) Bdbs(s) Bdbc(t) Bdbc($c-fuji-blue-1-a):h Cur(p) sec-nav-itm Fw(500) Miw(36px) " style="margin-right:16px;" data-test="secnav-list-itm" data-reactid="26"><a class="D(b) Td(n) Ta(start) C(black) Lh(34px)" href="/options/highest-implied-volatility" title="Options: Highest Implied Volatility" data-reactid="27">Options: Highest Implied Volatility</a></li>
                                                   <li class=" D(ib) Bdbw(3px) Bdbs(s) Bdbc(t) Bdbc($c-fuji-blue-1-a):h Cur(p) sec-nav-itm Fw(500) Miw(36px) " style="margin-right:16px;" data-test="secnav-list-itm" data-reactid="28"><a class="D(b) Td(n) Ta(start) C(black) Lh(34px)" href="/bonds" title="US Treasury Bonds Rates" data-reactid="29">US Treasury Bonds Rates</a></li>
                                                </ul>
                                             </div>
                                          </div>
                                       </div>
                                       <script>if (window.performance) {window.performance.mark && window.performance.mark('SecondaryNav-0-SecondaryNav');window.performance.measure && window.performance.measure('SecondaryNav-0-SecondaryNavDone','PageStart','SecondaryNav-0-SecondaryNav');}</script>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div id="YDC-Lead" class="YDC-Lead" data-reactid="20">
                        <div id="YDC-Lead-Stack" class="YDC-Lead-Stack" data-reactid="21">
                           <div data-reactid="22">
                              <div data-reactid="23">
                                 <div id="mrt-node-Lead-0-Ad" data-locator="subtree-root">
                                    <div id="Lead-0-Ad-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="-1494640727">
                                       <div data-reactid="2">
                                          <div id="defaultLDRB-sizer" class="darla-container" style="margin-bottom:8px;padding-top:12px;margin-left:auto;margin-right:auto;text-align:center;line-height:0px;position:relative;z-index:5;" data-reactid="3">
                                             <div id="defaultLDRB-wrapper" class="" data-reactid="4">
                                                <div id="defaultdestLDRB" style="width:728px;height:90px;"></div>
                                             </div>
                                          </div>
                                       </div>
                                    </div>
                                 </div>
                                 <script>if (window.performance) {window.performance.mark && window.performance.mark('Lead-0-Ad');window.performance.measure && window.performance.measure('Lead-0-AdDone','PageStart','Lead-0-Ad');}</script>
                              </div>
                              <div data-reactid="24">
                                 <div id="mrt-node-Lead-1-FinanceHeader" data-locator="subtree-root">
                                    <div id="Lead-1-FinanceHeader-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="128314238">
                                       <div class="Bxz(bb) H(100%) Pos(r) Maw($newGridWidth) Miw($minGridWidth) Miw(a)!--tab768 Miw(a)!--tab1024 Mstart(a) Mend(a) Px(20px) Z(3) My(10px)" data-reactid="2">
                                          <div class="" data-reactid="3">
                                             <div class="D(ib) Fl(end) Pb(6px)" data-reactid="4">
                                                <span class="Fz(xs) Fw(b) D(ib) C($c-fuji-grey-j)" data-reactid="5">
                                                   <svg class="H(16px) W(16px) Va(m)! Mend(5px) Cur(a)! Fill($c-fuji-grey-j)! Stk($c-fuji-grey-j)! Cur(p)" width="16" style="fill:#464e56;stroke:#464e56;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 48 48" data-icon="live" data-reactid="6">
                                                      <path d="M24 20c-2.205 0-4 1.795-4 4s1.795 4 4 4 4-1.795 4-4-1.795-4-4-4M37.12 24.032c0-4.09-1.764-7.896-4.78-10.537-.83-.727-2.094-.644-2.822.187-.727.832-.644 2.095.187 2.823 2.158 1.89 3.416 4.604 3.416 7.527 0 2.932-1.265 5.654-3.434 7.543-.833.726-.92 1.99-.194 2.822.725.833 1.99.92 2.822.194 3.032-2.64 4.807-6.458 4.807-10.558zM45.097 23.982c0-6.996-3.29-13.45-8.77-17.58-.883-.664-2.137-.488-2.802.394-.664.882-.488 2.136.394 2.8 4.487 3.384 7.177 8.66 7.177 14.386 0 5.775-2.736 11.09-7.288 14.468-.89.658-1.074 1.91-.416 2.798.658.887 1.91 1.073 2.797.415 5.56-4.124 8.907-10.625 8.907-17.68zM15 24.032c0-2.923 1.26-5.638 3.416-7.527.83-.728.915-1.99.187-2.823-.727-.83-1.99-.914-2.822-.187-3.015 2.64-4.78 6.448-4.78 10.537 0 4.1 1.776 7.918 4.808 10.56.833.725 2.096.638 2.822-.195.725-.833.638-2.096-.195-2.822-2.17-1.89-3.435-4.61-3.435-7.543zM7 23.982c0-5.726 2.69-11.002 7.178-14.385.882-.665 1.06-1.92.394-2.8-.665-.883-1.92-1.06-2.8-.394C6.29 10.533 3 16.986 3 23.983c0 7.055 3.347 13.556 8.906 17.68.887.658 2.14.472 2.798-.415.658-.887.472-2.14-.415-2.798C9.735 35.073 7 29.757 7 23.982z" data-reactid="7"></path>
                                                   </svg>
                                                   <span class="Va(m)" data-reactid="8">U.S. Markets closed</span>
                                                </span>
                                             </div>
                                          </div>
                                          <div class="Whs(nw) D(ib) Bgc(#fff) W(100%) Bxz(bb)" id="market-summary" aria-label="Market summary containing a list of 14 items" tabindex="0" data-reactid="9">
                                             <div class="Pos(r) Bxz(bb) Mstart(a) Mend(a) Ov(h)" data-reactid="10">
                                                <div class="D(ib) Fl(start)" data-reactid="11">
                                                   <div class="Carousel-Mask Pos(r) Ov(h) market-summary M(0) Pos(r) Ov(h) D(ib) Va(t)" style="width:392px;" data-reactid="12">
                                                      <ul class="Carousel-Slider Pos(r) Whs(nw)" style="margin-left:0;margin-right:-2px;" data-reactid="13">
                                                         <li style="width:45.9%;" class=" D(ib) Bxz(bb) Bdc($c-fuji-grey-c)  Mend(16px)  BdEnd " aria-label="S&amp;P 500" data-reactid="14">
                                                            <h3 class="Maw(160px)" data-reactid="15">
                                                               <a class="Fz(s) Ell Fw(b) C($c-fuji-blue-1-b)" href="/quote/^GSPC?p=^GSPC" title="S&amp;P 500" aria-label="S&amp;P 500 has increased by 0.51% or 13.11 points to 2,575.21 points" data-reactid="16">S&amp;P 500</a><br data-reactid="17"/>
                                                               <span class="Trsdu(0.3s) Fz(s) Mt(4px) Mb(0px) Fw(b) D(ib)" data-reactid="18">
                                                                  <!-- react-text: 19 -->2,575.21<!-- /react-text -->
                                                               </span>
                                                               <div class="Fz(xs) Fw(b)  C($dataGreen)" data-reactid="20">
                                                                  <span class="Trsdu(0.3s)  C($dataGreen)" data-reactid="21">
                                                                     <!-- react-text: 22 -->+<!-- /react-text --><!-- react-text: 23 -->13.11<!-- /react-text -->
                                                                  </span>
                                                                  <span class="Mstart(2px)" data-reactid="24">
                                                                     <!-- react-text: 25 -->(<!-- /react-text -->
                                                                     <span class="Trsdu(0.3s)  C($dataGreen)" data-reactid="26">
                                                                        <!-- react-text: 27 -->+<!-- /react-text --><!-- react-text: 28 -->0.51%<!-- /react-text -->
                                                                     </span>
                                                                     <!-- react-text: 29 -->)<!-- /react-text -->
                                                                  </span>
                                                               </div>
                                                               <a target="_blank" rel="noopener" class="Fl(end) Mt(-30px)" href="/chart/^GSPC" data-symbol="^GSPC" title="S&amp;P 500 Chart" data-reactid="30">
                                                                  <canvas style="width:70px;height:25px;" data-reactid="31"></canvas>
                                                               </a>
                                                            </h3>
                                                         </li>
                                                         <li style="width:45.9%;" class=" D(ib) Bxz(bb) Bdc($c-fuji-grey-c)  Mend(16px) " aria-label="Dow 30" data-reactid="32">
                                                            <h3 class="Maw(160px)" data-reactid="33">
                                                               <a class="Fz(s) Ell Fw(b) C($c-fuji-blue-1-b)" href="/quote/^DJI?p=^DJI" title="Dow 30" aria-label="Dow 30 has increased by 0.71% or 165.59 points to 23,328.63 points" data-reactid="34">Dow 30</a><br data-reactid="35"/>
                                                               <span class="Trsdu(0.3s) Fz(s) Mt(4px) Mb(0px) Fw(b) D(ib)" data-reactid="36">
                                                                  <!-- react-text: 37 -->23,328.63<!-- /react-text -->
                                                               </span>
                                                               <div class="Fz(xs) Fw(b)  C($dataGreen)" data-reactid="38">
                                                                  <span class="Trsdu(0.3s)  C($dataGreen)" data-reactid="39">
                                                                     <!-- react-text: 40 -->+<!-- /react-text --><!-- react-text: 41 -->165.59<!-- /react-text -->
                                                                  </span>
                                                                  <span class="Mstart(2px)" data-reactid="42">
                                                                     <!-- react-text: 43 -->(<!-- /react-text -->
                                                                     <span class="Trsdu(0.3s)  C($dataGreen)" data-reactid="44">
                                                                        <!-- react-text: 45 -->+<!-- /react-text --><!-- react-text: 46 -->0.71%<!-- /react-text -->
                                                                     </span>
                                                                     <!-- react-text: 47 -->)<!-- /react-text -->
                                                                  </span>
                                                               </div>
                                                               <a target="_blank" rel="noopener" class="Fl(end) Mt(-30px)" href="/chart/^DJI" data-symbol="^DJI" title="Dow 30 Chart" data-reactid="48">
                                                                  <canvas style="width:70px;height:25px;" data-reactid="49"></canvas>
                                                               </a>
                                                            </h3>
                                                         </li>
                                                      </ul>
                                                   </div>
                                                   <div class="D(ib) Z(5) T(0) End(0) nav" data-reactid="50">
                                                      <button class="market-summary-button P(0) Zoom(1) O(n):f Bgc(#fff) H(60px) W(22px) Bdendc($c-fuji-grey-c) Bdendw(1px) Bdends(s) Disabled" title="previous" data-reactid="51">
                                                         <svg class="Mstart(-8px) Fill($c-fuji-grey-c)! Stk($c-fuji-grey-c)! Cur(p)" width="30" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="30" viewBox="0 0 48 48" data-icon="caret-left" data-reactid="52">
                                                            <path d="M16.14 24.102L28.865 36.83c.78.78 2.048.78 2.828 0 .78-.78.78-2.047 0-2.828l-9.9-9.9 9.9-9.9c.78-.78.78-2.047 0-2.827-.78-.78-2.047-.78-2.828 0L16.14 24.102z" data-reactid="53"></path>
                                                         </svg>
                                                      </button>
                                                      <button class="market-summary-button P(0) Zoom(1) O(n):f Bgc(#fff) H(60px) W(22px) Bgc($extraLightBlue):h Bgc($extraLightBlue):f" title="next" data-reactid="54">
                                                         <svg class="Mstart(-6px) Fill($c-fuji-blue-1-b)! Stk($c-fuji-blue-1-b)! Cur(p)" width="30" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="30" viewBox="0 0 48 48" data-icon="caret-right" data-reactid="55">
                                                            <path d="M33.447 24.102L20.72 11.375c-.78-.78-2.048-.78-2.828 0-.78.78-.78 2.047 0 2.828l9.9 9.9-9.9 9.9c-.78.78-.78 2.047 0 2.827.78.78 2.047.78 2.828 0l12.727-12.728z" data-reactid="56"></path>
                                                         </svg>
                                                      </button>
                                                   </div>
                                                </div>
                                                <div class="broker-buttons D(ib) Fl(end) H(60px)" style="width:528px;" data-reactid="57">
                                                   <div style="display:inline-block;width:136px;" data-reactid="58">
                                                      <div data-reactid="59">
                                                         <div id="defaultFB2-sizer" class="darla-container Pos-r Z-0 Pos(r) Ov(a) Z(0)" style="height:100%;width:100%;" data-reactid="60">
                                                            <div id="defaultFB2-wrapper" class="" data-reactid="61">
                                                               <div id="defaultdestFB2" style="width:120px;height:60px;"></div>
                                                            </div>
                                                         </div>
                                                      </div>
                                                   </div>
                                                   <div style="display:inline-block;width:136px;" data-reactid="62">
                                                      <div data-reactid="63">
                                                         <div id="defaultFB2-1-sizer" class="darla-container Pos-r Z-0 Pos(r) Ov(a) Z(0)" style="height:100%;width:100%;" data-reactid="64">
                                                            <div id="defaultFB2-1-wrapper" class="" data-reactid="65">
                                                               <div id="defaultdestFB2-1" style="width:120px;height:60px;"></div>
                                                            </div>
                                                         </div>
                                                      </div>
                                                   </div>
                                                   <div style="display:inline-block;width:136px;" data-reactid="66">
                                                      <div data-reactid="67">
                                                         <div id="defaultFB2-2-sizer" class="darla-container Pos-r Z-0 Pos(r) Ov(a) Z(0)" style="height:100%;width:100%;" data-reactid="68">
                                                            <div id="defaultFB2-2-wrapper" class="" data-reactid="69">
                                                               <div id="defaultdestFB2-2" style="width:120px;height:60px;"></div>
                                                            </div>
                                                         </div>
                                                      </div>
                                                   </div>
                                                   <div style="display:inline-block;width:120px;" data-reactid="70">
                                                      <div data-reactid="71">
                                                         <div id="defaultFB2-3-sizer" class="darla-container Pos-r Z-0 Pos(r) Ov(a) Z(0)" style="height:100%;width:100%;" data-reactid="72">
                                                            <div id="defaultFB2-3-wrapper" class="" data-reactid="73">
                                                               <div id="defaultdestFB2-3" style="width:120px;height:60px;"></div>
                                                            </div>
                                                         </div>
                                                      </div>
                                                   </div>
                                                </div>
                                                <div class="Cl(b)" data-reactid="74"></div>
                                             </div>
                                          </div>
                                       </div>
                                    </div>
                                 </div>
                                 <script>if (window.performance) {window.performance.mark && window.performance.mark('Lead-1-FinanceHeader');window.performance.measure && window.performance.measure('Lead-1-FinanceHeaderDone','PageStart','Lead-1-FinanceHeader');}</script>
                              </div>
                              <div data-reactid="25">
                                 <div id="mrt-node-Lead-2-FeatureBar" data-locator="subtree-root">
                                    <div id="Lead-2-FeatureBar-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="1211441024">
                                       <!-- react-empty: 2 -->
                                    </div>
                                 </div>
                                 <script>if (window.performance) {window.performance.mark && window.performance.mark('Lead-2-FeatureBar');window.performance.measure && window.performance.measure('Lead-2-FeatureBarDone','PageStart','Lead-2-FeatureBar');}</script>
                              </div>
                              <div data-reactid="26">
                                 <div id="mrt-node-Lead-3-ScreenerCriteria" data-locator="subtree-root">
                                    <div id="Lead-3-ScreenerCriteria-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="-239214679">
                                       <div id="screener-criteria" class="Bxz(bb) Px(20px) Mb(20px) Maw($newGridWidth) Mx(a)" data-test="screener-criteria" data-reactid="2">
                                          <div class="Mb(10px)" data-reactid="3">
                                             <a class="Fw(b) Fz(17px)" href="/screener" data-reactid="4"><span data-reactid="5">All Screeners</span></a><span class="C($c-fuji-grey-j) Fz(17px) Mx(6px) Fw(500)" data-reactid="6">/</span>
                                             <h1 class="Fw(b) Fz(17px) D(ib)" data-reactid="7">Day Losers</h1>
                                          </div>
                                          <div class="Pos(r) Pt(16px) Pb(20px) Bd Bdc($finLightGrayAlt) W(100%) Bgc($panelBackground) Bdrs(3px) " data-reactid="8">
                                             <header data-reactid="9">
                                                <button class="Bd(0) P(0) M(0) Mstart(2px) O(n):f" data-test="crit-tggl-btn" data-reactid="10">
                                                   <svg class="Va(m)! Mt(-3px)  Mt(-3px) Cur(p)" width="20" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="18" viewBox="0 0 48 48" data-icon="caret-right" data-reactid="11">
                                                      <path d="M33.447 24.102L20.72 11.375c-.78-.78-2.048-.78-2.828 0-.78.78-.78 2.047 0 2.828l9.9 9.9-9.9 9.9c-.78.78-.78 2.047 0 2.827.78.78 2.047.78 2.828 0l12.727-12.728z" data-reactid="12"></path>
                                                   </svg>
                                                   <span class="Fw(500) Fz(m) C(black)" data-reactid="13">
                                                      <span data-reactid="14">
                                                         <!-- react-text: 15 -->Applied Filters for <!-- /react-text --><span data-reactid="16">Stocks</span><!-- react-text: 17 --> screener<!-- /react-text -->
                                                      </span>
                                                   </span>
                                                   <span class="C($c-fuji-grey-j) Mstart(10px) Fz(12px) Fw(n) D(b)--mobp Mstart(20px)--mobp Mstart(20px)--mobl Ta(start)--mobp Mt(5px)--mobp D(b)--mobl Ta(start)--mobl Mt(5px)--mobl" data-reactid="18"><span data-reactid="19">Currency in USD</span></span>
                                                </button>
                                             </header>
                                             <div class="Mstart(22px) Pend(25px) " data-reactid="20">
                                                <!-- react-empty: 21 -->
                                                <div class="Mt(15px)" data-reactid="22"><button class="Bgc($c-fuji-blue-1-b) Bgc($actionBlueHover):h C(white) Fw(500) Px(20px) Py(9px) Bdrs(3px) Bd(0) Fz(s) D(ib) Whs(nw) Miw(110px)" data-reactid="23"><span data-reactid="24">Edit</span></button><button class="C($c-fuji-blue-1-b) Bgc(white) Bd Bdc($c-fuji-blue-1-b) Bdc($actionBlueHover):h C($actionBlueHover):h Fw(500) Px(20px) Py(8px) Bdrs(3px) Fz(s) D(ib) Mstart(20px) Whs(nw) Miw(110px)" data-reactid="25"><span data-reactid="26">Save As</span></button></div>
                                             </div>
                                             <div class="W(100%) D(ib) Pos(a) B(0)" data-reactid="27">
                                                <div class="fprogbar" data-reactid="28"></div>
                                             </div>
                                          </div>
                                       </div>
                                    </div>
                                 </div>
                                 <script>if (window.performance) {window.performance.mark && window.performance.mark('Lead-3-ScreenerCriteria');window.performance.measure && window.performance.measure('Lead-3-ScreenerCriteriaDone','PageStart','Lead-3-ScreenerCriteria');}</script>
                              </div>
                              <div data-reactid="27">
                                 <div id="mrt-node-Lead-4-ScreenerResults" data-locator="subtree-root">
                                    <div id="Lead-4-ScreenerResults-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="1166595485">
                                       <section id="screener-results" class="Ta(start) Bxz(bb) Px(20px) Maw($newGridWidth) Mx(a)" aria-label="Screener Results" data-test="screener-results" data-reactid="2">
                                          <ul class="W(100%) Lh(1.7) List(n) Whs(nw) H(50px) Bdbs(s) BdB(4px) Bdbc($finLightGray) Cf Mb(15px) fin-tab-items Bgc($panelBackground)" data-reactid="3">
                                             <li class="D(ib) H(50px) Fw(500) fin-tab-item desktop_Bgc($lightBlue):h desktop-lite_Bgc($lightBlue):h selected" data-reactid="4">
                                                <a class="D(b) Td(n) Lh(50px) Ta(c) Bdbw(3px) Bdbs(s) Bdbc($finLightGray) Px(15px) selected_Bdbc($c-fuji-blue-1-a) selected_C($finDarkLink) selected_Bgc($navSelectedBlue) C($finDarkGray) Px(20px)!" href="/losers" data-reactid="5">
                                                   <!-- react-text: 6 --><!-- /react-text --><span data-reactid="7">Results List</span>
                                                </a>
                                             </li>
                                             <li class="D(ib) H(50px) Fw(500) fin-tab-item desktop_Bgc($lightBlue):h desktop-lite_Bgc($lightBlue):h " data-reactid="8">
                                                <a class="D(b) Td(n) Lh(50px) Ta(c) Bdbw(3px) Bdbs(s) Bdbc($finLightGray) Px(15px) selected_Bdbc($c-fuji-blue-1-a) selected_C($finDarkLink) selected_Bgc($navSelectedBlue) C($finDarkGray) Px(20px)!" href="/losers/heatmap" data-reactid="9">
                                                   <!-- react-text: 10 --><!-- /react-text --><span data-reactid="11">Heatmap View</span><img src="https://s.yimg.com/uc/New.png" class="H(13px) W(25px) Mstart(5px) Va(m)" alt="new" data-reactid="12"/>
                                                </a>
                                             </li>
                                          </ul>
                                          <div id="fin-scr-res-table" class="Pos(r) Pos(r) Mih(265px)" data-reactid="13">
                                             <div class="W(100%) Mb(5px)" data-reactid="14">
                                                <div class="D(ib) Fz(m) Fw(b) Lh(23px)" data-reactid="15">
                                                   <span data-reactid="16">
                                                      <!-- react-text: 17 -->Matching <!-- /react-text --><span data-reactid="18">Stocks</span>
                                                   </span>
                                                   <span class="Mstart(15px) Fw(500) Fz(s)" data-reactid="19"><span data-reactid="20">1-28 of 28 results</span></span>
                                                </div>
                                                <div class="D(ib) Mstart(30px)" data-test="table-toolbar" data-reactid="21">
                                                   <div class="D(ib) Pos(r) " data-reactid="22">
                                                      <button class="Bd(0) Fz(s) C($c-fuji-blue-1-b) C($actionBlueHover):h Fw(500) Py(0) Va(tb) addPortfolio Op(0.5) C($gray)!" disabled="" data-reactid="23">
                                                         <svg class="H(16px) W(23px) Va(m)! Mend(3px) Cur(a)! Cur(p)" width="23" style="fill:#787d82;stroke:#787d82;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="star" data-reactid="24">
                                                            <path d="M8.485 7.83l-6.515.21c-.887.028-1.3 1.117-.66 1.732l4.99 4.78-1.414 6.124c-.2 1.14.767 1.49 1.262 1.254l5.87-3.22 5.788 3.22c.48.228 1.464-.097 1.26-1.254l-1.33-6.124 4.962-4.78c.642-.615.228-1.704-.658-1.732l-6.486-.21-2.618-6.22c-.347-.815-1.496-.813-1.84.003L8.486 7.83zm7.06 6.05l1.11 5.11-4.63-2.576L7.33 18.99l1.177-5.103-4.088-3.91 5.41-.18 2.19-5.216 2.19 5.216 5.395.18-4.06 3.903z" data-reactid="25"></path>
                                                         </svg>
                                                         <span class="Va(m) H(16px) D(ib) Lh(17px)" data-reactid="26"><span data-reactid="27">Add to Portfolio</span></span>
                                                      </button>
                                                   </div>
                                                </div>
                                                <span class="Mstart(10px) Fw(n) Fz(12px) C($gray) Fl(end) Lh(26px) Lh(16px)--mobp Lh(16px)--mobl Fl(start)--sm Mstart(0px)--sm" data-reactid="28">
                                                   <svg class="H(16px) W(16px) Va(m)! Fill($finOrange)! Stk($finOrange) Cur(a)! Mb(3px) Mend(5px) Cur(p)" width="16" style="fill:#ff7b12;stroke:#ff7b12;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 48 48" data-icon="attention" data-reactid="29">
                                                      <path d="M24.993 46.424c-12.13 0-22-9.87-22-22s9.87-22 22-22 22 9.87 22 22-9.87 22-22 22zm0-40c-9.925 0-18 8.075-18 18 0 9.926 8.075 18 18 18s18-8.074 18-18c0-9.924-8.075-18-18-18zM24.993 27.424c-1.104 0-2-.895-2-2v-10c0-1.104.896-2 2-2s2 .896 2 2v10c0 1.105-.895 2-2 2zM22.993 33.424a2 2 0 1 0 4 0 2 2 0 1 0-4 0z" data-reactid="30"></path>
                                                   </svg>
                                                   <span data-reactid="31">Results were generated a few mins ago. Pricing data is updated frequently. Currency in USD</span>
                                                </span>
                                             </div>
                                             <div class="Pos(r)" data-reactid="32">
                                                <div class="Ovx(s) W(100%)" id="scr-res-table" data-reactid="33">
                                                   <table class="W(100%) Pos(r) Bdcl(c) BdB Bdc($c-fuji-grey-c)" data-reactid="34">
                                                      <thead data-reactid="35">
                                                         <tr class="C($c-fuji-grey-j)" data-reactid="36">
                                                            <th class="Va(m) W(28px) Px(6px) Bxz(bb) Py(4px)" data-reactid="37">
                                                               <label class="Ta(c) Pos(r)" data-reactid="38">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="39"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="40">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="41"></path>
                                                                  </svg>
                                                               </label>
                                                            </th>
                                                            <th class="Ta(start) Pstart(6px) Pend(10px) Bgc($extraLightBlue):h Va(m) Py(4px)! Fz(xs)  Fw(400)!" data-reactid="42"><span data-reactid="43">Symbol</span></th>
                                                            <th class="Ta(start) Pend(10px) Bgc($extraLightBlue):h Va(m) Py(4px)! Fz(xs)  Cur(p)  Fw(400)!" data-reactid="44"><span data-reactid="45">Company</span></th>
                                                            <th class="Ta(end) Pstart(20px) Bgc($extraLightBlue):h Va(m) Py(4px)! Fz(xs)  Cur(p)  Fw(400)!" data-reactid="46"><span data-reactid="47">Price (Intraday)</span></th>
                                                            <th class="Ta(end) Pstart(20px) Bgc($extraLightBlue):h Va(m) Py(4px)! Fz(xs)  Cur(p)  Fw(400)!" data-reactid="48"><span data-reactid="49">Change</span></th>
                                                            <th class="Ta(end) Pstart(20px) Bgc($extraLightBlue):h Va(m) Py(4px)! Fz(xs)  Cur(p) C(black) Fw(500)" data-reactid="50">
                                                               <span data-reactid="51">% Change</span>
                                                               <svg class="Va(m)! W(14px) H(14px) Fill(black)! Stk(black)! Mb(2px) Cur(p)" width="48" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="48" viewBox="0 0 48 48" data-icon="caret-up" data-reactid="52">
                                                                  <path d="M24.21 16.03L11.48 28.76c-.78.78-.78 2.047 0 2.827.78.78 2.048.78 2.83 0l9.898-9.9 9.9 9.9c.78.78 2.047.78 2.827 0 .78-.78.78-2.047 0-2.828L24.21 16.03z" data-reactid="53"></path>
                                                               </svg>
                                                            </th>
                                                            <th class="Ta(end) Pstart(20px) Bgc($extraLightBlue):h Va(m) Py(4px)! Fz(xs)  Cur(p)  Fw(400)!" data-reactid="54"><span data-reactid="55">Volume</span></th>
                                                            <th class="Ta(end) Pstart(20px) Bgc($extraLightBlue):h Va(m) Py(4px)! Fz(xs)  Fw(400)!" data-reactid="56"><span data-reactid="57">Avg Vol (3 month)</span></th>
                                                            <th class="Ta(end) Pstart(20px) Pend(10px) W(120px) Bgc($extraLightBlue):h Va(m) Py(4px)! Fz(xs)  Cur(p)  Fw(400)!" data-reactid="58"><span data-reactid="59">Market Cap</span></th>
                                                            <th class="Ta(end) Pstart(20px) Bgc($extraLightBlue):h Va(m) Py(4px)! Fz(xs)  Fw(400)!" data-reactid="60"><span data-reactid="61">PE Ratio (TTM)</span></th>
                                                            <th class="Ta(end) Pstart(20px) Bgc($extraLightBlue):h Va(m) Py(4px)! Fz(xs)  Cur(p)  Fw(400)! Pend(6px)" data-reactid="62"><span data-reactid="63">52 Week Range</span></th>
                                                         </tr>
                                                      </thead>
                                                      <tbody data-reactid="64">
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h " data-reactid="65">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="66">
                                                               <label class="Ta(c) Pos(r)" data-reactid="67">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="68"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="69">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="70"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="71"><a href="/quote/DMPZF?p=DMPZF" title="DOMINO&#x27;S PIZZA GRP ORD GBP0.005" class="Fw(b)" data-reactid="72">DMPZF</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="73">Domino&#x27;s Pizza Group plc</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="74">
                                                               <span class="Trsdu(0.3s) " data-reactid="75">
                                                                  <!-- react-text: 76 -->4.40<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="77">
                                                               <span class="Trsdu(0.3s)  C($dataGreen)" data-reactid="78">
                                                                  <!-- react-text: 79 -->+<!-- /react-text --><!-- react-text: 80 -->0.71<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="81">
                                                               <span class="Trsdu(0.3s)  C($dataGreen)" data-reactid="82">
                                                                  <!-- react-text: 83 -->+<!-- /react-text --><!-- react-text: 84 -->19.22%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="85">310</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="86"><span data-reactid="87">N/A</span></td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="88">2.505B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="89"><span data-reactid="90">N/A</span></td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="91">
                                                               <canvas style="width:140px;height:23px;" data-reactid="92"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h Bgc($altRowColor) " data-reactid="93">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="94">
                                                               <label class="Ta(c) Pos(r)" data-reactid="95">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="96"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="97">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="98"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="99"><a href="/quote/CELG?p=CELG" title="Celgene Corporation" class="Fw(b)" data-reactid="100">CELG</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="101">Celgene Corporation</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="102">
                                                               <span class="Trsdu(0.3s) " data-reactid="103">
                                                                  <!-- react-text: 104 -->121.33<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="105">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="106">
                                                                  <!-- react-text: 107 -->-14.63<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="108">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="109">
                                                                  <!-- react-text: 110 -->-10.76%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="111">27.765M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="112">4.097M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="113">94.923B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="114">37.58</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="115">
                                                               <canvas style="width:140px;height:23px;" data-reactid="116"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h " data-reactid="117">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="118">
                                                               <label class="Ta(c) Pos(r)" data-reactid="119">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="120"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="121">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="122"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="123"><a href="/quote/NCR?p=NCR" title="NCR Corporation" class="Fw(b)" data-reactid="124">NCR</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="125">NCR Corporation</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="126">
                                                               <span class="Trsdu(0.3s) " data-reactid="127">
                                                                  <!-- react-text: 128 -->33.05<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="129">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="130">
                                                                  <!-- react-text: 131 -->-4.00<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="132">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="133">
                                                                  <!-- react-text: 134 -->-10.80%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="135">9.485M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="136">1.121M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="137">4.016B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="138">20.36</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="139">
                                                               <canvas style="width:140px;height:23px;" data-reactid="140"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h Bgc($altRowColor) " data-reactid="141">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="142">
                                                               <label class="Ta(c) Pos(r)" data-reactid="143">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="144"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="145">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="146"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="147"><a href="/quote/LHO?p=LHO" title="LaSalle Hotel Properties" class="Fw(b)" data-reactid="148">LHO</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="149">LaSalle Hotel Properties</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="150">
                                                               <span class="Trsdu(0.3s) " data-reactid="151">
                                                                  <!-- react-text: 152 -->28.52<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="153">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="154">
                                                                  <!-- react-text: 155 -->-1.94<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="156">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="157">
                                                                  <!-- react-text: 158 -->-6.37%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="159">4.657M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="160">1.025M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="161">3.233B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="162">10.61</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="163">
                                                               <canvas style="width:140px;height:23px;" data-reactid="164"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h " data-reactid="165">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="166">
                                                               <label class="Ta(c) Pos(r)" data-reactid="167">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="168"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="169">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="170"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="171"><a href="/quote/GNTX?p=GNTX" title="Gentex Corporation" class="Fw(b)" data-reactid="172">GNTX</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="173">Gentex Corporation</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="174">
                                                               <span class="Trsdu(0.3s) " data-reactid="175">
                                                                  <!-- react-text: 176 -->19.38<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="177">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="178">
                                                                  <!-- react-text: 179 -->-1.28<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="180">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="181">
                                                                  <!-- react-text: 182 -->-6.20%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="183">6.08M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="184">1.99M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="185">5.534B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="186">15.38</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="187">
                                                               <canvas style="width:140px;height:23px;" data-reactid="188"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h Bgc($altRowColor) " data-reactid="189">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="190">
                                                               <label class="Ta(c) Pos(r)" data-reactid="191">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="192"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="193">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="194"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="195"><a href="/quote/IBKC?p=IBKC" title="IBERIABANK Corporation" class="Fw(b)" data-reactid="196">IBKC</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="197">IBERIABANK Corporation</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="198">
                                                               <span class="Trsdu(0.3s) " data-reactid="199">
                                                                  <!-- react-text: 200 -->75.45<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="201">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="202">
                                                                  <!-- react-text: 203 -->-4.70<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="204">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="205">
                                                                  <!-- react-text: 206 -->-5.86%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="207">3.012M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="208">392,065</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="209">4.046B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="210">18.38</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="211">
                                                               <canvas style="width:140px;height:23px;" data-reactid="212"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h " data-reactid="213">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="214">
                                                               <label class="Ta(c) Pos(r)" data-reactid="215">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="216"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="217">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="218"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="219"><a href="/quote/CLF?p=CLF" title="Cleveland-Cliffs Inc." class="Fw(b)" data-reactid="220">CLF</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="221">Cleveland-Cliffs Inc.</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="222">
                                                               <span class="Trsdu(0.3s) " data-reactid="223">
                                                                  <!-- react-text: 224 -->7.02<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="225">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="226">
                                                                  <!-- react-text: 227 -->-0.42<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="228">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="229">
                                                                  <!-- react-text: 230 -->-5.65%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="231">28.558M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="232">10.661M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="233">2.081B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="234">32.20</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="235">
                                                               <canvas style="width:140px;height:23px;" data-reactid="236"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h Bgc($altRowColor) " data-reactid="237">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="238">
                                                               <label class="Ta(c) Pos(r)" data-reactid="239">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="240"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="241">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="242"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="243"><a href="/quote/FOLD?p=FOLD" title="Amicus Therapeutics, Inc." class="Fw(b)" data-reactid="244">FOLD</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="245">Amicus Therapeutics, Inc.</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="246">
                                                               <span class="Trsdu(0.3s) " data-reactid="247">
                                                                  <!-- react-text: 248 -->13.59<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="249">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="250">
                                                                  <!-- react-text: 251 -->-0.72<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="252">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="253">
                                                                  <!-- react-text: 254 -->-5.03%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="255">2.898M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="256">3.383M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="257">2.236B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="258"><span data-reactid="259">N/A</span></td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="260">
                                                               <canvas style="width:140px;height:23px;" data-reactid="261"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h " data-reactid="262">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="263">
                                                               <label class="Ta(c) Pos(r)" data-reactid="264">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="265"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="266">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="267"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="268"><a href="/quote/ARNC-PB?p=ARNC-PB" title="Arconic Inc. Depository Shares " class="Fw(b)" data-reactid="269">ARNC-PB</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="270">Arconic Inc.</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="271">
                                                               <span class="Trsdu(0.3s) " data-reactid="272">
                                                                  <!-- react-text: 273 -->38.90<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="274">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="275">
                                                                  <!-- react-text: 276 -->-1.97<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="277">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="278">
                                                                  <!-- react-text: 279 -->-4.82%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="280">4.097M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="281"><span data-reactid="282">N/A</span></td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="283">10.973B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="284"><span data-reactid="285">N/A</span></td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="286">
                                                               <canvas style="width:140px;height:23px;" data-reactid="287"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h Bgc($altRowColor) " data-reactid="288">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="289">
                                                               <label class="Ta(c) Pos(r)" data-reactid="290">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="291"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="292">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="293"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="294"><a href="/quote/WFT?p=WFT" title="Weatherford International plc (" class="Fw(b)" data-reactid="295">WFT</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="296">Weatherford International plc</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="297">
                                                               <span class="Trsdu(0.3s) " data-reactid="298">
                                                                  <!-- react-text: 299 -->3.54<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="300">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="301">
                                                                  <!-- react-text: 302 -->-0.16<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="303">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="304">
                                                                  <!-- react-text: 305 -->-4.32%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="306">43.706M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="307">16.051M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="308">3.501B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="309"><span data-reactid="310">N/A</span></td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="311">
                                                               <canvas style="width:140px;height:23px;" data-reactid="312"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h " data-reactid="313">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="314">
                                                               <label class="Ta(c) Pos(r)" data-reactid="315">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="316"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="317">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="318"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="319"><a href="/quote/DRH?p=DRH" title="Diamondrock Hospitality Company" class="Fw(b)" data-reactid="320">DRH</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="321">DiamondRock Hospitality Company</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="322">
                                                               <span class="Trsdu(0.3s) " data-reactid="323">
                                                                  <!-- react-text: 324 -->10.73<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="325">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="326">
                                                                  <!-- react-text: 327 -->-0.48<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="328">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="329">
                                                                  <!-- react-text: 330 -->-4.28%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="331">2.581M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="332">1.944M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="333">2.149B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="334">21.72</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="335">
                                                               <canvas style="width:140px;height:23px;" data-reactid="336"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h Bgc($altRowColor) " data-reactid="337">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="338">
                                                               <label class="Ta(c) Pos(r)" data-reactid="339">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="340"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="341">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="342"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="343"><a href="/quote/BTG?p=BTG" title="B2Gold Corp Common shares (Cana" class="Fw(b)" data-reactid="344">BTG</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="345">B2Gold Corp.</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="346">
                                                               <span class="Trsdu(0.3s) " data-reactid="347">
                                                                  <!-- react-text: 348 -->2.56<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="349">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="350">
                                                                  <!-- react-text: 351 -->-0.11<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="352">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="353">
                                                                  <!-- react-text: 354 -->-4.12%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="355">2.955M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="356">3.072M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="357">2.48B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="358">43.39</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="359">
                                                               <canvas style="width:140px;height:23px;" data-reactid="360"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h " data-reactid="361">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="362">
                                                               <label class="Ta(c) Pos(r)" data-reactid="363">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="364"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="365">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="366"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="367"><a href="/quote/GRAM?p=GRAM" title="Grana y Montero S.A.A. American" class="Fw(b)" data-reactid="368">GRAM</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="369">Graa y Montero S.A.A.</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="370">
                                                               <span class="Trsdu(0.3s) " data-reactid="371">
                                                                  <!-- react-text: 372 -->4.47<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="373">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="374">
                                                                  <!-- react-text: 375 -->-0.19<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="376">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="377">
                                                                  <!-- react-text: 378 -->-4.08%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="379">389,208</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="380">241,210</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="381">2.95B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="382">14.19</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="383">
                                                               <canvas style="width:140px;height:23px;" data-reactid="384"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h Bgc($altRowColor) " data-reactid="385">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="386">
                                                               <label class="Ta(c) Pos(r)" data-reactid="387">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="388"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="389">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="390"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="391"><a href="/quote/PG?p=PG" title="Procter &amp; Gamble Company (The)" class="Fw(b)" data-reactid="392">PG</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="393">The Procter &amp; Gamble Company</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="394">
                                                               <span class="Trsdu(0.3s) " data-reactid="395">
                                                                  <!-- react-text: 396 -->88.25<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="397">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="398">
                                                                  <!-- react-text: 399 -->-3.34<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="400">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="401">
                                                                  <!-- react-text: 402 -->-3.65%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="403">19.998M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="404">6.785M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="405">225.038B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="406">15.78</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="407">
                                                               <canvas style="width:140px;height:23px;" data-reactid="408"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h " data-reactid="409">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="410">
                                                               <label class="Ta(c) Pos(r)" data-reactid="411">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="412"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="413">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="414"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="415"><a href="/quote/PEB?p=PEB" title="Pebblebrook Hotel Trust  of Ben" class="Fw(b)" data-reactid="416">PEB</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="417">Pebblebrook Hotel Trust</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="418">
                                                               <span class="Trsdu(0.3s) " data-reactid="419">
                                                                  <!-- react-text: 420 -->35.67<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="421">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="422">
                                                                  <!-- react-text: 423 -->-1.32<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="424">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="425">
                                                                  <!-- react-text: 426 -->-3.57%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="427">1.712M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="428">639,432</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="429">2.468B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="430">129.71</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="431">
                                                               <canvas style="width:140px;height:23px;" data-reactid="432"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h Bgc($altRowColor) " data-reactid="433">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="434">
                                                               <label class="Ta(c) Pos(r)" data-reactid="435">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="436"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="437">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="438"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="439"><a href="/quote/HOMB?p=HOMB" title="Home BancShares, Inc." class="Fw(b)" data-reactid="440">HOMB</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="441">Home Bancshares, Inc. (Conway, AR)</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="442">
                                                               <span class="Trsdu(0.3s) " data-reactid="443">
                                                                  <!-- react-text: 444 -->24.11<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="445">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="446">
                                                                  <!-- react-text: 447 -->-0.85<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="448">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="449">
                                                                  <!-- react-text: 450 -->-3.41%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="451">3.47M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="452">1.084M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="453">4.188B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="454">18.03</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="455">
                                                               <canvas style="width:140px;height:23px;" data-reactid="456"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h " data-reactid="457">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="458">
                                                               <label class="Ta(c) Pos(r)" data-reactid="459">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="460"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="461">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="462"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="463"><a href="/quote/KGC?p=KGC" title="Kinross Gold Corporation" class="Fw(b)" data-reactid="464">KGC</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="465">Kinross Gold Corporation</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="466">
                                                               <span class="Trsdu(0.3s) " data-reactid="467">
                                                                  <!-- react-text: 468 -->4.16<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="469">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="470">
                                                                  <!-- react-text: 471 -->-0.14<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="472">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="473">
                                                                  <!-- react-text: 474 -->-3.26%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="475">9.416M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="476">10.044M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="477">5.118B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="478">99.05</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="479">
                                                               <canvas style="width:140px;height:23px;" data-reactid="480"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h Bgc($altRowColor) " data-reactid="481">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="482">
                                                               <label class="Ta(c) Pos(r)" data-reactid="483">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="484"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="485">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="486"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="487"><a href="/quote/KL?p=KL" title="Kirkland Lake Gold Ltd." class="Fw(b)" data-reactid="488">KL</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="489">Kirkland Lake Gold Ltd.</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="490">
                                                               <span class="Trsdu(0.3s) " data-reactid="491">
                                                                  <!-- react-text: 492 -->13.00<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="493">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="494">
                                                                  <!-- react-text: 495 -->-0.42<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="496">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="497">
                                                                  <!-- react-text: 498 -->-3.13%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="499">465,593</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="500">383,249</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="501">2.66B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="502">32.02</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="503">
                                                               <canvas style="width:140px;height:23px;" data-reactid="504"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h " data-reactid="505">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="506">
                                                               <label class="Ta(c) Pos(r)" data-reactid="507">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="508"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="509">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="510"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="511"><a href="/quote/GRPN?p=GRPN" title="Groupon, Inc." class="Fw(b)" data-reactid="512">GRPN</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="513">Groupon, Inc.</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="514">
                                                               <span class="Trsdu(0.3s) " data-reactid="515">
                                                                  <!-- react-text: 516 -->4.80<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="517">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="518">
                                                                  <!-- react-text: 519 -->-0.15<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="520">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="521">
                                                                  <!-- react-text: 522 -->-3.03%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="523">19.493M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="524">7.003M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="525">2.669B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="526"><span data-reactid="527">N/A</span></td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="528">
                                                               <canvas style="width:140px;height:23px;" data-reactid="529"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h Bgc($altRowColor) " data-reactid="530">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="531">
                                                               <label class="Ta(c) Pos(r)" data-reactid="532">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="533"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="534">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="535"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="536"><a href="/quote/SAM?p=SAM" title="Boston Beer Company, Inc. (The)" class="Fw(b)" data-reactid="537">SAM</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="538">The Boston Beer Company, Inc.</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="539">
                                                               <span class="Trsdu(0.3s) " data-reactid="540">
                                                                  <!-- react-text: 541 -->172.85<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="542">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="543">
                                                                  <!-- react-text: 544 -->-5.30<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="545">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="546">
                                                                  <!-- react-text: 547 -->-2.98%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="548">205,584</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="549">183,989</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="550">2.055B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="551">24.59</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="552">
                                                               <canvas style="width:140px;height:23px;" data-reactid="553"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h " data-reactid="554">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="555">
                                                               <label class="Ta(c) Pos(r)" data-reactid="556">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="557"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="558">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="559"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="560"><a href="/quote/CTRP?p=CTRP" title="Ctrip.com International, Ltd. -" class="Fw(b)" data-reactid="561">CTRP</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="562">Ctrip.com International, Ltd.</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="563">
                                                               <span class="Trsdu(0.3s) " data-reactid="564">
                                                                  <!-- react-text: 565 -->48.35<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="566">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="567">
                                                                  <!-- react-text: 568 -->-1.45<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="569">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="570">
                                                                  <!-- react-text: 571 -->-2.91%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="572">13.406M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="573">4.627M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="574">25.318B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="575">690.71</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="576">
                                                               <canvas style="width:140px;height:23px;" data-reactid="577"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h Bgc($altRowColor) " data-reactid="578">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="579">
                                                               <label class="Ta(c) Pos(r)" data-reactid="580">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="581"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="582">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="583"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="584"><a href="/quote/NS?p=NS" title="Nustar Energy L.P.  Common Unit" class="Fw(b)" data-reactid="585">NS</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="586">NuStar Energy L.P.</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="587">
                                                               <span class="Trsdu(0.3s) " data-reactid="588">
                                                                  <!-- react-text: 589 -->34.77<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="590">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="591">
                                                                  <!-- react-text: 592 -->-1.01<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="593">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="594">
                                                                  <!-- react-text: 595 -->-2.82%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="596">491,840</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="597">323,246</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="598">3.235B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="599">47.76</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="600">
                                                               <canvas style="width:140px;height:23px;" data-reactid="601"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h " data-reactid="602">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="603">
                                                               <label class="Ta(c) Pos(r)" data-reactid="604">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="605"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="606">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="607"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="608"><a href="/quote/RLI?p=RLI" title="RLI Corp." class="Fw(b)" data-reactid="609">RLI</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="610">RLI Corp.</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="611">
                                                               <span class="Trsdu(0.3s) " data-reactid="612">
                                                                  <!-- react-text: 613 -->58.03<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="614">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="615">
                                                                  <!-- react-text: 616 -->-1.68<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="617">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="618">
                                                                  <!-- react-text: 619 -->-2.81%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="620">297,823</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="621">151,281</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="622">2.556B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="623">25.68</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="624">
                                                               <canvas style="width:140px;height:23px;" data-reactid="625"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h Bgc($altRowColor) " data-reactid="626">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="627">
                                                               <label class="Ta(c) Pos(r)" data-reactid="628">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="629"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="630">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="631"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="632"><a href="/quote/MOMO?p=MOMO" title="Momo Inc. - American Depositary" class="Fw(b)" data-reactid="633">MOMO</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="634">Momo Inc.</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="635">
                                                               <span class="Trsdu(0.3s) " data-reactid="636">
                                                                  <!-- react-text: 637 -->31.89<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="638">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="639">
                                                                  <!-- react-text: 640 -->-0.92<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="641">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="642">
                                                                  <!-- react-text: 643 -->-2.80%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="644">4.586M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="645">6.187M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="646">6.287B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="647">25.01</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="648">
                                                               <canvas style="width:140px;height:23px;" data-reactid="649"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h " data-reactid="650">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="651">
                                                               <label class="Ta(c) Pos(r)" data-reactid="652">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="653"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="654">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="655"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="656"><a href="/quote/SHO?p=SHO" title="Sunstone Hotel Investors, Inc. " class="Fw(b)" data-reactid="657">SHO</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="658">Sunstone Hotel Investors, Inc.</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="659">
                                                               <span class="Trsdu(0.3s) " data-reactid="660">
                                                                  <!-- react-text: 661 -->16.53<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="662">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="663">
                                                                  <!-- react-text: 664 -->-0.43<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="665">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="666">
                                                                  <!-- react-text: 667 -->-2.54%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="668">1.944M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="669">1.625M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="670">3.725B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="671">21.44</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="672">
                                                               <canvas style="width:140px;height:23px;" data-reactid="673"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h Bgc($altRowColor) " data-reactid="674">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="675">
                                                               <label class="Ta(c) Pos(r)" data-reactid="676">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="677"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="678">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="679"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="680"><a href="/quote/RLJ?p=RLJ" title="RLJ Lodging Trust  of Beneficia" class="Fw(b)" data-reactid="681">RLJ</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="682">RLJ Lodging Trust</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="683">
                                                               <span class="Trsdu(0.3s) " data-reactid="684">
                                                                  <!-- react-text: 685 -->21.98<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="686">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="687">
                                                                  <!-- react-text: 688 -->-0.58<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="689">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="690">
                                                                  <!-- react-text: 691 -->-2.57%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="692">1.773M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="693">1.996M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="694">6.58B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="695">15.16</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="696">
                                                               <canvas style="width:140px;height:23px;" data-reactid="697"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h " data-reactid="698">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="699">
                                                               <label class="Ta(c) Pos(r)" data-reactid="700">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="701"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="702">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="703"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="704"><a href="/quote/VRX?p=VRX" title="Valeant Pharmaceuticals Interna" class="Fw(b)" data-reactid="705">VRX</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="706">Valeant Pharmaceuticals International, Inc.</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="707">
                                                               <span class="Trsdu(0.3s) " data-reactid="708">
                                                                  <!-- react-text: 709 -->12.13<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="710">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="711">
                                                                  <!-- react-text: 712 -->-0.35<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="713">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="714">
                                                                  <!-- react-text: 715 -->-2.80%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="716">9.259M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="717">11.95M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="718">4.228B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="719"><span data-reactid="720">N/A</span></td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="721">
                                                               <canvas style="width:140px;height:23px;" data-reactid="722"></canvas>
                                                            </td>
                                                         </tr>
                                                         <tr class="H(32px) Bgc($extraLightBlue):h BdT Bdtc($tableBorderGray) Bdtc($tableBorderBlue):h Bgc($altRowColor) " data-reactid="723">
                                                            <td class="Va(m)W(28px) Px(6px) Bxz(bb) Pt(7px) Pb(8px)" data-reactid="724">
                                                               <label class="Ta(c) Pos(r)" data-reactid="725">
                                                                  <input type="checkbox" class="Pos(a) V(h)" data-reactid="726"/>
                                                                  <svg class="Va(m)! H(16px) W(16px) Stk($plusGray)! Fill($plusGray)!  Cur(p)" width="16" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" height="16" viewBox="0 0 24 24" data-icon="checkbox-unchecked" data-reactid="727">
                                                                     <path d="M3 3h18v18H3V3zm19-2H2c-.553 0-1 .448-1 1v20c0 .552.447 1 1 1h20c.552 0 1-.448 1-1V2c0-.552-.448-1-1-1z" data-reactid="728"></path>
                                                                  </svg>
                                                               </label>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)" data-reactid="729"><a href="/quote/ENB?p=ENB" title="Enbridge Inc" class="Fw(b)" data-reactid="730">ENB</a></td>
                                                            <td class="Va(m) Fz(s) Ta(start) Pend(10px)" data-reactid="731">Enbridge Inc.</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)Fw(500)" data-reactid="732">
                                                               <span class="Trsdu(0.3s) " data-reactid="733">
                                                                  <!-- react-text: 734 -->39.31<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="735">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="736">
                                                                  <!-- react-text: 737 -->-1.02<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="738">
                                                               <span class="Trsdu(0.3s)  C($dataRed)" data-reactid="739">
                                                                  <!-- react-text: 740 -->-2.53%<!-- /react-text -->
                                                               </span>
                                                            </td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="741">3.889M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="742">1.789M</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(10px) W(120px)" data-reactid="743">63.861B</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px)" data-reactid="744">32.19</td>
                                                            <td class="Va(m) Fz(s) Ta(end) Pstart(20px) Pend(6px) " data-reactid="745">
                                                               <canvas style="width:140px;height:23px;" data-reactid="746"></canvas>
                                                            </td>
                                                         </tr>
                                                      </tbody>
                                                   </table>
                                                </div>
                                                <!-- react-empty: 747 -->
                                                <div class="Pos(a) W(20px) End(-20px) T(0px) H(100%) Bxsh($moreContentBoxShadow)" data-reactid="748"></div>
                                                <div class="Pos(a) W(35px) End(-35px) T(-10px) H(105%) Bgc(white)" data-reactid="749"></div>
                                             </div>
                                          </div>
                                       </section>
                                    </div>
                                 </div>
                                 <script>if (window.performance) {window.performance.mark && window.performance.mark('Lead-4-ScreenerResults');window.performance.measure && window.performance.measure('Lead-4-ScreenerResultsDone','PageStart','Lead-4-ScreenerResults');}</script>
                              </div>
                              <div data-reactid="28">
                                 <div id="mrt-node-Lead-5-Ad" data-locator="subtree-root">
                                    <div id="Lead-5-Ad-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="682137535">
                                       <div data-reactid="2">
                                          <div id="defaultLDRB2-sizer" class="darla-container" style="margin-bottom:8px;margin-top:8px;margin-left:auto;margin-right:auto;text-align:center;line-height:0px;position:relative;z-index:4;" data-reactid="3">
                                             <div id="defaultLDRB2-wrapper" class="" data-reactid="4">
                                                <div id="defaultdestLDRB2" style="width:728px;height:90px;"></div>
                                             </div>
                                          </div>
                                       </div>
                                    </div>
                                 </div>
                                 <script>if (window.performance) {window.performance.mark && window.performance.mark('Lead-5-Ad');window.performance.measure && window.performance.measure('Lead-5-AdDone','PageStart','Lead-5-Ad');}</script>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="Pos(r) Bgc($bg-content) Miw(1007px) Maw(1260px) tablet_Miw(600px)--noRightRail Bxz(bb) Bdstartc(t) Bdstartw(20px) Bdendc(t) Bdends(s) Bdendw(20px) Bdstarts(s) Mx(a)" data-reactid="29">
                        <div id="YDC-Col1" class="YDC-Col1 Bdendc(t) Bdendw(340px) tablet_Bdendw(0)--noRightRail Bdends(s) Mt(17px) Pos(r)" data-reactid="30">
                           <div id="Main" role="content" tabindex="-1" data-reactid="31">
                              <div data-reactid="32">
                                 <div id="mrt-node-screenerDetail-0-Stream" data-locator="subtree-root">
                                    <div id="screenerDetail-0-Stream-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="559621334">
                                       <div data-reactid="2"></div>
                                    </div>
                                 </div>
                                 <script>if (window.performance) {window.performance.mark && window.performance.mark('FinStream');window.performance.measure && window.performance.measure('FinStreamDone','PageStart','FinStream');}</script>
                              </div>
                              <div data-reactid="33">
                                 <div id="mrt-node-Col1-1-AdUnitWithTdAds" data-locator="subtree-root">
                                    <div id="Col1-1-AdUnitWithTdAds-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="-943875508">
                                       <div class="ad-foot" data-reactid="2">
                                          <div data-reactid="3">
                                             <div data-reactid="4">
                                                <div id="defaultFOOT-sizer" class="darla-container Pos-r Z-0 Pos(r) Ov(a) Z(0)" style="height:0;width:0;" data-reactid="5">
                                                   <div id="defaultFOOT-wrapper" class="Pos-a T-0 B-0 Start-0 End-0 Ov-h Pos(a) T(0) B(0) Start(0) End(0) Ov(h)" data-reactid="6">
                                                      <div id="defaultdestFOOT" style=""></div>
                                                   </div>
                                                </div>
                                             </div>
                                          </div>
                                       </div>
                                    </div>
                                 </div>
                                 <script>if (window.performance) {window.performance.mark && window.performance.mark('Col1-1-AdUnitWithTdAds');window.performance.measure && window.performance.measure('Col1-1-AdUnitWithTdAdsDone','PageStart','Col1-1-AdUnitWithTdAds');}</script>
                              </div>
                              <div data-reactid="34">
                                 <div id="mrt-node-Col1-2-AdUnitWithTdAds" data-locator="subtree-root">
                                    <div id="Col1-2-AdUnitWithTdAds-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="-1427268619">
                                       <div class="ad-fsrvy" data-reactid="2">
                                          <div data-reactid="3">
                                             <div data-reactid="4">
                                                <div id="defaultFSRVY-sizer" class="darla-container Pos-r Z-0 Pos(r) Ov(a) Z(0)" style="height:0;width:0;" data-reactid="5">
                                                   <div id="defaultFSRVY-wrapper" class="Pos-a T-0 B-0 Start-0 End-0 Ov-h Pos(a) T(0) B(0) Start(0) End(0) Ov(h)" data-reactid="6">
                                                      <div id="defaultdestFSRVY" style=""></div>
                                                   </div>
                                                </div>
                                             </div>
                                          </div>
                                       </div>
                                    </div>
                                 </div>
                                 <script>if (window.performance) {window.performance.mark && window.performance.mark('Col1-2-AdUnitWithTdAds');window.performance.measure && window.performance.measure('Col1-2-AdUnitWithTdAdsDone','PageStart','Col1-2-AdUnitWithTdAds');}</script>
                              </div>
                           </div>
                        </div>
                        <div class="Pos(a) W(300px) End(0) T(0) tablet_D(n)--noRightRail" data-reactid="35">
                           <!-- react-empty: 36 -->
                           <div id="YDC-Col2" class="YDC-Col2" data-reactid="37">
                              <div class="sticky-outer-wrapper" data-reactid="38">
                                 <div class="sticky-inner-wrapper" style="position:relative;top:0px;" data-reactid="39">
                                    <div id="YDC-Col2-Stack" class="YDC-Col2-Stack Pos(r) W(300px)" data-reactid="40">
                                       <div id="Aside" role="complementary" tabindex="-1" data-reactid="41">
                                          <div data-reactid="42">
                                             <div id="mrt-node-Col2-0-AdUnitWithTdAds" data-locator="subtree-root">
                                                <div id="Col2-0-AdUnitWithTdAds-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="-1211991752">
                                                   <div class="ad-lrec" data-reactid="2">
                                                      <div data-reactid="3">
                                                         <div data-reactid="4">
                                                            <div id="defaultLREC-sizer" class="darla-container D-n D(n)" data-reactid="5">
                                                               <div id="defaultLREC-wrapper" class="" data-reactid="6">
                                                                  <div id="defaultdestLREC" style=""></div>
                                                               </div>
                                                            </div>
                                                         </div>
                                                      </div>
                                                   </div>
                                                </div>
                                             </div>
                                             <script>if (window.performance) {window.performance.mark && window.performance.mark('Col2-0-AdUnitWithTdAds');window.performance.measure && window.performance.measure('Col2-0-AdUnitWithTdAdsDone','PageStart','Col2-0-AdUnitWithTdAds');}</script>
                                          </div>
                                          <div data-reactid="43">
                                             <div id="mrt-node-Col2-1-Stream" data-locator="subtree-root">
                                                <div id="Col2-1-Stream-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="264957217">
                                                   <div id="Col2-1-Stream" class="tdv2-applet-stream Bdc(#e2e2e6)" style="max-width:900px;" data-reactid="2">
                                                      <ul class="Mb(0) Ov(h) P(0) Wow(bw)" data-reactid="3">
                                                         <li class="js-stream-content Pos(r)" data-reactid="4">
                                                            <div class="Py(14px) smartphone_Px(20px) smartphone_Bxsh(streamBoxShadow) Cf" data-test-locator="featured" data-reactid="5">
                                                               <div class="Pos(r)" data-reactid="6">
                                                                  <div class="Pos(r)" data-reactid="7">
                                                                     <div class="Pos(r) smartphone_Mx(a) smartphone_Mb(12px)" style="max-width:600px;" data-reactid="8">
                                                                        <div class=" Mb(6px) Bdrs(2px) Bgz(cv) Trsdu(0s)!" style="padding-bottom:52%;background-image:url(https://s.yimg.com/bt/api/res/1.2/C7bZScIwyFssTn8ihYYXfg--/YXBwaWQ9eW5ld3M7aD0zMTI7dz02MDA7cT03NTtmaT1maWxsO3B5b2ZmPTMw/https://s.yimg.com/uu/api/res/1.2/k.ABxP5e4BTou_KXm_uaDw--~B/dz01MTMyO2g9MzQ0NzthcHBpZD15dGFjaHlvbg--/http://globalfinance.zenfs.com/images/US_AHTTP_AP_NEWSBRIEFS/68c70288dc714174a67fbc7cf050cf8d_original.jpg);" data-reactid="9"></div>
                                                                     </div>
                                                                     <h3 class="M(0) Py(1px)" data-reactid="10"><a class="Fz(13px) LineClamp(4,96px) C(#0078ff):h Td(n) C($c-fuji-blue-4-b) smartphone_C(#000) smartphone_Fz(19px)" href="/news/trump-voting-commission-criticized-lack-transparency-140503565--politics.html" data-reactid="11"><span class="Ff($ff-primary) Fw(600) Lts($lspacing-sm) Fsm($fsmoothing) Fsmw($fsmoothing) Fsmm($fsmoothing) smartphone_Fw(500)" data-reactid="12">Trump voting commission criticized for lack of transparency</span><u class="StretchedBox Z(1)" data-reactid="13"></u></a></h3>
                                                                     <div class="Lh(1.2) Fz(11px) smartphone_Fz(13px) Pos(r) Z(1) Mt(4px) C(#96989f)" data-reactid="14">
                                                                        <div class="C(#959595)" data-reactid="15">Associated Press</div>
                                                                     </div>
                                                                  </div>
                                                               </div>
                                                            </div>
                                                         </li>
                                                         <li class="js-stream-content Pos(r)" data-reactid="16">
                                                            <div class="controller Feedback Pos(r)" data-beacon="" data-tp-beacon="" data-reactid="17">
                                                               <div class="Py(14px) smartphone_Px(20px) Pos(r) Ov(h) smartphone_Bxsh(streamBoxShadow)" data-reactid="18">
                                                                  <div class="Mx(a)" style="max-width:600px;" data-reactid="19">
                                                                     <div class=" Bdrs(2px) Bgz(cv) smartphone_Mx(0) Mb(6px) smartphone_Mb(12px) Trsdu(0s)!" style="padding-bottom:52%;background-image:url(https://s.yimg.com/bt/api/res/1.2/TwghYGD24QdM.9DkRH89gQ--/YXBwaWQ9eW5ld3M7aD0zMTI7dz02MDA7cT03NTtmaT1maWxsO3B5b2ZmPTMw/https://s.yimg.com/av/moneyball/ads/1504216947696-2579.jpg);" data-reactid="20"></div>
                                                                  </div>
                                                                  <h3 class="M(0) Py(1px)" data-reactid="21"><a rel="nofollow noopener noreferrer" class="C(#0078ff):h Td(n) smartphone_C(#000) Fz(13px) LineClamp(4,96px) C($c-fuji-blue-4-b) smartphone_Fz(19px)" target="_blank" href="https://beap.gemini.yahoo.com/mbclk?bv=1.0.0&amp;es=hR6_gG4GIS9OY3yeXgr0u9yr1tWage6aylbnx4OJqeoKmlZKT8_xIaOqHCHOPGhSuN_72jsmb8LsrUN4IJGkzP6GrsWnK4KZ1.pwAkyn26VYNayNmiKrTsOYZWn6jsBKjOGRGoDcq3imdoOP8lptgZC0JxHr.rNZqwla8mghJHVkF.xG1sXa4uG_70xgBR9Cl8pUe70h_FHgg4w2aY_g7B9xbgRGUmG4bMLK_Oqjc14pCOfoKIAoOnBtuBsMpvUictxokzJ_vu5ZutEtXfmIA3GL9fhQUemj9v47VoJOMRZivlEpL3NUe58WfztT3ZNSIKd6koOYtPK6VqM57UzajtufYv6yeIg4VvJR0bUGwmpwohF7OLSH3vyyyiXwXdraeIeYRjDdbi.tEPTbW4Bs4Kp3vAeDdpKeXjXs9UKLV5VaCAVaSGVvNp0qbEx.DQUqb9HaJWPOG88WttfATX93EweoFsnzl39nR4yt9XWpnLpKls73Gp1ytygjhRUHpFFevYZspbuMSC9djWPEKwWnjC0LFGIJTf24Ptwyn6Bwu38O.ElYKqE5fSX5.3zi1hAZ20F0pIgQUzNMLzpehrpKMuMVvlnFJg--%26lp=http%3A%2F%2Fmaxlol.com%2Fthe-funniest-things-news-anchors-have-done-on-air%2F%3Futm_source%3Dyahoo%26utm_medium%3Dreferral%26utm_campaign%3Dnews-lm-1" data-reactid="22"><span class="Ff($ff-primary) Fw(600) Lts($lspacing-sm) Fsm($fsmoothing) Fsmw($fsmoothing) Fsmm($fsmoothing) smartphone_Fw(500)" data-reactid="23">Troubled News Anchors Does The Unexpected On Air!</span><u class="StretchedBox Z(1)" data-reactid="24"></u></a></h3>
                                                                  <div class="Fz(11px) smartphone_Fz(13px) Pos(r) Z(1) Ell" data-reactid="25">
                                                                     <a class="C(#96989f) Td(n) Whs(nw) Mend(6px) Lh(1.6)" rel="noopener noreferrer" target="_blank" href="https://beap.gemini.yahoo.com/mbclk?bv=1.0.0&amp;es=hR6_gG4GIS9OY3yeXgr0u9yr1tWage6aylbnx4OJqeoKmlZKT8_xIaOqHCHOPGhSuN_72jsmb8LsrUN4IJGkzP6GrsWnK4KZ1.pwAkyn26VYNayNmiKrTsOYZWn6jsBKjOGRGoDcq3imdoOP8lptgZC0JxHr.rNZqwla8mghJHVkF.xG1sXa4uG_70xgBR9Cl8pUe70h_FHgg4w2aY_g7B9xbgRGUmG4bMLK_Oqjc14pCOfoKIAoOnBtuBsMpvUictxokzJ_vu5ZutEtXfmIA3GL9fhQUemj9v47VoJOMRZivlEpL3NUe58WfztT3ZNSIKd6koOYtPK6VqM57UzajtufYv6yeIg4VvJR0bUGwmpwohF7OLSH3vyyyiXwXdraeIeYRjDdbi.tEPTbW4Bs4Kp3vAeDdpKeXjXs9UKLV5VaCAVaSGVvNp0qbEx.DQUqb9HaJWPOG88WttfATX93EweoFsnzl39nR4yt9XWpnLpKls73Gp1ytygjhRUHpFFevYZspbuMSC9djWPEKwWnjC0LFGIJTf24Ptwyn6Bwu38O.ElYKqE5fSX5.3zi1hAZ20F0pIgQUzNMLzpehrpKMuMVvlnFJg--%26lp=http%3A%2F%2Fmaxlol.com%2Fthe-funniest-things-news-anchors-have-done-on-air%2F%3Futm_source%3Dyahoo%26utm_medium%3Dreferral%26utm_campaign%3Dnews-lm-1" data-reactid="26">MaxLOL</a>
                                                                     <span data-reactid="27">
                                                                        <a class="Mend(6px) C($c-fuji-grey-e) Td(n)" href="http://help.yahoo.com/kb/index?page=content&amp;y=PROD_FRONT&amp;locale=en_US&amp;id=SLN14553" rel="noopener noreferrer" target="_blank" data-reactid="28">Sponsored</a>
                                                                        <a href="https://info.yahoo.com/privacy/us/yahoo/relevantads.html" target="_blank" rel="noopener noreferrer" data-reactid="29">
                                                                           <i class="Pos(r) T(3px)" data-reactid="30">
                                                                              <svg class="Cur(p)" width="15" style="vertical-align:baseline;fill:$c-fuji-grey-e;stroke:$c-fuji-grey-e;stroke-width:0;" height="15" viewBox="0 0 24 24" data-icon="sponsor" data-reactid="31">
                                                                                 <path d="M5.636 4.222c-.39-.39-1.023-.39-1.414 0s-.39 1.024 0 1.414l.707.707c.39.39 1.022.39 1.414 0 .39-.39.39-1.023 0-1.414l-.708-.708zM4.93 17.658l-.708.707c-.39.39-.39 1.023 0 1.414.39.39 1.023.39 1.414 0l.707-.708c.39-.39.39-1.024 0-1.414-.39-.39-1.023-.39-1.414 0zm14.14 0c-.39-.39-1.023-.39-1.413 0-.39.39-.39 1.023 0 1.414l.707.707c.39.39 1.024.39 1.414 0 .39-.392.39-1.025 0-1.415l-.707-.707zm0-11.315l.708-.707c.39-.39.39-1.023 0-1.414s-1.024-.39-1.414 0l-.707.707c-.39.39-.39 1.024 0 1.414.39.39 1.023.39 1.414 0zM22 11h-1c-.553 0-1 .448-1 1s.447 1 1 1h1c.552 0 1-.448 1-1s-.448-1-1-1zM10 9h5c.552 0 1-.448 1-1s-.448-1-1-1h-2c0-.55-.447-1-1-1s-1 .45-1 1H9.5C8.12 7 7 8.12 7 9.5v1C7 11.88 8.12 13 9.5 13H13c.552 0 1 .448 1 1s-.448 1-1 1H8c-.553 0-1 .448-1 1s.447 1 1 1h3c0 .55.447 1 1 1s1-.45 1-1h.5c1.38 0 2.5-1.12 2.5-2.5v-1c0-1.38-1.37-2.5-3-2.5h-3c-.553 0-1-.448-1-1s.447-1 1-1zm2-5c.553 0 1-.448 1-1V2c0-.552-.447-1-1-1s-1 .448-1 1v1c0 .552.447 1 1 1zm-9 7H2c-.553 0-1 .448-1 1s.447 1 1 1h1c.552 0 1-.448 1-1s-.448-1-1-1zm9 9c-.553 0-1 .448-1 1v1c0 .552.447 1 1 1s1-.448 1-1v-1c0-.552-.447-1-1-1z" data-reactid="32"></path>
                                                                              </svg>
                                                                           </i>
                                                                        </a>
                                                                     </span>
                                                                  </div>
                                                               </div>
                                                               <!-- react-text: 33 --><!-- /react-text -->
                                                            </div>
                                                         </li>
                                                         <li class="js-stream-content Pos(r)" data-reactid="34">
                                                            <div class="Py(14px) smartphone_Px(20px) smartphone_Bxsh(streamBoxShadow) Cf" data-test-locator="featured" data-reactid="35">
                                                               <div class="Pos(r)" data-reactid="36">
                                                                  <div class="Pos(r)" data-reactid="37">
                                                                     <div class="Pos(r) smartphone_Mx(a) smartphone_Mb(12px)" style="max-width:600px;" data-reactid="38">
                                                                        <div class=" Mb(6px) Bdrs(2px) Bgz(cv) Trsdu(0s)!" style="padding-bottom:52%;background-image:url(https://s.yimg.com/bt/api/res/1.2/quSlgBMGV1OdLxAAiIF8eQ--/YXBwaWQ9eW5ld3M7aD0zMTI7dz02MDA7cT03NTtmaT1maWxsO3B5b2ZmPTMw/https://s.yimg.com/uu/api/res/1.2/T0wmua4rmm3kqzEdhfSOMA--~B/dz01ODA7aD00MDE7YXBwaWQ9eXRhY2h5b24-/http://media.zenfs.com/en-US/homerun/motleyfool.com/dac4d42b72622e518024fabbc45b90f4);" data-reactid="39"></div>
                                                                     </div>
                                                                     <h3 class="M(0) Py(1px)" data-reactid="40"><a class="Fz(13px) LineClamp(4,96px) C(#0078ff):h Td(n) C($c-fuji-blue-4-b) smartphone_C(#000) smartphone_Fz(19px)" href="/news/apos-much-average-50-something-110000289.html" data-reactid="41"><span class="Ff($ff-primary) Fw(600) Lts($lspacing-sm) Fsm($fsmoothing) Fsmw($fsmoothing) Fsmm($fsmoothing) smartphone_Fw(500)" data-reactid="42">Here&#x27;s How Much the Average 50-Something American Has Saved for Retirement</span><u class="StretchedBox Z(1)" data-reactid="43"></u></a></h3>
                                                                     <div class="Lh(1.2) Fz(11px) smartphone_Fz(13px) Pos(r) Z(1) Mt(4px) C(#96989f)" data-reactid="44">
                                                                        <div class="C(#959595)" data-reactid="45">Motley Fool</div>
                                                                     </div>
                                                                  </div>
                                                               </div>
                                                            </div>
                                                         </li>
                                                      </ul>
                                                   </div>
                                                </div>
                                             </div>
                                             <script>if (window.performance) {window.performance.mark && window.performance.mark('Col2-1-Stream');window.performance.measure && window.performance.measure('Col2-1-StreamDone','PageStart','Col2-1-Stream');}</script>
                                          </div>
                                          <div data-reactid="44">
                                             <div id="mrt-node-Col2-2-AdUnitWithTdAds" data-locator="subtree-root">
                                                <div id="Col2-2-AdUnitWithTdAds-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="-905740195">
                                                   <div class="ad-lrec2" data-reactid="2">
                                                      <div data-reactid="3">
                                                         <div data-reactid="4">
                                                            <div id="defaultLREC2-sizer" class="darla-container" data-reactid="5">
                                                               <div id="defaultLREC2-wrapper" class="" data-reactid="6">
                                                                  <div id="defaultdestLREC2" style="width:300px;height:250px;"></div>
                                                               </div>
                                                            </div>
                                                         </div>
                                                      </div>
                                                   </div>
                                                </div>
                                             </div>
                                             <script>if (window.performance) {window.performance.mark && window.performance.mark('Col2-2-AdUnitWithTdAds');window.performance.measure && window.performance.measure('Col2-2-AdUnitWithTdAdsDone','PageStart','Col2-2-AdUnitWithTdAds');}</script>
                                          </div>
                                          <div data-reactid="45">
                                             <div id="mrt-node-Col2-3-LinkOut" data-locator="subtree-root">
                                                <div id="Col2-3-LinkOut-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="-7779303"><a class="Mt(20px) Ta(c) btn btn-white W(100%)" href="https://smallbusiness.yahoo.com" data-reactid="2"><span data-reactid="3">Yahoo Small Business</span></a></div>
                                             </div>
                                             <script>if (window.performance) {window.performance.mark && window.performance.mark('Col2-3-LinkOut');window.performance.measure && window.performance.measure('Col2-3-LinkOutDone','PageStart','Col2-3-LinkOut');}</script>
                                          </div>
                                          <div data-reactid="46">
                                             <div id="mrt-node-Col2-4-Footer" data-locator="subtree-root">
                                                <div id="Col2-4-Footer-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="-1198394440">
                                                   <div id="Col2-4-Footer" class="footer Bgc(#fff) Pb(15px) Ta(c) Pt(25px) H(130px)" data-test="finance-footer" data-reactid="2">
                                                      <div class="D(b) Ta(c) Pos(a) B(15px) W(100%)" data-reactid="3"><img src="https://s.yimg.com/os/finance/dd-site/img/Oath_YFin_Logo_EN.svg" alt="Oath: Yahoo Finance" class="W(90px)" data-reactid="4"/></div>
                                                      <div class="Fz(s) D(ib) Pt(5px) " data-reactid="5">
                                                         <div class="Pb(5px) D(b)" data-reactid="6"><a class="Mend(10px) C($grey6) C($c-fuji-blue-1-b):h" href="https://help.yahoo.com/kb/index?page=content&amp;y=PROD_FIN_DESK&amp;locale=en_US&amp;id=SLN2310" rel="nofollow" data-reactid="7"><span data-reactid="8">Data Disclaimer</span></a><a class="Mend(10px) C($grey6) C($c-fuji-blue-1-b):h" href="https://help.yahoo.com/kb/index?page=content&amp;y=PROD_FIN_DESK&amp;locale=en_US" rel="nofollow" data-reactid="9"><span data-reactid="10">Help</span></a><a class="Mend(10px) C($grey6) C($c-fuji-blue-1-b):h" href="https://yahoo.uservoice.com/forums/439018-finance-stock-screener" rel="nofollow" data-reactid="11"><span data-reactid="12">Suggestions</span></a></div>
                                                         <div class="Pb(5px) D(b)" data-reactid="13"><a class="Mend(10px) C($grey6) C($c-fuji-blue-1-b):h" href="http://info.yahoo.com/privacy/us/yahoo/" rel="nofollow" data-reactid="14"><span data-reactid="15">Privacy</span></a><a class="Mend(10px) C($grey6) C($c-fuji-blue-1-b):h" href="http://info.yahoo.com/relevantads/" rel="nofollow" data-reactid="16"><span data-reactid="17">About Our Ads</span></a><a class="Mend(10px) C($grey6) C($c-fuji-blue-1-b):h" href="http://info.yahoo.com/legal/us/yahoo/utos/utos-173.html" rel="nofollow" data-reactid="18"><span data-reactid="19">Terms (Updated)</span></a></div>
                                                      </div>
                                                      <div class="D(b)" data-reactid="20">
                                                         <ul class="follow-button-group M(0) Va(m) D(ib) Ta(c)" data-reactid="21">
                                                            <li class="D(ib) M(0) Cur(p) twitter" style="width:25px;height:25px;line-height:25px;" title="Follow on Twitter" data-reactid="22">
                                                               <a class="Td(n) C(#000)" href="https://twitter.com/YahooFinance" target="_blank" data-reactid="23">
                                                                  <svg class="Va(m)! Cur(p)" width="13" style="fill:#767d84;stroke:#767d84;stroke-width:0;vertical-align:bottom;" height="13" viewBox="0 0 32 32" data-icon="LogoTwitter" data-reactid="24">
                                                                     <path d="M30.402 7.094c-1.058.47-2.198.782-3.392.928 1.218-.725 2.154-1.885 2.595-3.256-1.134.674-2.405 1.165-3.75 1.43-1.077-1.148-2.612-1.862-4.31-1.862-3.268 0-5.915 2.635-5.915 5.893 0 .464.056.91.155 1.34-4.915-.244-9.266-2.59-12.18-6.158-.51.87-.806 1.885-.806 2.96 0 2.044 1.045 3.847 2.633 4.905-.974-.032-1.883-.3-2.68-.736v.07c0 2.857 2.034 5.236 4.742 5.773-.498.138-1.022.21-1.56.21-.38 0-.75-.034-1.11-.103.75 2.344 2.93 4.042 5.518 4.09-2.024 1.58-4.57 2.523-7.333 2.523-.478 0-.952-.032-1.41-.085 2.613 1.674 5.72 2.65 9.054 2.65 10.872 0 16.814-8.976 16.814-16.765 0-.254-.008-.507-.018-.762 1.155-.83 2.155-1.868 2.95-3.047z" data-reactid="25"></path>
                                                                  </svg>
                                                               </a>
                                                            </li>
                                                            <li class="D(ib) M(0) Cur(p) facebook" style="width:25px;height:25px;line-height:25px;" title="Follow on Facebook" data-reactid="26">
                                                               <a class="Td(n) C(#000)" href="https://facebook.com/yahoofinance" target="_blank" data-reactid="27">
                                                                  <svg class="Va(m)! Cur(p)" width="13" style="fill:#767d84;stroke:#767d84;stroke-width:0;vertical-align:bottom;" height="13" viewBox="0 0 32 32" data-icon="LogoFacebook" data-reactid="28">
                                                                     <path d="M12.752 30.4V16.888H9.365V12.02h3.387V7.865c0-3.264 2.002-6.264 6.613-6.264 1.866 0 3.248.19 3.248.19l-.11 4.54s-1.404-.013-2.943-.013c-1.66 0-1.93.81-1.93 2.152v3.553h5.008l-.22 4.867h-4.786V30.4h-4.88z" data-reactid="29"></path>
                                                                  </svg>
                                                               </a>
                                                            </li>
                                                            <li class="D(ib) M(0) Cur(p) tumblr" style="width:25px;height:25px;line-height:25px;" title="Follow on Tumblr" data-reactid="30">
                                                               <a class="Td(n) C(#000)" href="http://yahoofinance.tumblr.com" target="_blank" data-reactid="31">
                                                                  <svg class="Va(m)! Cur(p)" width="13" style="fill:#767d84;stroke:#767d84;stroke-width:0;vertical-align:bottom;" height="13" viewBox="0 0 24 24" data-icon="LogoTumblr" data-reactid="32">
                                                                     <path d="M15.4 19.1c-1.1 0-2.5-.7-2.5-1.1v-7.8h4.9V6.8h-4.9V1.7H10C9.9 3 9.5 4.1 8.9 5c-.2.5-.5.8-.9 1.1-.6.4-1.2.7-1.9.7h-.5v3.4H8v8.4c0 3.2 2.9 3.7 4.8 3.7h1.3c3 0 3.6-.3 4.3-.6V18c-.9.6-2 1.1-3 1.1z" data-reactid="33"></path>
                                                                  </svg>
                                                               </a>
                                                            </li>
                                                         </ul>
                                                      </div>
                                                   </div>
                                                </div>
                                             </div>
                                             <script>if (window.performance) {window.performance.mark && window.performance.mark('Col2-4-Footer');window.performance.measure && window.performance.measure('Col2-4-FooterDone','PageStart','Col2-4-Footer');}</script>
                                          </div>
                                       </div>
                                    </div>
                                 </div>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div id="YDC-Overlay" class="YDC-Overlay" data-reactid="47">
                        <div id="YDC-Overlay-Stack" class="YDC-Overlay-Stack Z(11) End(0) Pos(f) Start(0) lw-nav-open_Pos(r) lw-nav-open_Z(10) T(0)" data-reactid="48">
                           <div data-reactid="49">
                              <div data-reactid="50">
                                 <div id="mrt-node-Overlay-0-Lightbox" data-locator="subtree-root">
                                    <div id="Overlay-0-Lightbox-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="-1142446977">
                                       <div id="Overlay-0-Lightbox" class="lightbox" data-reactid="2">
                                          <div tabindex="-1" class="lightbox-wrapper Ta(c) Pos(f) T(0) Start(0) H(100%) W(100%)  D(n)! Op(0)" data-reactid="3">
                                             <div id="myLightboxContainer" class="Ta(start) Pos(r) Z(1) T(0) Maw(100%) P(0)  D(n)!" aria-describedby="lightbox-container" role="alertdialog" data-reactid="4"></div>
                                             <b class="ModalShim" data-reactid="5"></b><b class="IEShim" data-reactid="6"></b>
                                          </div>
                                       </div>
                                    </div>
                                 </div>
                                 <script>if (window.performance) {window.performance.mark && window.performance.mark('Overlay-0-Lightbox');window.performance.measure && window.performance.measure('Overlay-0-LightboxDone','PageStart','Overlay-0-Lightbox');}</script>
                              </div>
                              <div data-reactid="51">
                                 <div id="mrt-node-Overlay-1-Null" data-locator="subtree-root">
                                    <div id="Overlay-1-Null-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="-1353506498">
                                       <div data-reactid="2"></div>
                                    </div>
                                 </div>
                                 <script>if (window.performance) {window.performance.mark && window.performance.mark('Overlay-1-Null');window.performance.measure && window.performance.measure('Overlay-1-NullDone','PageStart','Overlay-1-Null');}</script>
                              </div>
                              <div data-reactid="52">
                                 <div id="mrt-node-Overlay-2-Null" data-locator="subtree-root">
                                    <div id="Overlay-2-Null-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="-1348067009">
                                       <div data-reactid="2"></div>
                                    </div>
                                 </div>
                                 <script>if (window.performance) {window.performance.mark && window.performance.mark('Overlay-2-Null');window.performance.measure && window.performance.measure('Overlay-2-NullDone','PageStart','Overlay-2-Null');}</script>
                              </div>
                              <div data-reactid="53">
                                 <div id="mrt-node-Overlay-3-Notification" data-locator="subtree-root">
                                    <div id="Overlay-3-Notification-Proxy" data-reactroot="" data-reactid="1" data-react-checksum="-1918619327">
                                       <div class="" data-reactid="2"><span data-reactid="3"></span></div>
                                    </div>
                                 </div>
                                 <script>if (window.performance) {window.performance.mark && window.performance.mark('Overlay-3-Notification');window.performance.measure && window.performance.measure('Overlay-3-NotificationDone','PageStart','Overlay-3-Notification');}</script>
                              </div>
                           </div>
                        </div>
                     </div>
                  </div>
               </div>
               <div class="render-target-modal D(n) modal-open_D(b) modal-postopen_D(b) H(100%) Pos(a) W(100%) Z(9) O(n)!:f" id="render-target-modal" data-reactid="54"><span data-reactid="55"></span></div>
               <div class="render-target-viewer D(n) viewer-open_D(b) viewer-postopen_D(b) H(100%) Pos(a) W(100%) Z(10)" id="render-target-viewer" data-reactid="56"><span data-reactid="57"></span></div>
            </div>
         </div>
      </div>
      <div>
         <script type="text/javascript">window._loadEvt = false;
            window._adPerfData = [];
            window._adPosMsg = [];
            window._perfMark = function _perfMark (name) {if (window.performance && window.performance.mark){try {if (window.performance.getEntriesByName("NAVIGATE_START") && window.performance.getEntriesByName("NAVIGATE_START")[0]) { name = "CL_" + name ;}window.performance.mark(name);} catch (e) {console.warn(name + ' could not be marked:',e);}};};
            window._perfMeasure = function _perfMeasure (name, start, end) {if (window.performance && window.performance.measure){try {if (window.performance.getEntriesByName("NAVIGATE_START") && window.performance.getEntriesByName("NAVIGATE_START")[0]) { start = "CL_" + start ;end = "CL_" + end ;name = "CL_" + name ;}window.performance.measure(name, start, end);} catch (e) {console.warn(name + ' could not be added:',e);}};};
            window._pushAdPerfMetric = function _pushAdPerfMetric(key) {if (window.performance && window.performance.now) {_adPerfData.push([key, Math.round(window.performance.now())]);}};
            window._fireAdPerfBeacon = function _fireAdPerfBeacon(eventName) {try {if (window && window.rapidInstance && window.performance) {var navClickMark = window.performance.getEntriesByName('NAVIGATE_START') &&window.performance.getEntriesByName('NAVIGATE_START').pop();var navClickTime = navClickMark && navClickMark.startTime \n\t 0;var userTime = {};window.performance.getEntries().forEach(function forEachPerfTime (item) {if (item.name.search('DARLA_') > -1) {if (item.entryType === "mark") {userTime[item.name] = Math.round(item.startTime) - navClickTime;window.performance.clearMarks(item.name);} else if (item.entryType === "measure") {userTime[item.name] = Math.round(item.duration);window.performance.clearMeasures(item.name);}}});var perfData = {perf_usertime: {utm: userTime}};
            window.rapidInstance.beaconPerformanceData(perfData);}} catch (e) {console.warn('Could not send the beacon:',e);}};
            window.DARLA_CONFIG = {"debug":false,"dm":1,"autoRotation":10000,"rotationTimingDisabled":true,"k2":{"res":{"rate":5,"pos":["BTN","BTN-1","BTN-2","BTN-3","BTN1","LREC","LREC2","LREC3","LDRB","MAST"]}},"positions":{"DEFAULT":{"name":"DEFAULT","enable":true,"fallback":null,"metaSize":false,"staticLayout":false,"clean":"defaultcleanDEFAULT","dest":"defaultdestDEFAULT","id":"DEFAULT"},"BTN1":{"id":"BTN1","clean":"defaultcleanBTN1","dest":"defaultdestBTN1","metaSize":true,"w":120,"h":60,"enable":true,"fallback":null,"staticLayout":false},"BTN1-1":{"id":"BTN1","clean":"defaultcleanBTN1-1","dest":"defaultdestBTN1-1","metaSize":true,"w":120,"h":60,"enable":true,"fallback":null,"staticLayout":false},"BTN":{"id":"BTN","clean":"defaultcleanBTN","dest":"defaultdestBTN","metaSize":true,"w":120,"h":60,"enable":true,"fallback":null,"staticLayout":false},"BTN-1":{"id":"BTN-1","clean":"defaultcleanBTN-1","dest":"defaultdestBTN-1","w":120,"h":60,"enable":true,"fallback":null,"metaSize":false,"staticLayout":false},"BTN-2":{"id":"BTN-2","clean":"defaultcleanBTN-2","dest":"defaultdestBTN-2","metaSize":true,"w":120,"h":60,"enable":true,"fallback":null,"staticLayout":false},"BTN-3":{"id":"BTN-3","clean":"defaultcleanBTN-3","dest":"defaultdestBTN-3","metaSize":true,"w":120,"h":60,"enable":true,"fallback":null,"staticLayout":false},"BTN-5":{"id":"BTN-5","clean":"defaultcleanBTN-5","dest":"defaultdestBTN-5","metaSize":true,"w":120,"h":60,"enable":true,"fallback":null,"staticLayout":false},"BTN-6":{"id":"BTN-6","clean":"defaultcleanBTN-6","dest":"defaultdestBTN-6","metaSize":true,"w":120,"h":60,"enable":true,"fallback":null,"staticLayout":false},"BTN-7":{"id":"BTN-7","clean":"defaultcleanBTN-7","dest":"defaultdestBTN-7","metaSize":true,"w":120,"h":60,"enable":true,"fallback":null,"staticLayout":false},"BTN-8":{"id":"BTN-8","clean":"defaultcleanBTN-8","dest":"defaultdestBTN-8","metaSize":true,"w":120,"h":60,"enable":true,"fallback":null,"staticLayout":false},"FOOT":{"id":"FOOT","clean":"defaultcleanFOOT","dest":"defaultdestFOOT","fr":"expIfr_exp","failed":true,"enable":true,"fallback":null,"metaSize":false,"staticLayout":false},"FSRVY":{"id":"FSRVY","clean":"defaultcleanFSRVY","dest":"defaultdestFSRVY","fr":"expIfr_exp","failed":true,"enable":true,"fallback":null,"metaSize":false,"staticLayout":false},"SCREC":{"id":"SCREC","clean":"defaultcleanSCREC","dest":"defaultdestSCREC","w":300,"h":65,"enable":true,"fallback":null,"metaSize":false,"staticLayout":false},"LREC":{"id":"LREC","clean":"defaultcleanLREC","dest":"defaultdestLREC","w":300,"h":250,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"staticLayout":true,"fdb":true,"failed":true,"enable":true,"fallback":null,"metaSize":false},"LREC-9":{"id":"LREC-9","w":300,"h":250,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"staticLayout":true,"fdb":true,"clean":"defaultcleanLREC-9","dest":"defaultdestLREC-9","enable":true,"fallback":null,"metaSize":false},"LREC2":{"id":"LREC2","clean":"defaultcleanLREC2","dest":"defaultdestLREC2","w":300,"h":250,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"staticLayout":true,"fdb":true,"enable":true,"fallback":null,"metaSize":false},"LREC2-4":{"id":"LREC2-4","w":300,"h":250,"autoFetch":false,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"enable":true,"staticLayout":true,"fdb":true,"z":9,"clean":"defaultcleanLREC2-4","dest":"defaultdestLREC2-4","fallback":null,"metaSize":false},"LREC2-5":{"id":"LREC2-5","w":300,"h":250,"autoFetch":false,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"enable":true,"staticLayout":true,"fdb":true,"z":9,"clean":"defaultcleanLREC2-5","dest":"defaultdestLREC2-5","fallback":null,"metaSize":false},"LREC2-6":{"id":"LREC2-6","w":300,"h":250,"autoFetch":false,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"enable":true,"staticLayout":true,"fdb":true,"z":9,"clean":"defaultcleanLREC2-6","dest":"defaultdestLREC2-6","fallback":null,"metaSize":false},"LREC2-7":{"id":"LREC2-7","w":300,"h":250,"autoFetch":false,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"enable":true,"staticLayout":true,"fdb":true,"z":9,"clean":"defaultcleanLREC2-7","dest":"defaultdestLREC2-7","fallback":null,"metaSize":false},"LREC2-8":{"id":"LREC2-8","w":300,"h":250,"autoFetch":false,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"enable":true,"staticLayout":true,"fdb":true,"z":9,"clean":"defaultcleanLREC2-8","dest":"defaultdestLREC2-8","fallback":null,"metaSize":false},"LREC2-9":{"id":"LREC2-9","w":300,"h":250,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"staticLayout":true,"fdb":true,"clean":"defaultcleanLREC2-9","dest":"defaultdestLREC2-9","enable":true,"fallback":null,"metaSize":false},"LREC3":{"id":"LREC3","clean":"defaultcleanLREC3","dest":"defaultdestLREC3","w":300,"h":250,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"staticLayout":true,"fdb":true,"enable":true,"fallback":null,"metaSize":false},"LREC3-4":{"id":"LREC3-4","w":300,"h":250,"autoFetch":false,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"enable":true,"staticLayout":true,"fdb":true,"z":9,"clean":"defaultcleanLREC3-4","dest":"defaultdestLREC3-4","fallback":null,"metaSize":false},"LREC3-5":{"id":"LREC3-5","w":300,"h":250,"autoFetch":false,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"enable":true,"staticLayout":true,"fdb":true,"z":9,"clean":"defaultcleanLREC3-5","dest":"defaultdestLREC3-5","fallback":null,"metaSize":false},"LREC3-6":{"id":"LREC3-6","w":300,"h":250,"autoFetch":false,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"enable":true,"staticLayout":true,"fdb":true,"z":9,"clean":"defaultcleanLREC3-6","dest":"defaultdestLREC3-6","fallback":null,"metaSize":false},"LREC3-7":{"id":"LREC3-7","w":300,"h":250,"autoFetch":false,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"enable":true,"staticLayout":true,"fdb":true,"z":9,"clean":"defaultcleanLREC3-7","dest":"defaultdestLREC3-7","fallback":null,"metaSize":false},"LREC3-8":{"id":"LREC3-8","w":300,"h":250,"autoFetch":false,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"enable":true,"staticLayout":true,"fdb":true,"z":9,"clean":"defaultcleanLREC3-8","dest":"defaultdestLREC3-8","fallback":null,"metaSize":false},"LREC3-9":{"id":"LREC3-9","w":300,"h":250,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"staticLayout":true,"fdb":true,"clean":"defaultcleanLREC3-9","dest":"defaultdestLREC3-9","enable":true,"fallback":null,"metaSize":false},"LREC4":{"id":"LREC4","clean":"defaultcleanLREC4","dest":"defaultdestLREC4","w":300,"h":250,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"staticLayout":true,"fdb":true,"enable":true,"fallback":null,"metaSize":false},"LDRB":{"id":"LDRB","clean":"defaultcleanLDRB","dest":"defaultdestLDRB","w":728,"h":90,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"staticLayout":true,"fdb":true,"enable":true,"fallback":null,"metaSize":false},"LDRB-9":{"id":"LDRB-9","w":728,"h":90,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"staticLayout":true,"fdb":true,"clean":"defaultcleanLDRB-9","dest":"defaultdestLDRB-9","enable":true,"fallback":null,"metaSize":false},"LDRB2":{"id":"LDRB2","clean":"defaultcleanLDRB2","dest":"defaultdestLDRB2","w":728,"h":90,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"staticLayout":true,"fdb":true,"enable":true,"fallback":null,"metaSize":false},"LDRB2-1":{"id":"LDRB2-1","w":728,"h":90,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"staticLayout":true,"fdb":true,"clean":"defaultcleanLDRB2-1","dest":"defaultdestLDRB2-1","enable":true,"fallback":null,"metaSize":false},"LDRB2-2":{"id":"LDRB2-2","w":728,"h":90,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"staticLayout":true,"fdb":true,"clean":"defaultcleanLDRB2-2","dest":"defaultdestLDRB2-2","enable":true,"fallback":null,"metaSize":false},"LDRB2-3":{"id":"LDRB2-3","w":728,"h":90,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"staticLayout":true,"fdb":true,"clean":"defaultcleanLDRB2-3","dest":"defaultdestLDRB2-3","enable":true,"fallback":null,"metaSize":false},"LDRB2-4":{"id":"LDRB2-4","w":728,"h":90,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1},"staticLayout":true,"fdb":true,"clean":"defaultcleanLDRB2-4","dest":"defaultdestLDRB2-4","enable":true,"fallback":null,"metaSize":false},"MAST":{"id":"MAST","clean":"defaultcleanMAST","dest":"defaultdestMAST","w":970,"h":250,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1,"resize-to":1},"fdb":{"on":"1","where":"inside"},"closeBtn":{"mode":2,"useShow":1,"adc":0},"metaSize":true,"fclose":2,"enable":true,"fallback":null,"staticLayout":false},"MAST-9":{"id":"MAST-9","w":970,"h":250,"fr":"expIfr_exp","supports":{"exp-ovr":1,"exp-push":1,"resize-to":1},"fdb":{"on":"1","where":"inside"},"closeBtn":{"mode":2,"useShow":1,"adc":0},"metaSize":true,"fclose":2,"clean":"defaultcleanMAST-9","dest":"defaultdestMAST-9","enable":true,"fallback":null,"staticLayout":false},"MON":{"id":"MON","w":300,"h":600,"fr":"expIfr_exp","autoFetch":false,"supports":{"exp-ovr":1,"exp-push":1},"enable":true,"staticLayout":true,"fdb":true,"clean":"defaultcleanMON","dest":"defaultdestMON","fallback":null,"metaSize":false},"MON-1":{"id":"MON-1","w":300,"h":600,"fr":"expIfr_exp","autoFetch":false,"supports":{"exp-ovr":1,"exp-push":1},"enable":true,"staticLayout":true,"fdb":true,"clean":"defaultcleanMON-1","dest":"defaultdestMON-1","fallback":null,"metaSize":false},"FB2":{"id":"FB2","clean":"defaultcleanFB2","dest":"defaultdestFB2","metaSize":true,"w":120,"h":60,"enable":true,"fallback":null,"staticLayout":false},"FB2-1":{"id":"FB2-1","clean":"defaultcleanFB2-1","dest":"defaultdestFB2-1","metaSize":true,"w":120,"h":60,"enable":true,"fallback":null,"staticLayout":false},"FB2-2":{"id":"FB2-2","clean":"defaultcleanFB2-2","dest":"defaultdestFB2-2","metaSize":true,"w":120,"h":60,"enable":true,"fallback":null,"staticLayout":false},"FB2-3":{"id":"FB2-3","clean":"defaultcleanFB2-3","dest":"defaultdestFB2-3","metaSize":true,"w":120,"h":60,"enable":true,"fallback":null,"staticLayout":false},"NE4":{"id":"NE4","clean":"defaultcleanNE4","dest":"defaultdestNE4","metaSize":true,"w":120,"h":60,"enable":true,"fallback":null,"staticLayout":false},"NE4-1":{"id":"NE4-1","clean":"defaultcleanNE4-1","dest":"defaultdestNE4-1","metaSize":true,"w":120,"h":60,"enable":true,"fallback":null,"staticLayout":false},"NE4-2":{"id":"NE4-2","clean":"defaultcleanNE4-2","dest":"defaultdestNE4-2","metaSize":true,"w":120,"h":60,"enable":true,"fallback":null,"staticLayout":false},"NE4-3":{"id":"NE4-3","clean":"defaultcleanNE4-3","dest":"defaultdestNE4-3","metaSize":true,"w":120,"h":60,"enable":true,"fallback":null,"staticLayout":false},"SPL":{"id":"SPL","flex":"both","enable":true,"autoFetch":false,"staticLayout":false,"fdb":false,"supports":{"cmsg":1},"uhslot":".YDC-UH","meta":{"type":"stream"},"css":".Mags-FontA{font-family:\"HelveticaNeue\",Helvetica,Arial,sans-serif;font-weight:300;}.Mags-FontA.Size1{font-size:13px;}.Mags-FontA.Size2{font-size:16px;}.Mags-FontA.Size3{font-size:20px;}.Mags-FontA.Size4{font-size:22px;}.Mags-FontA.Size5{font-size:33px;}.Mags-FontA.Size6{font-size:35px;}.Mags-FontA.Size7{font-size:58px;}.Mags-FontA.Size8{font-size:70px;}.Mags-FontA.Size9{font-size:100px;}.Mags-FontB{font-family:Georgia,Times,serif;font-weight:400;}.Mags-FontB.Size1{font-size:18px;}.Mags-FontC{font-family:\"HelveticaNeue\",Helvetica,Arial,sans-serif;font-weight:400;}.Mags-FontC.Size1{font-size:11px;}.Mags-FontC.Size2{font-size:14px;}.Mags-FontC.Size3{font-size:16px;}.Mags-FontC.Size4{font-size:20px;}.Mags-FontC.Size5{font-size:30px;}.Mags-FontC.Size6{font-size:32px;}.Mags-FontC.Size7{font-size:52px;}","clean":"defaultcleanSPL","dest":"defaultdestSPL","fallback":null,"metaSize":false}},"events":{"DEFAULT":{"sp":1183335883,"ssl":1,"secure":1,"ult":{"pg":{"property":"finance_en-US","test":["fin-strm-test2","fndmtest","finssl"]}}},"adFetch":{"ps":"FB2,FB2-1,FB2-2,FB2-3,LDRB,LDRB2,LREC,LREC2,FOOT,FSRVY","sp":1183335883,"sa":" Y-BUCKET=fin-strm-test2,fndmtest,finssl","optionalps":"","site":"finance","ssl":1,"secure":1,"ult":{"pg":{"property":"finance_en-US","test":["fin-strm-test2","fndmtest","finssl"]}}},"AUTO":{"ddd":0,"name":"AUTO","autoStart":1,"autoMax":25,"autoIV":1,"autoRT":10000,"autoDDG":1,"npv":1,"ps":{"BTN":{},"BTN-1":{},"BTN-2":{},"BTN-3":{},"BTN-5":{},"BTN-6":{},"BTN-7":{},"BTN-8":{},"BTN1":{},"FB2":{},"FB2-1":{},"FB2-2":{},"FB2-3":{},"LDRB":{},"LDRB-9":{},"LDRB2":{},"LDRB2-1":{},"LDRB2-2":{},"LDRB2-9":{},"LREC":{},"LREC-9":{},"LREC2":{},"LREC2-4":{},"LREC2-5":{},"LREC2-6":{},"LREC2-7":{},"LREC2-8":{},"LREC2-9":{},"LREC3":{},"LREC3-4":{},"LREC3-5":{},"LREC3-6":{},"LREC3-7":{},"LREC3-8":{},"LREC3-9":{},"MAST":{"autoRT":30000},"MAST-9":{"autoRT":30000},"MON":{},"MON-1":{},"NE4":{},"NE4-1":{},"NE4-2":{},"NE4-3":{},"SCREC":{},"SPL":{"autoRT":30000}},"sa":" Y-BUCKET=fin-strm-test2,fndmtest,finssl","ssl":1,"secure":1,"ult":{"pg":{"property":"finance_en-US","test":["fin-strm-test2","fndmtest","finssl"]}}},"TD_AUTO":{"ps":"DEFAULT,BTN1,BTN1-1,BTN,BTN-1,BTN-2,BTN-3,BTN-5,BTN-6,BTN-7,BTN-8,FOOT,FSRVY,SCREC,LREC,LREC-9,LREC2,LREC2-4,LREC2-5,LREC2-6,LREC2-7,LREC2-8,LREC2-9,LREC3,LREC3-4,LREC3-5,LREC3-6,LREC3-7,LREC3-8,LREC3-9,LREC4,LDRB,LDRB-9,LDRB2,LDRB2-1,LDRB2-2,LDRB2-3,LDRB2-4,MAST,MAST-9,MON,MON-1,FB2,FB2-1,FB2-2,FB2-3,NE4,NE4-1,NE4-2,NE4-3,SPL","ssl":1,"secure":1,"ult":{"pg":{"property":"finance_en-US","test":["fin-strm-test2","fndmtest","finssl"]}}}},"useYAC":0,"usePE":1,"servicePath":"","xservicePath":"","beaconPath":"","renderPath":"","allowFiF":false,"srenderPath":"https://s.yimg.com/rq/darla/3-0-8/html/r-sf.html","renderFile":"https://s.yimg.com/rq/darla/3-0-8/html/r-sf.html","sfbrenderPath":"https://s.yimg.com/rq/darla/3-0-8/html/r-sf.html","msgPath":"https://fc.yahoo.com/sdarla/3-0-8/html/msg.html","cscPath":"https://s.yimg.com/rq/darla/3-0-8/html/r-csc.html","root":"sdarla","edgeRoot":"https://s.yimg.com/rq/darla/3-0-8","sedgeRoot":"https://s.yimg.com/rq/darla/3-0-8","version":"3-0-8","tpbURI":"","hostFile":"https://s.yimg.com/rq/darla/3-0-8/js/g-r-min.js","beaconsDisabled":true,"fdb_locale":"What don't you like about this ad?\n\tIt's offensive\n\tSomething else\n\tThank you for helping us improve your Yahoo experience\n\tIt's not relevant\n\tIt's distracting\n\tI don't like this ad\n\tSend\n\tDone\n\tWhy do I see ads?\n\tLearn more about your feedback.","property":"","lang":"en-US","auto_render":true}
            window.DARLA_CONFIG.servicePath = window.location.protocol + "//fc.yahoo.com/sdarla/php/fc.php";window.DARLA_CONFIG.dm = 1;window.DARLA_CONFIG.onStartRequest = function() {window._perfMark('DARLA_REQSTART');};
            window.DARLA_CONFIG.onFinishRequest = function() {window._perfMark('DARLA_REQEND');};
            window.DARLA_CONFIG.onStartParse = function() {window._perfMark('DARLA_PSTART');};
            window.DARLA_CONFIG.onSuccess = function(eventName) {if (eventName === 'AUTO') {return;}if (window._DarlaEvents) {window._DarlaEvents.emit("success", {eventName: eventName});}window._perfMark('DARLA_DONE_' + eventName);window._darlaSuccessEvt = eventName;if (window._loadEvt) {window._fireAdPerfBeacon(eventName);}};
            window.DARLA_CONFIG.onStartPosRender = function(posItem) {var posId = posItem && posItem.pos;window._perfMark('DARLA_ADSTART_' + posId);if (window._pushAdPerfMetric) {window._pushAdPerfMetric("DARLA_ADSTART_" + posId);}};
            window.DARLA_CONFIG.onFinishPosRender = function(posId, reqList, posItem) {var ltime;window._perfMark('DARLA_ADEND_' + posId);window._perfMeasure('DARLA_RENDERTIME_' + posId, 'DARLA_ADSTART_'+posId, 'DARLA_ADEND_'+posId);if(window._DarlaEvents) {window._DarlaEvents.emit("finishrender", {pos:posId, list:reqList, item:posItem});}var aboveFoldPositions = ["MAST","LDRB","SPRZ","SPL","LREC","BTN","BTN-1","BTN-2","BTN-3","BTN1","FB2","FB2-1","FB2-2","FB2-3","NE4","NE4-1","NE4-2","NE4-3"];if (window._pushAdPerfMetric) {if (window.performance && window.performance.now) {ltime = window.performance.now();}window._pushAdPerfMetric("ADEND_"+posId);var adModDiv = posItem.conf.dest.replace("dest", "") + "-sizer";setTimeout(function () {if (window.performance && window.YAFT !== undefined &&window.YAFT.isInitialized() && -1 !== aboveFoldPositions.indexOf(posId)) {window.YAFT.triggerCustomTiming(adModDiv, "", ltime);}}, 300);}};
            window.DARLA_CONFIG.onBeforePosMsg = function(msg, posId) {var maxWidth = 970, maxHeight = 600;var newWidth, newHeight, pos;if ("MAST" !== posId) {return;}if (msg === "resize-to") {newWidth = arguments[2];newHeight = arguments[3];} else if (msg === "exp-push" \n\t msg === "exp-ovr") {pos = $sf.host.get("MAST");newWidth = pos.conf.w + arguments[6] + arguments[7];newHeight = pos.conf.h + arguments[5] + arguments[8];}if (newWidth > maxWidth \n\t newHeight > maxHeight) {return true;}};
            window.DARLA_CONFIG.onFinishParse = function(eventName, response) {try {window._perfMark('DARLA_PEND');if (eventName === "prefetch") {window._DarlaPrefetchResponse = response;}if (window._DarlaEvents) {window._DarlaEvents.emit("finishparse", {response: response,eventName: eventName});}} catch (e) {console.error(e);throw e;}
            };
            window.DARLA_CONFIG.onStartPrefetchRequest = function(eventName) {window._perfMark('DARLA_PFSTART');};
            window.DARLA_CONFIG.onFinishPrefetchRequest = function(eventName, status) {window._perfMark('DARLA_PFEND');try {window._DarlaEvents.emit('finishprefetch', {status: status,eventName: eventName});} catch (e) {console.error(e);throw e;}
            };
            window.DARLA_CONFIG.onPosMsg = function(cmd, pos, msg) {try {if (window._DarlaEvents && cmd === "cmsg") {var posmsg = {pos: pos,msg: msg};window._DarlaEvents.emit("splashmsg", posmsg);if (window._adPosMsg) {window._adPosMsg[window._adPosMsg.length] = posmsg;}}if (window._DarlaEvents && (cmd === "ui-fclose-show" \n\t cmd === "ui-fclose-close")) {setTimeout(function _emitAdResize(){window._DarlaEvents.emit("adresize", {pos: pos})}, 0);}} catch (e) {console.error(e);throw e;}
            };
            (function () {var _onloadEvt = function _onloadEvtHandler() {window._loadEvt = true;if (window._darlaSuccessEvt) {window._fireAdPerfBeacon(window._darlaSuccessEvt);}};if (window.addEventListener) {window.addEventListener("load", _onloadEvt);} else if (window.attachEvent) {window.attachEvent("onload", _onloadEvt);}function _onDarlaError (type) {return function _darlaErrHandler(evName) {try {if (window._DarlaEvents) {window._DarlaEvents.emit("darlaerror" + evName);window._DarlaEvents.emit("darlaerror", {type: type,eventName: evName,error: true});}} catch (e) {console.error(e);throw e;}};};window.DARLA_CONFIG.onRequestTimeout = _onDarlaError("requestTimeout");window.DARLA_CONFIG.onRenderTimeout = _onDarlaError("renderTimeout");window.DARLA_CONFIG.onFailure = _onDarlaError("failure");window.DARLA_CONFIG.onIdle = function onDarlaIdle () {    try {        window._DarlaEvents && window._DarlaEvents.emit("onIdle");    } catch (e) {        console.error(e);        throw e;    }};})();
            window.$sf = window.sf = {};
            window.$sf.host = {onReady: function (autorender, deferrender, firstRenderPos, deferRenderDelay) {window._perfMark('DARLA_ONREADY');window._perfMeasure('DARLA_ONREADY');window.sfready = true;if (window._DarlaEvents && !autorender) {window._DarlaEvents.emit("darlaboot");} else if (autorender){window._perfMark('DARLA_RSTART');if (typeof DARLA !== "undefined" && DARLA) {if (deferrender && firstRenderPos) {var firstBatchPos = [];var prefetchedPos = DARLA.prefetched();if (prefetchedPos.length <= 0) {return;}var firstRender = firstRenderPos.split(',');if (firstRender && firstRender.length > 0) {for (var i = 0; i < firstRender.length; i++) {var position = firstRender[i];var index = prefetchedPos.indexOf(position);if (index >= 0) {firstBatchPos = firstBatchPos.concat(prefetchedPos.splice(index, 1));}};}if (firstBatchPos.length > 0) {var renderWithRetry = function(pos) {if (DARLA.inProgress()) {var waittime = 600, maxwait = 100, deferRetry = 0, interval;interval = setInterval(function() {deferRetry ++;if (!DARLA.inProgress()){clearInterval(interval);DARLA.render(pos);}if (deferRetry > maxwait){clearInterval(interval);}}, waittime);} else {DARLA.render(pos);}};renderWithRetry(firstBatchPos);setTimeout(renderWithRetry, deferRenderDelay, prefetchedPos);} else {DARLA.render();}} else {DARLA.render();}}}}
            };
            window.sf_host = window.$sf.host;
            document.onreadystatechange = function () {if (document.readyState == "interactive") {window._perfMark('DOM_INTERACTIVE');}};
         </script>
         <script type="text/x-safeframe" id="fc" _ver="3-0-8">{"positions":[{"id":"FB2","html":"<!-- APT Vendor: WSOD, Format: Standard Graphical -->\n<scr"+"ipt type=\"text\/javascr"+"ipt\" src=\"https:\/\/ad.wsod.com\/embed\/a5878a3d6f2be40db26311f6f8fb21a3\/2588.0.js.120x60\/1508695682.34205?yud=smpv%3d3%26ed%3dKfb2BHkzObF0OPI9Q.6FtZbkSlSvfEhrSl0lwGMNEGZAiMbcAU1DtE48AMo5h5s1zE0pOuA.4Q6jOFfF6U76FqI95vbkRpoYW8CCuiClkYC057aIUYPIPVkjClGgvYGDXZzOU_D5tw6fjkTYMoAJeBHF_g2oAgmvWvXeLa8nAOd4UwT8MjtyZKmH2uLYgn6j4BRg247hXeJ_38N4VVxswd698hycufIoFqg2QlDK9hoZP.6zKwp.MCSTXeMyZQx8N.lHST6_SXlhBR3AhSxeGmSch8oC9Lttol4X.O7xQ_bSMQ8T9Ya6EzeMFHkWLslSmbxfqnExyac3pg8yYkhXUMcH_G4pm1Ir3cgjvzJsP2Lgu3OiAMSlLCJkGgEIfjh_prlwQKrCn.Mg4sHNESG3rxw8P0Ms.kphT5a_7PPPw8HOUx9oS2L1Mb.RLoVvpEgqCSSKWN9n5MB71io7ZpFgXaoV3w.mowgEQbPyDcNEMBR8IoyxYHdJdb__ofy6K.YuDP9A6gv_Jw6vJbdHqND53eqgOqMJTm.PvGhe2zqCqm5rOWhXFOr4UBTsJ42gkJrL0w2GhXnpDRmcbKi87msYHGIFaAcbUBbTG8qbM3U_rnewml.0LfS6WkJW34Pp4CSz_ySAp5CJSvgRGtYUHy.ycciuFN7o0dulAPjcW7g7ec0n4KPzozkifgbTOnXB3BMQG_25P4NAk4lhQ7zKF4NDK8cEinwc6DJknsbZ.L0AdUb1Wod_CdrZxcV0YBacjLr.1GP43BwMyTWHeBjCl8FBr30hhyJmJ31Xlvuj9IMEtgB7.s5w8ZrX2YOX1tzutPfFBK4bRbMTsQXtqaPpxalS6rtTQF_QazgKU2SaJ4K8yTXvA_BvXEINkp5ntCU6PKZmBhJZHq8I4n6nGuYTF_2ZAKH3gvVGo.AcgnkuTb64WgzX0so.vrIoljVHJYT3eOqMb2g0bVqbZ3HF51Pa3qyWP2zQBg4Lwb1kLcwVZHcc_V.rRn_3ModuugnknVL6NqelwPG85QzcKwu1uLhqsvSqOcYLF5jpEZh5Gx2Efbp9XGwivHvf4CYTPmXYOYk1589NG6hkYK1NBXA0q.jOqIwM669ErxuIZE7QubY9qn7Y2cOTVnT6xDT1fR65OIuAA1WZBACn1Tz2Dyk.en65qrCwYXhJIJa6lzIiJRjJepRkB9W3gmV80wEMMVZ5zVtLCtAd.km2L9NCCephXF7Vvcu5fcIzmfoJlMhQZrJQreoytny4Mnpf5.cPX9RnQkvmF4Z5j7Iy4DB1lJU0RcVwM4ufQA--&encver=1&encalgo=3DES-CFB-SHA1&app=apt&intf=1&click=https:\/\/beap-bc.yahoo.com\/yc\/YnY9MS4wLjAmYnM9KDE3aDhkYjN0ZChnaWQkaktVdW1UWXpMaktsdGZsMldhWVYyd2suTWpBNExnQUFBQUNXUGZyVixzdCQxNTA4Njk1NjgyNzMzNzk1LHNpJDQ0NTEwNTEsc3AkMTE4MzMzNTg4MyxjdCQyNSx5YngkT3BEQ1ozM2IuMTdyTC5QOHoyUnFKUSxsbmckZW4tdXMsY3IkNDYyMTQzMTA1MSx2JDIuMCxhaWQkM1kzWVF0Z25PSEUtLGJpJDIzNDE5ODYwNTEsbW1lJDk4NDk2MTAwNjQ2NjE2NDgxOTUsciQwLHlvbyQxLGFncCQzNTc1MDY2NTUxLGFwJEZCMikp\/0\/*\"><\/scr"+"ipt><NOSCR"+"IPT><a href=\"https:\/\/beap-bc.yahoo.com\/yc\/YnY9MS4wLjAmYnM9KDE3dWlham05YihnaWQkaktVdW1UWXpMaktsdGZsMldhWVYyd2suTWpBNExnQUFBQUNXUGZyVixzdCQxNTA4Njk1NjgyNzMzNzk1LHNpJDQ0NTEwNTEsc3AkMTE4MzMzNTg4MyxjdCQyNSx5YngkT3BEQ1ozM2IuMTdyTC5QOHoyUnFKUSxsbmckZW4tdXMsY3IkNDYyMTQzMTA1MSx2JDIuMCxhaWQkM1kzWVF0Z25PSEUtLGJpJDIzNDE5ODYwNTEsbW1lJDk4NDk2MTAwNjQ2NjE2NDgxOTUsciQxLHJkJDFiMm5tZGtiaSx5b28kMSxhZ3AkMzU3NTA2NjU1MSxhcCRGQjIpKQ\/2\/*https:\/\/ad.wsod.com\/click\/a5878a3d6f2be40db26311f6f8fb21a3\/2588.0.img.120x60\/1508695682.34205?yud=smpv%3d3%26ed%3dKfb2BHkzObF0OPI9Q.6FtZbkSlSvfEhrSl0lwGMNEGZAiMbcAU1DtE48AMo5h5s1zE0pOuA.4Q6jOFfF6U76FqI95vbkRpoYW8CCuiClkYC057aIUYPIPVkjClGgvYGDXZzOU_D5tw6fjkTYMoAJeBHF_g2oAgmvWvXeLa8nAOd4UwT8MjtyZKmH2uLYgn6j4BRg247hXeJ_38N4VVxswd698hycufIoFqg2QlDK9hoZP.6zKwp.MCSTXeMyZQx8N.lHST6_SXlhBR3AhSxeGmSch8oC9Lttol4X.O7xQ_bSMQ8T9Ya6EzeMFHkWLslSmbxfqnExyac3pg8yYkhXUMcH_G4pm1Ir3cgjvzJsP2Lgu3OiAMSlLCJkGgEIfjh_prlwQKrCn.Mg4sHNESG3rxw8P0Ms.kphT5a_7PPPw8HOUx9oS2L1Mb.RLoVvpEgqCSSKWN9n5MB71io7ZpFgXaoV3w.mowgEQbPyDcNEMBR8IoyxYHdJdb__ofy6K.YuDP9A6gv_Jw6vJbdHqND53eqgOqMJTm.PvGhe2zqCqm5rOWhXFOr4UBTsJ42gkJrL0w2GhXnpDRmcbKi87msYHGIFaAcbUBbTG8qbM3U_rnewml.0LfS6WkJW34Pp4CSz_ySAp5CJSvgRGtYUHy.ycciuFN7o0dulAPjcW7g7ec0n4KPzozkifgbTOnXB3BMQG_25P4NAk4lhQ7zKF4NDK8cEinwc6DJknsbZ.L0AdUb1Wod_CdrZxcV0YBacjLr.1GP43BwMyTWHeBjCl8FBr30hhyJmJ31Xlvuj9IMEtgB7.s5w8ZrX2YOX1tzutPfFBK4bRbMTsQXtqaPpxalS6rtTQF_QazgKU2SaJ4K8yTXvA_BvXEINkp5ntCU6PKZmBhJZHq8I4n6nGuYTF_2ZAKH3gvVGo.AcgnkuTb64WgzX0so.vrIoljVHJYT3eOqMb2g0bVqbZ3HF51Pa3qyWP2zQBg4Lwb1kLcwVZHcc_V.rRn_3ModuugnknVL6NqelwPG85QzcKwu1uLhqsvSqOcYLF5jpEZh5Gx2Efbp9XGwivHvf4CYTPmXYOYk1589NG6hkYK1NBXA0q.jOqIwM669ErxuIZE7QubY9qn7Y2cOTVnT6xDT1fR65OIuAA1WZBACn1Tz2Dyk.en65qrCwYXhJIJa6lzIiJRjJepRkB9W3gmV80wEMMVZ5zVtLCtAd.km2L9NCCephXF7Vvcu5fcIzmfoJlMhQZrJQreoytny4Mnpf5.cPX9RnQkvmF4Z5j7Iy4DB1lJU0RcVwM4ufQA--&encver=1&encalgo=3DES-CFB-SHA1&app=apt&intf=1\" target=\"_blank\"><img width=\"120\" height=\"60\" border=\"0\" src=\"https:\/\/ad.wsod.com\/embed\/a5878a3d6f2be40db26311f6f8fb21a3\/2588.0.img.120x60\/1508695682.34205?yud=smpv%3d3%26ed%3dKfb2BHkzObF0OPI9Q.6FtZbkSlSvfEhrSl0lwGMNEGZAiMbcAU1DtE48AMo5h5s1zE0pOuA.4Q6jOFfF6U76FqI95vbkRpoYW8CCuiClkYC057aIUYPIPVkjClGgvYGDXZzOU_D5tw6fjkTYMoAJeBHF_g2oAgmvWvXeLa8nAOd4UwT8MjtyZKmH2uLYgn6j4BRg247hXeJ_38N4VVxswd698hycufIoFqg2QlDK9hoZP.6zKwp.MCSTXeMyZQx8N.lHST6_SXlhBR3AhSxeGmSch8oC9Lttol4X.O7xQ_bSMQ8T9Ya6EzeMFHkWLslSmbxfqnExyac3pg8yYkhXUMcH_G4pm1Ir3cgjvzJsP2Lgu3OiAMSlLCJkGgEIfjh_prlwQKrCn.Mg4sHNESG3rxw8P0Ms.kphT5a_7PPPw8HOUx9oS2L1Mb.RLoVvpEgqCSSKWN9n5MB71io7ZpFgXaoV3w.mowgEQbPyDcNEMBR8IoyxYHdJdb__ofy6K.YuDP9A6gv_Jw6vJbdHqND53eqgOqMJTm.PvGhe2zqCqm5rOWhXFOr4UBTsJ42gkJrL0w2GhXnpDRmcbKi87msYHGIFaAcbUBbTG8qbM3U_rnewml.0LfS6WkJW34Pp4CSz_ySAp5CJSvgRGtYUHy.ycciuFN7o0dulAPjcW7g7ec0n4KPzozkifgbTOnXB3BMQG_25P4NAk4lhQ7zKF4NDK8cEinwc6DJknsbZ.L0AdUb1Wod_CdrZxcV0YBacjLr.1GP43BwMyTWHeBjCl8FBr30hhyJmJ31Xlvuj9IMEtgB7.s5w8ZrX2YOX1tzutPfFBK4bRbMTsQXtqaPpxalS6rtTQF_QazgKU2SaJ4K8yTXvA_BvXEINkp5ntCU6PKZmBhJZHq8I4n6nGuYTF_2ZAKH3gvVGo.AcgnkuTb64WgzX0so.vrIoljVHJYT3eOqMb2g0bVqbZ3HF51Pa3qyWP2zQBg4Lwb1kLcwVZHcc_V.rRn_3ModuugnknVL6NqelwPG85QzcKwu1uLhqsvSqOcYLF5jpEZh5Gx2Efbp9XGwivHvf4CYTPmXYOYk1589NG6hkYK1NBXA0q.jOqIwM669ErxuIZE7QubY9qn7Y2cOTVnT6xDT1fR65OIuAA1WZBACn1Tz2Dyk.en65qrCwYXhJIJa6lzIiJRjJepRkB9W3gmV80wEMMVZ5zVtLCtAd.km2L9NCCephXF7Vvcu5fcIzmfoJlMhQZrJQreoytny4Mnpf5.cPX9RnQkvmF4Z5j7Iy4DB1lJU0RcVwM4ufQA--&encver=1&encalgo=3DES-CFB-SHA1&app=apt&intf=1&\" \/><\/a><\/NOSCR"+"IPT><SCR"+"IPT language='JavaScript1.1' SRC=\"https:\/\/ad.doubleclick.net\/ddm\/trackimpj\/N3941.yahoo2\/B20343280.205954558;dc_trk_aid=405704229;dc_trk_cid=67442974;ord=1508695682.34205;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=?\"><\/SCR"+"IPT><scr"+"ipt>var url = \"\"; if(url && url.search(\"http\") != -1){document.write('<scr"+"ipt src=\"' + url + '\"><\\\/scr"+"ipt>');}<\/scr"+"ipt><!--QYZ 2341986051,4621431051,;;FB2;1183335883;1-->","lowHTML":"","meta":{"y":{"pos":"FB2","cscHTML":"<scr"+"ipt language=javascr"+"ipt>\nif(window.xzq_d==null)window.xzq_d=new Object();\nwindow.xzq_d['3Y3YQtgnOHE-']='(as$13atfob4b,aid$3Y3YQtgnOHE-,bi$2341986051,agp$3575066551,cr$4621431051,ct$25,at$H,eob$gd1_match_id=-1:ypos=FB2)';\n<\/scr"+"ipt><noscr"+"ipt><img width=1 height=1 alt=\"\" src=\"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3&al=(as$13atfob4b,aid$3Y3YQtgnOHE-,bi$2341986051,agp$3575066551,cr$4621431051,ct$25,at$H,eob$gd1_match_id=-1:ypos=FB2)\"><\/noscr"+"ipt>","cscURI":"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3&al=(as$13atfob4b,aid$3Y3YQtgnOHE-,bi$2341986051,agp$3575066551,cr$4621431051,ct$25,at$H,eob$gd1_match_id=-1:ypos=FB2)","behavior":"non_exp","adID":"9849610064661648195","matchID":"999999.999999.999999.999999","bookID":"2341986051","slotID":"0","serveType":"-1","err":false,"hasExternal":false,"supp_ugc":"0","placementID":"3575066551","fdb":"{ \\\"fdb_url\\\": \\\"https:\\\\\\\/\\\\\\\/beap-bc.yahoo.com\\\\\\\/af\\\\\\\/us?bv=1.0.0&bs=(1602rkkfc(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,srv$1,si$4451051,ct$25,exp$1508702882733795,adv$23994100343,li$3575929051,cr$4621431051,v$1.0,pbid$20459933223,seid$313287051))&al=(type${type},cmnt${cmnt},subo${subo})&r=10\\\", \\\"fdb_on\\\": \\\"1\\\", \\\"fdb_exp\\\": \\\"1508702882733\\\", \\\"fdb_intl\\\": \\\"en-US\\\" }","serveTime":"1508695682733795","impID":"3Y3YQtgnOHE-","creativeID":4621431051,"adc":"{\\\"label\\\":\\\"AdChoices\\\",\\\"url\\\":\\\"https:\\\\\/\\\\\/info.yahoo.com\\\\\/privacy\\\\\/us\\\\\/yahoo\\\\\/relevantads.html\\\",\\\"close\\\":\\\"Close\\\",\\\"closeAd\\\":\\\"Close Ad\\\",\\\"showAd\\\":\\\"Show ad\\\",\\\"collapse\\\":\\\"Collapse\\\",\\\"fdb\\\":\\\"I don't like this ad\\\",\\\"code\\\":\\\"en-us\\\"}","is3rd":0,"facStatus":{"fedStatusCode":"0","fedStatusMessage":"federation is not configured for ad slot"},"userProvidedData":{},"facRotation":{},"slotData":{"pt":"3","bamt":"10000000000.000000","namt":"0.001170","isLiveAdPreview":"false","is_ad_feedback":"false","trusted_custom":"false","isCompAds":"false","adjf":"1.000000","alpha":"1.000000","ffrac":"1.000000","pcpm":"-1.000000","fc":"false","ecpm":949.20204,"sdate":"1506957163","edate":"1509508799","bimpr":0,"pimpr":-92464064,"spltp":100,"frp":"false","pvid":"jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV"},"size":"120x60"}},"conf":{"w":120,"h":60}},{"id":"FB2-1","html":"<!-- APT Vendor: Google, Format: Standard Graphical -->\n<ins class='dcmads' style='display:inline-block;width:120px;height:60px'data-dcm-reverse-click-tracker='1'data-dcm-click-tracker='https:\/\/beap-bc.yahoo.com\/yc\/YnY9MS4wLjAmYnM9KDE3aHQwcG9pbChnaWQkaktVdW1UWXpMaktsdGZsMldhWVYyd2suTWpBNExnQUFBQUNXUGZyVixzdCQxNTA4Njk1NjgyNzMzNzk1LHNpJDQ0NTEwNTEsc3AkMTE4MzMzNTg4MyxjdCQyNSx5YngkT3BEQ1ozM2IuMTdyTC5QOHoyUnFKUSxsbmckZW4tdXMsY3IkNDYyNjY5NjA1MSx2JDIuMCxhaWQkTktQWVF0Z25PSEUtLGJpJDIzNDI3MTQ1NTEsbW1lJDk4NTE5ODMwMzQwOTI2ODkzNDYsciQwLHlvbyQxLGFncCQzNTc2NDI5MDUxLGFwJEZCMikp\/0\/*'\n    data-dcm-placement='N6036.Yahoo\/B10732953.143436002'\n    data-dcm-rendering-mode='scr"+"ipt'\n    data-dcm-https-only\n    data-dcm-resettable-device-id=''\n    data-dcm-app-id=''>\n  <scr"+"ipt src='https:\/\/www.googletagservices.com\/dcm\/dcmads.js'><\/scr"+"ipt>\n<\/ins><!--1508695682.34733--><scr"+"ipt>var url = \"\"; if(url && url.search(\"http\") != -1){document.write('<scr"+"ipt src=\"' + url + '\"><\\\/scr"+"ipt>');}<\/scr"+"ipt><!--QYZ 2342714551,4626696051,;;FB2;1183335883;1-->","lowHTML":"","meta":{"y":{"pos":"FB2-1","cscHTML":"<scr"+"ipt language=javascr"+"ipt>\nif(window.xzq_d==null)window.xzq_d=new Object();\nwindow.xzq_d['NKPYQtgnOHE-']='(as$13aausqnc,aid$NKPYQtgnOHE-,bi$2342714551,agp$3576429051,cr$4626696051,ct$25,at$H,eob$gd1_match_id=-1:ypos=FB2)';\n<\/scr"+"ipt><noscr"+"ipt><img width=1 height=1 alt=\"\" src=\"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3&al=(as$13aausqnc,aid$NKPYQtgnOHE-,bi$2342714551,agp$3576429051,cr$4626696051,ct$25,at$H,eob$gd1_match_id=-1:ypos=FB2)\"><\/noscr"+"ipt>","cscURI":"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3&al=(as$13aausqnc,aid$NKPYQtgnOHE-,bi$2342714551,agp$3576429051,cr$4626696051,ct$25,at$H,eob$gd1_match_id=-1:ypos=FB2)","behavior":"non_exp","adID":"9851983034092689346","matchID":"999999.999999.999999.999999","bookID":"2342714551","slotID":"1","serveType":"-1","err":false,"hasExternal":false,"supp_ugc":"0","placementID":"3576429051","fdb":"{ \\\"fdb_url\\\": \\\"https:\\\\\\\/\\\\\\\/beap-bc.yahoo.com\\\\\\\/af\\\\\\\/us?bv=1.0.0&bs=(1609mkmkg(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,srv$1,si$4451051,ct$25,exp$1508702882733795,adv$21063385913,li$3577348051,cr$4626696051,v$1.0,pbid$20459933223,seid$313287051))&al=(type${type},cmnt${cmnt},subo${subo})&r=10\\\", \\\"fdb_on\\\": \\\"1\\\", \\\"fdb_exp\\\": \\\"1508702882733\\\", \\\"fdb_intl\\\": \\\"en-US\\\" }","serveTime":"1508695682733795","impID":"NKPYQtgnOHE-","creativeID":4626696051,"adc":"{\\\"label\\\":\\\"AdChoices\\\",\\\"url\\\":\\\"https:\\\\\/\\\\\/info.yahoo.com\\\\\/privacy\\\\\/us\\\\\/yahoo\\\\\/relevantads.html\\\",\\\"close\\\":\\\"Close\\\",\\\"closeAd\\\":\\\"Close Ad\\\",\\\"showAd\\\":\\\"Show ad\\\",\\\"collapse\\\":\\\"Collapse\\\",\\\"fdb\\\":\\\"I don't like this ad\\\",\\\"code\\\":\\\"en-us\\\"}","is3rd":0,"facStatus":{"fedStatusCode":"0","fedStatusMessage":"federation is not configured for ad slot"},"userProvidedData":{},"facRotation":{},"slotData":{"pt":"3","bamt":"10000000000.000000","namt":"0.000980","isLiveAdPreview":"false","is_ad_feedback":"false","trusted_custom":"false","isCompAds":"false","adjf":"1.000000","alpha":"0.707071","ffrac":"0.707071","pcpm":"-1.000000","fc":"false","ecpm":0,"sdate":"1508435700","edate":"1509508740","bimpr":0,"pimpr":-6741097,"spltp":70.707071,"frp":"false","pvid":"jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV"},"size":"120x60"}},"conf":{"w":120,"h":60}},{"id":"FB2-2","html":"<!-- APT Vendor: MediaMind, Format: Standard Graphical -->\n<scr"+"ipt language=javascr"+"ipt> var gfEbForceStreaming  =  1;  <\/scr"+"ipt> <scr"+"ipt src=\"https:\/\/fw.adsafeprotected.com\/rjss\/bs.serving-sys.com\/114750\/19248027\/BurstingPipe\/adServer.bs?cn=rsb&c=28&pli=22660673&PluID=0&w=120&h=60&ord=1508695682.34797&ucm=true&ncu=$$https:\/\/beap-bc.yahoo.com\/yc\/YnY9MS4wLjAmYnM9KDE3dWYwazJpbyhnaWQkaktVdW1UWXpMaktsdGZsMldhWVYyd2suTWpBNExnQUFBQUNXUGZyVixzdCQxNTA4Njk1NjgyNzMzNzk1LHNpJDQ0NTEwNTEsc3AkMTE4MzMzNTg4MyxjdCQyNSx5YngkT3BEQ1ozM2IuMTdyTC5QOHoyUnFKUSxsbmckZW4tdXMsY3IkNDYyOTE3NjU1MSx2JDIuMCxhaWQkaTdqWVF0Z25PSEUtLGJpJDIzNDIwNTQwNTEsbW1lJDk4NDk4OTM1MzI1MDMxODQ4NzAsciQwLHJkJDExa2pxcG02Nix5b28kMSxhZ3AkMzU3NTE4NzA1MSxhcCRGQjIpKQ\/2\/*https:\/\/s.yimg.com\/dh\/ap\/noncscsec\/pixel.png$$&z=500\"><\/scr"+"ipt> <noscr"+"ipt> <a href=\"https:\/\/beap-bc.yahoo.com\/yc\/YnY9MS4wLjAmYnM9KDE3aGI5MHA5NChnaWQkaktVdW1UWXpMaktsdGZsMldhWVYyd2suTWpBNExnQUFBQUNXUGZyVixzdCQxNTA4Njk1NjgyNzMzNzk1LHNpJDQ0NTEwNTEsc3AkMTE4MzMzNTg4MyxjdCQyNSx5YngkT3BEQ1ozM2IuMTdyTC5QOHoyUnFKUSxsbmckZW4tdXMsY3IkNDYyOTE3NjU1MSx2JDIuMCxhaWQkaTdqWVF0Z25PSEUtLGJpJDIzNDIwNTQwNTEsbW1lJDk4NDk4OTM1MzI1MDMxODQ4NzAsciQxLHlvbyQxLGFncCQzNTc1MTg3MDUxLGFwJEZCMikp\/0\/*https%3A\/\/bs.serving-sys.com\/BurstingPipe\/adServer.bs%3Fcn%3Dbrd%26FlightID%3D22660673%26Page%3D%26PluID%3D0%26Pos%3D352225530\" target=\"_blank\"><img src=\"https:\/\/fw.adsafeprotected.com\/rfw\/bs.serving-sys.com\/114750\/19248026\/BurstingPipe\/adServer.bs?cn=bsr&FlightID=22660673&Page=&PluID=0&Pos=352225530\" border=0 width=120 height=60><\/a> <\/noscr"+"ipt><scr"+"ipt>var url = \"\"; if(url && url.search(\"http\") != -1){document.write('<scr"+"ipt src=\"' + url + '\"><\\\/scr"+"ipt>');}<\/scr"+"ipt><!--QYZ 2342054051,4629176551,;;FB2;1183335883;1-->","lowHTML":"","meta":{"y":{"pos":"FB2-2","cscHTML":"<scr"+"ipt language=javascr"+"ipt>\nif(window.xzq_d==null)window.xzq_d=new Object();\nwindow.xzq_d['i7jYQtgnOHE-']='(as$13a5kbv4f,aid$i7jYQtgnOHE-,bi$2342054051,agp$3575187051,cr$4629176551,ct$25,at$H,eob$gd1_match_id=-1:ypos=FB2)';\n<\/scr"+"ipt><noscr"+"ipt><img width=1 height=1 alt=\"\" src=\"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3&al=(as$13a5kbv4f,aid$i7jYQtgnOHE-,bi$2342054051,agp$3575187051,cr$4629176551,ct$25,at$H,eob$gd1_match_id=-1:ypos=FB2)\"><\/noscr"+"ipt>","cscURI":"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3&al=(as$13a5kbv4f,aid$i7jYQtgnOHE-,bi$2342054051,agp$3575187051,cr$4629176551,ct$25,at$H,eob$gd1_match_id=-1:ypos=FB2)","behavior":"non_exp","adID":"9849893532503184870","matchID":"999999.999999.999999.999999","bookID":"2342054051","slotID":"2","serveType":"-1","err":false,"hasExternal":false,"supp_ugc":"0","placementID":"3575187051","fdb":"{ \\\"fdb_url\\\": \\\"https:\\\\\\\/\\\\\\\/beap-bc.yahoo.com\\\\\\\/af\\\\\\\/us?bv=1.0.0&bs=(160it3j7b(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,srv$1,si$4451051,ct$25,exp$1508702882733795,adv$22978787195,li$3576087551,cr$4629176551,v$1.0,pbid$20459933223,seid$313287051))&al=(type${type},cmnt${cmnt},subo${subo})&r=10\\\", \\\"fdb_on\\\": \\\"1\\\", \\\"fdb_exp\\\": \\\"1508702882733\\\", \\\"fdb_intl\\\": \\\"en-US\\\" }","serveTime":"1508695682733795","impID":"i7jYQtgnOHE-","creativeID":4629176551,"adc":"{\\\"label\\\":\\\"AdChoices\\\",\\\"url\\\":\\\"https:\\\\\/\\\\\/info.yahoo.com\\\\\/privacy\\\\\/us\\\\\/yahoo\\\\\/relevantads.html\\\",\\\"close\\\":\\\"Close\\\",\\\"closeAd\\\":\\\"Close Ad\\\",\\\"showAd\\\":\\\"Show ad\\\",\\\"collapse\\\":\\\"Collapse\\\",\\\"fdb\\\":\\\"I don't like this ad\\\",\\\"code\\\":\\\"en-us\\\"}","is3rd":0,"facStatus":{"fedStatusCode":"0","fedStatusMessage":"federation is not configured for ad slot"},"userProvidedData":{},"facRotation":{},"slotData":{"pt":"0","bamt":"10000000000.000000","namt":"0.001250","isLiveAdPreview":"false","is_ad_feedback":"false","trusted_custom":"false","isCompAds":"false","adjf":"1.000000","alpha":"1.000000","ffrac":"0.777457","pcpm":"-1.000000","fc":"false","dimpr":12312178,"ecpm":1.25,"sdate":"1507139814","edate":"1509508740","bimpr":17280000,"pimpr":4967822,"spltp":0,"frp":"false","pvid":"jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV"},"size":"120x60"}},"conf":{"w":120,"h":60}},{"id":"FB2-3","html":"<!-- APT Vendor: WSOD, Format: Standard Graphical -->\n<scr"+"ipt type=\"text\/javascr"+"ipt\" src=\"https:\/\/ad.wsod.com\/embed\/577da7fee6e9ff57afc5f23882acdf54\/357.0.js.120x60\/1508695682.34870?yud=smpv%3d3%26ed%3dKfb2BHkzObF0OPI9Q.6FtZbkSlSvfEhrSl0lwGMNEGZAiMbcAU1DtE48AMo5h5s1zE0pOuA.4Q6jOFfF6U76FqI95vbkRpoYW8CCuiClkYC057aIUYPIPVkjClGgvYGDXZzOU_D5tw6fjkTYMoAJeBHF_g2oAgmvWvXeLa8nAOd4UwT8MjtyZKmH2uLYgn6j4BRg247hXeJ_38N4VVxswd698hycufIoFqg2QlDK9hoZP.6zKwp.MCSTXeMyZQx8N.lHST6_SXlhBR3AhSxeGmSch8oC9Lttol4X.O7xQ_bSMQ8T9Ya6EzeMFHkWLslSmbxfqnExyac3pg8yYkhXUMcH_G4pm1Ir3cgjvzJsP2Lgu3OiAMSlLCJkGgEIfjh_prlwQKrCn.Mg4sHNESG3rxw8P0Ms.kphT5a_7PPPw8HOUx9oS2L1Mb.RLoVvpEgqCSSKWN9n5MB71io7ZpFgXaoV3w.mowgEQbPyDcNEMBR8IoyxYHdJdb__ofy6K.YuDP9A6gv_Jw6vJbdHqND53eqgOqMJTm.PvGhe2zqCqm5rOWhXFOr4UBTsJ42gkJrL0w2GhXnpDRmcbKi87msYHGIFaAcbUBbTG8qbM3U_rnewml.0LfS6WkJW34Pp4CSz_ySAp5CJSvgRGtYUHy.ycciuFN7o0dulAPjcW7g7ec0n4KPzozkifgbTOnXB3BMQG_25P4NAk4lhQ7zKF4NDK8cEinwc6DJknsbZ.L0AdUb1Wod_CdrZxcV0YBacjLr.1GP43BwMyTWHeBjCl8FBr30hhyJmJ31Xlvuj9IMEtgB7.s5w8ZrX2YOX1tzutPfFBK4bRbMTsQXtqaPpxalS6rtTQF_QazgKU2SaJ4K8yTXvA_BvXEINkp5ntCU6PKZmBhJZHq8I4n6nGuYTF_2ZAKH3gvVGo.AcgnkuTb64WgzX0so.vrIoljVHJYT3eOqMb2g0bVqbZ3HF51Pa3qyWP2zQBg4Lwb1kLcwVZHcc_V.rRn_3ModuugnknVL6NqelwPG85QzcKwu1uLhqsvSqOcYLF5jpEZh5Gx2Efbp9XGwivHvf4CYTPmXYOYk1589NG6hkYK1NBXA0q.jOqIwM669ErxuIZE7QubY9qn7Y2cOTVnT6xDT1fR65OIuAA1WZBACn1Tz2Dyk.en65qrCwYXhJIJa6lzIiJRjJepRkB9W3gmV80wEMMVZ5zVtLCtAd.km2L9NCCephXF7Vvcu5fcIzmfoJlMhQZrJQreoytny4Mnpf5.cPX9RhQUTjEoZ5LTTGsZuG7nhkjomKTuF_.g--&encver=1&encalgo=3DES-CFB-SHA1&app=apt&intf=1&click=https:\/\/beap-bc.yahoo.com\/yc\/YnY9MS4wLjAmYnM9KDE3aGFpNDg5cChnaWQkaktVdW1UWXpMaktsdGZsMldhWVYyd2suTWpBNExnQUFBQUNXUGZyVixzdCQxNTA4Njk1NjgyNzMzNzk1LHNpJDQ0NTEwNTEsc3AkMTE4MzMzNTg4MyxjdCQyNSx5YngkT3BEQ1ozM2IuMTdyTC5QOHoyUnFKUSxsbmckZW4tdXMsY3IkNDYyNDE5MjU1MSx2JDIuMCxhaWQkNHMzWVF0Z25PSEUtLGJpJDIzNDIyOTc1NTEsbW1lJDk4NTA4NDI3MjAyNzU2MDA3NTYsciQwLHlvbyQxLGFncCQzNTc1NjUwMDUxLGFwJEZCMikp\/0\/*\"><\/scr"+"ipt><NOSCR"+"IPT><a href=\"https:\/\/beap-bc.yahoo.com\/yc\/YnY9MS4wLjAmYnM9KDE3dW51M3EyOShnaWQkaktVdW1UWXpMaktsdGZsMldhWVYyd2suTWpBNExnQUFBQUNXUGZyVixzdCQxNTA4Njk1NjgyNzMzNzk1LHNpJDQ0NTEwNTEsc3AkMTE4MzMzNTg4MyxjdCQyNSx5YngkT3BEQ1ozM2IuMTdyTC5QOHoyUnFKUSxsbmckZW4tdXMsY3IkNDYyNDE5MjU1MSx2JDIuMCxhaWQkNHMzWVF0Z25PSEUtLGJpJDIzNDIyOTc1NTEsbW1lJDk4NTA4NDI3MjAyNzU2MDA3NTYsciQxLHJkJDFiMW5vMnIxbix5b28kMSxhZ3AkMzU3NTY1MDA1MSxhcCRGQjIpKQ\/2\/*https:\/\/ad.wsod.com\/click\/577da7fee6e9ff57afc5f23882acdf54\/357.0.img.120x60\/1508695682.34870?yud=smpv%3d3%26ed%3dKfb2BHkzObF0OPI9Q.6FtZbkSlSvfEhrSl0lwGMNEGZAiMbcAU1DtE48AMo5h5s1zE0pOuA.4Q6jOFfF6U76FqI95vbkRpoYW8CCuiClkYC057aIUYPIPVkjClGgvYGDXZzOU_D5tw6fjkTYMoAJeBHF_g2oAgmvWvXeLa8nAOd4UwT8MjtyZKmH2uLYgn6j4BRg247hXeJ_38N4VVxswd698hycufIoFqg2QlDK9hoZP.6zKwp.MCSTXeMyZQx8N.lHST6_SXlhBR3AhSxeGmSch8oC9Lttol4X.O7xQ_bSMQ8T9Ya6EzeMFHkWLslSmbxfqnExyac3pg8yYkhXUMcH_G4pm1Ir3cgjvzJsP2Lgu3OiAMSlLCJkGgEIfjh_prlwQKrCn.Mg4sHNESG3rxw8P0Ms.kphT5a_7PPPw8HOUx9oS2L1Mb.RLoVvpEgqCSSKWN9n5MB71io7ZpFgXaoV3w.mowgEQbPyDcNEMBR8IoyxYHdJdb__ofy6K.YuDP9A6gv_Jw6vJbdHqND53eqgOqMJTm.PvGhe2zqCqm5rOWhXFOr4UBTsJ42gkJrL0w2GhXnpDRmcbKi87msYHGIFaAcbUBbTG8qbM3U_rnewml.0LfS6WkJW34Pp4CSz_ySAp5CJSvgRGtYUHy.ycciuFN7o0dulAPjcW7g7ec0n4KPzozkifgbTOnXB3BMQG_25P4NAk4lhQ7zKF4NDK8cEinwc6DJknsbZ.L0AdUb1Wod_CdrZxcV0YBacjLr.1GP43BwMyTWHeBjCl8FBr30hhyJmJ31Xlvuj9IMEtgB7.s5w8ZrX2YOX1tzutPfFBK4bRbMTsQXtqaPpxalS6rtTQF_QazgKU2SaJ4K8yTXvA_BvXEINkp5ntCU6PKZmBhJZHq8I4n6nGuYTF_2ZAKH3gvVGo.AcgnkuTb64WgzX0so.vrIoljVHJYT3eOqMb2g0bVqbZ3HF51Pa3qyWP2zQBg4Lwb1kLcwVZHcc_V.rRn_3ModuugnknVL6NqelwPG85QzcKwu1uLhqsvSqOcYLF5jpEZh5Gx2Efbp9XGwivHvf4CYTPmXYOYk1589NG6hkYK1NBXA0q.jOqIwM669ErxuIZE7QubY9qn7Y2cOTVnT6xDT1fR65OIuAA1WZBACn1Tz2Dyk.en65qrCwYXhJIJa6lzIiJRjJepRkB9W3gmV80wEMMVZ5zVtLCtAd.km2L9NCCephXF7Vvcu5fcIzmfoJlMhQZrJQreoytny4Mnpf5.cPX9RhQUTjEoZ5LTTGsZuG7nhkjomKTuF_.g--&encver=1&encalgo=3DES-CFB-SHA1&app=apt&intf=1\" target=\"_blank\"><img width=\"120\" height=\"60\" border=\"0\" src=\"https:\/\/ad.wsod.com\/embed\/577da7fee6e9ff57afc5f23882acdf54\/357.0.img.120x60\/1508695682.34870?yud=smpv%3d3%26ed%3dKfb2BHkzObF0OPI9Q.6FtZbkSlSvfEhrSl0lwGMNEGZAiMbcAU1DtE48AMo5h5s1zE0pOuA.4Q6jOFfF6U76FqI95vbkRpoYW8CCuiClkYC057aIUYPIPVkjClGgvYGDXZzOU_D5tw6fjkTYMoAJeBHF_g2oAgmvWvXeLa8nAOd4UwT8MjtyZKmH2uLYgn6j4BRg247hXeJ_38N4VVxswd698hycufIoFqg2QlDK9hoZP.6zKwp.MCSTXeMyZQx8N.lHST6_SXlhBR3AhSxeGmSch8oC9Lttol4X.O7xQ_bSMQ8T9Ya6EzeMFHkWLslSmbxfqnExyac3pg8yYkhXUMcH_G4pm1Ir3cgjvzJsP2Lgu3OiAMSlLCJkGgEIfjh_prlwQKrCn.Mg4sHNESG3rxw8P0Ms.kphT5a_7PPPw8HOUx9oS2L1Mb.RLoVvpEgqCSSKWN9n5MB71io7ZpFgXaoV3w.mowgEQbPyDcNEMBR8IoyxYHdJdb__ofy6K.YuDP9A6gv_Jw6vJbdHqND53eqgOqMJTm.PvGhe2zqCqm5rOWhXFOr4UBTsJ42gkJrL0w2GhXnpDRmcbKi87msYHGIFaAcbUBbTG8qbM3U_rnewml.0LfS6WkJW34Pp4CSz_ySAp5CJSvgRGtYUHy.ycciuFN7o0dulAPjcW7g7ec0n4KPzozkifgbTOnXB3BMQG_25P4NAk4lhQ7zKF4NDK8cEinwc6DJknsbZ.L0AdUb1Wod_CdrZxcV0YBacjLr.1GP43BwMyTWHeBjCl8FBr30hhyJmJ31Xlvuj9IMEtgB7.s5w8ZrX2YOX1tzutPfFBK4bRbMTsQXtqaPpxalS6rtTQF_QazgKU2SaJ4K8yTXvA_BvXEINkp5ntCU6PKZmBhJZHq8I4n6nGuYTF_2ZAKH3gvVGo.AcgnkuTb64WgzX0so.vrIoljVHJYT3eOqMb2g0bVqbZ3HF51Pa3qyWP2zQBg4Lwb1kLcwVZHcc_V.rRn_3ModuugnknVL6NqelwPG85QzcKwu1uLhqsvSqOcYLF5jpEZh5Gx2Efbp9XGwivHvf4CYTPmXYOYk1589NG6hkYK1NBXA0q.jOqIwM669ErxuIZE7QubY9qn7Y2cOTVnT6xDT1fR65OIuAA1WZBACn1Tz2Dyk.en65qrCwYXhJIJa6lzIiJRjJepRkB9W3gmV80wEMMVZ5zVtLCtAd.km2L9NCCephXF7Vvcu5fcIzmfoJlMhQZrJQreoytny4Mnpf5.cPX9RhQUTjEoZ5LTTGsZuG7nhkjomKTuF_.g--&encver=1&encalgo=3DES-CFB-SHA1&app=apt&intf=1&\" \/><\/a><\/NOSCR"+"IPT><img src=\"https:\/\/sp.analytics.yahoo.com\/spp.pl?a=10000&.yp=416417&ec=brokeragertgbtn\"\/><scr"+"ipt>var url = \"\"; if(url && url.search(\"http\") != -1){document.write('<scr"+"ipt src=\"' + url + '\"><\\\/scr"+"ipt>');}<\/scr"+"ipt><!--QYZ 2342297551,4624192551,;;FB2;1183335883;1-->","lowHTML":"","meta":{"y":{"pos":"FB2-3","cscHTML":"<scr"+"ipt language=javascr"+"ipt>\nif(window.xzq_d==null)window.xzq_d=new Object();\nwindow.xzq_d['4s3YQtgnOHE-']='(as$13aq5mls2,aid$4s3YQtgnOHE-,bi$2342297551,agp$3575650051,cr$4624192551,ct$25,at$H,eob$gd1_match_id=-1:ypos=FB2)';\n<\/scr"+"ipt><noscr"+"ipt><img width=1 height=1 alt=\"\" src=\"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3&al=(as$13aq5mls2,aid$4s3YQtgnOHE-,bi$2342297551,agp$3575650051,cr$4624192551,ct$25,at$H,eob$gd1_match_id=-1:ypos=FB2)\"><\/noscr"+"ipt>","cscURI":"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3&al=(as$13aq5mls2,aid$4s3YQtgnOHE-,bi$2342297551,agp$3575650051,cr$4624192551,ct$25,at$H,eob$gd1_match_id=-1:ypos=FB2)","behavior":"non_exp","adID":"9850842720275600756","matchID":"999999.999999.999999.999999","bookID":"2342297551","slotID":"3","serveType":"-1","err":false,"hasExternal":false,"supp_ugc":"0","placementID":"3575650051","fdb":"{ \\\"fdb_url\\\": \\\"https:\\\\\\\/\\\\\\\/beap-bc.yahoo.com\\\\\\\/af\\\\\\\/us?bv=1.0.0&bs=(160r5n3bc(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,srv$1,si$4451051,ct$25,exp$1508702882733795,adv$21074470295,li$3576570551,cr$4624192551,v$1.0,pbid$20459933223,seid$313287051))&al=(type${type},cmnt${cmnt},subo${subo})&r=10\\\", \\\"fdb_on\\\": \\\"1\\\", \\\"fdb_exp\\\": \\\"1508702882733\\\", \\\"fdb_intl\\\": \\\"en-US\\\" }","serveTime":"1508695682733795","impID":"4s3YQtgnOHE-","creativeID":4624192551,"adc":"{\\\"label\\\":\\\"AdChoices\\\",\\\"url\\\":\\\"https:\\\\\/\\\\\/info.yahoo.com\\\\\/privacy\\\\\/us\\\\\/yahoo\\\\\/relevantads.html\\\",\\\"close\\\":\\\"Close\\\",\\\"closeAd\\\":\\\"Close Ad\\\",\\\"showAd\\\":\\\"Show ad\\\",\\\"collapse\\\":\\\"Collapse\\\",\\\"fdb\\\":\\\"I don't like this ad\\\",\\\"code\\\":\\\"en-us\\\"}","is3rd":0,"facStatus":{"fedStatusCode":"0","fedStatusMessage":"federation is not configured for ad slot"},"userProvidedData":{},"facRotation":{},"slotData":{"pt":"3","bamt":"10000000000.000000","namt":"0.000490","isLiveAdPreview":"false","is_ad_feedback":"false","trusted_custom":"false","isCompAds":"false","adjf":"1.000000","alpha":"1.000000","ffrac":"1.000000","pcpm":"-1.000000","fc":"false","ecpm":6251.046152,"sdate":"1507757538","edate":"1514782799","bimpr":0,"pimpr":-1316283,"spltp":100,"frp":"false","pvid":"jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV"},"size":"120x60"}},"conf":{"w":120,"h":60}},{"id":"LDRB","html":"<style type=\"text\/css\">\n.CAN_ad .yadslug {\n    position: absolute !important; right: 1px; top:1px; display:inline-block\n!important; z-index : 999;\n    color:#999 !important;text-decoration:none;background:#fff\nurl('https:\/\/secure.footprint.net\/yieldmanager\/apex\/mediastore\/adchoice_1.png') no-repeat 100% 0\n!important;cursor:hand !important;height:12px !important;padding:0px 14px 0px\n1px !important;display:inline-block !important;\n}\n.CAN_ad .yadslug span {display:none !important;}\n.CAN_ad .yadslug:hover {zoom: 1;}\n.CAN_ad .yadslug:hover span {display:inline-block !important;color:#999\n!important;}\n.CAN_ad .yadslug:hover span, .CAN_ad .yadslug:hover {font:11px arial\n!important;}\n<\/style>    \n<div class=\"CAN_ad\" style=\"display:inline-block;position: relative;\">\n<a class=\"yadslug\"\nhref=\"http:\/\/info.yahoo.com\/relevantads\/\"\ntarget=\"_blank\"><span>AdChoices<\/span><\/a><!-- APT Vendor: Doubleclick, Format: Standard Graphical -->\n<SCR"+"IPT language='JavaScript1.1' SRC=\"https:\/\/fw.adsafeprotected.com\/rjss\/dc\/71202\/17996282\/ddm\/adj\/N805.yahoo.comSD1509\/B10657587.142694916;sz=728x90;click=https:\/\/beap-bc.yahoo.com\/yc\/YnY9MS4wLjAmYnM9KDE3aWQyMzMyMChnaWQkaktVdW1UWXpMaktsdGZsMldhWVYyd2suTWpBNExnQUFBQUNXUGZyVixzdCQxNTA4Njk1NjgyNzMzNzk1LHNpJDQ0NTEwNTEsc3AkMTE4MzMzNTg4MyxjdCQyNSx5YngkT3BEQ1ozM2IuMTdyTC5QOHoyUnFKUSxsbmckZW4tdXMsY3IkNDYxODMwNTU1MSx2JDIuMCxhaWQkNXczWlF0Z25PSEUtLGJpJDIzMzU2MDI1NTEsbW1lJDk4MjczNDcxMDE2ODI4MjkzOTgsciQwLHlvbyQxLGFncCQzNTY0NDEyMDUxLGFwJExEUkIpKQ\/2\/*;ord=1508695682.34141;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=?\">\n<\/SCR"+"IPT>\n<NOSCR"+"IPT>\n<A HREF=\"https:\/\/beap-bc.yahoo.com\/yc\/YnY9MS4wLjAmYnM9KDE3dnJhbDFqNChnaWQkaktVdW1UWXpMaktsdGZsMldhWVYyd2suTWpBNExnQUFBQUNXUGZyVixzdCQxNTA4Njk1NjgyNzMzNzk1LHNpJDQ0NTEwNTEsc3AkMTE4MzMzNTg4MyxjdCQyNSx5YngkT3BEQ1ozM2IuMTdyTC5QOHoyUnFKUSxsbmckZW4tdXMsY3IkNDYxODMwNTU1MSx2JDIuMCxhaWQkNXczWlF0Z25PSEUtLGJpJDIzMzU2MDI1NTEsbW1lJDk4MjczNDcxMDE2ODI4MjkzOTgsciQxLHJkJDEzOGZiM3E1bCx5b28kMSxhZ3AkMzU2NDQxMjA1MSxhcCRMRFJCKSk\/1\/*https:\/\/ad.doubleclick.net\/ddm\/jump\/N805.yahoo.comSD1509\/B10657587.142694916;sz=728x90;ord=1508695682.34141?\">\n<IMG SRC=\"https:\/\/fw.adsafeprotected.com\/rfw\/dc\/71202\/17996281\/ddm\/ad\/N805.yahoo.comSD1509\/B10657587.142694916;sz=728x90;ord=1508695682.34141;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=?\" BORDER=0 WIDTH=728 HEIGHT=90 ALT=\"Advertisement\"><\/A>\n<\/NOSCR"+"IPT>\n<scr"+"ipt>var url = \"\"; if(url && url.search(\"http\") != -1){document.write('<scr"+"ipt src=\"' + url + '\"><\\\/scr"+"ipt>');}<\/scr"+"ipt><!--QYZ 2335602551,4618305551,;;LDRB;1183335883;1--><\/div>","lowHTML":"","meta":{"y":{"pos":"LDRB","cscHTML":"<scr"+"ipt language=javascr"+"ipt>\nif(window.xzq_d==null)window.xzq_d=new Object();\nwindow.xzq_d['5w3ZQtgnOHE-']='(as$13alekldf,aid$5w3ZQtgnOHE-,bi$2335602551,agp$3564412051,cr$4618305551,ct$25,at$H,eob$gd1_match_id=-1:ypos=LDRB)';\n<\/scr"+"ipt><noscr"+"ipt><img width=1 height=1 alt=\"\" src=\"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3&al=(as$13alekldf,aid$5w3ZQtgnOHE-,bi$2335602551,agp$3564412051,cr$4618305551,ct$25,at$H,eob$gd1_match_id=-1:ypos=LDRB)\"><\/noscr"+"ipt>","cscURI":"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3&al=(as$13alekldf,aid$5w3ZQtgnOHE-,bi$2335602551,agp$3564412051,cr$4618305551,ct$25,at$H,eob$gd1_match_id=-1:ypos=LDRB)","behavior":"non_exp","adID":"9827347101682829398","matchID":"999999.999999.999999.999999","bookID":"2335602551","slotID":"6","serveType":"-1","err":false,"hasExternal":false,"supp_ugc":"0","placementID":"3564412051","fdb":"{ \\\"fdb_url\\\": \\\"https:\\\\\\\/\\\\\\\/beap-bc.yahoo.com\\\\\\\/af\\\\\\\/us?bv=1.0.0&bs=(160qb4isb(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,srv$1,si$4451051,ct$25,exp$1508702882733795,adv$21074470295,li$3565011051,cr$4618305551,v$1.0,pbid$20459933223,seid$313287051))&al=(type${type},cmnt${cmnt},subo${subo})&r=10\\\", \\\"fdb_on\\\": \\\"1\\\", \\\"fdb_exp\\\": \\\"1508702882733\\\", \\\"fdb_intl\\\": \\\"en-US\\\" }","serveTime":"1508695682733795","impID":"5w3ZQtgnOHE-","creativeID":4618305551,"adc":"{\\\"label\\\":\\\"AdChoices\\\",\\\"url\\\":\\\"https:\\\\\/\\\\\/info.yahoo.com\\\\\/privacy\\\\\/us\\\\\/yahoo\\\\\/relevantads.html\\\",\\\"close\\\":\\\"Close\\\",\\\"closeAd\\\":\\\"Close Ad\\\",\\\"showAd\\\":\\\"Show ad\\\",\\\"collapse\\\":\\\"Collapse\\\",\\\"fdb\\\":\\\"I don't like this ad\\\",\\\"code\\\":\\\"en-us\\\"}","is3rd":0,"facStatus":{"fedStatusCode":"10","fedStatusMessage":"no replacement for exclusive contract"},"userProvidedData":{},"facRotation":{},"slotData":{"pt":"3","bamt":"10000000000.000000","namt":"0.016100","isLiveAdPreview":"false","is_ad_feedback":"false","trusted_custom":"false","isCompAds":"false","adjf":"1.000000","alpha":"1.000000","ffrac":"1.000000","pcpm":"-1.000000","fc":"false","ecpm":0,"sdate":"1504238400","edate":"1514782799","bimpr":0,"pimpr":-5304307,"spltp":100,"frp":"false","pvid":"jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV"},"size":"728x90"}},"conf":{"w":728,"h":90}},{"id":"LDRB2","html":"<!-- APT Vendor: Right Media, Format: Standard Graphical -->\n<SCR"+"IPT TYPE=\"text\/javascr"+"ipt\" SRC=\"https:\/\/na.ads.yahoo.com\/yax\/banner?ve=1&tt=1&si=313287051&megamodal=${MEGAMODAL}&bucket=fin-strm-test2,fndmtest,finssl&asz=728x90&u=https:\/\/finance.yahoo.com\/losers&gdAdId=PiPZQtgnOHE-&gdUuid=jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV&gdSt=1508695682733795&publisher_blob=${RS}\n\tjKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV\n\t1183335883\n\tLDRB2\n\t1508695682.34324\n\t3-0-8:ysd:1&pub_redirect=https:\/\/beap-bc.yahoo.com\/yc\/YnY9MS4wLjAmYnM9KDE3amlta21sYyhnaWQkaktVdW1UWXpMaktsdGZsMldhWVYyd2suTWpBNExnQUFBQUNXUGZyVixzdCQxNTA4Njk1NjgyNzMzNzk1LHNpJDQ0NTEwNTEsc3AkMTE4MzMzNTg4MyxjdCQyNSx5YngkT3BEQ1ozM2IuMTdyTC5QOHoyUnFKUSxsbmckZW4tdXMsY3IkNDUyNzA2ODU1MSx2JDIuMCxhaWQkUGlQWlF0Z25PSEUtLGJpJDIzMTUyMjIwNTEsbW1lJDk3NDk3OTcxNzIxODYwNzE4MjUsciQwLHlvbyQxLGFncCQzNTM2MDI1NTUxLGFwJExEUkIyKSk\/1\/*&K=1\"><\/SCR"+"IPT><scr"+"ipt>var url = \"\"; if(url && url.search(\"http\") != -1){document.write('<scr"+"ipt src=\"' + url + '\"><\\\/scr"+"ipt>');}<\/scr"+"ipt><!--QYZ 2315222051,4527068551,;;LDRB2;1183335883;1-->","lowHTML":"","meta":{"y":{"pos":"LDRB2","cscHTML":"<scr"+"ipt language=javascr"+"ipt>\nif(window.xzq_d==null)window.xzq_d=new Object();\nwindow.xzq_d['PiPZQtgnOHE-']='(as$13aman70k,aid$PiPZQtgnOHE-,bi$2315222051,agp$3536025551,cr$4527068551,ct$25,at$H,eob$gd1_match_id=-1:ypos=LDRB2)';\n<\/scr"+"ipt><noscr"+"ipt><img width=1 height=1 alt=\"\" src=\"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3&al=(as$13aman70k,aid$PiPZQtgnOHE-,bi$2315222051,agp$3536025551,cr$4527068551,ct$25,at$H,eob$gd1_match_id=-1:ypos=LDRB2)\"><\/noscr"+"ipt>","cscURI":"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3&al=(as$13aman70k,aid$PiPZQtgnOHE-,bi$2315222051,agp$3536025551,cr$4527068551,ct$25,at$H,eob$gd1_match_id=-1:ypos=LDRB2)","behavior":"non_exp","adID":"9749797172186071825","matchID":"999999.999999.999999.999999","bookID":"2315222051","slotID":"7","serveType":"-1","err":false,"hasExternal":false,"supp_ugc":"0","placementID":"3536025551","fdb":"{ \\\"fdb_url\\\": \\\"https:\\\\\\\/\\\\\\\/beap-bc.yahoo.com\\\\\\\/af\\\\\\\/us?bv=1.0.0&bs=(1602hcj4p(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,srv$1,si$4451051,ct$25,exp$1508702882733795,adv$26513753608,li$3535932051,cr$4527068551,v$1.0,pbid$20459933223,seid$313287051))&al=(type${type},cmnt${cmnt},subo${subo})&r=10\\\", \\\"fdb_on\\\": \\\"1\\\", \\\"fdb_exp\\\": \\\"1508702882733\\\", \\\"fdb_intl\\\": \\\"en-US\\\" }","serveTime":"1508695682733795","impID":"PiPZQtgnOHE-","creativeID":4527068551,"adc":"{\\\"label\\\":\\\"AdChoices\\\",\\\"url\\\":\\\"https:\\\\\/\\\\\/info.yahoo.com\\\\\/privacy\\\\\/us\\\\\/yahoo\\\\\/relevantads.html\\\",\\\"close\\\":\\\"Close\\\",\\\"closeAd\\\":\\\"Close Ad\\\",\\\"showAd\\\":\\\"Show ad\\\",\\\"collapse\\\":\\\"Collapse\\\",\\\"fdb\\\":\\\"I don't like this ad\\\",\\\"code\\\":\\\"en-us\\\"}","is3rd":1,"facStatus":{"fedStatusCode":"0","fedStatusMessage":"federation is not configured for ad slot"},"userProvidedData":{},"facRotation":{},"slotData":{"pt":"8","bamt":"10000000000.000000","namt":"0.000000","isLiveAdPreview":"false","is_ad_feedback":"false","trusted_custom":"false","isCompAds":"false","adjf":"1.000000","alpha":"-1.000000","ffrac":"0.988134","pcpm":"-1.000000","fc":"false","sdate":"1473794849","edate":"1561953540","bimpr":99986538496,"pimpr":0,"spltp":0,"frp":"false","pvid":"jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV"},"size":"728x90"}},"conf":{"w":728,"h":90}},{"id":"LREC","html":"<!-- SpaceID=1183335883 loc=LREC noad --><!-- fac2-replaced-gd2 booking id 2315223051-->","lowHTML":"","meta":{"y":{"pos":"LREC","cscHTML":"<scr"+"ipt language=javascr"+"ipt> if(window.xzq_d==null)window.xzq_d=new Object();window.xzq_d['lTjZQtgnOHE-']='(as$12566pir4,aid$lTjZQtgnOHE-,cr$-1,ct$25,at$H,eob$fac2_r=1:gd1_match_id=-1:ypos=LREC)';<\/scr"+"ipt><noscr"+"ipt><img width=1 height=1 alt=\"\" src=\"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(136n62j08(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,si$4451051,sp$1183335883,pv$1,v$2.0,st$1508695682995463))&t=J_3-D_3&al=(as$12566pir4,aid$lTjZQtgnOHE-,cr$-1,ct$25,at$H,eob$fac2_r=1:gd1_match_id=-1:ypos=LREC)\"><\/noscr"+"ipt>","cscURI":"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(136n62j08(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,si$4451051,sp$1183335883,pv$1,v$2.0,st$1508695682995463))&t=J_3-D_3&al=(as$12566pir4,aid$lTjZQtgnOHE-,cr$-1,ct$25,at$H,eob$fac2_r=1:gd1_match_id=-1:ypos=LREC)","behavior":"non_exp","adID":"#","matchID":"999999.999999.999999.999999","bookID":"2315223051","slotID":"8","serveType":"-1","err":"invalid (darla) (no)","hasExternal":false,"supp_ugc":"0","placementID":"3536034551","fdb":"{ \\\"fdb_url\\\": \\\"https:\\\\\\\/\\\\\\\/beap-bc.yahoo.com\\\\\\\/af\\\\\\\/us?bv=1.0.0&bs=(160fr6sfu(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,srv$1,si$4451051,ct$25,exp$1508702882733795,adv$26513753608,li$3535921551,cr$4527082051,v$1.0,pbid$20459933223,seid$313287051))&al=(type${type},cmnt${cmnt},subo${subo})&r=10\\\", \\\"fdb_on\\\": \\\"1\\\", \\\"fdb_exp\\\": \\\"1508702882733\\\", \\\"fdb_intl\\\": \\\"en-US\\\" }","serveTime":"1508695682733795","impID":"lTjZQtgnOHE-","creativeID":4527082051,"adc":"{\\\"label\\\":\\\"AdChoices\\\",\\\"url\\\":\\\"https:\\\\\/\\\\\/info.yahoo.com\\\\\/privacy\\\\\/us\\\\\/yahoo\\\\\/relevantads.html\\\",\\\"close\\\":\\\"Close\\\",\\\"closeAd\\\":\\\"Close Ad\\\",\\\"showAd\\\":\\\"Show ad\\\",\\\"collapse\\\":\\\"Collapse\\\",\\\"fdb\\\":\\\"I don't like this ad\\\",\\\"code\\\":\\\"en-us\\\"}","is3rd":1,"facStatus":{},"userProvidedData":{},"facRotation":{},"slotData":{"pt":"8","bamt":"10000000000.000000","namt":"0.000000","isLiveAdPreview":"false","is_ad_feedback":"false","trusted_custom":"false","isCompAds":"false","adjf":"1.000000","alpha":"-1.000000","ffrac":"0.909711","pcpm":"-1.000000","fc":"false","sdate":"1473794855","edate":"1561953540","bimpr":99667238912,"pimpr":0,"spltp":0,"frp":"false","pvid":"jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV"},"size":"300x250"}},"conf":{"w":300,"h":250}},{"id":"LREC2","html":"<!-- APT Vendor: Right Media, Format: Standard Graphical -->\n<SCR"+"IPT TYPE=\"text\/javascr"+"ipt\" SRC=\"https:\/\/na.ads.yahoo.com\/yax\/banner?ve=1&tt=1&si=313287051&megamodal=${MEGAMODAL}&bucket=fin-strm-test2,fndmtest,finssl&asz=300x250&u=https:\/\/finance.yahoo.com\/losers&gdAdId=7E3ZQtgnOHE-&gdUuid=jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV&gdSt=1508695682733795&publisher_blob=${RS}\n\tjKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV\n\t1183335883\n\tLREC2\n\t1508695682.34532\n\t3-0-8:ysd:1&pub_redirect=https:\/\/beap-bc.yahoo.com\/yc\/YnY9MS4wLjAmYnM9KDE3am5ncTFvMChnaWQkaktVdW1UWXpMaktsdGZsMldhWVYyd2suTWpBNExnQUFBQUNXUGZyVixzdCQxNTA4Njk1NjgyNzMzNzk1LHNpJDQ0NTEwNTEsc3AkMTE4MzMzNTg4MyxjdCQyNSx5YngkT3BEQ1ozM2IuMTdyTC5QOHoyUnFKUSxsbmckZW4tdXMsY3IkNDUyNzA2ODA1MSx2JDIuMCxhaWQkN0UzWlF0Z25PSEUtLGJpJDIzMTUyMjI1NTEsbW1lJDk3NDk3OTkzMTk2Njk3MTk4MjQsciQwLHlvbyQxLGFncCQzNTM2MDI1MDUxLGFwJExSRUMyKSk\/1\/*&K=1\"><\/SCR"+"IPT><!--313287051 --><scr"+"ipt>var url = \"\"; if(url && url.search(\"http\") != -1){document.write('<scr"+"ipt src=\"' + url + '\"><\\\/scr"+"ipt>');}<\/scr"+"ipt><!--QYZ 2315222551,4527068051,;;LREC2;1183335883;1-->","lowHTML":"","meta":{"y":{"pos":"LREC2","cscHTML":"<scr"+"ipt language=javascr"+"ipt>\nif(window.xzq_d==null)window.xzq_d=new Object();\nwindow.xzq_d['7E3ZQtgnOHE-']='(as$13a3jhabd,aid$7E3ZQtgnOHE-,bi$2315222551,agp$3536025051,cr$4527068051,ct$25,at$H,eob$gd1_match_id=-1:ypos=LREC2)';\n<\/scr"+"ipt><noscr"+"ipt><img width=1 height=1 alt=\"\" src=\"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3&al=(as$13a3jhabd,aid$7E3ZQtgnOHE-,bi$2315222551,agp$3536025051,cr$4527068051,ct$25,at$H,eob$gd1_match_id=-1:ypos=LREC2)\"><\/noscr"+"ipt>","cscURI":"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3&al=(as$13a3jhabd,aid$7E3ZQtgnOHE-,bi$2315222551,agp$3536025051,cr$4527068051,ct$25,at$H,eob$gd1_match_id=-1:ypos=LREC2)","behavior":"non_exp","adID":"9749799319669719824","matchID":"999999.999999.999999.999999","bookID":"2315222551","slotID":"9","serveType":"-1","err":false,"hasExternal":false,"supp_ugc":"0","placementID":"3536025051","fdb":"{ \\\"fdb_url\\\": \\\"https:\\\\\\\/\\\\\\\/beap-bc.yahoo.com\\\\\\\/af\\\\\\\/us?bv=1.0.0&bs=(160ivimhu(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,srv$1,si$4451051,ct$25,exp$1508702882733795,adv$26513753608,li$3535931551,cr$4527068051,v$1.0,pbid$20459933223,seid$313287051))&al=(type${type},cmnt${cmnt},subo${subo})&r=10\\\", \\\"fdb_on\\\": \\\"1\\\", \\\"fdb_exp\\\": \\\"1508702882733\\\", \\\"fdb_intl\\\": \\\"en-US\\\" }","serveTime":"1508695682733795","impID":"7E3ZQtgnOHE-","creativeID":4527068051,"adc":"{\\\"label\\\":\\\"AdChoices\\\",\\\"url\\\":\\\"https:\\\\\/\\\\\/info.yahoo.com\\\\\/privacy\\\\\/us\\\\\/yahoo\\\\\/relevantads.html\\\",\\\"close\\\":\\\"Close\\\",\\\"closeAd\\\":\\\"Close Ad\\\",\\\"showAd\\\":\\\"Show ad\\\",\\\"collapse\\\":\\\"Collapse\\\",\\\"fdb\\\":\\\"I don't like this ad\\\",\\\"code\\\":\\\"en-us\\\"}","is3rd":1,"facStatus":{"fedStatusCode":"0","fedStatusMessage":"federation is not configured for ad slot"},"userProvidedData":{},"facRotation":{},"slotData":{"pt":"8","bamt":"10000000000.000000","namt":"0.000000","isLiveAdPreview":"false","is_ad_feedback":"false","trusted_custom":"false","isCompAds":"false","adjf":"1.000000","alpha":"-1.000000","ffrac":"0.913172","pcpm":"-1.000000","fc":"false","sdate":"1473794852","edate":"1561953540","bimpr":99372466176,"pimpr":0,"spltp":0,"frp":"false","pvid":"jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV"},"size":"300x250"}},"conf":{"w":300,"h":250}},{"id":"FOOT","html":"<!-- SpaceID=1183335883 loc=FOOT noad --><!-- fac-gd2-noad --><!-- gd2-status-2 --><!--QYZ CMS_NONE_AVAIL,,;;FOOT;1183335883;2-->","lowHTML":"","meta":{"y":{"pos":"FOOT","cscHTML":"<scr"+"ipt language=javascr"+"ipt>\nif(window.xzq_d==null)window.xzq_d=new Object();\nwindow.xzq_d['OePYQtgnOHE-']='(as$125ld2h8t,aid$OePYQtgnOHE-,cr$-1,ct$25,at$H,eob$gd1_match_id=-1:ypos=FOOT)';\n<\/scr"+"ipt><noscr"+"ipt><img width=1 height=1 alt=\"\" src=\"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3&al=(as$125ld2h8t,aid$OePYQtgnOHE-,cr$-1,ct$25,at$H,eob$gd1_match_id=-1:ypos=FOOT)\"><\/noscr"+"ipt>","cscURI":"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3&al=(as$125ld2h8t,aid$OePYQtgnOHE-,cr$-1,ct$25,at$H,eob$gd1_match_id=-1:ypos=FOOT)","behavior":"non_exp","adID":"#2","matchID":"#2","bookID":"-1","slotID":"4","serveType":"-1","err":"invalid_space","hasExternal":false,"supp_ugc":"0","placementID":-1,"fdb":"{ \\\"fdb_url\\\": \\\"http:\\\\\/\\\\\/beap-bc.yahoo.com\\\\\/af?bv=1.0.0&bs=(15ir45r6b(gid$jmTVQDk4LjHHbFsHU5jMkgKkMTAuNwAAAACljpkK,st$1402537233026922,srv$1,si$13303551,adv$25941429036,ct$25,li$3239250051,exp$1402544433026922,cr$4154984551,pbid$25372728133,v$1.0))&al=(type${type},cmnt${cmnt},subo${subo})&r=10\\\", \\\"fdb_on\\\": \\\"1\\\", \\\"fdb_exp\\\": \\\"1402544433026\\\", \\\"fdb_intl\\\": \\\"en-us\\\" , \\\"d\\\" : \\\"1\\\" }","serveTime":"1508695682733795","impID":"","creativeID":-1,"adc":"{\\\"label\\\":\\\"AdChoices\\\",\\\"url\\\":\\\"https:\\\\\/\\\\\/info.yahoo.com\\\\\/privacy\\\\\/us\\\\\/yahoo\\\\\/relevantads.html\\\",\\\"close\\\":\\\"Close\\\",\\\"closeAd\\\":\\\"Close Ad\\\",\\\"showAd\\\":\\\"Show ad\\\",\\\"collapse\\\":\\\"Collapse\\\",\\\"fdb\\\":\\\"I don't like this ad\\\",\\\"code\\\":\\\"en-us\\\"}","is3rd":0,"facStatus":{"fedStatusCode":"0","fedStatusMessage":"federation is not configured for ad slot"},"userProvidedData":{},"facRotation":{},"slotData":{"pt":"0","bamt":"10000000000.000000","namt":"0.000000","isLiveAdPreview":"false","is_ad_feedback":"false","trusted_custom":"false","isCompAds":"false","pvid":"jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV"}}}},{"id":"FSRVY","html":"<!-- APT Vendor: Right Media, Format: Standard Graphical -->\n<!-- BEGIN STANDARD TAG - 1 x 1 - APT Run-of Yahoo US O&O Redirects - DO NOT MODIFY -->\n<SCR"+"IPT TYPE=\"text\/javascr"+"ipt\" SRC=\"https:\/\/na.ads.yahoo.com\/yax\/banner?ve=1&tt=1&si=313287051&asz=1x1&u=https:\/\/finance.yahoo.com\/losers&gdAdId=kPjYQtgnOHE-&gdUuid=jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV&gdSt=1508695682733795&publisher_blob=${RS}\n\tjKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV\n\t1183335883\n\tFSRVY\n\t1508695682.35215\n\t3-0-8:ysd:1&pub_redirect=https:\/\/beap-bc.yahoo.com\/yc\/YnY9MS4wLjAmYnM9KDE3ajN2dHNoMihnaWQkaktVdW1UWXpMaktsdGZsMldhWVYyd2suTWpBNExnQUFBQUNXUGZyVixzdCQxNTA4Njk1NjgyNzMzNzk1LHNpJDQ0NTEwNTEsc3AkMTE4MzMzNTg4MyxjdCQyNSx5YngkT3BEQ1ozM2IuMTdyTC5QOHoyUnFKUSxsbmckZW4tdXMsY3IkNDUyODE3NzA1MSx2JDIuMCxhaWQka1BqWVF0Z25PSEUtLGJpJDIzMTU5MzIwNTEsbW1lJDk3NTI1MTU4ODY0ODQ0NDE4NTAsciQwLHlvbyQxLGFncCQzNTM3MDA2NTUxLGFwJEZTUlZZKSk\/1\/*&K=1\"><\/SCR"+"IPT>\n<!-- END TAG --><scr"+"ipt>var url = \"\"; if(url && url.search(\"http\") != -1){document.write('<scr"+"ipt src=\"' + url + '\"><\\\/scr"+"ipt>');}<\/scr"+"ipt><!--QYZ 2315932051,4528177051,;;FSRVY;1183335883;1-->","lowHTML":"","meta":{"y":{"pos":"FSRVY","cscHTML":"<scr"+"ipt language=javascr"+"ipt>\nif(window.xzq_d==null)window.xzq_d=new Object();\nwindow.xzq_d['kPjYQtgnOHE-']='(as$13a6d9lne,aid$kPjYQtgnOHE-,bi$2315932051,agp$3537006551,cr$4528177051,ct$25,at$H,eob$gd1_match_id=-1:ypos=FSRVY)';\n<\/scr"+"ipt><noscr"+"ipt><img width=1 height=1 alt=\"\" src=\"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3&al=(as$13a6d9lne,aid$kPjYQtgnOHE-,bi$2315932051,agp$3537006551,cr$4528177051,ct$25,at$H,eob$gd1_match_id=-1:ypos=FSRVY)\"><\/noscr"+"ipt>","cscURI":"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3&al=(as$13a6d9lne,aid$kPjYQtgnOHE-,bi$2315932051,agp$3537006551,cr$4528177051,ct$25,at$H,eob$gd1_match_id=-1:ypos=FSRVY)","behavior":"non_exp","adID":"9752515886484441850","matchID":"999999.999999.999999.999999","bookID":"2315932051","slotID":"5","serveType":"-1","err":false,"hasExternal":false,"supp_ugc":"0","placementID":"3537006551","fdb":"{ \\\"fdb_url\\\": \\\"https:\\\\\\\/\\\\\\\/beap-bc.yahoo.com\\\\\\\/af\\\\\\\/us?bv=1.0.0&bs=(160pljgha(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,srv$1,si$4451051,ct$25,exp$1508702882733795,adv$26513753608,li$3536867051,cr$4528177051,v$1.0,pbid$20459933223,seid$313287051))&al=(type${type},cmnt${cmnt},subo${subo})&r=10\\\", \\\"fdb_on\\\": \\\"1\\\", \\\"fdb_exp\\\": \\\"1508702882733\\\", \\\"fdb_intl\\\": \\\"en-US\\\" }","serveTime":"1508695682733795","impID":"kPjYQtgnOHE-","creativeID":4528177051,"adc":"{\\\"label\\\":\\\"AdChoices\\\",\\\"url\\\":\\\"https:\\\\\/\\\\\/info.yahoo.com\\\\\/privacy\\\\\/us\\\\\/yahoo\\\\\/relevantads.html\\\",\\\"close\\\":\\\"Close\\\",\\\"closeAd\\\":\\\"Close Ad\\\",\\\"showAd\\\":\\\"Show ad\\\",\\\"collapse\\\":\\\"Collapse\\\",\\\"fdb\\\":\\\"I don't like this ad\\\",\\\"code\\\":\\\"en-us\\\"}","is3rd":1,"facStatus":{"fedStatusCode":"0","fedStatusMessage":"federation is not configured for ad slot"},"userProvidedData":{},"facRotation":{},"slotData":{"pt":"8","bamt":"10000000000.000000","namt":"0.000000","isLiveAdPreview":"false","is_ad_feedback":"false","trusted_custom":"false","isCompAds":"false","adjf":"1.000000","alpha":"-1.000000","ffrac":"1.000000","pcpm":"-1.000000","fc":"false","sdate":"1474408390","edate":"1561953540","bimpr":82733924352,"pimpr":0,"spltp":0,"frp":"false","pvid":"jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV"},"size":"1x1"}},"conf":{"w":1,"h":1}}],"conf":{"useYAC":0,"usePE":1,"servicePath":"","xservicePath":"","beaconPath":"","renderPath":"","allowFiF":false,"srenderPath":"https:\/\/s.yimg.com\/rq\/darla\/3-0-8\/html\/r-sf.html","renderFile":"https:\/\/s.yimg.com\/rq\/darla\/3-0-8\/html\/r-sf.html","sfbrenderPath":"https:\/\/s.yimg.com\/rq\/darla\/3-0-8\/html\/r-sf.html","msgPath":"https:\/\/fc.yahoo.com\/sdarla\/3-0-8\/html\/msg.html","cscPath":"https:\/\/s.yimg.com\/rq\/darla\/3-0-8\/html\/r-csc.html","root":"sdarla","edgeRoot":"https:\/\/s.yimg.com\/rq\/darla\/3-0-8","sedgeRoot":"https:\/\/s.yimg.com\/rq\/darla\/3-0-8","version":"3-0-8","tpbURI":"","hostFile":"https:\/\/s.yimg.com\/rq\/darla\/3-0-8\/js\/g-r-min.js","property":"finance_en-US","fdb_locale":"What don't you like about this ad?\n\tIt's offensive\n\tSomething else\n\tThank you for helping us improve your Yahoo experience\n\tIt's not relevant\n\tIt's distracting\n\tI don't like this ad\n\tSend\n\tDone\n\tWhy do I see ads?\n\tLearn more about your feedback.","positions":{"FB2":{"dest":"destFB2","asz":"120x60","id":"FB2","h":"60","w":"120"},"FB2-1":{"dest":"destFB2-1","asz":"120x60","id":"FB2-1","h":"60","w":"120"},"FB2-2":{"dest":"destFB2-2","asz":"120x60","id":"FB2-2","h":"60","w":"120"},"FB2-3":{"dest":"destFB2-3","asz":"120x60","id":"FB2-3","h":"60","w":"120"},"LDRB":{"dest":"destLDRB","asz":"728x90","id":"LDRB","h":"90","w":"728"},"LDRB2":{"dest":"destLDRB2","asz":"728x90","id":"LDRB2","h":"90","w":"728"},"LREC":{"dest":"destLREC","asz":"300x250","id":"LREC","h":"250","w":"300"},"LREC2":{"dest":"destLREC2","asz":"300x250","id":"LREC2","h":"250","w":"300"},"FOOT":{"dest":"destFOOT","id":"FOOT"},"FSRVY":{"dest":"destFSRVY","id":"FSRVY","w":1,"h":1}},"events":{"DEFAULT":{"ult":{"pg":{"property":"finance_en-US","test":"fin-strm-test2,fndmtest,finssl"}},"clw":{"LREC":{"blocked_by":"MON-1"},"MON-1":{"blocked_by":"LREC"},"MAST":{"blocked_by":"SPL,LDRB"},"LDRB":{"blocked_by":"MAST,SPL"},"SPL":{"blocked_by":"MAST,LDRB"}}}},"lang":"en-US","spaceID":"1183335883","debug":false,"asString":"{\"useYAC\":0,\"usePE\":1,\"servicePath\":\"\",\"xservicePath\":\"\",\"beaconPath\":\"\",\"renderPath\":\"\",\"allowFiF\":false,\"srenderPath\":\"https:\\\/\\\/s.yimg.com\\\/rq\\\/darla\\\/3-0-8\\\/html\\\/r-sf.html\",\"renderFile\":\"https:\\\/\\\/s.yimg.com\\\/rq\\\/darla\\\/3-0-8\\\/html\\\/r-sf.html\",\"sfbrenderPath\":\"https:\\\/\\\/s.yimg.com\\\/rq\\\/darla\\\/3-0-8\\\/html\\\/r-sf.html\",\"msgPath\":\"https:\\\/\\\/fc.yahoo.com\\\/sdarla\\\/3-0-8\\\/html\\\/msg.html\",\"cscPath\":\"https:\\\/\\\/s.yimg.com\\\/rq\\\/darla\\\/3-0-8\\\/html\\\/r-csc.html\",\"root\":\"sdarla\",\"edgeRoot\":\"https:\\\/\\\/s.yimg.com\\\/rq\\\/darla\\\/3-0-8\",\"sedgeRoot\":\"https:\\\/\\\/s.yimg.com\\\/rq\\\/darla\\\/3-0-8\",\"version\":\"3-0-8\",\"tpbURI\":\"\",\"hostFile\":\"https:\\\/\\\/s.yimg.com\\\/rq\\\/darla\\\/3-0-8\\\/js\\\/g-r-min.js\",\"property\":\"finance_en-US\",\"fdb_locale\":\"What don't you like about this ad?\n\tIt's offensive\n\tSomething else\n\tThank you for helping us improve your Yahoo experience\n\tIt's not relevant\n\tIt's distracting\n\tI don't like this ad\n\tSend\n\tDone\n\tWhy do I see ads?\n\tLearn more about your feedback.\",\"positions\":{\"FB2\":{\"dest\":\"destFB2\",\"asz\":\"120x60\",\"id\":\"FB2\",\"h\":\"60\",\"w\":\"120\"},\"FB2-1\":{\"dest\":\"destFB2-1\",\"asz\":\"120x60\",\"id\":\"FB2-1\",\"h\":\"60\",\"w\":\"120\"},\"FB2-2\":{\"dest\":\"destFB2-2\",\"asz\":\"120x60\",\"id\":\"FB2-2\",\"h\":\"60\",\"w\":\"120\"},\"FB2-3\":{\"dest\":\"destFB2-3\",\"asz\":\"120x60\",\"id\":\"FB2-3\",\"h\":\"60\",\"w\":\"120\"},\"LDRB\":{\"dest\":\"destLDRB\",\"asz\":\"728x90\",\"id\":\"LDRB\",\"h\":\"90\",\"w\":\"728\"},\"LDRB2\":{\"dest\":\"destLDRB2\",\"asz\":\"728x90\",\"id\":\"LDRB2\",\"h\":\"90\",\"w\":\"728\"},\"LREC\":{\"dest\":\"destLREC\",\"asz\":\"300x250\",\"id\":\"LREC\",\"h\":\"250\",\"w\":\"300\"},\"LREC2\":{\"dest\":\"destLREC2\",\"asz\":\"300x250\",\"id\":\"LREC2\",\"h\":\"250\",\"w\":\"300\"},\"FOOT\":{\"dest\":\"destFOOT\",\"id\":\"FOOT\"},\"FSRVY\":{\"dest\":\"destFSRVY\",\"id\":\"FSRVY\",\"w\":1,\"h\":1}},\"events\":{\"DEFAULT\":{\"ult\":{\"pg\":{\"property\":\"finance_en-US\",\"test\":\"fin-strm-test2,fndmtest,finssl\"}},\"clw\":{\"LREC\":{\"blocked_by\":\"MON-1\"},\"MON-1\":{\"blocked_by\":\"LREC\"},\"MAST\":{\"blocked_by\":\"SPL,LDRB\"},\"LDRB\":{\"blocked_by\":\"MAST,SPL\"},\"SPL\":{\"blocked_by\":\"MAST,LDRB\"}}}},\"lang\":\"en-US\",\"spaceID\":\"1183335883\",\"debug\":false}"},"meta":{"y":{"pageEndHTML":"<scr"+"ipt language=javascr"+"ipt>\n(function(){window.xzq_p=function(R){M=R};window.xzq_svr=function(R){J=R};function F(S){var T=document;if(T.xzq_i==null){T.xzq_i=new Array();T.xzq_i.c=0}var R=T.xzq_i;R[++R.c]=new Image();R[R.c].src=S}window.xzq_sr=function(){var S=window;var Y=S.xzq_d;if(Y==null){return }if(J==null){return }var T=J+M;if(T.length>P){C();return }var X=\"\";var U=0;var W=Math.random();var V=(Y.hasOwnProperty!=null);var R;for(R in Y){if(typeof Y[R]==\"string\"){if(V&&!Y.hasOwnProperty(R)){continue}if(T.length+X.length+Y[R].length<=P){X+=Y[R]}else{if(T.length+Y[R].length>P){}else{U++;N(T,X,U,W);X=Y[R]}}}}if(U){U++}N(T,X,U,W);C()};function N(R,U,S,T){if(U.length>0){R+=\"&al=\"}F(R+U+\"&s=\"+S+\"&r=\"+T)}function C(){window.xzq_d=null;M=null;J=null}function K(R){xzq_sr()}function B(R){xzq_sr()}function L(U,V,W){if(W){var R=W.toString();var T=U;var Y=R.match(new RegExp(\"\\\\\\\\(([^\\\\\\\\)]*)\\\\\\\\)\"));Y=(Y[1].length>0?Y[1]:\"e\");T=T.replace(new RegExp(\"\\\\\\\\([^\\\\\\\\)]*\\\\\\\\)\",\"g\"),\"(\"+Y+\")\");if(R.indexOf(T)<0){var X=R.indexOf(\"{\");if(X>0){R=R.substring(X,R.length)}else{return W}R=R.replace(new RegExp(\"([^a-zA-Z0-9$_])this([^a-zA-Z0-9$_])\",\"g\"),\"$1xzq_this$2\");var Z=T+\";var rv = f( \"+Y+\",this);\";var S=\"{var a0 = '\"+Y+\"';var ofb = '\"+escape(R)+\"' ;var f = new Function( a0, 'xzq_this', unescape(ofb));\"+Z+\"return rv;}\";return new Function(Y,S)}else{return W}}return V}window.xzq_eh=function(){if(E\n\tI){this.onload=L(\"xzq_onload(e)\",K,this.onload,0);if(E&&typeof (this.onbeforeunload)!=O){this.onbeforeunload=L(\"xzq_dobeforeunload(e)\",B,this.onbeforeunload,0)}}};window.xzq_s=function(){setTimeout(\"xzq_sr()\",1)};var J=null;var M=null;var Q=navigator.appName;var H=navigator.appVersion;var G=navigator.userAgent;var A=parseInt(H);var D=Q.indexOf(\"Microsoft\");var E=D!=-1&&A>=4;var I=(Q.indexOf(\"Netscape\")!=-1\n\tQ.indexOf(\"Opera\")!=-1)&&A>=4;var O=\"undefined\";var P=2000})();\n<\/scr"+"ipt><scr"+"ipt language=javascr"+"ipt>\nif(window.xzq_svr)xzq_svr('https:\/\/beap-bc.yahoo.com\/');\nif(window.xzq_p)xzq_p('yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3');\nif(window.xzq_s)xzq_s();\n<\/scr"+"ipt><noscr"+"ipt><img width=1 height=1 alt=\"\" src=\"https:\/\/beap-bc.yahoo.com\/yi?bv=1.0.0&bs=(1367ru8vo(gid$jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV,st$1508695682733795,si$4451051,sp$1183335883,pv$1,v$2.0))&t=J_3-D_3\"><\/noscr"+"ipt><scr"+"ipt>(function(c){var d=\"https:\/\/\",a=c&&c.JSON,e=\"ypcdb\",g=document,b;function j(n,q,p,o){var m,r;try{m=new Date();m.setTime(m.getTime()+o*1000);g.cookie=[n,\"=\",encodeURIComponent(q),\"; domain=\",p,\"; path=\/; max-age=\",o,\"; expires=\",m.toUTCString()].join(\"\")}catch(r){}}function k(m){return function(){i(m)}}function i(n){var m,o;try{m=new Image();m.onerror=m.onload=function(){m.onerror=m.onload=null;m=null};m.src=n}catch(o){}}function f(o){var p=\"\",n,s,r,q;if(o){try{n=o.match(\/^https?:\\\/\\\/([^\\\/\\?]*)(yahoo\\.com\n\tyimg\\.com\n\tflickr\\.com\n\tyahoo\\.net\n\trivals\\.com)(:\\d+)?([\\\/\\?]\n\t$)\/);if(n&&n[2]){p=n[2]}n=(n&&n[1])\n\tnull;s=n?n.length-1:-1;r=n&&s>=0?n[s]:null;if(r&&r!=\".\"&&r!=\"\/\"){p=\"\"}}catch(q){p=\"\"}}return p}function l(B,n,q,m,p){var u,s,t,A,r,F,z,E,C,y,o,D,x,v=1000,w=v;try{b=location}catch(z){b=null}try{if(a){C=a.parse(p)}else{y=new Function(\"return \"+p);C=y()}}catch(z){C=null}if(y){y=null}try{s=b.hostname;t=b.protocol;if(t){t+=\"\/\/\"}}catch(z){s=t=\"\"}if(!s){try{A=g.URL\n\tb.href\n\t\"\";r=A.match(\/^((http[s]?)\\:[\\\/]+)?([^:\\\/\\s]+\n\t[\\:\\dabcdef\\.]+)\/i);if(r&&r[1]&&r[3]){t=r[1]\n\t\"\";s=r[3]\n\t\"\"}}catch(z){t=s=\"\"}}if(!s\n\t!C\n\t!t\n\t!q){return}A=g.URL\n\tb.href\n\t\"\";E=f(A);if(!E\n\tg.cookie.indexOf(\"ypcdb=\"+n)>-1){return}if(t===d){q=m}u=0;while(F=q[u++]){o=F.lastIndexOf(\"=\");if(o!=-1){D=F.substr(1+o);x=C[D];if(x){setTimeout(k(t+F+x),w);w+=v}}}u=0;while(F=B[u++]){setTimeout(k(t+F),w);w+=v}setTimeout(function(){j(e,n,E,86400)},w)}function h(){l(['ads.yahoo.com\/get-user-id?ver=2&s=800000008&type=redirect&ts=1508695682&sig=7b954ccf177649f4'],'972e86848cadfa53f7c264e0fedd1ad8',['csync.flickr.com\/csync?ver=2.1','csync.yahooapis.com\/csync?ver=2.1'],['csync.flickr.com\/csync?ver=2.1','csync.yahooapis.com\/csync?ver=2.1'],'{\"2.1\":\"&id=23351&value=noqscrcpdp5re%26o%3d4%26q%3dWGYjPxkcLRWK5owhtaEoR8Z.ElN-%26f%3do3%26v%3dPQu.Rz3zpnVQMknu5OMS&optout=h%3d1&timeout=1508695682&sig=13j7lt01n\"}')}if(c.addEventListener){c.addEventListener(\"load\",h,false)}else{if(c.attachEvent){c.attachEvent(\"onload\",h)}else{c.onload=h}}})(window);\n<\/scr"+"ipt>","pos_list":["FB2","FB2-1","FB2-2","FB2-3","LDRB","LDRB2","LREC","LREC2","FOOT","FSRVY"],"transID":"darla_prefetch_1508695682732_258389139_3","k2_uri":"","fac_rt":"63294","spaceID":"1183335883","lookupTime":266,"procTime":281,"npv":0,"pvid":"jKUumTYzLjKltfl2WaYV2wk.MjA4LgAAAACWPfrV","serveTime":"1508695682733795","ep":{"site-attribute":" Y-BUCKET=fin-strm-test2,fndmtest,finssl","tgt":"_blank","secure":true,"ref":"https:\/\/finance.yahoo.com\/losers","ult":{"pg":{"property":"finance_en-US","test":"fin-strm-test2,fndmtest,finssl"}},"clw":{"LREC":{"blocked_by":"MON-1"},"MON-1":{"blocked_by":"LREC"},"MAST":{"blocked_by":"SPL,LDRB"},"LDRB":{"blocked_by":"MAST,SPL"},"SPL":{"blocked_by":"MAST,LDRB"}},"lang":"en-US","filter":"no_expandable;exp_iframe_expandable;","darlaID":"darla_instance_1508695682732_788894027_2"},"pym":{".":"v0.0.9;;-;"},"host":"","filtered":[],"pe":"CWZ1bmN0aW9uIGRwZWQoKSB7IAoJaWYod2luZG93Lnh6cV9kPT1udWxsKXdpbmRvdy54enFfZD1uZXcgT2JqZWN0KCk7CndpbmRvdy54enFfZFsnM1kzWVF0Z25PSEUtJ109JyhhcyQxM2F0Zm9iNGIsYWlkJDNZM1lRdGduT0hFLSxiaSQyMzQxOTg2MDUxLGFncCQzNTc1MDY2NTUxLGNyJDQ2MjE0MzEwNTEsY3QkMjUsYXQkSCxlb2IkZ2QxX21hdGNoX2lkPS0xOnlwb3M9RkIyKSc7CglpZih3aW5kb3cueHpxX2Q9PW51bGwpd2luZG93Lnh6cV9kPW5ldyBPYmplY3QoKTsKd2luZG93Lnh6cV9kWydOS1BZUXRnbk9IRS0nXT0nKGFzJDEzYWF1c3FuYyxhaWQkTktQWVF0Z25PSEUtLGJpJDIzNDI3MTQ1NTEsYWdwJDM1NzY0MjkwNTEsY3IkNDYyNjY5NjA1MSxjdCQyNSxhdCRILGVvYiRnZDFfbWF0Y2hfaWQ9LTE6eXBvcz1GQjIpJzsKCWlmKHdpbmRvdy54enFfZD09bnVsbCl3aW5kb3cueHpxX2Q9bmV3IE9iamVjdCgpOwp3aW5kb3cueHpxX2RbJ2k3allRdGduT0hFLSddPScoYXMkMTNhNWtidjRmLGFpZCRpN2pZUXRnbk9IRS0sYmkkMjM0MjA1NDA1MSxhZ3AkMzU3NTE4NzA1MSxjciQ0NjI5MTc2NTUxLGN0JDI1LGF0JEgsZW9iJGdkMV9tYXRjaF9pZD0tMTp5cG9zPUZCMiknOwoJaWYod2luZG93Lnh6cV9kPT1udWxsKXdpbmRvdy54enFfZD1uZXcgT2JqZWN0KCk7CndpbmRvdy54enFfZFsnNHMzWVF0Z25PSEUtJ109JyhhcyQxM2FxNW1sczIsYWlkJDRzM1lRdGduT0hFLSxiaSQyMzQyMjk3NTUxLGFncCQzNTc1NjUwMDUxLGNyJDQ2MjQxOTI1NTEsY3QkMjUsYXQkSCxlb2IkZ2QxX21hdGNoX2lkPS0xOnlwb3M9RkIyKSc7CglpZih3aW5kb3cueHpxX2Q9PW51bGwpd2luZG93Lnh6cV9kPW5ldyBPYmplY3QoKTsKd2luZG93Lnh6cV9kWyc1dzNaUXRnbk9IRS0nXT0nKGFzJDEzYWxla2xkZixhaWQkNXczWlF0Z25PSEUtLGJpJDIzMzU2MDI1NTEsYWdwJDM1NjQ0MTIwNTEsY3IkNDYxODMwNTU1MSxjdCQyNSxhdCRILGVvYiRnZDFfbWF0Y2hfaWQ9LTE6eXBvcz1MRFJCKSc7CglpZih3aW5kb3cueHpxX2Q9PW51bGwpd2luZG93Lnh6cV9kPW5ldyBPYmplY3QoKTsKd2luZG93Lnh6cV9kWydQaVBaUXRnbk9IRS0nXT0nKGFzJDEzYW1hbjcwayxhaWQkUGlQWlF0Z25PSEUtLGJpJDIzMTUyMjIwNTEsYWdwJDM1MzYwMjU1NTEsY3IkNDUyNzA2ODU1MSxjdCQyNSxhdCRILGVvYiRnZDFfbWF0Y2hfaWQ9LTE6eXBvcz1MRFJCMiknOwoJaWYod2luZG93Lnh6cV9kPT1udWxsKXdpbmRvdy54enFfZD1uZXcgT2JqZWN0KCk7d2luZG93Lnh6cV9kWydsVGpaUXRnbk9IRS0nXT0nKGFzJDEyNTY2cGlyNCxhaWQkbFRqWlF0Z25PSEUtLGNyJC0xLGN0JDI1LGF0JEgsZW9iJGZhYzJfcj0xOmdkMV9tYXRjaF9pZD0tMTp5cG9zPUxSRUMpJzsKCWlmKHdpbmRvdy54enFfZD09bnVsbCl3aW5kb3cueHpxX2Q9bmV3IE9iamVjdCgpOwp3aW5kb3cueHpxX2RbJzdFM1pRdGduT0hFLSddPScoYXMkMTNhM2poYWJkLGFpZCQ3RTNaUXRnbk9IRS0sYmkkMjMxNTIyMjU1MSxhZ3AkMzUzNjAyNTA1MSxjciQ0NTI3MDY4MDUxLGN0JDI1LGF0JEgsZW9iJGdkMV9tYXRjaF9pZD0tMTp5cG9zPUxSRUMyKSc7CglpZih3aW5kb3cueHpxX2Q9PW51bGwpd2luZG93Lnh6cV9kPW5ldyBPYmplY3QoKTsKd2luZG93Lnh6cV9kWydPZVBZUXRnbk9IRS0nXT0nKGFzJDEyNWxkMmg4dCxhaWQkT2VQWVF0Z25PSEUtLGNyJC0xLGN0JDI1LGF0JEgsZW9iJGdkMV9tYXRjaF9pZD0tMTp5cG9zPUZPT1QpJztpZih3aW5kb3cueHpxX2Q9PW51bGwpd2luZG93Lnh6cV9kPW5ldyBPYmplY3QoKTsKd2luZG93Lnh6cV9kWydrUGpZUXRnbk9IRS0nXT0nKGFzJDEzYTZkOWxuZSxhaWQka1BqWVF0Z25PSEUtLGJpJDIzMTU5MzIwNTEsYWdwJDM1MzcwMDY1NTEsY3IkNDUyODE3NzA1MSxjdCQyNSxhdCRILGVvYiRnZDFfbWF0Y2hfaWQ9LTE6eXBvcz1GU1JWWSknOwoJCSB9OwpkcGVkLnRyYW5zSUQgPSAiZGFybGFfcHJlZmV0Y2hfMTUwODY5NTY4MjczMl8yNTgzODkxMzlfMyI7CgoJZnVuY3Rpb24gZHBlcigpIHsgCgkKaWYod2luZG93Lnh6cV9zdnIpeHpxX3N2cignaHR0cHM6Ly9iZWFwLWJjLnlhaG9vLmNvbS8nKTsKaWYod2luZG93Lnh6cV9wKXh6cV9wKCd5aT9idj0xLjAuMCZicz0oMTM2N3J1OHZvKGdpZCRqS1V1bVRZekxqS2x0ZmwyV2FZVjJ3ay5NakE0TGdBQUFBQ1dQZnJWLHN0JDE1MDg2OTU2ODI3MzM3OTUsc2kkNDQ1MTA1MSxzcCQxMTgzMzM1ODgzLHB2JDEsdiQyLjApKSZ0PUpfMy1EXzMnKTsKaWYod2luZG93Lnh6cV9zKXh6cV9zKCk7CgoKCShmdW5jdGlvbihjKXt2YXIgZD0iaHR0cHM6Ly8iLGE9YyYmYy5KU09OLGU9InlwY2RiIixnPWRvY3VtZW50LGI7ZnVuY3Rpb24gaihuLHEscCxvKXt2YXIgbSxyO3RyeXttPW5ldyBEYXRlKCk7bS5zZXRUaW1lKG0uZ2V0VGltZSgpK28qMTAwMCk7Zy5jb29raWU9W24sIj0iLGVuY29kZVVSSUNvbXBvbmVudChxKSwiOyBkb21haW49IixwLCI7IHBhdGg9LzsgbWF4LWFnZT0iLG8sIjsgZXhwaXJlcz0iLG0udG9VVENTdHJpbmcoKV0uam9pbigiIil9Y2F0Y2gocil7fX1mdW5jdGlvbiBrKG0pe3JldHVybiBmdW5jdGlvbigpe2kobSl9fWZ1bmN0aW9uIGkobil7dmFyIG0sbzt0cnl7bT1uZXcgSW1hZ2UoKTttLm9uZXJyb3I9bS5vbmxvYWQ9ZnVuY3Rpb24oKXttLm9uZXJyb3I9bS5vbmxvYWQ9bnVsbDttPW51bGx9O20uc3JjPW59Y2F0Y2gobyl7fX1mdW5jdGlvbiBmKG8pe3ZhciBwPSIiLG4scyxyLHE7aWYobyl7dHJ5e249by5tYXRjaCgvXmh0dHBzPzpcL1wvKFteXC9cP10qKSh5YWhvb1wuY29tfHlpbWdcLmNvbXxmbGlja3JcLmNvbXx5YWhvb1wubmV0fHJpdmFsc1wuY29tKSg6XGQrKT8oW1wvXD9dfCQpLyk7aWYobiYmblsyXSl7cD1uWzJdfW49KG4mJm5bMV0pfHxudWxsO3M9bj9uLmxlbmd0aC0xOi0xO3I9biYmcz49MD9uW3NdOm51bGw7aWYociYmciE9Ii4iJiZyIT0iLyIpe3A9IiJ9fWNhdGNoKHEpe3A9IiJ9fXJldHVybiBwfWZ1bmN0aW9uIGwoQixuLHEsbSxwKXt2YXIgdSxzLHQsQSxyLEYseixFLEMseSxvLEQseCx2PTEwMDAsdz12O3RyeXtiPWxvY2F0aW9ufWNhdGNoKHope2I9bnVsbH10cnl7aWYoYSl7Qz1hLnBhcnNlKHApfWVsc2V7eT1uZXcgRnVuY3Rpb24oInJldHVybiAiK3ApO0M9eSgpfX1jYXRjaCh6KXtDPW51bGx9aWYoeSl7eT1udWxsfXRyeXtzPWIuaG9zdG5hbWU7dD1iLnByb3RvY29sO2lmKHQpe3QrPSIvLyJ9fWNhdGNoKHope3M9dD0iIn1pZighcyl7dHJ5e0E9Zy5VUkx8fGIuaHJlZnx8IiI7cj1BLm1hdGNoKC9eKChodHRwW3NdPylcOltcL10rKT8oW146XC9cc10rfFtcOlxkYWJjZGVmXC5dKykvaSk7aWYociYmclsxXSYmclszXSl7dD1yWzFdfHwiIjtzPXJbM118fCIifX1jYXRjaCh6KXt0PXM9IiJ9fWlmKCFzfHwhQ3x8IXR8fCFxKXtyZXR1cm59QT1nLlVSTHx8Yi5ocmVmfHwiIjtFPWYoQSk7aWYoIUV8fGcuY29va2llLmluZGV4T2YoInlwY2RiPSIrbik+LTEpe3JldHVybn1pZih0PT09ZCl7cT1tfXU9MDt3aGlsZShGPXFbdSsrXSl7bz1GLmxhc3RJbmRleE9mKCI9Iik7aWYobyE9LTEpe0Q9Ri5zdWJzdHIoMStvKTt4PUNbRF07aWYoeCl7c2V0VGltZW91dChrKHQrRit4KSx3KTt3Kz12fX19dT0wO3doaWxlKEY9Qlt1KytdKXtzZXRUaW1lb3V0KGsodCtGKSx3KTt3Kz12fXNldFRpbWVvdXQoZnVuY3Rpb24oKXtqKGUsbixFLDg2NDAwKX0sdyl9ZnVuY3Rpb24gaCgpe2woWydhZHMueWFob28uY29tL2dldC11c2VyLWlkP3Zlcj0yJnM9ODAwMDAwMDA4JnR5cGU9cmVkaXJlY3QmdHM9MTUwODY5NTY4MiZzaWc9N2I5NTRjY2YxNzc2NDlmNCddLCc5NzJlODY4NDhjYWRmYTUzZjdjMjY0ZTBmZWRkMWFkOCcsWydjc3luYy5mbGlja3IuY29tL2NzeW5jP3Zlcj0yLjEnLCdjc3luYy55YWhvb2FwaXMuY29tL2NzeW5jP3Zlcj0yLjEnXSxbJ2NzeW5jLmZsaWNrci5jb20vY3N5bmM\/dmVyPTIuMScsJ2NzeW5jLnlhaG9vYXBpcy5jb20vY3N5bmM\/dmVyPTIuMSddLCd7IjIuMSI6IiZpZD0yMzM1MSZ2YWx1ZT1ub3FzY3JjcGRwNXJlJTI2byUzZDQlMjZxJTNkV0dZalB4a2NMUldLNW93aHRhRW9SOFouRWxOLSUyNmYlM2RvMyUyNnYlM2RQUXUuUnozenBuVlFNa251NU9NUyZvcHRvdXQ9aCUzZDEmdGltZW91dD0xNTA4Njk1NjgyJnNpZz0xM2o3bHQwMW4ifScpfWlmKGMuYWRkRXZlbnRMaXN0ZW5lcil7Yy5hZGRFdmVudExpc3RlbmVyKCJsb2FkIixoLGZhbHNlKX1lbHNle2lmKGMuYXR0YWNoRXZlbnQpe2MuYXR0YWNoRXZlbnQoIm9ubG9hZCIsaCl9ZWxzZXtjLm9ubG9hZD1ofX19KSh3aW5kb3cpOwoKCgkKIH07CmRwZXIudHJhbnNJRCA9ImRhcmxhX3ByZWZldGNoXzE1MDg2OTU2ODI3MzJfMjU4Mzg5MTM5XzMiOwoK"}}}</script>
         <meta itemprop="metadata/x-safeframe" content="eyJwb3NpdGlvbnMiOlt7ImlkIjoiRkIyIiwibG93SFRNTCI6IiIsIm1ldGEiOnsieSI6eyJwb3MiOiJGQjIiLCJiZWhhdmlvciI6Im5vbl9leHAiLCJhZElEIjoiOTg0OTYxMDA2NDY2MTY0ODE5NSIsIm1hdGNoSUQiOiI5OTk5OTkuOTk5OTk5Ljk5OTk5OS45OTk5OTkiLCJib29rSUQiOiIyMzQxOTg2MDUxIiwic2xvdElEIjoiMCIsInNlcnZlVHlwZSI6Ii0xIiwiZXJyIjpmYWxzZSwiaGFzRXh0ZXJuYWwiOmZhbHNlLCJzdXBwX3VnYyI6IiIsInBsYWNlbWVudElEIjoiMzU3NTA2NjU1MSIsImZkYiI6InsgXFxcImZkYl91cmxcXFwiOiBcXFwiaHR0cHM6XFxcXFxcXC9cXFxcXFxcL2JlYXAtYmMueWFob28uY29tXFxcXFxcXC9hZlxcXFxcXFwvdXM/YnY9MS4wLjAmYnM9KDE2MDJya2tmYyhnaWQkaktVdW1UWXpMaktsdGZsMldhWVYyd2suTWpBNExnQUFBQUNXUGZyVixzdCQxNTA4Njk1NjgyNzMzNzk1LHNydiQxLHNpJDQ0NTEwNTEsY3QkMjUsZXhwJDE1MDg3MDI4ODI3MzM3OTUsYWR2JDIzOTk0MTAwMzQzLGxpJDM1NzU5MjkwNTEsY3IkNDYyMTQzMTA1MSx2JDEuMCxwYmlkJDIwNDU5OTMzMjIzLHNlaWQkMzEzMjg3MDUxKSkmYWw9KHR5cGUke3R5cGV9LGNtbnQke2NtbnR9LHN1Ym8ke3N1Ym99KSZyPTEwXFxcIiwgXFxcImZkYl9vblxcXCI6IFxcXCIxXFxcIiwgXFxcImZkYl9leHBcXFwiOiBcXFwiMTUwODcwMjg4MjczM1xcXCIsIFxcXCJmZGJfaW50bFxcXCI6IFxcXCJlbi1VU1xcXCIgfSIsInNlcnZlVGltZSI6IjE1MDg2OTU2ODI3MzM3OTUiLCJpbXBJRCI6IjNZM1lRdGduT0hFLSIsImNyZWF0aXZlSUQiOjQ2MjE0MzEwNTEsImFkYyI6IntcXFwibGFiZWxcXFwiOlxcXCJBZENob2ljZXNcXFwiLFxcXCJ1cmxcXFwiOlxcXCJodHRwczpcXFxcXC9cXFxcXC9pbmZvLnlhaG9vLmNvbVxcXFxcL3ByaXZhY3lcXFxcXC91c1xcXFxcL3lhaG9vXFxcXFwvcmVsZXZhbnRhZHMuaHRtbFxcXCIsXFxcImNsb3NlXFxcIjpcXFwiQ2xvc2VcXFwiLFxcXCJjbG9zZUFkXFxcIjpcXFwiQ2xvc2UgQWRcXFwiLFxcXCJzaG93QWRcXFwiOlxcXCJTaG93IGFkXFxcIixcXFwiY29sbGFwc2VcXFwiOlxcXCJDb2xsYXBzZVxcXCIsXFxcImZkYlxcXCI6XFxcIkkgZG9uJ3QgbGlrZSB0aGlzIGFkXFxcIixcXFwiY29kZVxcXCI6XFxcImVuLXVzXFxcIn0iLCJpczNyZCI6MCwiZmFjU3RhdHVzIjp7fSwidXNlclByb3ZpZGVkRGF0YSI6e30sImZhY1JvdGF0aW9uIjp7fSwic2xvdERhdGEiOnt9LCJzaXplIjoiMTIweDYwIn19LCJjb25mIjp7InciOjEyMCwiaCI6NjB9fSx7ImlkIjoiRkIyLTEiLCJsb3dIVE1MIjoiIiwibWV0YSI6eyJ5Ijp7InBvcyI6IkZCMi0xIiwiYmVoYXZpb3IiOiJub25fZXhwIiwiYWRJRCI6Ijk4NTE5ODMwMzQwOTI2ODkzNDYiLCJtYXRjaElEIjoiOTk5OTk5Ljk5OTk5OS45OTk5OTkuOTk5OTk5IiwiYm9va0lEIjoiMjM0MjcxNDU1MSIsInNsb3RJRCI6IjEiLCJzZXJ2ZVR5cGUiOiItMSIsImVyciI6ZmFsc2UsImhhc0V4dGVybmFsIjpmYWxzZSwic3VwcF91Z2MiOiIiLCJwbGFjZW1lbnRJRCI6IjM1NzY0MjkwNTEiLCJmZGIiOiJ7IFxcXCJmZGJfdXJsXFxcIjogXFxcImh0dHBzOlxcXFxcXFwvXFxcXFxcXC9iZWFwLWJjLnlhaG9vLmNvbVxcXFxcXFwvYWZcXFxcXFxcL3VzP2J2PTEuMC4wJmJzPSgxNjA5bWtta2coZ2lkJGpLVXVtVFl6TGpLbHRmbDJXYVlWMndrLk1qQTRMZ0FBQUFDV1BmclYsc3QkMTUwODY5NTY4MjczMzc5NSxzcnYkMSxzaSQ0NDUxMDUxLGN0JDI1LGV4cCQxNTA4NzAyODgyNzMzNzk1LGFkdiQyMTA2MzM4NTkxMyxsaSQzNTc3MzQ4MDUxLGNyJDQ2MjY2OTYwNTEsdiQxLjAscGJpZCQyMDQ1OTkzMzIyMyxzZWlkJDMxMzI4NzA1MSkpJmFsPSh0eXBlJHt0eXBlfSxjbW50JHtjbW50fSxzdWJvJHtzdWJvfSkmcj0xMFxcXCIsIFxcXCJmZGJfb25cXFwiOiBcXFwiMVxcXCIsIFxcXCJmZGJfZXhwXFxcIjogXFxcIjE1MDg3MDI4ODI3MzNcXFwiLCBcXFwiZmRiX2ludGxcXFwiOiBcXFwiZW4tVVNcXFwiIH0iLCJzZXJ2ZVRpbWUiOiIxNTA4Njk1NjgyNzMzNzk1IiwiaW1wSUQiOiJOS1BZUXRnbk9IRS0iLCJjcmVhdGl2ZUlEIjo0NjI2Njk2MDUxLCJhZGMiOiJ7XFxcImxhYmVsXFxcIjpcXFwiQWRDaG9pY2VzXFxcIixcXFwidXJsXFxcIjpcXFwiaHR0cHM6XFxcXFwvXFxcXFwvaW5mby55YWhvby5jb21cXFxcXC9wcml2YWN5XFxcXFwvdXNcXFxcXC95YWhvb1xcXFxcL3JlbGV2YW50YWRzLmh0bWxcXFwiLFxcXCJjbG9zZVxcXCI6XFxcIkNsb3NlXFxcIixcXFwiY2xvc2VBZFxcXCI6XFxcIkNsb3NlIEFkXFxcIixcXFwic2hvd0FkXFxcIjpcXFwiU2hvdyBhZFxcXCIsXFxcImNvbGxhcHNlXFxcIjpcXFwiQ29sbGFwc2VcXFwiLFxcXCJmZGJcXFwiOlxcXCJJIGRvbid0IGxpa2UgdGhpcyBhZFxcXCIsXFxcImNvZGVcXFwiOlxcXCJlbi11c1xcXCJ9IiwiaXMzcmQiOjAsImZhY1N0YXR1cyI6e30sInVzZXJQcm92aWRlZERhdGEiOnt9LCJmYWNSb3RhdGlvbiI6e30sInNsb3REYXRhIjp7fSwic2l6ZSI6IjEyMHg2MCJ9fSwiY29uZiI6eyJ3IjoxMjAsImgiOjYwfX0seyJpZCI6IkZCMi0yIiwibG93SFRNTCI6IiIsIm1ldGEiOnsieSI6eyJwb3MiOiJGQjItMiIsImJlaGF2aW9yIjoibm9uX2V4cCIsImFkSUQiOiI5ODQ5ODkzNTMyNTAzMTg0ODcwIiwibWF0Y2hJRCI6Ijk5OTk5OS45OTk5OTkuOTk5OTk5Ljk5OTk5OSIsImJvb2tJRCI6IjIzNDIwNTQwNTEiLCJzbG90SUQiOiIyIiwic2VydmVUeXBlIjoiLTEiLCJlcnIiOmZhbHNlLCJoYXNFeHRlcm5hbCI6ZmFsc2UsInN1cHBfdWdjIjoiIiwicGxhY2VtZW50SUQiOiIzNTc1MTg3MDUxIiwiZmRiIjoieyBcXFwiZmRiX3VybFxcXCI6IFxcXCJodHRwczpcXFxcXFxcL1xcXFxcXFwvYmVhcC1iYy55YWhvby5jb21cXFxcXFxcL2FmXFxcXFxcXC91cz9idj0xLjAuMCZicz0oMTYwaXQzajdiKGdpZCRqS1V1bVRZekxqS2x0ZmwyV2FZVjJ3ay5NakE0TGdBQUFBQ1dQZnJWLHN0JDE1MDg2OTU2ODI3MzM3OTUsc3J2JDEsc2kkNDQ1MTA1MSxjdCQyNSxleHAkMTUwODcwMjg4MjczMzc5NSxhZHYkMjI5Nzg3ODcxOTUsbGkkMzU3NjA4NzU1MSxjciQ0NjI5MTc2NTUxLHYkMS4wLHBiaWQkMjA0NTk5MzMyMjMsc2VpZCQzMTMyODcwNTEpKSZhbD0odHlwZSR7dHlwZX0sY21udCR7Y21udH0sc3VibyR7c3Vib30pJnI9MTBcXFwiLCBcXFwiZmRiX29uXFxcIjogXFxcIjFcXFwiLCBcXFwiZmRiX2V4cFxcXCI6IFxcXCIxNTA4NzAyODgyNzMzXFxcIiwgXFxcImZkYl9pbnRsXFxcIjogXFxcImVuLVVTXFxcIiB9Iiwic2VydmVUaW1lIjoiMTUwODY5NTY4MjczMzc5NSIsImltcElEIjoiaTdqWVF0Z25PSEUtIiwiY3JlYXRpdmVJRCI6NDYyOTE3NjU1MSwiYWRjIjoie1xcXCJsYWJlbFxcXCI6XFxcIkFkQ2hvaWNlc1xcXCIsXFxcInVybFxcXCI6XFxcImh0dHBzOlxcXFxcL1xcXFxcL2luZm8ueWFob28uY29tXFxcXFwvcHJpdmFjeVxcXFxcL3VzXFxcXFwveWFob29cXFxcXC9yZWxldmFudGFkcy5odG1sXFxcIixcXFwiY2xvc2VcXFwiOlxcXCJDbG9zZVxcXCIsXFxcImNsb3NlQWRcXFwiOlxcXCJDbG9zZSBBZFxcXCIsXFxcInNob3dBZFxcXCI6XFxcIlNob3cgYWRcXFwiLFxcXCJjb2xsYXBzZVxcXCI6XFxcIkNvbGxhcHNlXFxcIixcXFwiZmRiXFxcIjpcXFwiSSBkb24ndCBsaWtlIHRoaXMgYWRcXFwiLFxcXCJjb2RlXFxcIjpcXFwiZW4tdXNcXFwifSIsImlzM3JkIjowLCJmYWNTdGF0dXMiOnt9LCJ1c2VyUHJvdmlkZWREYXRhIjp7fSwiZmFjUm90YXRpb24iOnt9LCJzbG90RGF0YSI6e30sInNpemUiOiIxMjB4NjAifX0sImNvbmYiOnsidyI6MTIwLCJoIjo2MH19LHsiaWQiOiJGQjItMyIsImxvd0hUTUwiOiIiLCJtZXRhIjp7InkiOnsicG9zIjoiRkIyLTMiLCJiZWhhdmlvciI6Im5vbl9leHAiLCJhZElEIjoiOTg1MDg0MjcyMDI3NTYwMDc1NiIsIm1hdGNoSUQiOiI5OTk5OTkuOTk5OTk5Ljk5OTk5OS45OTk5OTkiLCJib29rSUQiOiIyMzQyMjk3NTUxIiwic2xvdElEIjoiMyIsInNlcnZlVHlwZSI6Ii0xIiwiZXJyIjpmYWxzZSwiaGFzRXh0ZXJuYWwiOmZhbHNlLCJzdXBwX3VnYyI6IiIsInBsYWNlbWVudElEIjoiMzU3NTY1MDA1MSIsImZkYiI6InsgXFxcImZkYl91cmxcXFwiOiBcXFwiaHR0cHM6XFxcXFxcXC9cXFxcXFxcL2JlYXAtYmMueWFob28uY29tXFxcXFxcXC9hZlxcXFxcXFwvdXM/YnY9MS4wLjAmYnM9KDE2MHI1bjNiYyhnaWQkaktVdW1UWXpMaktsdGZsMldhWVYyd2suTWpBNExnQUFBQUNXUGZyVixzdCQxNTA4Njk1NjgyNzMzNzk1LHNydiQxLHNpJDQ0NTEwNTEsY3QkMjUsZXhwJDE1MDg3MDI4ODI3MzM3OTUsYWR2JDIxMDc0NDcwMjk1LGxpJDM1NzY1NzA1NTEsY3IkNDYyNDE5MjU1MSx2JDEuMCxwYmlkJDIwNDU5OTMzMjIzLHNlaWQkMzEzMjg3MDUxKSkmYWw9KHR5cGUke3R5cGV9LGNtbnQke2NtbnR9LHN1Ym8ke3N1Ym99KSZyPTEwXFxcIiwgXFxcImZkYl9vblxcXCI6IFxcXCIxXFxcIiwgXFxcImZkYl9leHBcXFwiOiBcXFwiMTUwODcwMjg4MjczM1xcXCIsIFxcXCJmZGJfaW50bFxcXCI6IFxcXCJlbi1VU1xcXCIgfSIsInNlcnZlVGltZSI6IjE1MDg2OTU2ODI3MzM3OTUiLCJpbXBJRCI6IjRzM1lRdGduT0hFLSIsImNyZWF0aXZlSUQiOjQ2MjQxOTI1NTEsImFkYyI6IntcXFwibGFiZWxcXFwiOlxcXCJBZENob2ljZXNcXFwiLFxcXCJ1cmxcXFwiOlxcXCJodHRwczpcXFxcXC9cXFxcXC9pbmZvLnlhaG9vLmNvbVxcXFxcL3ByaXZhY3lcXFxcXC91c1xcXFxcL3lhaG9vXFxcXFwvcmVsZXZhbnRhZHMuaHRtbFxcXCIsXFxcImNsb3NlXFxcIjpcXFwiQ2xvc2VcXFwiLFxcXCJjbG9zZUFkXFxcIjpcXFwiQ2xvc2UgQWRcXFwiLFxcXCJzaG93QWRcXFwiOlxcXCJTaG93IGFkXFxcIixcXFwiY29sbGFwc2VcXFwiOlxcXCJDb2xsYXBzZVxcXCIsXFxcImZkYlxcXCI6XFxcIkkgZG9uJ3QgbGlrZSB0aGlzIGFkXFxcIixcXFwiY29kZVxcXCI6XFxcImVuLXVzXFxcIn0iLCJpczNyZCI6MCwiZmFjU3RhdHVzIjp7fSwidXNlclByb3ZpZGVkRGF0YSI6e30sImZhY1JvdGF0aW9uIjp7fSwic2xvdERhdGEiOnt9LCJzaXplIjoiMTIweDYwIn19LCJjb25mIjp7InciOjEyMCwiaCI6NjB9fSx7ImlkIjoiTERSQiIsImxvd0hUTUwiOiIiLCJtZXRhIjp7InkiOnsicG9zIjoiTERSQiIsImJlaGF2aW9yIjoibm9uX2V4cCIsImFkSUQiOiI5ODI3MzQ3MTAxNjgyODI5Mzk4IiwibWF0Y2hJRCI6Ijk5OTk5OS45OTk5OTkuOTk5OTk5Ljk5OTk5OSIsImJvb2tJRCI6IjIzMzU2MDI1NTEiLCJzbG90SUQiOiI2Iiwic2VydmVUeXBlIjoiLTEiLCJlcnIiOmZhbHNlLCJoYXNFeHRlcm5hbCI6ZmFsc2UsInN1cHBfdWdjIjoiIiwicGxhY2VtZW50SUQiOiIzNTY0NDEyMDUxIiwiZmRiIjoieyBcXFwiZmRiX3VybFxcXCI6IFxcXCJodHRwczpcXFxcXFxcL1xcXFxcXFwvYmVhcC1iYy55YWhvby5jb21cXFxcXFxcL2FmXFxcXFxcXC91cz9idj0xLjAuMCZicz0oMTYwcWI0aXNiKGdpZCRqS1V1bVRZekxqS2x0ZmwyV2FZVjJ3ay5NakE0TGdBQUFBQ1dQZnJWLHN0JDE1MDg2OTU2ODI3MzM3OTUsc3J2JDEsc2kkNDQ1MTA1MSxjdCQyNSxleHAkMTUwODcwMjg4MjczMzc5NSxhZHYkMjEwNzQ0NzAyOTUsbGkkMzU2NTAxMTA1MSxjciQ0NjE4MzA1NTUxLHYkMS4wLHBiaWQkMjA0NTk5MzMyMjMsc2VpZCQzMTMyODcwNTEpKSZhbD0odHlwZSR7dHlwZX0sY21udCR7Y21udH0sc3VibyR7c3Vib30pJnI9MTBcXFwiLCBcXFwiZmRiX29uXFxcIjogXFxcIjFcXFwiLCBcXFwiZmRiX2V4cFxcXCI6IFxcXCIxNTA4NzAyODgyNzMzXFxcIiwgXFxcImZkYl9pbnRsXFxcIjogXFxcImVuLVVTXFxcIiB9Iiwic2VydmVUaW1lIjoiMTUwODY5NTY4MjczMzc5NSIsImltcElEIjoiNXczWlF0Z25PSEUtIiwiY3JlYXRpdmVJRCI6NDYxODMwNTU1MSwiYWRjIjoie1xcXCJsYWJlbFxcXCI6XFxcIkFkQ2hvaWNlc1xcXCIsXFxcInVybFxcXCI6XFxcImh0dHBzOlxcXFxcL1xcXFxcL2luZm8ueWFob28uY29tXFxcXFwvcHJpdmFjeVxcXFxcL3VzXFxcXFwveWFob29cXFxcXC9yZWxldmFudGFkcy5odG1sXFxcIixcXFwiY2xvc2VcXFwiOlxcXCJDbG9zZVxcXCIsXFxcImNsb3NlQWRcXFwiOlxcXCJDbG9zZSBBZFxcXCIsXFxcInNob3dBZFxcXCI6XFxcIlNob3cgYWRcXFwiLFxcXCJjb2xsYXBzZVxcXCI6XFxcIkNvbGxhcHNlXFxcIixcXFwiZmRiXFxcIjpcXFwiSSBkb24ndCBsaWtlIHRoaXMgYWRcXFwiLFxcXCJjb2RlXFxcIjpcXFwiZW4tdXNcXFwifSIsImlzM3JkIjowLCJmYWNTdGF0dXMiOnt9LCJ1c2VyUHJvdmlkZWREYXRhIjp7fSwiZmFjUm90YXRpb24iOnt9LCJzbG90RGF0YSI6e30sInNpemUiOiI3Mjh4OTAifX0sImNvbmYiOnsidyI6NzI4LCJoIjo5MH19LHsiaWQiOiJMRFJCMiIsImxvd0hUTUwiOiIiLCJtZXRhIjp7InkiOnsicG9zIjoiTERSQjIiLCJiZWhhdmlvciI6Im5vbl9leHAiLCJhZElEIjoiOTc0OTc5NzE3MjE4NjA3MTgyNSIsIm1hdGNoSUQiOiI5OTk5OTkuOTk5OTk5Ljk5OTk5OS45OTk5OTkiLCJib29rSUQiOiIyMzE1MjIyMDUxIiwic2xvdElEIjoiNyIsInNlcnZlVHlwZSI6Ii0xIiwiZXJyIjpmYWxzZSwiaGFzRXh0ZXJuYWwiOmZhbHNlLCJzdXBwX3VnYyI6IiIsInBsYWNlbWVudElEIjoiMzUzNjAyNTU1MSIsImZkYiI6InsgXFxcImZkYl91cmxcXFwiOiBcXFwiaHR0cHM6XFxcXFxcXC9cXFxcXFxcL2JlYXAtYmMueWFob28uY29tXFxcXFxcXC9hZlxcXFxcXFwvdXM/YnY9MS4wLjAmYnM9KDE2MDJoY2o0cChnaWQkaktVdW1UWXpMaktsdGZsMldhWVYyd2suTWpBNExnQUFBQUNXUGZyVixzdCQxNTA4Njk1NjgyNzMzNzk1LHNydiQxLHNpJDQ0NTEwNTEsY3QkMjUsZXhwJDE1MDg3MDI4ODI3MzM3OTUsYWR2JDI2NTEzNzUzNjA4LGxpJDM1MzU5MzIwNTEsY3IkNDUyNzA2ODU1MSx2JDEuMCxwYmlkJDIwNDU5OTMzMjIzLHNlaWQkMzEzMjg3MDUxKSkmYWw9KHR5cGUke3R5cGV9LGNtbnQke2NtbnR9LHN1Ym8ke3N1Ym99KSZyPTEwXFxcIiwgXFxcImZkYl9vblxcXCI6IFxcXCIxXFxcIiwgXFxcImZkYl9leHBcXFwiOiBcXFwiMTUwODcwMjg4MjczM1xcXCIsIFxcXCJmZGJfaW50bFxcXCI6IFxcXCJlbi1VU1xcXCIgfSIsInNlcnZlVGltZSI6IjE1MDg2OTU2ODI3MzM3OTUiLCJpbXBJRCI6IlBpUFpRdGduT0hFLSIsImNyZWF0aXZlSUQiOjQ1MjcwNjg1NTEsImFkYyI6IntcXFwibGFiZWxcXFwiOlxcXCJBZENob2ljZXNcXFwiLFxcXCJ1cmxcXFwiOlxcXCJodHRwczpcXFxcXC9cXFxcXC9pbmZvLnlhaG9vLmNvbVxcXFxcL3ByaXZhY3lcXFxcXC91c1xcXFxcL3lhaG9vXFxcXFwvcmVsZXZhbnRhZHMuaHRtbFxcXCIsXFxcImNsb3NlXFxcIjpcXFwiQ2xvc2VcXFwiLFxcXCJjbG9zZUFkXFxcIjpcXFwiQ2xvc2UgQWRcXFwiLFxcXCJzaG93QWRcXFwiOlxcXCJTaG93IGFkXFxcIixcXFwiY29sbGFwc2VcXFwiOlxcXCJDb2xsYXBzZVxcXCIsXFxcImZkYlxcXCI6XFxcIkkgZG9uJ3QgbGlrZSB0aGlzIGFkXFxcIixcXFwiY29kZVxcXCI6XFxcImVuLXVzXFxcIn0iLCJpczNyZCI6MSwiZmFjU3RhdHVzIjp7fSwidXNlclByb3ZpZGVkRGF0YSI6e30sImZhY1JvdGF0aW9uIjp7fSwic2xvdERhdGEiOnt9LCJzaXplIjoiNzI4eDkwIn19LCJjb25mIjp7InciOjcyOCwiaCI6OTB9fSx7ImlkIjoiTFJFQyIsImxvd0hUTUwiOiIiLCJtZXRhIjp7InkiOnsicG9zIjoiTFJFQyIsImJlaGF2aW9yIjoibm9uX2V4cCIsImFkSUQiOiIjIiwibWF0Y2hJRCI6Ijk5OTk5OS45OTk5OTkuOTk5OTk5Ljk5OTk5OSIsImJvb2tJRCI6IjIzMTUyMjMwNTEiLCJzbG90SUQiOiI4Iiwic2VydmVUeXBlIjoiLTEiLCJlcnIiOiJpbnZhbGlkIChkYXJsYSkgKG5vKSIsImhhc0V4dGVybmFsIjpmYWxzZSwic3VwcF91Z2MiOiIiLCJwbGFjZW1lbnRJRCI6IjM1MzYwMzQ1NTEiLCJmZGIiOiJ7IFxcXCJmZGJfdXJsXFxcIjogXFxcImh0dHBzOlxcXFxcXFwvXFxcXFxcXC9iZWFwLWJjLnlhaG9vLmNvbVxcXFxcXFwvYWZcXFxcXFxcL3VzP2J2PTEuMC4wJmJzPSgxNjBmcjZzZnUoZ2lkJGpLVXVtVFl6TGpLbHRmbDJXYVlWMndrLk1qQTRMZ0FBQUFDV1BmclYsc3QkMTUwODY5NTY4MjczMzc5NSxzcnYkMSxzaSQ0NDUxMDUxLGN0JDI1LGV4cCQxNTA4NzAyODgyNzMzNzk1LGFkdiQyNjUxMzc1MzYwOCxsaSQzNTM1OTIxNTUxLGNyJDQ1MjcwODIwNTEsdiQxLjAscGJpZCQyMDQ1OTkzMzIyMyxzZWlkJDMxMzI4NzA1MSkpJmFsPSh0eXBlJHt0eXBlfSxjbW50JHtjbW50fSxzdWJvJHtzdWJvfSkmcj0xMFxcXCIsIFxcXCJmZGJfb25cXFwiOiBcXFwiMVxcXCIsIFxcXCJmZGJfZXhwXFxcIjogXFxcIjE1MDg3MDI4ODI3MzNcXFwiLCBcXFwiZmRiX2ludGxcXFwiOiBcXFwiZW4tVVNcXFwiIH0iLCJzZXJ2ZVRpbWUiOiIxNTA4Njk1NjgyNzMzNzk1IiwiaW1wSUQiOiJsVGpaUXRnbk9IRS0iLCJjcmVhdGl2ZUlEIjo0NTI3MDgyMDUxLCJhZGMiOiJ7XFxcImxhYmVsXFxcIjpcXFwiQWRDaG9pY2VzXFxcIixcXFwidXJsXFxcIjpcXFwiaHR0cHM6XFxcXFwvXFxcXFwvaW5mby55YWhvby5jb21cXFxcXC9wcml2YWN5XFxcXFwvdXNcXFxcXC95YWhvb1xcXFxcL3JlbGV2YW50YWRzLmh0bWxcXFwiLFxcXCJjbG9zZVxcXCI6XFxcIkNsb3NlXFxcIixcXFwiY2xvc2VBZFxcXCI6XFxcIkNsb3NlIEFkXFxcIixcXFwic2hvd0FkXFxcIjpcXFwiU2hvdyBhZFxcXCIsXFxcImNvbGxhcHNlXFxcIjpcXFwiQ29sbGFwc2VcXFwiLFxcXCJmZGJcXFwiOlxcXCJJIGRvbid0IGxpa2UgdGhpcyBhZFxcXCIsXFxcImNvZGVcXFwiOlxcXCJlbi11c1xcXCJ9IiwiaXMzcmQiOjEsImZhY1N0YXR1cyI6e30sInVzZXJQcm92aWRlZERhdGEiOnt9LCJmYWNSb3RhdGlvbiI6e30sInNsb3REYXRhIjp7fSwic2l6ZSI6IjMwMHgyNTAifX0sImNvbmYiOnsidyI6MzAwLCJoIjoyNTB9fSx7ImlkIjoiTFJFQzIiLCJsb3dIVE1MIjoiIiwibWV0YSI6eyJ5Ijp7InBvcyI6IkxSRUMyIiwiYmVoYXZpb3IiOiJub25fZXhwIiwiYWRJRCI6Ijk3NDk3OTkzMTk2Njk3MTk4MjQiLCJtYXRjaElEIjoiOTk5OTk5Ljk5OTk5OS45OTk5OTkuOTk5OTk5IiwiYm9va0lEIjoiMjMxNTIyMjU1MSIsInNsb3RJRCI6IjkiLCJzZXJ2ZVR5cGUiOiItMSIsImVyciI6ZmFsc2UsImhhc0V4dGVybmFsIjpmYWxzZSwic3VwcF91Z2MiOiIiLCJwbGFjZW1lbnRJRCI6IjM1MzYwMjUwNTEiLCJmZGIiOiJ7IFxcXCJmZGJfdXJsXFxcIjogXFxcImh0dHBzOlxcXFxcXFwvXFxcXFxcXC9iZWFwLWJjLnlhaG9vLmNvbVxcXFxcXFwvYWZcXFxcXFxcL3VzP2J2PTEuMC4wJmJzPSgxNjBpdmltaHUoZ2lkJGpLVXVtVFl6TGpLbHRmbDJXYVlWMndrLk1qQTRMZ0FBQUFDV1BmclYsc3QkMTUwODY5NTY4MjczMzc5NSxzcnYkMSxzaSQ0NDUxMDUxLGN0JDI1LGV4cCQxNTA4NzAyODgyNzMzNzk1LGFkdiQyNjUxMzc1MzYwOCxsaSQzNTM1OTMxNTUxLGNyJDQ1MjcwNjgwNTEsdiQxLjAscGJpZCQyMDQ1OTkzMzIyMyxzZWlkJDMxMzI4NzA1MSkpJmFsPSh0eXBlJHt0eXBlfSxjbW50JHtjbW50fSxzdWJvJHtzdWJvfSkmcj0xMFxcXCIsIFxcXCJmZGJfb25cXFwiOiBcXFwiMVxcXCIsIFxcXCJmZGJfZXhwXFxcIjogXFxcIjE1MDg3MDI4ODI3MzNcXFwiLCBcXFwiZmRiX2ludGxcXFwiOiBcXFwiZW4tVVNcXFwiIH0iLCJzZXJ2ZVRpbWUiOiIxNTA4Njk1NjgyNzMzNzk1IiwiaW1wSUQiOiI3RTNaUXRnbk9IRS0iLCJjcmVhdGl2ZUlEIjo0NTI3MDY4MDUxLCJhZGMiOiJ7XFxcImxhYmVsXFxcIjpcXFwiQWRDaG9pY2VzXFxcIixcXFwidXJsXFxcIjpcXFwiaHR0cHM6XFxcXFwvXFxcXFwvaW5mby55YWhvby5jb21cXFxcXC9wcml2YWN5XFxcXFwvdXNcXFxcXC95YWhvb1xcXFxcL3JlbGV2YW50YWRzLmh0bWxcXFwiLFxcXCJjbG9zZVxcXCI6XFxcIkNsb3NlXFxcIixcXFwiY2xvc2VBZFxcXCI6XFxcIkNsb3NlIEFkXFxcIixcXFwic2hvd0FkXFxcIjpcXFwiU2hvdyBhZFxcXCIsXFxcImNvbGxhcHNlXFxcIjpcXFwiQ29sbGFwc2VcXFwiLFxcXCJmZGJcXFwiOlxcXCJJIGRvbid0IGxpa2UgdGhpcyBhZFxcXCIsXFxcImNvZGVcXFwiOlxcXCJlbi11c1xcXCJ9IiwiaXMzcmQiOjEsImZhY1N0YXR1cyI6e30sInVzZXJQcm92aWRlZERhdGEiOnt9LCJmYWNSb3RhdGlvbiI6e30sInNsb3REYXRhIjp7fSwic2l6ZSI6IjMwMHgyNTAifX0sImNvbmYiOnsidyI6MzAwLCJoIjoyNTB9fSx7ImlkIjoiRk9PVCIsImxvd0hUTUwiOiIiLCJtZXRhIjp7InkiOnsicG9zIjoiRk9PVCIsImJlaGF2aW9yIjoibm9uX2V4cCIsImFkSUQiOiIjMiIsIm1hdGNoSUQiOiIjMiIsImJvb2tJRCI6Ii0xIiwic2xvdElEIjoiNCIsInNlcnZlVHlwZSI6Ii0xIiwiZXJyIjoiaW52YWxpZF9zcGFjZSIsImhhc0V4dGVybmFsIjpmYWxzZSwic3VwcF91Z2MiOiIiLCJwbGFjZW1lbnRJRCI6LTEsImZkYiI6InsgXFxcImZkYl91cmxcXFwiOiBcXFwiaHR0cDpcXFxcXC9cXFxcXC9iZWFwLWJjLnlhaG9vLmNvbVxcXFxcL2FmP2J2PTEuMC4wJmJzPSgxNWlyNDVyNmIoZ2lkJGptVFZRRGs0TGpISGJGc0hVNWpNa2dLa01UQXVOd0FBQUFDbGpwa0ssc3QkMTQwMjUzNzIzMzAyNjkyMixzcnYkMSxzaSQxMzMwMzU1MSxhZHYkMjU5NDE0MjkwMzYsY3QkMjUsbGkkMzIzOTI1MDA1MSxleHAkMTQwMjU0NDQzMzAyNjkyMixjciQ0MTU0OTg0NTUxLHBiaWQkMjUzNzI3MjgxMzMsdiQxLjApKSZhbD0odHlwZSR7dHlwZX0sY21udCR7Y21udH0sc3VibyR7c3Vib30pJnI9MTBcXFwiLCBcXFwiZmRiX29uXFxcIjogXFxcIjFcXFwiLCBcXFwiZmRiX2V4cFxcXCI6IFxcXCIxNDAyNTQ0NDMzMDI2XFxcIiwgXFxcImZkYl9pbnRsXFxcIjogXFxcImVuLXVzXFxcIiAsIFxcXCJkXFxcIiA6IFxcXCIxXFxcIiB9Iiwic2VydmVUaW1lIjoiMTUwODY5NTY4MjczMzc5NSIsImltcElEIjoiIiwiY3JlYXRpdmVJRCI6LTEsImFkYyI6IntcXFwibGFiZWxcXFwiOlxcXCJBZENob2ljZXNcXFwiLFxcXCJ1cmxcXFwiOlxcXCJodHRwczpcXFxcXC9cXFxcXC9pbmZvLnlhaG9vLmNvbVxcXFxcL3ByaXZhY3lcXFxcXC91c1xcXFxcL3lhaG9vXFxcXFwvcmVsZXZhbnRhZHMuaHRtbFxcXCIsXFxcImNsb3NlXFxcIjpcXFwiQ2xvc2VcXFwiLFxcXCJjbG9zZUFkXFxcIjpcXFwiQ2xvc2UgQWRcXFwiLFxcXCJzaG93QWRcXFwiOlxcXCJTaG93IGFkXFxcIixcXFwiY29sbGFwc2VcXFwiOlxcXCJDb2xsYXBzZVxcXCIsXFxcImZkYlxcXCI6XFxcIkkgZG9uJ3QgbGlrZSB0aGlzIGFkXFxcIixcXFwiY29kZVxcXCI6XFxcImVuLXVzXFxcIn0iLCJpczNyZCI6MCwiZmFjU3RhdHVzIjp7fSwidXNlclByb3ZpZGVkRGF0YSI6e30sImZhY1JvdGF0aW9uIjp7fSwic2xvdERhdGEiOnt9fX19LHsiaWQiOiJGU1JWWSIsImxvd0hUTUwiOiIiLCJtZXRhIjp7InkiOnsicG9zIjoiRlNSVlkiLCJiZWhhdmlvciI6Im5vbl9leHAiLCJhZElEIjoiOTc1MjUxNTg4NjQ4NDQ0MTg1MCIsIm1hdGNoSUQiOiI5OTk5OTkuOTk5OTk5Ljk5OTk5OS45OTk5OTkiLCJib29rSUQiOiIyMzE1OTMyMDUxIiwic2xvdElEIjoiNSIsInNlcnZlVHlwZSI6Ii0xIiwiZXJyIjpmYWxzZSwiaGFzRXh0ZXJuYWwiOmZhbHNlLCJzdXBwX3VnYyI6IiIsInBsYWNlbWVudElEIjoiMzUzNzAwNjU1MSIsImZkYiI6InsgXFxcImZkYl91cmxcXFwiOiBcXFwiaHR0cHM6XFxcXFxcXC9cXFxcXFxcL2JlYXAtYmMueWFob28uY29tXFxcXFxcXC9hZlxcXFxcXFwvdXM/YnY9MS4wLjAmYnM9KDE2MHBsamdoYShnaWQkaktVdW1UWXpMaktsdGZsMldhWVYyd2suTWpBNExnQUFBQUNXUGZyVixzdCQxNTA4Njk1NjgyNzMzNzk1LHNydiQxLHNpJDQ0NTEwNTEsY3QkMjUsZXhwJDE1MDg3MDI4ODI3MzM3OTUsYWR2JDI2NTEzNzUzNjA4LGxpJDM1MzY4NjcwNTEsY3IkNDUyODE3NzA1MSx2JDEuMCxwYmlkJDIwNDU5OTMzMjIzLHNlaWQkMzEzMjg3MDUxKSkmYWw9KHR5cGUke3R5cGV9LGNtbnQke2NtbnR9LHN1Ym8ke3N1Ym99KSZyPTEwXFxcIiwgXFxcImZkYl9vblxcXCI6IFxcXCIxXFxcIiwgXFxcImZkYl9leHBcXFwiOiBcXFwiMTUwODcwMjg4MjczM1xcXCIsIFxcXCJmZGJfaW50bFxcXCI6IFxcXCJlbi1VU1xcXCIgfSIsInNlcnZlVGltZSI6IjE1MDg2OTU2ODI3MzM3OTUiLCJpbXBJRCI6ImtQallRdGduT0hFLSIsImNyZWF0aXZlSUQiOjQ1MjgxNzcwNTEsImFkYyI6IntcXFwibGFiZWxcXFwiOlxcXCJBZENob2ljZXNcXFwiLFxcXCJ1cmxcXFwiOlxcXCJodHRwczpcXFxcXC9cXFxcXC9pbmZvLnlhaG9vLmNvbVxcXFxcL3ByaXZhY3lcXFxcXC91c1xcXFxcL3lhaG9vXFxcXFwvcmVsZXZhbnRhZHMuaHRtbFxcXCIsXFxcImNsb3NlXFxcIjpcXFwiQ2xvc2VcXFwiLFxcXCJjbG9zZUFkXFxcIjpcXFwiQ2xvc2UgQWRcXFwiLFxcXCJzaG93QWRcXFwiOlxcXCJTaG93IGFkXFxcIixcXFwiY29sbGFwc2VcXFwiOlxcXCJDb2xsYXBzZVxcXCIsXFxcImZkYlxcXCI6XFxcIkkgZG9uJ3QgbGlrZSB0aGlzIGFkXFxcIixcXFwiY29kZVxcXCI6XFxcImVuLXVzXFxcIn0iLCJpczNyZCI6MSwiZmFjU3RhdHVzIjp7fSwidXNlclByb3ZpZGVkRGF0YSI6e30sImZhY1JvdGF0aW9uIjp7fSwic2xvdERhdGEiOnt9LCJzaXplIjoiMXgxIn19LCJjb25mIjp7InciOjEsImgiOjF9fV0sImNvbmYiOm51bGwsIm1ldGEiOnsieSI6eyJwb3NfbGlzdCI6WyJGQjIiLCJGQjItMSIsIkZCMi0yIiwiRkIyLTMiLCJMRFJCIiwiTERSQjIiLCJMUkVDIiwiTFJFQzIiLCJGT09UIiwiRlNSVlkiXSwidHJhbnNJRCI6ImRhcmxhX3ByZWZldGNoXzE1MDg2OTU2ODI3MzJfMjU4Mzg5MTM5XzMiLCJrMl91cmkiOiIiLCJmYWNfcnQiOiI2MzI5NCIsInNwYWNlSUQiOiIxMTgzMzM1ODgzIiwibG9va3VwVGltZSI6MjY2LCJwcm9jVGltZSI6MjgxLCJucHYiOjAsInB2aWQiOiJqS1V1bVRZekxqS2x0ZmwyV2FZVjJ3ay5NakE0TGdBQUFBQ1dQZnJWIiwic2VydmVUaW1lIjoiMTUwODY5NTY4MjczMzc5NSIsImVwIjp7InNpdGUtYXR0cmlidXRlIjoiIFktQlVDS0VUPWZpbi1zdHJtLXRlc3QyLGZuZG10ZXN0LGZpbnNzbCIsInRndCI6Il9ibGFuayIsInNlY3VyZSI6dHJ1ZSwicmVmIjoiaHR0cHM6XC9cL2ZpbmFuY2UueWFob28uY29tXC9sb3NlcnMiLCJ1bHQiOnsicGciOnsicHJvcGVydHkiOiJmaW5hbmNlX2VuLVVTIiwidGVzdCI6ImZpbi1zdHJtLXRlc3QyLGZuZG10ZXN0LGZpbnNzbCJ9fSwiY2x3Ijp7IkxSRUMiOnsiYmxvY2tlZF9ieSI6Ik1PTi0xIn0sIk1PTi0xIjp7ImJsb2NrZWRfYnkiOiJMUkVDIn0sIk1BU1QiOnsiYmxvY2tlZF9ieSI6IlNQTCxMRFJCIn0sIkxEUkIiOnsiYmxvY2tlZF9ieSI6Ik1BU1QsU1BMIn0sIlNQTCI6eyJibG9ja2VkX2J5IjoiTUFTVCxMRFJCIn19LCJsYW5nIjoiZW4tVVMiLCJmaWx0ZXIiOiJub19leHBhbmRhYmxlO2V4cF9pZnJhbWVfZXhwYW5kYWJsZTsiLCJkYXJsYUlEIjoiZGFybGFfaW5zdGFuY2VfMTUwODY5NTY4MjczMl83ODg4OTQwMjdfMiJ9LCJweW0iOnsiLiI6InYwLjAuOTs7LTsifSwiaG9zdCI6IiIsImZpbHRlcmVkIjpbXX19fQ==">
         <!-- gq1-sdarlaws-008.adx.gq1.yahoo.com Sun Oct 22 18:08:02 UTC 2017 -->
         <script type="text/javascript">if (typeof DARLA !== "undefined" && DARLA) {DARLA.config(window.DARLA_CONFIG);window.sf_host.onReady(true,true,'FB2,FB2-1,FB2-2,FB2-3,LDRB,LREC',3000);}</script>
      </div>
      <script>
         (function (root) {
         /* -- Data -- */
         root.App \n\t (root.App = {});
         root.App.now = 1508695682640;
         }(this));
      </script><script src="https://s.yimg.com/zz/combo?os/yaft/yaft-0.3.6.min.js&os/yaft/yaft-plugin-aftnoad-0.1.3.min.js" defer></script>
      <script src="https://s.yimg.com/os/finance/dd-site/js/main.4a80f204d607bc3682f7.js" defer></script>
      <script>window.webpackPublicPath='https://s.yimg.com/os/finance/dd-site/js/';</script>
   </body>
</html>

        '''
