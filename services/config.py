class ConfigService:

    def __init__(self, reply_service):
        self.reply_service = reply_service
        self.prize = [30, 10, -10, -30]
        self.configs = {'レート': '点3', '順位点': str(self.prize), '飛び賞': 'なし', 'チップ': 'なし'}

    def reply(self):
        s = [f'{key}: {value}' for key, value in self.configs.items()]
        self.reply_service.add('[設定]\n' + '\n'.join(s))

    def get_rate(self):
        return int(self.configs['レート'][1:]) * 10