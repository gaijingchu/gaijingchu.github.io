# -*- coding: utf-8 -*-
"""Build reading.html (bilingual) from the book table below + quotes_full.json.

Usage:  python3 build/gen_reading.py       (from the homepage/ directory, or anywhere)
Edit ROWS / NOBEL below to add books; edit quotes_full.json to add excerpts.
"""
import json, html, pathlib

HERE = pathlib.Path(__file__).resolve().parent
SITE = HERE.parent

# group key -> (zh heading, en heading)
GROUPS = [
 ("en",    "英语文学",   "English"),
 ("ru",    "俄语文学",   "Russian"),
 ("fr",    "法语文学",   "French"),
 ("de",    "德语文学",   "German"),
 ("jp",    "日语文学",   "Japanese"),
 ("es",    "西班牙语文学", "Spanish"),
 ("sv",    "瑞典语文学",  "Swedish"),
 ("da",    "丹麦语文学",  "Danish"),
 ("pl",    "波兰语文学",  "Polish"),
 ("it",    "意大利语文学", "Italian"),
 ("bn",    "孟加拉语文学", "Bengali"),
]

# g | zh_title | en_title | zh_author | en_author | zh_nat | en_nat
ROWS = """
fr|约翰·克利斯朵夫|Jean-Christophe|罗曼·罗兰|Romain Rolland|法|French
fr|忏悔录|The Confessions|卢梭|Jean-Jacques Rousseau|日内瓦，法语作家|Genevan, French-language
fr|三个火枪手|The Three Musketeers|大仲马|Alexandre Dumas père|法|French
fr|基督山伯爵|The Count of Monte Cristo|大仲马|Alexandre Dumas père|法|French
fr|黑郁金香|The Black Tulip|大仲马|Alexandre Dumas père|法|French
fr|茶花女|The Lady of the Camellias|小仲马|Alexandre Dumas fils|法|French
fr|卡门|Carmen|梅里美|Prosper Mérimée|法|French
fr|欧也妮·葛朗台|Eugénie Grandet|巴尔扎克|Honoré de Balzac|法|French
fr|高老头|Le Père Goriot|巴尔扎克|Honoré de Balzac|法|French
fr|都兰趣话|Droll Stories|巴尔扎克|Honoré de Balzac|法|French
fr|悲惨世界|Les Misérables|雨果|Victor Hugo|法|French
fr|巴黎圣母院|The Hunchback of Notre-Dame|雨果|Victor Hugo|法|French
fr|笑面人|The Man Who Laughs|雨果|Victor Hugo|法|French
fr|包法利夫人|Madame Bovary|福楼拜|Gustave Flaubert|法|French
fr|漂亮朋友|Bel-Ami|莫泊桑|Guy de Maupassant|法|French
fr|莫泊桑短篇小说选|Selected Short Stories|莫泊桑|Guy de Maupassant|法|French
fr|红与黑|The Red and the Black|司汤达|Stendhal|法|French
fr|娜娜|Nana|左拉|Émile Zola|法|French
fr|小酒店|L’Assommoir|左拉|Émile Zola|法|French
fr|局外人|The Stranger|加缪|Albert Camus|法（生于法属阿尔及利亚）|French (b. French Algeria)
fr|鼠疫|The Plague|加缪|Albert Camus|法（生于法属阿尔及利亚）|French (b. French Algeria)
fr|名人传|Lives of Illustrious Men|罗曼·罗兰|Romain Rolland|法|French
fr|窄门|Strait Is the Gate|纪德|André Gide|法|French
fr|波纳尔之罪|The Crime of Sylvestre Bonnard|法郎士|Anatole France|法|French
fr|爱的荒漠|The Desert of Love|弗朗索瓦·莫里亚克|François Mauriac|法|French
en|傲慢与偏见|Pride and Prejudice|简·奥斯汀|Jane Austen|英|English
en|理智与情感|Sense and Sensibility|简·奥斯汀|Jane Austen|英|English
en|爱玛|Emma|简·奥斯汀|Jane Austen|英|English
en|劝导|Persuasion|简·奥斯汀|Jane Austen|英|English
en|诺桑觉寺|Northanger Abbey|简·奥斯汀|Jane Austen|英|English
en|曼斯菲尔德庄园|Mansfield Park|简·奥斯汀|Jane Austen|英|English
en|双城记|A Tale of Two Cities|狄更斯|Charles Dickens|英|English
en|雾都孤儿|Oliver Twist|狄更斯|Charles Dickens|英|English
en|大卫·科波菲尔|David Copperfield|狄更斯|Charles Dickens|英|English
en|简·爱|Jane Eyre|夏洛蒂·勃朗特|Charlotte Brontë|英|English
en|呼啸山庄|Wuthering Heights|艾米莉·勃朗特|Emily Brontë|英|English
en|米德尔马契|Middlemarch|乔治·艾略特|George Eliot|英|English
en|德伯家的苔丝|Tess of the d’Urbervilles|哈代|Thomas Hardy|英|English
en|南方与北方|North and South|盖斯凯尔夫人|Elizabeth Gaskell|英|English
en|海浪|The Waves|弗吉尼亚·伍尔夫|Virginia Woolf|英|English
en|达洛维夫人|Mrs Dalloway|弗吉尼亚·伍尔夫|Virginia Woolf|英|English
en|威尼斯商人|The Merchant of Venice|莎士比亚|William Shakespeare|英|English
en|罗密欧与朱丽叶|Romeo and Juliet|莎士比亚|William Shakespeare|英|English
en|面纱|The Painted Veil|毛姆|W. Somerset Maugham|英|British
en|人性的枷锁|Of Human Bondage|毛姆|W. Somerset Maugham|英|British
en|刀锋|The Razor’s Edge|毛姆|W. Somerset Maugham|英|British
en|蝇王|Lord of the Flies|戈尔丁|William Golding|英|British
en|有产业的人|The Man of Property|高尔斯华绥|John Galsworthy|英|British
en|骑虎|In Chancery|高尔斯华绥|John Galsworthy|英|British
en|出租|To Let|高尔斯华绥|John Galsworthy|英|British
en|查泰莱夫人的情人|Lady Chatterley’s Lover|D·H·劳伦斯|D. H. Lawrence|英|English
en|儿子与情人|Sons and Lovers|D·H·劳伦斯|D. H. Lawrence|英|English
en|道连·格雷的画像|The Picture of Dorian Gray|王尔德|Oscar Wilde|爱尔兰|Irish
en|王尔德奇异故事集|Selected Stories|王尔德|Oscar Wilde|爱尔兰|Irish
en|尤利西斯|Ulysses|乔伊斯|James Joyce|爱尔兰|Irish
en|华伦夫人的职业|Mrs Warren’s Profession|萧伯纳|George Bernard Shaw|爱尔兰|Irish
en|英国佬的另一个岛|John Bull’s Other Island|萧伯纳|George Bernard Shaw|爱尔兰|Irish
en|芭芭拉少校|Major Barbara|萧伯纳|George Bernard Shaw|爱尔兰|Irish
en|圣女贞德|Saint Joan|萧伯纳|George Bernard Shaw|爱尔兰|Irish
en|千岁人|Back to Methuselah|萧伯纳|George Bernard Shaw|爱尔兰|Irish
en|牛虻|The Gadfly|伏尼契|Ethel Lilian Voynich|爱尔兰出生的英国作家|Irish-born British
ru|卡拉马佐夫兄弟|The Brothers Karamazov|陀思妥耶夫斯基|Fyodor Dostoevsky|俄|Russian
ru|罪与罚|Crime and Punishment|陀思妥耶夫斯基|Fyodor Dostoevsky|俄|Russian
ru|白痴|The Idiot|陀思妥耶夫斯基|Fyodor Dostoevsky|俄|Russian
ru|群魔|Demons|陀思妥耶夫斯基|Fyodor Dostoevsky|俄|Russian
ru|少年|The Adolescent|陀思妥耶夫斯基|Fyodor Dostoevsky|俄|Russian
ru|被侮辱与被损害的|The Insulted and Humiliated|陀思妥耶夫斯基|Fyodor Dostoevsky|俄|Russian
ru|白夜|White Nights|陀思妥耶夫斯基|Fyodor Dostoevsky|俄|Russian
ru|穷人|Poor Folk|陀思妥耶夫斯基|Fyodor Dostoevsky|俄|Russian
ru|赌徒|The Gambler|陀思妥耶夫斯基|Fyodor Dostoevsky|俄|Russian
ru|死屋手记|The House of the Dead|陀思妥耶夫斯基|Fyodor Dostoevsky|俄|Russian
ru|战争与和平|War and Peace|托尔斯泰|Leo Tolstoy|俄|Russian
ru|安娜·卡列尼娜|Anna Karenina|托尔斯泰|Leo Tolstoy|俄|Russian
ru|复活|Resurrection|托尔斯泰|Leo Tolstoy|俄|Russian
ru|猎人笔记|A Sportsman’s Sketches|屠格涅夫|Ivan Turgenev|俄|Russian
ru|前夜|On the Eve|屠格涅夫|Ivan Turgenev|俄|Russian
ru|父与子|Fathers and Sons|屠格涅夫|Ivan Turgenev|俄|Russian
ru|死魂灵|Dead Souls|果戈里|Nikolai Gogol|乌克兰裔俄语作家|Ukrainian-born, Russian-language
ru|当代英雄|A Hero of Our Time|莱蒙托夫|Mikhail Lermontov|俄|Russian
ru|契诃夫短篇小说选|Selected Short Stories|契诃夫|Anton Chekhov|俄|Russian
ru|樱桃园·三姊妹·万尼亚舅舅|The Cherry Orchard · Three Sisters · Uncle Vanya|契诃夫|Anton Chekhov|俄|Russian
ru|米佳的爱情|Mitya’s Love|蒲宁|Ivan Bunin|俄裔无国籍流亡作家|Russian émigré (stateless)
ru|童年|My Childhood|高尔基|Maxim Gorky|俄|Russian
ru|在人间|In the World|高尔基|Maxim Gorky|俄|Russian
ru|我的大学|My Universities|高尔基|Maxim Gorky|苏联|Soviet
ru|日瓦戈医生|Doctor Zhivago|帕斯捷尔纳克|Boris Pasternak|苏联|Soviet
ru|静静的顿河|And Quiet Flows the Don|肖洛霍夫|Mikhail Sholokhov|苏联|Soviet
ru|大师和玛格丽特|The Master and Margarita|布尔加科夫|Mikhail Bulgakov|苏联（生于基辅）|Soviet (b. Kyiv)
ru|癌症楼|Cancer Ward|索尔仁尼琴|Aleksandr Solzhenitsyn|苏联／俄罗斯|Soviet / Russian
ru|古拉格群岛|The Gulag Archipelago|索尔仁尼琴|Aleksandr Solzhenitsyn|苏联／俄罗斯|Soviet / Russian
en|红字|The Scarlet Letter|霍桑|Nathaniel Hawthorne|美|American
en|七个尖角顶的宅第|The House of the Seven Gables|霍桑|Nathaniel Hawthorne|美|American
en|白鲸|Moby-Dick|梅尔维尔|Herman Melville|美|American
en|马克·吐温短篇小说选|Selected Short Stories|马克·吐温|Mark Twain|美|American
en|爱伦·坡小说选|Selected Tales|爱伦·坡|Edgar Allan Poe|美|American
en|杰克·伦敦小说选|Selected Stories|杰克·伦敦|Jack London|美|American
en|马丁·伊登|Martin Eden|杰克·伦敦|Jack London|美|American
en|美国的悲剧|An American Tragedy|德莱塞|Theodore Dreiser|美|American
en|嘉丽妹妹|Sister Carrie|德莱塞|Theodore Dreiser|美|American
en|第二十二条军规|Catch-22|约瑟夫·海勒|Joseph Heller|美|American
en|了不起的盖茨比|The Great Gatsby|菲茨杰拉德|F. Scott Fitzgerald|美|American
en|飘|Gone with the Wind|玛格丽特·米切尔|Margaret Mitchell|美|American
en|小妇人|Little Women|路易莎·梅·奥尔科特|Louisa May Alcott|美|American
en|欧·亨利短篇小说选|Selected Short Stories|欧·亨利|O. Henry|美|American
en|汤姆叔叔的小屋|Uncle Tom’s Cabin|斯托夫人|Harriet Beecher Stowe|美|American
en|巴比特|Babbitt|辛克莱·刘易斯|Sinclair Lewis|美|American
en|一位女士的画像|The Portrait of a Lady|亨利·詹姆斯|Henry James|美（1915 年入英籍）|American (naturalised British 1915)
de|浮士德|Faust|歌德|Johann Wolfgang von Goethe|德|German
de|少年维特的烦恼|The Sorrows of Young Werther|歌德|Johann Wolfgang von Goethe|德|German
de|魔山|The Magic Mountain|托马斯·曼|Thomas Mann|德|German
de|特雷庇姑娘|The Maiden of Treppi|保尔·海泽|Paul Heyse|德|German
de|朗读者|The Reader|本哈德·施林克|Bernhard Schlink|德|German
de|在轮下|Beneath the Wheel|赫尔曼·黑塞|Hermann Hesse|德裔瑞士|German-born Swiss
de|老妇还乡|The Visit|迪伦马特|Friedrich Dürrenmatt|瑞士|Swiss
de|茨威格中短篇小说选|Selected Novellas and Stories|茨威格|Stefan Zweig|奥地利（后流亡，入英籍）|Austrian (exiled; British subject 1940)
de|卡夫卡中短篇小说全集|The Complete Stories|卡夫卡|Franz Kafka|奥匈帝国·布拉格，德语犹太作家|Bohemian, German-language (b. Prague)
jp|雪国|Snow Country|川端康成|Yasunari Kawabata|日|Japanese
jp|伊豆的舞女|The Dancing Girl of Izu|川端康成|Yasunari Kawabata|日|Japanese
jp|湖|The Lake|川端康成|Yasunari Kawabata|日|Japanese
jp|罗生门|Rashōmon|芥川龙之介|Ryūnosuke Akutagawa|日|Japanese
jp|挪威的森林|Norwegian Wood|村上春树|Haruki Murakami|日|Japanese
jp|海边的卡夫卡|Kafka on the Shore|村上春树|Haruki Murakami|日|Japanese
es|百年孤独|One Hundred Years of Solitude|马尔克斯|Gabriel García Márquez|哥伦比亚|Colombian
es|霍乱时期的爱情|Love in the Time of Cholera|马尔克斯|Gabriel García Márquez|哥伦比亚|Colombian
es|爱情、疯狂与死亡的故事|Stories of Love, Madness and Death|奥拉西奥·基罗加|Horacio Quiroga|乌拉圭|Uruguayan
es|玉米人|Men of Maize|阿斯图里亚斯|Miguel Ángel Asturias|危地马拉|Guatemalan
sv|尼尔斯骑鹅旅行记|The Wonderful Adventures of Nils|塞尔玛·拉格洛夫|Selma Lagerlöf|瑞典|Swedish
sv|查理十二世的人马|The Charles Men|海顿斯坦姆|Verner von Heidenstam|瑞典|Swedish
da|明娜|Minna|耶勒鲁普|Karl Gjellerup|丹麦|Danish
da|幸运儿彼尔|Lucky Per|彭托皮丹|Henrik Pontoppidan|丹麦|Danish
it|十日谈|The Decameron|薄伽丘|Giovanni Boccaccio|意大利|Italian
pl|你往何处去|Quo Vadis|显克维奇|Henryk Sienkiewicz|波兰|Polish
pl|十字军骑士|The Knights of the Cross|显克维奇|Henryk Sienkiewicz|波兰|Polish
bn|戈拉|Gora|泰戈尔|Rabindranath Tagore|印度|Indian
""".strip().split("\n")

