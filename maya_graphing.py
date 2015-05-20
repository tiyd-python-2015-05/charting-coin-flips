import maya.cmds as cmd
import functools

def createUI( pWindowTitle, pApplyCallback ):

    windowID='myWindowID'

    cmd.window( windowID, title=pWindowTitle, sizeable=False, resizeToFitChildren=True )
    cmd.rowColumnLayout( numberOfColumns=2, columnWidth=[(1,75), (2, 150)], columnOffset=[(1,'right',2)] )
    cmd.text( label='Bin Counts: ' )
    the_bins = cmd.textField(text='0,1,2,3,4,5,6,7,8,9')
    cmd.separator( h=10, style='none' )
    cmd.separator( h=10, style='none' )
    cmd.button( label='Enter', command=functools.partial( pApplyCallback, the_bins ))

    def cancelCallback( *pArgs ):
        if cmd.window( windowID, exists=True ):
            cmd.deleteUI( windowID )

    cmd.button( label='Cancel', command=cancelCallback )

    cmd.showWindow()

def applyCallback( pthe_bins, *pArgs ):
    counts = cmd.textField( pthe_bins, query=True, text=True )
    print (counts)
    int_counts = [int(x.strip()) for x in counts.split(',')]
    print (int_counts)
    draw_chart(int_counts)

createUI("Bin_Count", applyCallback)

def draw_chart(bins):
    idx = 0
    for num in bins:
        if num != 0:
            result = cmd.polyCube( w=1, h=0.01*(num), d=1, name='my_cube#' )

            cmd.move( -(1 + (1.5 * idx)), .5*(.01*num), 0, result )

            idx += 1
