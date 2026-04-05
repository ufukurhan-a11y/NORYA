#!/usr/bin/env python3
import json, sqlite3, sys
from datetime import datetime, timezone

DB = "/Users/ufukurhan/norya/norya.db"
cover = "/static/images/blog/apob-cholesterol-hero.jpg"

def load_and_insert(filepath, lang, cover_img, category, reading_time):
    with open(filepath, encoding='utf-8') as f:
        data = json.load(f)
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    cur.execute('''INSERT INTO blog_posts
        (slug, lang, title, meta_title, meta_description, content_json, cover_image, category, author_name, is_published, is_featured, reading_time_minutes, created_at, published_at)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
        (data['slug'], lang, data['title'], data['meta_title'], data['meta_description'],
         json.dumps(data['sections'], ensure_ascii=False), cover_img, category,
         data.get('author', 'Norya Editorial Team'), False, False, reading_time, now, None))
    conn.commit()
    print(f'{lang.upper()} eklendi: id={cur.lastrowid}, slug={data["slug"]}')
    conn.close()
    return data['slug']

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        lang = sys.argv[1]
        print(f'Lang: {lang}, using generic insertion...')
