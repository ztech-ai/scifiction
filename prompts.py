PROMPT_CONFIG = {
    'version': '1.0',
    'templates': {
        'default': {
            'system': "你是一个科幻小说作家，请生成结构完整的科幻短篇故事",
            'user_template': "{prompt}"
        },
        'future_city': {
            'label': '未来都市',
            'system': "你是一个科幻作家，请创作关于未来都市的短篇小说，包含赛博朋克元素和科技伦理冲突",
            'user_template': "以{theme}为主题，描写一个发生在22世纪智能城市的悬疑故事",
            'params': ['theme']
        },
        'time_travel': {
            'label': '时间旅行',
            'system': "你擅长创作时间旅行题材的科幻小说，故事需要包含因果悖论和哲学思考",
            'user_template': "以{theme}为关键线索，写一个涉及平行时空交错的惊悚故事",
            'params': ['theme']
        },
        'alien_contact': {
            'label': '外星接触',
            'system': "你专注于描写外星文明与人类首次接触的科幻故事，要求包含文化差异和星际政治",
            'user_template': "以{theme}为核心事件，创作一个颠覆认知的外星接触故事",
            'params': ['theme']
        }
    }
}