from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    openapi_api_key = fields.Char(string="API Key", help="Provide the API key here", config_parameter="hia_chatgpt_integration.openapi_api_key", required=True)
    chatgpt_model_id = fields.Many2one('chatgpt.model', 'ChatGPT Model', ondelete='cascade',  config_parameter="hia_chatgpt_integration.chatgpt_model_id")
    tempreture_id = fields.Many2one('chatgpt.tempreture', 'ChatGPT Tempreture', ondelete='cascade', config_parameter="hia_chatgpt_integration.tempreture_id")