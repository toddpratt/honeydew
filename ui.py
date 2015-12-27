import npyscreen
import shlex

from twisted.internet import reactor

class ActionController(npyscreen.ActionControllerSimple):

  def process_command_complete(self, command_line, widget):
    if command_line.startswith('/'):
      args = shlex.split(command_line)
    else:
      self.parent.sendLine(command_line)

class IrcForm(npyscreen.FormMuttActive):
  ACTION_CONTROLLER = ActionController

  def create(self):
    super(IrcForm, self).create()
    self.wMain.values.append('Connected.')

  def sendLine(self, line):
    self.parentApp.sendLine(line)

class IrcClient(npyscreen.NPSAppManaged):

  def onStart(self):
    self.form = self.addForm("MAIN", IrcForm)
    self.form.add_handlers({
        '^Q': self.quit,
        })

  def got_line(self, line):
    self.form.wMain.values.append(line)
    self.form.wMain.display()

  def quit(self, *args, **kwargs):
    self.switchForm(None)
    reactor.stop()

  def sendLine(self, line):
    self.factory.proto.sendLine(line)
    self.form.wMain.values.append(line)
    self.form.wMain.display()