# year | zh_name | en_name | zh_nat | en_nat | zh_works | en_works
NOBEL = """
1905|显克维奇|Henryk Sienkiewicz|波兰|Polish|你往何处去 · 十字军骑士|Quo Vadis · The Knights of the Cross
1909|塞尔玛·拉格洛夫|Selma Lagerlöf|瑞典|Swedish|尼尔斯骑鹅旅行记|The Wonderful Adventures of Nils
1910|保尔·海泽|Paul Heyse|德|German|特雷庇姑娘|The Maiden of Treppi
1913|泰戈尔|Rabindranath Tagore|印度|Indian|戈拉|Gora
1915|罗曼·罗兰|Romain Rolland|法|French|约翰·克利斯朵夫|Jean-Christophe
1916|海顿斯坦姆|Verner von Heidenstam|瑞典|Swedish|查理十二世的人马|The Charles Men
1917|耶勒鲁普|Karl Gjellerup|丹麦|Danish|明娜|Minna
1917|彭托皮丹|Henrik Pontoppidan|丹麦|Danish|幸运儿彼尔|Lucky Per
1921|法郎士|Anatole France|法|French|波纳尔之罪|The Crime of Sylvestre Bonnard
1925|萧伯纳|George Bernard Shaw|爱尔兰|Irish|华伦夫人的职业 · 芭芭拉少校 · 圣女贞德|Mrs Warren’s Profession · Major Barbara · Saint Joan
1929|托马斯·曼|Thomas Mann|德|German|魔山|The Magic Mountain
1930|辛克莱·刘易斯|Sinclair Lewis|美|American|巴比特|Babbitt
1932|高尔斯华绥|John Galsworthy|英|British|福尔赛世家（三部曲）|The Forsyte Saga
1933|蒲宁|Ivan Bunin|俄裔无国籍|Russian émigré (stateless)|米佳的爱情|Mitya’s Love
1946|黑塞|Hermann Hesse|德裔瑞士|German-born Swiss|在轮下|Beneath the Wheel
1947|纪德|André Gide|法|French|窄门|Strait Is the Gate
1952|弗朗索瓦·莫里亚克|François Mauriac|法|French|爱的荒漠|The Desert of Love
1957|加缪|Albert Camus|法|French|局外人 · 鼠疫|The Stranger · The Plague
1958|帕斯捷尔纳克|Boris Pasternak|苏联|Soviet|日瓦戈医生|Doctor Zhivago
1965|肖洛霍夫|Mikhail Sholokhov|苏联|Soviet|静静的顿河|And Quiet Flows the Don
1967|阿斯图里亚斯|Miguel Ángel Asturias|危地马拉|Guatemalan|玉米人|Men of Maize
1968|川端康成|Yasunari Kawabata|日|Japanese|雪国 · 伊豆的舞女 · 湖|Snow Country · The Dancing Girl of Izu · The Lake
1970|索尔仁尼琴|Aleksandr Solzhenitsyn|苏联／俄罗斯|Soviet / Russian|癌症楼 · 古拉格群岛|Cancer Ward · The Gulag Archipelago
1982|马尔克斯|Gabriel García Márquez|哥伦比亚|Colombian|百年孤独 · 霍乱时期的爱情|One Hundred Years of Solitude · Love in the Time of Cholera
1983|戈尔丁|William Golding|英|British|蝇王|Lord of the Flies
2012|莫言|Mo Yan|中|Chinese|蛙|Frog
""".strip().split("\n")


