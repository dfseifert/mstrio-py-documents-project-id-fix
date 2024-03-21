"""This is the demo script to show how administrator can manage documents and
dashboards in users' libraries.

This script will not work without replacing parameters with real values.
Its basic goal is to present what can be done with this module and to
ease its usage.
"""

from mstrio.project_objects import Dashboard, Document, list_documents,list_dashboards
from mstrio.users_and_groups import list_user_groups, list_users, User, UserGroup

from mstrio.connection import get_connection

# Define a variable which can be later used in a script
PROJECT_NAME = $project_name  # Project to connect to

conn = get_connection(workstationData, project_name=PROJECT_NAME)

# list all dashboards and documents within a project to which we have connection
dashboards = list_dashboards(connection=conn)
docs = list_documents(connection=conn)

# Define variables which can be later used in a script
DOCUMENT_NAME = $document_name
DASHBOARD_NAME = $dashboard_name

# get document and dashboard from by name or id and publish them to a library of
# an authenticated user
doc = Document(connection=conn, name=DOCUMENT_NAME)
dashboard = Dashboard(connection=conn, name=DASHBOARD_NAME)
doc.publish()
dashboard.publish()

# Define variables which can be later used in a script
USER_ID_1 = $user_id_1
USER_ID_2 = $user_id_2

# list all users and get 2 of them
users = list_users(connection=conn)
user_1 = User(connection=conn, id=USER_ID_1)
user_2 = User(connection=conn, id=USER_ID_2)

# share one dashboard/document to a given user(s) by passing user object(s)
# or id(s)
dashboard.publish(recipients=user_1)
dashboard.publish(recipients=[USER_ID_1, USER_ID_2])
# analogously we can take away dashboard(s)/document(s) from the library of the
# given user(s)
dashboard.unpublish(recipients=[user_1, user_2])
dashboard.unpublish(recipients=USER_ID_1)

# Define a variable which can be later used in a script
USER_GROUP_NAME = $user_group_name

# list all user groups and get one of them
user_groups_ = list_user_groups(connection=conn)
user_group_ = UserGroup(connection=conn, name=USER_GROUP_NAME)

# add users to given user group
user_group_.add_users(users=[user_1, user_2])

# Define variables which can be later used in a script
DOCUMENT_ID_1 = $document_id_1
DOCUMENT_ID_2 = $document_id_2
DOCUMENT_ID_3 = $document_id_3

# get documents with given ids to give to the user group and users which belong
# to it
docs_to_publish = list_documents(
    connection=conn,
    id=[DOCUMENT_ID_1, DOCUMENT_ID_2, DOCUMENT_ID_3],
)
for doc in docs_to_publish:
    doc.publish(recipients=user_group_)
