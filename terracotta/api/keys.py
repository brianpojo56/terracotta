"""api/keys.py

Flask route to handle /keys calls.
"""

from flask import jsonify
from marshmallow import Schema, fields

from terracotta.api.flask_api import convert_exceptions, metadata_api, spec


class KeyItemSchema(Schema):
    key = fields.String(description='Key name', required=True)
    description = fields.String(description='Key description')


class KeySchema(Schema):
    keys = fields.Nested(KeyItemSchema, many=True, required=True)


@metadata_api.route('/keys', methods=['GET'])
@convert_exceptions
def get_keys() -> str:
    """Get all key names
    ---
    get:
        summary: /keys
        description: List the names and descriptions (if available) of all known keys.
        responses:
            200:
                description: Array containing keys
                schema: KeySchema
    """
    from terracotta.handlers.keys import keys
    schema = KeySchema()
    payload = {'keys': keys()}
    return jsonify(schema.load(payload))


spec.definition('Keys', schema=KeySchema)
spec.definition('KeyItem', schema=KeyItemSchema)
