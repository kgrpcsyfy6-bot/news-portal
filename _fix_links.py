"""Fix remaining dead links across all HTML files."""
import re
from pathlib import Path

root = Path('.')

# 1. Fix auxiliary page navigation (5 files x 8 links)
nav_map = {
    'World':    'index.html#sec-world',
    'Politics': 'article-politics.html',
    'Business': 'article-business.html',
    'Tech':     'article-tech-ai.html',
    'Arts':     'index.html',
    'Health':   'article-health.html',
    'Sports':   'article-sports.html',
    'Culture':  'index.html#sec-culture',
}

aux_files = ['about.html', 'contact.html', 'terms.html', 'privacy.html', 'accessibility.html']

for fname in aux_files:
    path = root / fname
    if not path.exists():
        continue
    html = path.read_text(encoding='utf-8')
    modified = False
    for label, target in nav_map.items():
        pattern = '<a href="#" class="site-nav__link">' + label + '</a>'
        replacement = '<a href="' + target + '" class="site-nav__link">' + label + '</a>'
        if pattern in html:
            html = html.replace(pattern, replacement)
            modified = True
    if modified:
        path.write_text(html, encoding='utf-8')
        print(f'  OK {fname} - nav links fixed')

# 2. Fix index.html category story dead links
cat_article_map = {
    'sec-politics': 'article-politics.html',
    'sec-business': 'article-business.html',
    'sec-tech':     'article-tech-ai.html',
    'sec-climate':  'article-climate.html',
    'sec-health':   'article-health.html',
    'sec-sports':   'article-sports.html',
}

index_path = root / 'index.html'
html = index_path.read_text(encoding='utf-8')

for section_id, article in cat_article_map.items():
    section_start = html.find('data-od-id="' + section_id + '"')
    if section_start == -1:
        section_start = html.find('id="' + section_id + '"')
    if section_start == -1:
        continue

    section_end = html.find('</section>', section_start + 500)
    if section_end == -1:
        continue

    section_html = html[section_start:section_end]
    new_section = re.sub(
        r'<a href="#" class="(cat-feature|cat-headline)',
        '<a href="' + article + '" class="\\1',
        section_html
    )

    if new_section != section_html:
        html = html.replace(section_html, new_section)
        print(f'  OK index.html - {section_id} -> {article}')

# 3. Fix Top Stories dead links
ts_start = html.find('id="top-stories"')
if ts_start != -1:
    ts_end = html.find('</section>', ts_start)
    if ts_end == -1:
        ts_end = html.find('<!-- Poll / Have Your Say -->', ts_start)
    if ts_end != -1:
        ts_html = html[ts_start:ts_end]
        story_pattern = re.compile(r'<a href="#" class="story-item"(.*?)>(.*?)</a>', re.DOTALL)

        def replace_story(m):
            attrs = m.group(1)
            content = m.group(2)
            if 'Political' in content or 'Election' in content:
                article = 'article-politics.html'
            elif 'Business' in content or 'Trade' in content or 'Global' in content:
                article = 'article-business.html'
            elif 'Tech' in content or 'AI' in content or 'Apple' in content:
                article = 'article-tech-ai.html'
            elif 'Climate' in content or 'Arctic' in content:
                article = 'article-climate.html'
            elif 'Health' in content or 'Virus' in content:
                article = 'article-health.html'
            elif 'Sport' in content or 'Cup' in content:
                article = 'article-sports.html'
            elif 'KLIMS' in content:
                article = 'article-headline.html'
            else:
                article = 'index.html'
            return '<a href="' + article + '" class="story-item"' + attrs + '>' + content + '</a>'

        new_ts = story_pattern.sub(replace_story, ts_html)
        if new_ts != ts_html:
            html = html.replace(ts_html, new_ts)
            print('  OK index.html - Top Stories links fixed')

index_path.write_text(html, encoding='utf-8')
print('\nDone!')
