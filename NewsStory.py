import string
class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
    def getGuid(self):
        return self.guid
    def getTitle(self):
        return self.title
    def getSubject(self):
        return self.subject
    def getSummary(self):
        return self.summary
    def getLink(self):
        return self.link
class Trigger(object):
    def evaluate(self, story):
        raise NotImplementedError
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word
    def isWordIn(self, text):
        newtext = text.lower()
        L = list(newtext)
        for count in range(len(L)):
            for punct in string.punctuation:
                if L[count] == punct:
                    L[count] = ' '
        string1 = ''.join(L)
        L2 = string1.split()
        return self.word.lower() in L2
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        text = story.getTitle()
        return self.isWordIn(text)
class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        text = story.getSubject()
        return self.isWordIn(text)
class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        text = story.getSummary()
        return self.isWordIn(text)
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger
    def evaluate(self, story):
        return not self.trigger.evaluate(story)
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    def evaluate(self, story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    def evaluate(self, story):
        title =  story.getTitle()
        subject = story.getSubject()
        summary = story.getSummary()
        return self.phrase in title or self.phrase in subject or self.phrase in summary
def filterStories(stories, triggerlist):
    newstories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) == True:
                newstories.append(story)
    stories = newstories
    return stories


n = NewsStory('foo', 'myTitle', 'mySubject', 'some long summary', 'www.example.com')
print n.getGuid()
w = WordTrigger('cool')
print w.isWordIn('hello there how are you?')
t = TitleTrigger('hello')
print t.isTitleIn('hello,')
s = SubjectTrigger('hello')
print s.isSubjectIn('hello,,, how are you doing today?')