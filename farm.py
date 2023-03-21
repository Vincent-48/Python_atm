import random



p = nuke.Panel( 'submit to farm' )

p.addSingleLineInput( 'first', nuke.root().firstFrame() )
p.addSingleLineInput( 'last', nuke.root().lastFrame() )

p.addEnumerationPulldown( 'threads', '1 2 4 8' )
p.addSingleLineInput( 'batch size', '10' )
p.addBooleanCheckBox( 'local render', 0 )

p.show()

def submitToFarm():
    p = nuke.Panel( 'submit to farm' )

    p.addSingleLineInput( 'first', nuke.root().firstFrame() )
    p.addSingleLineInput( 'last', nuke.root().lastFrame() )

    p.addEnumerationPulldown( 'threads', '1 2 4 8' )
    p.addSingleLineInput( 'batch size', '10' )
    p.addBooleanCheckBox( 'local render', 0 )

    if p.show():
        args = dict( first = p.value('first'),
            last = p.value('last'),
            threads = p.value('threads'),
            batchSize = p.value('batch size'),
            local = p.value('local'))

        application = 'echo'
        #args = [ application, first, last, threads, batchSize, local ]
        cmdString = application + ' -range %(first)s-%(last)s -threads %(threads)s -batch %(batchSize)s' % args

        subprocess.Popen( cmdString.split() )

nuke.menu( 'Nuke' ).addCommand( 'Render/Send to Farm', submitToFarm )

def submitToFarm():
    p = nuke.Panel( 'submit to farm')

    p.addSingleLineInput( 'first', nuke.root().firstFrame() )
    p.addSingleLineInput( 'last', nuke.root().lastFrame() )

    p.addEnumerationPulldown( 'threads', '1 2 4 8' )
    p.addSingleLineInput( 'batch size', '10' )
    p.addBooleanCheckBox( 'local render', 0 )

    if p.show():
        args = dict( first = p.value('first'),
            last = p.value('last'),
            threads = p.value('threads'),
            batchSize = p.value('batch size'),
            local = p.value('local'))

        application = 'echo'
        #args = [ application, first, last, threads, batchSize, local ]
        cmdString = application + ' -range %(first)s-%(last)s -threads %(threads)s -batch %(batchSize)s' % args

        subprocess.Popen( cmdString.split() )

nuke.menu( 'Nuke' ).addCommand( 'Render/Send to Farm', submitToFarm )