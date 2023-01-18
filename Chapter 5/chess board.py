def validator(board):
    og_board={
        '1h':'w rook',"1g":'w knight','1f':'w bishop',"1e":"w king",
        "1d":"w queen","1c":"w bishop","1b":"w knight","1a":"w rook",
        '2a':'w pawn','2b':'w pawn','2c':'w pawn','2d':'w pawn','2e':'w pawn',
        '2f':'w pawn','2g':'w pawn','2h':'w pawn',
        '8h':'b rook',"8g":'b knight','8f':'b bishop',"8e":"b king",
        "8d":"b queen","8c":"b bishop","8b":"b knight","8a":"b rook",
        '7a':'b pawn','7b':'b pawn','7c':'b pawn','7d':'b pawn','7e':'b pawn',
        '7f':'b pawn','7g':'b pawn','7h':'b pawn'}
    if board==og_board:
        print("True")
    else:
        print("False")

exg_board=og_board={
        '1h':'w rook',"1g":'w knight','1f':'w bishop',"1e":"w king",
        "1d":"w queen","1c":"w bishop","1b":"w knight","1a":"w rook",
        '2a':'w pawn','2b':'w pawn','2c':'w pawn','2d':'w pawn','2e':'w pawn',
        '2f':'w pawn','2g':'w pawn','2h':'w pawn',
        '8h':'b rook',"8g":'b knight','8f':'b bishop',"8e":"b king",
        "8d":"b queen","8c":"b bishop","8b":"b knight","8a":"b rook",
        '7a':'b pawn','7b':'b pawn','7c':'b pawn','7d':'b pawn','7e':'b pawn',
        '7f':'b pawn','7g':'b pawn','7h':'b pawn'}
        # Enter the required dictionary in place of the above code

validator(exg_board)

