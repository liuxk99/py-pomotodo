import os
from datetime import datetime, timedelta, timezone
from time import sleep
from unittest import TestCase

from pomotodo import datetime_utils, utils, todo, app, file_utils
from pomotodo.client import PomotodoClient


def dump_pomos(pomos):
    print("There are %d pomos." % len(pomos))
    i = 0
    seconds = 0
    for item in pomos:
        i = i + 1
        seconds += item._length
        print("=> No.%02d" % i)
        print(item.to_markdown())
    # "总计 4 小时 47 分钟"
    print("完成了 %d 个番茄, 总计 %d seconds" % (i, seconds))


def dump_todos(todos):
    print("There are %d todos." % len(todos))
    i = 0
    for elem in todos:
        i = i + 1
        print("=> No.%02d" % i)
        print(elem)
    pass


class TestTrelloClient(TestCase):
    def setUp(self):
        p = utils.load("pomotodo.properties")
        print("token: %s" % p.properties['token'])
        self.client = PomotodoClient(
            token=p.properties['token']
        )
        pass

    def test_get_pomos_today(self):
        day_dt = datetime_utils.utc_today()
        app.get_pomos_date(self.client, day_dt)
        pass

    def test_get_pomos_yesterday(self):
        day_dt = datetime_utils.utc_yesterday()
        app.get_pomos_date(self.client, day_dt)
        pass

    def test_get_pomos_date(self):
        local_date = datetime_utils.from_iso8601("2021-07-10T00:00:00+0800")
        pomos = app.get_pomos_date(self.client, datetime_utils.to_utc(local_date))

        trello_str = utils.export_trello(pomos)

        pomos_filename = local_date.strftime("pomos-%Y%m%d.md")
        file_utils.write(pomos_filename, trello_str)
        pass

    def test_get_pomos_date_csv(self):
        local_date = datetime_utils.from_iso8601("2022-04-12T00:00:00+0800")
        pomos = app.get_pomos_date(self.client, datetime_utils.to_utc(local_date))

        trello_str = utils.export_trello(pomos)

        pomos_filename = local_date.strftime("pomos-%Y%m%d.md")
        file_utils.write(pomos_filename, trello_str)
        pass

    def test_get_pomo(self):
        uuid = "fa8e9021-87b5-4751-8c53-5aa047563ecd"
        self.client.get_pomo(uuid)
        pass

    def test_snap_todos(self):
        app.snap_todos_1(self.client)
        pass

    def test_export_pomos_csv(self):
        # csv_filename = utils.gen_pomos_snap_filename()
        date = "2022-05-07"
        csv_filename = "pomos-%s.csv" % date.replace('-', '.')
        csv_path = "csv" + os.sep + csv_filename
        print("csv path: %s" % csv_path)

        local_date = datetime_utils.from_iso8601("%sT00:00:00+0800" % date)
        app.export_pomos_client(self.client, local_date, csv_filename)
        pass

    def test_get_todos(self):
        todos = self.client.get_todos()
        todos.sort(key=todo.sort_key, reverse=True)
        dump_todos(todos)

        pass

    def test_get_todos_simple(self):
        todos = self.client.get_todos()
        for elem in todos:
            print(elem.description)

        pass

    def test_get_todo(self):
        uuid = "60dbbca2-60a5-4984-9cd5-4a0935016634"
        todo = self.client.get_todo(uuid)
        print(todo)
        pass

    def test_pin_todo(self):
        """
uuid: 6a580dc4-ff42-451a-9932-4da5af987b7b
 created_at: 2021-07-17T04:19:14.503000+00:00, updated_at: 2021-07-17T04:19:14.503000+00:00
 description: #时间管理 '日'·计划 |2021/07/17
        """
        uuid = "6a580dc4-ff42-451a-9932-4da5af987b7b"
        todo = self.client.pin_todo(uuid)
        print(todo)

        todo = self.client.unpin_todo(uuid)
        print(todo)
        pass

    def test_delete_todo(self):
        """
uuid: 4868ed6d-4f2a-410f-9d61-8b6c83699026
 created_at: 2021-07-15T22:19:36.664000+00:00, updated_at: 2021-07-15T22:19:36.664000+00:00
 description: #生命/健康 '锻炼'·散步 |2021/07/16
        """
        uuid = "4868ed6d-4f2a-410f-9d61-8b6c83699026"
        todo = self.client.get_todo(uuid)
        print(todo)

        result = self.client.delete_todo(uuid)
        print("result: %r" % result)
        pass

    def test_post_todo(self):
        now = datetime_utils.to_local(datetime.now())
        todo = self.client.post_todo("test %s" % now.isoformat())
        print(todo)
        pass

    def test_patch_todo(self):
        uuid = "9f8e962e-5572-4f7a-86cc-bfa7cdc1f60a"
        todo = self.client.get_todo(uuid)
        print("todo: %s" % todo)

        # description = todo.description + "..."
        # self.client.patch_todo(uuid, description=description)
        pass

    def test_todo_samples(self):
        now = datetime_utils.to_local(datetime.now())
        my_todo = self.client.post_todo("test %s" % now.isoformat())
        print(my_todo)

        description = my_todo.description + "..."
        patched_todo = self.client.patch_todo(my_todo.uuid, description=description)
        print("patch: " + my_todo.uuid)
        print(patched_todo)

        pinned_todo = self.client.pin_todo(patched_todo.uuid)
        print("pin: " + patched_todo.uuid)
        print(pinned_todo)

        pinned_todo = self.client.unpin_todo(patched_todo.uuid)
        print("unpin: " + pinned_todo.uuid)
        print(pinned_todo)

        sleep(60)
        result = self.client.delete_todo(pinned_todo.uuid)
        print("%r = delete_todo(%s)" % (result, pinned_todo.uuid))
        pass

    def test_generate_today_todos(self):
        date = datetime_utils.local_today()
        app.generate_today_todos(self.client, date)
        pass

    def test_generate_todos_by_date(self):
        local_date = datetime_utils.from_iso8601("2022-04-22T00:00:00+0800")
        app.generate_today_todos(self.client, local_date)
        pass

    def test_post_pomo(self):
        # import datetime
        # tz_string = datetime.datetime.now(datetime.timezone.utc).astimezone().tzname()
        # print(tz_string)
        # import time
        # print(time.tzname)

        utc_now = datetime.now(timezone.utc)

        start_at = (utc_now - timedelta(minutes=5)).isoformat(timespec='milliseconds').replace("+00:00", "Z")
        ended_at = utc_now.isoformat(timespec='milliseconds').replace("+00:00", "Z")
        description = "哈哈"

        print(start_at)
        print(ended_at)
        pomo = self.client.post_pomo(start_at, ended_at, None, description)
        print(pomo)

        pass
