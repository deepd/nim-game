__author__ = 'deep'

import main

g1 = main.nimGame(7,'M')
g2 = main.nimGame(15, 'M')
g3 = main.nimGame(21, 'M')

root1 = main.Node(g1.initial)
root2 = main.Node(g2.initial)
root3 = main.Node(g3.initial)

newroot1 = main.makeTreeMinimax(root1,g1)
newroot2 = main.makeTreeMinimax(root2,g2)
newroot3 = main.makeTreeMinimax(root3,g3)

newroot4 = main.makeTreeAplhaBeta(root1,g1)
newroot5 = main.makeTreeAplhaBeta(root2,g2)
newroot6 = main.makeTreeAplhaBeta(root3,g3)

main.representTree(newroot1,g1)
main.representTree(newroot2,g2)
main.representTree(newroot3,g3)

main.representTreeAlpha(newroot4,g1)
main.representTreeAlpha(newroot5,g2)
main.representTreeAlpha(newroot6,g3)

main.makeMoore(newroot1,g1)
main.makeMoore(newroot2,g2)