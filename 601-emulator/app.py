# <imports>
from ssl import PROTOCOL_TLS_CLIENT, SSLContext, CERT_NONE
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# </imports>

# <ssl>
ssl_context = SSLContext(PROTOCOL_TLS_CLIENT)
ssl_context.check_hostname = False
ssl_context.verify_mode = CERT_NONE
# </ssl>

# <client>
auth_provider = PlainTextAuthProvider(
    username="localhost",
    password=(
        "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnq"
        "yMsEcaGQy67XIw/Jw=="
    ),
)

cluster = Cluster(
    ["localhost"],
    port="10350",
    auth_provider=auth_provider,
    ssl_context=ssl_context,
)
session = cluster.connect()
# </client>

# <resources>
session.execute(
    "CREATE KEYSPACE IF NOT EXISTS cosmicworks WITH replication = {'class':'ba"
    "sicclass', 'replication_factor': 1};"
)

session.execute(
    "CREATE TABLE IF NOT EXISTS cosmicworks.products (id text PRIMARY KEY, nam"
    "e text)"
)
# </resources>

# <upsert>
item = {"id": "68719518371", "name": "Kiama classic surfboard"}
session.execute(
    "INSERT INTO cosmicworks.products (id, name) VALUES (%s, %s)",
    [item["id"], item["name"]],
)
# </upsert>
