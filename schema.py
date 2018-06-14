from marshmallow import Schema, fields, pprint
    
class PostMsgSchema(Schema):
    sender = fields.Str(required=True)
    conversation_id = fields.Str(required=True)
    message = fields.Str(required=True)
    
