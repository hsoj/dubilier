"""
"""


import datetime
import sqlalchemy
import discord.ext.commands
from . import (
    db,
    commands,
)


class Schedule(db.Mixin,
               db.Base):
    """
    """
    name = sqlalchemy.Column(sqlalchemy.String)
    notify = sqlalchemy.Column(sqlalchemy.String)
    format = sqlalchemy.Column(sqlalchemy.String)
    days = sqlalchemy.orm.relationship("ScheduleDay")
    fields = sqlalchemy.orm.relationship("ScheduleField")

    def __repr__(self) -> str:
        """
        """
        return "<Schedule(id={id}, name={name})>".format(id=self.id,
                                                         name=self.name)


class ScheduleDay(db.Mixin,
                  db.Base):
    """
    """
    schedule_id = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("schedule.id"))
    day = sqlalchemy.Column(sqlalchemy.String)
    time = sqlalchemy.Column(sqlalchemy.String)


class ScheduleField(db.Mixin,
                    db.Base):
    """
    """
    schedule_id = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("schedule.id"))
    key = sqlalchemy.Column(sqlalchemy.String)
    value = sqlalchemy.Column(sqlalchemy.String)


class Command(db.Mixin,
              commands.Command):
    """
    """

    def _build_time_tag(self, timestamp: str) -> str:
        """
        """
        time_tag = "<t:{time}:F>".format(time=timestamp)
        return time_tag

    def schedule_create(self, name: str, notify: str) -> None:
        """
        """
        schedule = Schedule(name=name, notify=notify)
        session_scope = self.db.session()
        if self.schedule_get(name=name) is None:
            with session_scope() as session:
                with session.begin():
                    session.add(schedule)
            

    def schedule_get(self, name: str) -> str:
        """
        """
        session_scope = self.db.session()
        with session_scope() as session:
            schedule = session.query(Schedule).filter(Schedule.name==name)
        if not schedule.count():
            return None
        return schedule.first()

    @discord.ext.commands.command()
    async def schedule(self, ctx, sub_command: str, *configs: str) -> None:
        """
        ?schedule create {name} {notify}
        ?schedule day {name} {day} {time}
        """
        print(sub_command)
        print(configs)
        # TODO: Make the subcommands a bit more dynamic on how they're
        # registered instead of a laundry list of if clauses
        if sub_command == "create":
            self.schedule_create(*configs)

    @discord.ext.commands.command()
    async def time(self, ctx) -> None:
        """
        """
        out_msg = "The time is {tag}"
        time_str = datetime.datetime.now().strftime("%s")
        time_tag = self._build_time_tag(timestamp=time_str)
        await ctx.send(out_msg.format(tag=time_tag))