def L(zh, en):
    """A bilingual inline fragment."""
    return f'<span class="lang-zh">{zh}</span><span class="lang-en">{en}</span>'


def build():
    books = [r.split("|") for r in ROWS]
    o = []
    A = o.append

    A('<!DOCTYPE html>')
    A('<html lang="en" data-lang="en">')
    A('<head>')
    A('<meta charset="utf-8">')
    A('<meta name="viewport" content="width=device-width, initial-scale=1">')
    A('<title>Reading — Jingchu Gai</title>')
    A('<meta name="description" content="A record of what I have read, and passages worth keeping. 读书记录与摘抄。">')
    A("<link rel=\"icon\" href=\"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📖</text></svg>\">")
    A('<link rel="stylesheet" href="assets/style.css">')
    A('<link rel="stylesheet" href="assets/reading.css">')
    A('</head>')
    A('<body>')
    A('<div class="wrap">')

    # ---- rail: identity + nav, sticky beside the content ----
    A('  <div class="layout">')
    A('    <aside class="rail">')
    A('      <div class="rail-inner">')
    A('        <h1 class="page-title">' + L("读书记录", "Reading") + '</h1>')
    A('        <p class="lede lang-en">A record of what I have read outside mathematics, and the '
      'passages I went back and copied out.</p>')
    A('        <p class="lede lang-zh zh-text">数学之外的阅读记录，'
      '以及那些让我停下来抄写的段落。</p>')
    A('        <nav>')
    A('          <a href="index.html">' + L("返回主页", "home") + '</a>')
    A('          <a href="#shelf">' + L("书单", "the list") + '</a>')
    A('          <a href="#nobel">' + L("诺贝尔文学奖", "nobel") + '</a>')
    A('          <a href="#excerpts">' + L("摘抄", "excerpts") + '</a>')
    A('          <span class="railtools">')
    A('            <span class="langswitch">')
    A('              <button type="button" data-lang="en">EN</button>')
    A('              <button type="button" data-lang="zh">中文</button>')
    A('            </span>')
    A('            <button id="theme" type="button" aria-label="Toggle color theme">&#9790;</button>')
    A('          </span>')
    A('        </nav>')
    A('      </div>')
    A('    </aside>')
    A('    <main>')

    # ---- shelf ----
    A('  <section id="shelf">')
    A('    <h2>' + L("书单", "The List") + '</h2>')
    A('    <p class="lede lang-en" style="font-size:15px">Grouped by the language a book was '
      '<em>written</em> in. Almost all of them I read in Chinese translation.</p>')
    A('    <p class="lede lang-zh zh-text" style="font-size:15px">按作品的<em>写作语言</em>分类。'
      '除英语原著外，均读的中译本。</p>')
    A('    <div class="shelf">')
    for key, zh_h, en_h in GROUPS:
        rows = [b for b in books if b[0] == key]
        A('      <details>')
        A(f'        <summary>{L(zh_h, en_h)}<span class="n">{len(rows)}</span></summary>')
        A('        <ul class="books">')
        for _, zt, et, za, ea, zn, en_ in rows:
            A('          <li>')
            A(f'            <span class="t">{L("《" + zt + "》", et)}</span>')
            A('            <span class="a">' + L(za, ea) + '</span>')
            A('          </li>')
        A('        </ul>')
        A('      </details>')
    A('    </div>')
    A('  </section>')

    # ---- nobel ----
    A('  <section id="nobel">')
    A('    <h2><svg class="medal" viewBox="0 0 24 24" fill="none" stroke="currentColor" aria-hidden="true"><path d="M8.6,13.6 L6,22 L12,19.2 L18,22 L15.4,13.6" stroke-width="1.5" stroke-linejoin="round"/><circle cx="12" cy="8.5" r="6.5" stroke-width="1.5"/><circle cx="12" cy="8.5" r="3.2" stroke-width="1.1" opacity=".45"/></svg>' + L("诺贝尔文学奖得主", "Nobel Laureates") + '</h2>')
    A('    <p class="lede lang-en" style="font-size:15px">An ongoing attempt to read my way through '
      'the winners of the Nobel Prize in Literature. These are the ones I have reached so far.</p>')
    A('    <p class="lede lang-zh zh-text" style="font-size:15px">我在尝试把历届诺贝尔文学奖的获奖作品读一遍，'
      '以下是目前读到的部分。</p>')
    A('    <div class="table-wrap">')
    A('    <table class="nobel">')
    A('      <thead><tr>')
    A(f'        <th>{L("年份", "Year")}</th><th>{L("作家", "Laureate")}</th><th>{L("所读作品", "Read")}</th>')
    A('      </tr></thead>')
    A('      <tbody>')
    for line in NOBEL:
        y, zn_, en_, znat, enat, zw, ew = line.split("|")
        A('        <tr>')
        A(f'          <td class="y">{y}</td>')
        A('          <td class="who">' + L(zn_, en_) + '</td>')
        A('          <td class="what">' + L("《" + zw.replace(" · ", "》《") + "》", ew) + '</td>')
        A('        </tr>')
    A('      </tbody>')
    A('    </table>')
    A('    </div>')
    A('  </section>')

    # ---- excerpts (collapsed; click a title to read the passage) ----
    quotes = json.load(open(HERE / "quotes_full.json"))
    A('  <section id="excerpts">')
    A('    <h2>' + L("摘抄", "Excerpts") + '</h2>')
    A('    <p class="lede lang-en" style="font-size:15px">Click a title to read the passage. '
      'Works written in English are quoted from the published original; everything else is a '
      'rendering of the Chinese translation I read.</p>')
    A('    <p class="lede lang-zh zh-text" style="font-size:15px">点击书名展开段落。'
      '英语原著引自出版原文；其余均据我所读的中译本转译成英文。</p>')
    A('    <div class="quotes">')
    for q in quotes:
        is_orig = q["source"] == "original"
        A('      <details>')
        A('        <summary>')
        A('          <span class="qt">' + L("《" + q["zh_title"] + "》", q["en_title"]) + '</span>')
        A('          <span class="qa">' + L(q["zh_author"], q["en_author"]) + '</span>')
        prov_cls = "prov orig-text" if is_orig else "prov"
        prov = L("原文" if is_orig else "转译", "original" if is_orig else "rendering")
        A(f'          <span class="{prov_cls}">{prov}</span>')
        A('        </summary>')
        A('        <blockquote class="lang-zh zh-text">')
        for p in q["zh"]:
            A(f'          <p>{p}</p>')
        A('        </blockquote>')
        if q.get("en"):
            A('        <blockquote class="lang-en">')
            for p in q["en"]:
                A('          <p>' + p.replace("\n", "<br>") + '</p>')
            A('        </blockquote>')
        else:
            A('        <blockquote class="lang-en"><p style="color:var(--faint)">'
              'The published original for this passage is not reproduced here.</p></blockquote>')
        if q.get("orig"):
            A(f'        <div class="orig"><em>{q["orig_label"]}:</em> {q["orig"]}</div>')
        A('      </details>')
    A('    </div>')
    A('  </section>')

    A('    </main>')
    A('  </div>')

    # ---- note ----
    A('  <div class="caveat">')
    A('    <p class="lang-en" style="margin:0"><b>A note on the texts.</b> '
      'Apart from the English-language works, I read all of these in Chinese translation, so the '
      'English titles here are the standard published ones rather than my own. Passages from books '
      'written in English are quoted from the original; the rest are renderings of the Chinese I '
      'read, and carry none of the authority of a published translation. Corrections are welcome — '
      'please <a href="mailto:jgai@andrew.cmu.edu">write to me</a>.</p>')
    A('    <p class="lang-zh zh-text" style="margin:0"><b>关于版本的说明。</b>'
      '除英语原著外，以下作品我读的都是中译本，页面上的英文书名取通行译名而非我的翻译。'
      '摘抄部分，英语原著引自原文；其余为我据中译本转译的英文，不具备出版译本的权威性。'
      '若有错漏，欢迎<a href="mailto:jgai@andrew.cmu.edu">来信指正</a>。</p>')
    A('  </div>')

    A('  <footer>')
    A('    <a href="index.html">' + L("返回主页", "Back to home") + '</a>')
    A('    <a href="mailto:jgai@andrew.cmu.edu">jgai@andrew.cmu.edu</a>')
    A('  </footer>')
    A('</div>')

    # ---- scripts ----
    A('''<script>
(function () {
  var root = document.documentElement;

  /* ---- language ---- */
  var btns = document.querySelectorAll(".langswitch button");
  function setLang(l) {
    root.setAttribute("data-lang", l);
    root.setAttribute("lang", l === "zh" ? "zh-Hans" : "en");
    btns.forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.lang === l));
    });
    try { localStorage.setItem("lang", l); } catch (e) {}
  }
  var saved = null;
  try { saved = localStorage.getItem("lang"); } catch (e) {}
  var prefersZh = (navigator.language || "en").toLowerCase().indexOf("zh") === 0;
  setLang(saved === "zh" || saved === "en" ? saved : (prefersZh ? "zh" : "en"));
  btns.forEach(function (b) {
    b.addEventListener("click", function () { setLang(b.dataset.lang); });
  });

  /* ---- theme (same contract as the home page) ---- */
  var tb = document.getElementById("theme"), st = null;
  try { st = localStorage.getItem("theme"); } catch (e) {}
  function applyTheme(t) {
    if (t) root.setAttribute("data-theme", t); else root.removeAttribute("data-theme");
    var dark = t ? t === "dark"
      : window.matchMedia("(prefers-color-scheme: dark)").matches;
    tb.textContent = dark ? "\\u2600" : "\\u263E";
  }
  applyTheme(st);
  tb.addEventListener("click", function () {
    var dark = root.getAttribute("data-theme")
      ? root.getAttribute("data-theme") === "dark"
      : window.matchMedia("(prefers-color-scheme: dark)").matches;
    var next = dark ? "light" : "dark";
    try { localStorage.setItem("theme", next); } catch (e) {}
    applyTheme(next);
  });
})();
</script>''')
    A('</body>')
    A('</html>')

    out = "\n".join(o)
    open(SITE / "reading.html", "w").write(out)
    print(f"books: {len(books)}  nobel: {len(NOBEL)}  quotes: {len(quotes)}  bytes: {len(out)}")
    for key, zh_h, _ in GROUPS:
        print(f"  {zh_h}: {len([b for b in books if b[0]==key])}")


build()
